"""The Ekey (legacy) integration."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

_PLATFORMS: list[Platform] = [Platform.EVENT]

# TODO Create ConfigEntry type alias with API object
# Alias name should be prefixed by integration name
# type New_NameConfigEntry = ConfigEntry[MyApi]  # noqa: F821


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Ekey (legacy) from a config entry."""

    await hass.config_entries.async_forward_entry_setups(entry, _PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, _PLATFORMS)
