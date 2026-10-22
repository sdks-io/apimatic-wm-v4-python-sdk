from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .issue3 import Issue3, Issue3Dict


class PublishAndTransactable3(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    issue_title: Optional[str] = Field(default=UNSET, alias="issueTitle")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    total_issue: Optional[int] = Field(default=UNSET, alias="totalIssue")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    max_issue: Optional[int] = Field(default=UNSET, alias="maxIssue")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    issues: Optional[list[Issue3]] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    score: Optional[int] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class PublishAndTransactable3Dict(TypedDict):
    issue_title: NotRequired[str]
    total_issue: NotRequired[int]
    max_issue: NotRequired[int]
    issues: NotRequired[list[Issue3Dict]]
    score: NotRequired[int]
