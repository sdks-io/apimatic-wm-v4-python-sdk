from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .gmv import Gmv, GmvDict


class Tax1(SdkBaseModel):
    tax_name: Optional[str] = Field(default=UNSET, alias="taxName")
    """taxName.<br><b style='color:green;'>Market availability: MX</b>"""

    tax_amount: Optional[Gmv] = Field(default=UNSET, alias="taxAmount")
    """taxName.<br><b style='color:green;'>Market availability: MX</b>"""


class Tax1Dict(TypedDict):
    tax_name: NotRequired[str]
    tax_amount: NotRequired[GmvDict]
