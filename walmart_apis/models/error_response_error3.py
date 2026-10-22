from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .error7 import Error7, Error7Dict


class ErrorResponseError3(SdkBaseModel):
    error: Error7


class ErrorResponseError3Dict(TypedDict):
    error: Error7Dict
