from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Error11(SdkBaseModel):
    code: Optional[str] = UNSET
    field: Optional[str] = UNSET
    description: Optional[str] = UNSET
    info: Optional[str] = UNSET
    severity: Optional[str] = UNSET
    category: Optional[str] = UNSET
    causes: Optional[list[Any]] = UNSET
    error_identifiers: Optional[Any] = Field(default=UNSET, alias="errorIdentifiers")


class Error11Dict(TypedDict):
    code: NotRequired[str]
    field: NotRequired[str]
    description: NotRequired[str]
    info: NotRequired[str]
    severity: NotRequired[str]
    category: NotRequired[str]
    causes: NotRequired[list[Any]]
    error_identifiers: NotRequired[Any]
