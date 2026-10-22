from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.issue_category1 import IssueCategory1OrStr


class IssueMetadata(SdkBaseModel):
    """Static metadata for an issue type. Provides human-readable information for building diagnostic UIs including
    issue name, description, severity, remediability, and help links.

    This metadata is the same for every item — it describes the issue type itself, not a specific occurrence on an
    item."""

    issue_name: Optional[str] = Field(default=UNSET, alias="issueName")
    """Human-readable issue name for UI short headline display."""

    issue_category: Optional[IssueCategory1OrStr] = Field(default=UNSET, alias="issueCategory")
    """Issue severity category.

    - **BLOCKED**: Item cannot be advertised
    - **LIMITED**: Item has reduced visibility or performance
    - **NO_ISSUES**: Item has no SEM eligibility issues"""

    is_fixable: Optional[bool] = Field(default=UNSET, alias="isFixable")
    """Whether the partner can remediate this issue. ``true`` = actionable by partner (show "Fix Now" UI affordance),
    ``false`` = requires Walmart or system intervention (informational only)."""

    issue_description: Optional[str] = Field(default=UNSET, alias="issueDescription")
    """Human-readable description of the issue with remediation guidance."""

    learn_more_url: OptionalNullable[str] = Field(default=UNSET, alias="learnMoreUrl")
    """Help link (Walmart-hosted or Google support) for additional information. May be null if no help link is available
    for this issue type."""


class IssueMetadataDict(TypedDict):
    issue_name: NotRequired[str]
    issue_category: NotRequired[IssueCategory1OrStr]
    is_fixable: NotRequired[bool]
    issue_description: NotRequired[str]
    learn_more_url: NotRequired[str | None]
