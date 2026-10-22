from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CustomerName(SdkBaseModel):
    """Customer information.<br><b style='color:green;'>Market availability: Global</b>"""

    first_name: Optional[str] = Field(default=UNSET, alias="firstName")
    """Customer first name.<br><b style='color:green;'>Market availability: Global</b>"""

    last_name: Optional[str] = Field(default=UNSET, alias="lastName")
    """Customer last name.<br><b style='color:green;'>Market availability: Global</b>"""


class CustomerNameDict(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
