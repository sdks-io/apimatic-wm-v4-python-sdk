from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .error7 import Error7, Error7Dict


class ErrorResponses(SdkBaseModel):
    error: Error7


class ErrorResponsesDict(TypedDict):
    error: Error7Dict
