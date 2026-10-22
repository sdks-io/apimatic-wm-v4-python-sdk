from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ShippingSpeed4(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US only</b>"""

    total_issue: Optional[int] = Field(default=UNSET, alias="totalIssue")
    """<br><b style='color:green;'>Market availability: US</b>"""

    shipping_type: Optional[str] = Field(default=UNSET, alias="shippingType")
    """<br><b style='color:green;'>Market availability: US only</b>"""

    issue_title: Optional[str] = Field(default=UNSET, alias="issueTitle")
    """<br><b style='color:green;'>Market availability: US only</b>"""

    issue_desc: Optional[str] = Field(default=UNSET, alias="issueDesc")
    """<br><b style='color:green;'>Market availability: US only</b>"""

    score: Optional[int] = UNSET
    """<br><b style='color:green;'>Market availability: US only</b>"""


class ShippingSpeed4Dict(TypedDict):
    total_issue: NotRequired[int]
    shipping_type: NotRequired[str]
    issue_title: NotRequired[str]
    issue_desc: NotRequired[str]
    score: NotRequired[int]
