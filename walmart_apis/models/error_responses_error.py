from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .error7 import Error7, Error7Dict


class ErrorResponsesError(SdkBaseModel):
    error: Error7


class ErrorResponsesErrorDict(TypedDict):
    error: Error7Dict
