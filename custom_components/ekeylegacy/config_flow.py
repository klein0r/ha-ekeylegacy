"""Config flow for the Ekey (legacy) integration."""

from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.const import CONF_PORT, CONF_TYPE
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv

from .const import (
    CONF_DELIMITER,
    DEFAULT_DELIMITER,
    DEFAULT_PORT,
    DOMAIN,
    TYPE_HOME,
    TYPE_MULTI,
)

SCHEMA_DEVICE = vol.Schema(
    {
        vol.Required(CONF_PORT, default=DEFAULT_PORT): cv.port,
        vol.Required(CONF_DELIMITER, default=DEFAULT_DELIMITER): cv.string,
        vol.Required(CONF_TYPE, default=TYPE_HOME): vol.In(
            (
                TYPE_HOME,
                TYPE_MULTI,
            )
        ),
    }
)


class EkeyLegacyFlowHandler(ConfigFlow, domain=DOMAIN):
    """Config flow for EkeyLegacy."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle a flow initialized by the user."""
        errors = {}

        if user_input is not None:
            _port = user_input[CONF_PORT]
            _type = user_input[CONF_TYPE]

            await self.async_set_unique_id(str(_port))
            self._abort_if_unique_id_configured()

            return self.async_create_entry(
                title=f"ekey {_type} - port {_port}", data=user_input
            )

        return self.async_show_form(
            step_id="user",
            data_schema=SCHEMA_DEVICE,
            errors=errors,
        )


async def _async_has_devices(hass: HomeAssistant) -> bool:
    """Return if there are devices that can be discovered."""
    # TODO Check if there are any devices that can be discovered in the network.
    # devices = await hass.async_add_executor_job(my_pypi_dependency.discover)
    return False


# config_entry_flow.register_discovery_flow(DOMAIN, "Ekey (legacy)", _async_has_devices)
