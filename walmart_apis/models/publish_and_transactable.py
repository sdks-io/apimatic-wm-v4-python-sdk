from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .issue1 import Issue1, Issue1Dict


class PublishAndTransactable(SdkBaseModel):
    issue_title: Optional[str] = Field(default=UNSET, alias="issueTitle")
    total_issue: Optional[int] = Field(default=UNSET, alias="totalIssue")
    max_issue: Optional[int] = Field(default=UNSET, alias="maxIssue")
    issues: Optional[list[Issue1]] = UNSET
    score: Optional[int] = UNSET


class PublishAndTransactableDict(TypedDict):
    issue_title: NotRequired[str]
    total_issue: NotRequired[int]
    max_issue: NotRequired[int]
    issues: NotRequired[list[Issue1Dict]]
    score: NotRequired[int]
