from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .failure_model import FailureModel, FailureModelDict
from .success_model import SuccessModel, SuccessModelDict


class BulkItemStatusUpdateResponsePayload(SdkBaseModel):
    """Response payload."""

    success: Optional[SuccessModel] = UNSET
    """Items succeeded."""

    failure: Optional[FailureModel] = UNSET
    """Items failed."""


class BulkItemStatusUpdateResponsePayloadDict(TypedDict):
    success: NotRequired[SuccessModelDict]
    failure: NotRequired[FailureModelDict]
