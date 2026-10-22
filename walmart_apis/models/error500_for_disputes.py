from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Error500ForDisputes(SdkBaseModel):
    code: Optional[str] = UNSET
    """Error code of the response."""

    description: Optional[str] = UNSET
    """Description of error."""

    severity: Optional[str] = UNSET
    """Severity of Error."""

    category: Optional[str] = UNSET
    """Category of error."""

    causes: Optional[list[str]] = UNSET
    """Causes of error."""

    error_identifiers: Optional[Any] = Field(default=UNSET, alias="errorIdentifiers")
    """Error Identifiers of the error."""


class Error500ForDisputesDict(TypedDict):
    code: NotRequired[str]
    description: NotRequired[str]
    severity: NotRequired[str]
    category: NotRequired[str]
    causes: NotRequired[list[str]]
    error_identifiers: NotRequired[Any]
