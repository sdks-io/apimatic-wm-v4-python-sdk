from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Error2(SdkBaseModel):
    code: str
    field: Optional[str] = UNSET
    description: str
    info: Optional[str] = UNSET
    severity: str
    category: str
    causes: Optional[list[str]] = UNSET
    error_identifiers: Optional[Any] = Field(default=UNSET, alias="errorIdentifiers")


class Error2Dict(TypedDict):
    code: str
    field: NotRequired[str]
    description: str
    info: NotRequired[str]
    severity: str
    category: str
    causes: NotRequired[list[str]]
    error_identifiers: NotRequired[Any]
