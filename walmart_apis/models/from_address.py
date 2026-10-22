from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FromAddress(SdkBaseModel):
    """From address"""

    contact_name: str = Field(alias="contactName")
    """Contact name"""

    company_name: Optional[str] = Field(default=UNSET, alias="companyName")
    """Company name"""

    address_line1: str = Field(alias="addressLine1")
    """Address Line 1"""

    address_line2: Optional[str] = Field(default=UNSET, alias="addressLine2")
    """Address Line 2"""

    city: str
    """city"""

    state: str
    """state"""

    postal_code: str = Field(alias="postalCode")
    """postal code"""

    country: str
    """country"""

    phone: str
    """phone"""

    email: Optional[str] = UNSET
    """email"""


class FromAddressDict(TypedDict):
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
