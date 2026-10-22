from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.issue_type import IssueTypeOrStr


class Issue(SdkBaseModel):
    """Issue affecting an item. Contains the issue type identifier only.

    The ``issueType`` serves as a lookup key into the issue metadata returned by the ``GET /item-issues/issue-types``
    reference endpoint. All static metadata (name, description, category, fixability, help links) lives in that
    endpoint's response."""

    issue_type: Optional[IssueTypeOrStr] = Field(default=UNSET, alias="issueType")
    """Lookup key into the issue metadata returned by the ``GET /item-issues/issue-types`` endpoint. Maps to one of the
    supported issue type enum values."""


class IssueDict(TypedDict):
    issue_type: NotRequired[IssueTypeOrStr]
