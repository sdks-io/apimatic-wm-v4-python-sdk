from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Error(SdkBaseModel):
    code: str = "INVALID_REQUEST_HEADER.GMP_GATEWAY_API"
    field: Optional[str] = UNSET
    description: str = "Incorrect Authorization header"
    info: Optional[str] = UNSET
    severity: str = "ERROR"
    category: str = "DATA"
    causes: Optional[list[Any]] = UNSET
    error_identifiers: Optional[Any] = Field(default=UNSET, alias="errorIdentifiers")


class ErrorDict(TypedDict):
    code: NotRequired[str]
    field: NotRequired[str]
    description: NotRequired[str]
    info: NotRequired[str]
    severity: NotRequired[str]
    category: NotRequired[str]
    causes: NotRequired[list[Any]]
    error_identifiers: NotRequired[Any]
