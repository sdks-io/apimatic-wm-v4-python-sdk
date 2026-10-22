from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ReturnAddress1(SdkBaseModel):
    """Return Address. This parameter is mandatory for orders using ``Yanwen`` for the carrier.

    <b style="color: green;">Market availability: US only</b>"""

    contact_name: str = Field(alias="contactName")
    """The name of the primary contact at the return address location."""

    address_line1: str = Field(alias="addressLine1")
    """Primary street address of the return location."""

    address_line2: Optional[str] = Field(default=UNSET, alias="addressLine2")
    """The additional address details for the return location (example, suite or apartment number)."""

    city: str
    """City of the return address location."""

    state: str
    """State or province of the return address. Use the standard two-letter code where applicable."""

    postal_code: str = Field(alias="postalCode")
    """ZIP or postal code of the return address location."""

    country: str
    """Country code of the return address location (example, US, CN)."""

    phone: str
    """Phone number associated with the return address location."""

    email: Optional[str] = UNSET
    """Email address associated with the return address location."""

    ship_node: Optional[str] = Field(default=UNSET, alias="shipNode")
    """Seller's ship node identifier associated with the return location."""


class ReturnAddress1Dict(TypedDict):
    contact_name: str
    address_line1: str
    address_line2: NotRequired[str]
    city: str
    state: str
    postal_code: str
    country: str
    phone: str
    email: NotRequired[str]
    ship_node: NotRequired[str]
