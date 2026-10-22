from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FromAddress4(SdkBaseModel):
    """From address - Seller's fulfillment center address."""

    postal_code: str = Field(alias="postalCode")
    """ZIP or postal code of the seller's fulfillment center."""

    country_code: str = Field(alias="countryCode")
    """Country code of the seller's fulfillment center (example, US, CN, IN)."""

    address_lines: list[str] = Field(alias="addressLines")
    """Street address lines for the seller's fulfillment center. Provide up to two lines. Provide up to two lines."""

    city: str
    """City of the seller's fulfillment center."""

    state: str
    """State or province of the seller's fulfillment center. Use the standard two-letter code where applicable."""


class FromAddress4Dict(TypedDict):
    postal_code: str
    country_code: str
    address_lines: list[str]
    city: str
    state: str
