from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .content_discoverability_issue import ContentDiscoverabilityIssue, ContentDiscoverabilityIssueDict


class ContentAndDiscoverability(SdkBaseModel):
    issue_count: Optional[int] = Field(default=UNSET, alias="issueCount")
    issues: Optional[list[ContentDiscoverabilityIssue]] = UNSET


class ContentAndDiscoverabilityDict(TypedDict):
    issue_count: NotRequired[int]
    issues: NotRequired[list[ContentDiscoverabilityIssueDict]]
