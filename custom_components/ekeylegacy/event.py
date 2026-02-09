"""Event entity for Ekey (legacy) integration."""

import asyncio
import logging

from homeassistant.components.event import EventDeviceClass, EventEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_PORT, CONF_TYPE
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from .const import CONF_DELIMITER, DOMAIN

_LOGGER = logging.getLogger(__name__)

class EkeyLegacyAuthEvent(EventEntity):
    """Representation of a Ekey (legacy) event entity."""

    _attr_device_class = EventDeviceClass.BUTTON
    _attr_event_types = ["authenticated", "failed"]

    def __init__(self, port: int, type: str, delimiter: str) -> None:
        """Initialize the Ekey (legacy) event entity."""
        self._attr_name = f"ekey {type}"
        self._attr_unique_id = f"{type}-{port}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, f"{type}-{port}")},
            manufacturer="ekey",
        )

        self._conf_port = port
        self._conf_type = type
        self._conf_delimiter = delimiter
        self._transport = None

    async def async_added_to_hass(self) -> None:
        """Register callbacks."""
        loop = asyncio.get_running_loop()
        self._transport, _ = await loop.create_datagram_endpoint(
            lambda: _EkeyUDPProtocol(self.hass, self),
            local_addr=("0.0.0.0", self._conf_port),
        )

    @callback
    def async_handle_event(self, message: str) -> None:
        """Handle the Ekey (legacy) event."""
        parts = message.strip().split(self._conf_delimiter)

        _LOGGER.info(
            "Received event '%s'",
            message,
        )

        is_successful = False

        if self._conf_type == "home" and len(parts) == 6:
            event_data = {
                "type": parts[0],
                "user": int(parts[1]),
                "finger": int(parts[2]),
                "scanner": parts[3],
                "action": parts[4],
                "relay": parts[5],
            }

            if event_data.action == "1"
                is_successful = True

        elif self._conf_type == "multi" and len(parts) == 10:
            event_data = {
                "type": parts[0],
                "user": int(parts[1]),
                "user_name": parts[2].lstrip("-"),
                "user_status": parts[3],
                "finger": int(parts[4]),
                "relay": parts[5],
                "scanner": parts[6],
                "scanner_name": parts[7].lstrip("-"),
                "action": parts[8],
                "digital_input": parts[8],
            }

            if event_data.action == "1"
                is_successful = True
        else:
            return

        if is_successful
            self._trigger_event("authenticated", event_data)
        else
            self._trigger_event("failed", event_data)

        self.async_write_ha_state()

    async def async_will_remove_from_hass(self) -> None:
        """Unregister the Ekey (legacy) event."""
        if self._transport is not None:
            self._transport.close()
            self._transport = None


class _EkeyUDPProtocol(asyncio.DatagramProtocol):
    """UDP protocol handler for incoming Ekey packets."""

    def __init__(self, hass: HomeAssistant, entity: EkeyLegacyAuthEvent) -> None:
        self.hass = hass
        self.entity = entity

    def datagram_received(self, data: bytes, addr) -> None:
        message = data.decode("ascii", errors="ignore")
        self.entity.async_handle_event(message)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up the Ekey (legacy) event platform."""
    async_add_entities(
        [
            EkeyLegacyAuthEvent(
                config_entry.data[CONF_PORT],
                config_entry.data[CONF_TYPE],
                config_entry.data[CONF_DELIMITER],
            )
        ]
    )
