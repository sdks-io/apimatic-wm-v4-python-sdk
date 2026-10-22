from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .issue16 import Issue16, Issue16Dict


class ContentAndDiscoverability4(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    issue_count: Optional[int] = Field(default=UNSET, alias="issueCount")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    issues: Optional[list[Issue16]] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class ContentAndDiscoverability4Dict(TypedDict):
    issue_count: NotRequired[int]
    issues: NotRequired[list[Issue16Dict]]
