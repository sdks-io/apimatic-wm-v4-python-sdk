from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .issues import Issues, IssuesDict


class DisputeContestRequest(SdkBaseModel):
    issues: list[Issues]
    """Items status included in the response list."""


class DisputeContestRequestDict(TypedDict):
    issues: list[IssuesDict]
