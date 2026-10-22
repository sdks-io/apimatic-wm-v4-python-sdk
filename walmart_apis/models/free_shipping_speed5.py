from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FreeShippingSpeed5(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    issue_title: Optional[str] = Field(default=UNSET, alias="issueTitle")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    issue_desc: Optional[str] = Field(default=UNSET, alias="issueDesc")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    score: Optional[int] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class FreeShippingSpeed5Dict(TypedDict):
    issue_title: NotRequired[str]
    issue_desc: NotRequired[str]
    score: NotRequired[int]
