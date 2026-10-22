from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .content_discoverability_issues_desc import ContentDiscoverabilityIssuesDesc, ContentDiscoverabilityIssuesDescDict


class ContentDiscoverabilityIssue(SdkBaseModel):
    score: Optional[float] = UNSET
    is_editable: Optional[bool] = Field(default=UNSET, alias="isEditable")
    attribute_value: Optional[str] = Field(default=UNSET, alias="attributeValue")
    is_spec_attribute: Optional[bool] = Field(default=UNSET, alias="isSpecAttribute")
    attribute_name: Optional[str] = Field(default=UNSET, alias="attributeName")
    issue_count: Optional[int] = Field(default=UNSET, alias="issueCount")
    issues: Optional[list[ContentDiscoverabilityIssuesDesc]] = UNSET


class ContentDiscoverabilityIssueDict(TypedDict):
    score: NotRequired[float]
    is_editable: NotRequired[bool]
    attribute_value: NotRequired[str]
    is_spec_attribute: NotRequired[bool]
    attribute_name: NotRequired[str]
    issue_count: NotRequired[int]
    issues: NotRequired[list[ContentDiscoverabilityIssuesDescDict]]
