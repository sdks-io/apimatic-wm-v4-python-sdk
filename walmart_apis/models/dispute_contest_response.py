from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status import StatusOrStr


class DisputeContestResponse(SdkBaseModel):
    """Items status included in the response list."""

    status: Optional[StatusOrStr] = UNSET
    """Status of the issue submitted."""


class DisputeContestResponseDict(TypedDict):
    status: NotRequired[StatusOrStr]
