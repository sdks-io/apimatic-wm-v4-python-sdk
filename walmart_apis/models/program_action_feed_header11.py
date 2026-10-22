from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ProgramActionFeedHeader11(SdkBaseModel):
    """ProgramAction feed header details. <br><b style='color:green;'>Market availability: US</span></b>"""

    version: Optional[str] = UNSET
    """This is static spec version. <br><b style='color:green;'>Market availability: US</span></b>"""

    locale: Optional[str] = UNSET
    """The associated language locale. <br><b style='color:green;'>Market availability: US</span></b>"""

    business_unit: Optional[str] = Field(default=UNSET, alias="businessUnit")
    """This is is static Walmart BU. <br><b style='color:green;'>Market availability: US</span></b>"""


class ProgramActionFeedHeader11Dict(TypedDict):
    version: NotRequired[str]
    locale: NotRequired[str]
    business_unit: NotRequired[str]
