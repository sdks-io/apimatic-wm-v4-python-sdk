from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShipmentLocation(SdkBaseModel):
    """From address - Seller's fulfilment center address."""

    postal_code: str = Field(alias="postalCode")
    country_code: str = Field(alias="countryCode")
    address_lines: list[str] = Field(alias="addressLines")
    """addressLines"""

    city: str
    """city"""

    state: str
    """state"""


class ShipmentLocationDict(TypedDict):
    postal_code: str
    country_code: str
    address_lines: list[str]
    city: str
    state: str
