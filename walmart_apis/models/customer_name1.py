from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CustomerName1(SdkBaseModel):
    """customerName.<br><b style='color:green;'>Market availability: MX</b>"""

    first_name: Optional[str] = Field(default=UNSET, alias="firstName")
    """firstName.<br><b style='color:green;'>Market availability: MX</b>"""

    last_name: Optional[str] = Field(default=UNSET, alias="lastName")
    """lastName.<br><b style='color:green;'>Market availability: MX</b>"""


class CustomerName1Dict(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
