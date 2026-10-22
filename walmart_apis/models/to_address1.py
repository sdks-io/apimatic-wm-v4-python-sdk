from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ToAddress1(SdkBaseModel):
    """To Address - Customer's delivery address."""

    postal_code: str = Field(alias="postalCode")
    """ZIP or postal code of the customer's delivery address."""

    country_code: str = Field(alias="countryCode")
    """Country code of the customer's delivery address (example, US)."""

    address_lines: list[str] = Field(alias="addressLines")
    """Street address lines for the customer's delivery address. Provide up to two lines."""

    city: str
    """City of the customer's delivery address."""

    state: str
    """State or province of the customer's delivery address. Use the standard two-letter code where applicable."""


class ToAddress1Dict(TypedDict):
    postal_code: str
    country_code: str
    address_lines: list[str]
    city: str
    state: str
