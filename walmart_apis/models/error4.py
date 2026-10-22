from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cause import Cause, CauseDict
from .enums.category import CategoryOrStr
from .enums.severity import SeverityOrStr


class Error4(SdkBaseModel):
    code: str
    field: Optional[str] = UNSET
    description: Optional[str] = UNSET
    info: Optional[str] = UNSET
    severity: Optional[SeverityOrStr] = UNSET
    category: Optional[CategoryOrStr] = UNSET
    causes: Optional[list[Cause]] = UNSET
    error_identifiers: Optional[dict[str, Any]] = Field(default=UNSET, alias="errorIdentifiers")


class Error4Dict(TypedDict):
    code: str
    field: NotRequired[str]
    description: NotRequired[str]
    info: NotRequired[str]
    severity: NotRequired[SeverityOrStr]
    category: NotRequired[CategoryOrStr]
    causes: NotRequired[list[CauseDict]]
    error_identifiers: NotRequired[dict[str, Any]]
