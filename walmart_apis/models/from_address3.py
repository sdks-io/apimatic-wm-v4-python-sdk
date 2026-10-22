from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FromAddress3(SdkBaseModel):
    """From address"""

    contact_name: str = Field(alias="contactName")
    """Contact name. <br/><b>Applicable to SWW only.</span></b>"""

    company_name: Optional[str] = Field(default=UNSET, alias="companyName")
    """Company name. <br/><b>Applicable to SWW only.</span></b>"""

    address_line1: str = Field(alias="addressLine1")
    """Address Line 1. <br/><b>Applicable to SWW only.</span></b>"""

    address_line2: Optional[str] = Field(default=UNSET, alias="addressLine2")
    """Address Line 2. <br/><b>Applicable to SWW only.</span></b>"""

    city: str
    """City of the from address location. <br/><b>Applicable to SWW only.</span></b>"""

    state: str
    """State or province of the from address. Use the standard two-letter code where applicable. <br/><b>Applicable to
    SWW only.</span></b>"""

    postal_code: str = Field(alias="postalCode")
    """ZIP or postal code of the from address location. <br/><b>Applicable to SWW only.</span></b>"""

    country: str
    """Country code of the from address location (example, US, CN). <br/><b>Applicable to SWW only.</span></b>"""

    phone: str
    """Phone number associated with the from address location. <br/><b>Applicable to SWW only.</span></b>"""

    email: Optional[str] = UNSET
    """Email address associated with the from address location. <br/><b>Applicable to SWW only.</span></b>"""


class FromAddress3Dict(TypedDict):
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
