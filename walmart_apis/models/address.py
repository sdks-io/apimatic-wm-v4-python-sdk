from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Address(SdkBaseModel):
    """Address object representing a physical location (fulfillment center, return address, or delivery address)."""

    contact_name: str = Field(alias="contactName")
    """Name of the primary contact at the address location."""

    company_name: Optional[str] = Field(default=UNSET, alias="companyName")
    """Name of the company or organization at the address location."""

    address_line1: str = Field(alias="addressLine1")
    """Primary street address line."""

    address_line2: Optional[str] = Field(default=UNSET, alias="addressLine2")
    """Additional address details (example, suite or apartment number)."""

    city: str
    """City of the address location."""

    state: str
    """State or province of the address. Use the standard two-letter code where applicable."""

    postal_code: str = Field(alias="postalCode")
    """ZIP or postal code of the address location."""

    country: str
    """Country code of the address location (example, US, MX, CA)."""

    phone: str
    """Phone number associated with the address location."""

    email: Optional[str] = UNSET
    """Email address associated with the address location."""


class AddressDict(TypedDict):
    contact_name: str
    company_name: NotRequired[str]
    address_line1: str
    address_line2: NotRequired[str]
    city: str
    state: str
    postal_code: str
    country: str
    phone: str
    email: NotRequired[str]
