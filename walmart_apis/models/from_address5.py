from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FromAddress5(SdkBaseModel):
    """Origin (ship-from) address used for the scan form.

    <b style="color: green;">Market availability: US only</b>"""

    contact_name: str = Field(alias="contactName")
    """Contact name for the origin address.

    <b style="color: green;">Market availability: US only</b>"""

    company_name: Optional[str] = Field(default=UNSET, alias="companyName")
    """Company name for the origin address.

    <b style="color: green;">Market availability: US only</b>"""

    address_line1: str = Field(alias="addressLine1")
    """First line of the origin street address.

    <b style="color: green;">Market availability: US only</b>"""

    address_line2: Optional[str] = Field(default=UNSET, alias="addressLine2")
    """Second line of the origin street address, such as suite or unit.

    <b style="color: green;">Market availability: US only</b>"""

    city: str
    """Origin city name.

    <b style="color: green;">Market availability: US only</b>"""

    state: str
    """Origin state or province. Use the region code when available. For example, CA, AK.

    <b style="color: green;">Market availability: US only</b>"""

    postal_code: str = Field(alias="postalCode")
    """Origin postal or ZIP code.

    <b style="color: green;">Market availability: US only</b>"""

    country: str
    """Origin country code. Use a two-letter code. For example, US, CN, IN.

    <b style="color: green;">Market availability: US only</b>"""

    phone: str
    """Origin contact phone number.

    <b style="color: green;">Market availability: US only</b>"""

    email: Optional[str] = UNSET
    """Origin contact email address.

    <b style="color: green;">Market availability: US only</b>"""


class FromAddress5Dict(TypedDict):
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
