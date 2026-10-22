from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FromAddress2(SdkBaseModel):
    """Defines the origin address from which the order will be shipped. This represents the seller’s fulfillment center
    location.

    <b style="color: green;">Market availability: US | CA | MX</b>"""

    contact_name: str = Field(alias="contactName")
    """The name of the primary contact at the fulfillment center. This name will appear on the shipping label.

    <b style="color: green;">Market availability: US | CA | MX</b>"""

    company_name: Optional[str] = Field(default=UNSET, alias="companyName")
    """The name of the seller’s company or fulfillment center.

    <b style="color: green;">Market availability: US | CA | MX</b>"""

    address_line1: str = Field(alias="addressLine1")
    """The primary street address of the fulfillment center.

    <b style="color: green;">Market availability: US | CA | MX</b>"""

    address_line2: Optional[str] = Field(default=UNSET, alias="addressLine2")
    """Additional address details.

    <b style="color: green;">Market availability: US | CA | MX</b>"""

    city: str
    """City in which the fulfillment center is located.

    <b style="color: green;">Market availability: US | CA | MX</b>"""

    state: str
    """State of the fulfillment center. Use the standard two-letter code.

    <b style="color: green;">Market availability: US | CA | MX</b>"""

    postal_code: str = Field(alias="postalCode")
    """ZIP or postal code of the fulfillment center’s location.

    <b style="color: green;">Market availability: US | CA | MX</b>"""

    country: str
    """The country code of the fulfillment center location.

    <b style="color: green;">Market availability: US | CA | MX</b>"""

    phone: str
    """A valid phone number associated with the fulfillment center.

    <b style="color: green;">Market availability: US | CA | MX</b>"""

    email: Optional[str] = UNSET
    """The email of the seller.

    <b style="color: green;">Market availability: US | CA | MX</b>"""


class FromAddress2Dict(TypedDict):
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
