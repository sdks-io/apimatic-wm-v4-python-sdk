from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Error7(SdkBaseModel):
    code: str
    field: Optional[str] = UNSET
    description: str
    info: str
    severity: str
    category: str
    causes: list[str]
    error_identifiers: dict[str, str] = Field(alias="errorIdentifiers")


class Error7Dict(TypedDict):
    code: str
    field: NotRequired[str]
    description: str
    info: str
    severity: str
    category: str
    causes: list[str]
    error_identifiers: dict[str, str]
