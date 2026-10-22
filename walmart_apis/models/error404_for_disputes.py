from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Error404ForDisputes(SdkBaseModel):
    code: Optional[str] = UNSET
    """Error code of the response."""

    description: Optional[str] = UNSET
    """Description of error."""

    info: Optional[str] = UNSET
    """Info of error."""

    severity: Optional[str] = UNSET
    """Severity of Error.

    Example: ERROR"""

    category: Optional[str] = UNSET
    """Category of error.

    Example: DATA"""

    causes: Optional[list[str]] = UNSET
    """Causes of error."""

    error_identifiers: Optional[Any] = Field(default=UNSET, alias="errorIdentifiers")
    """Error Identifiers of the error."""


class Error404ForDisputesDict(TypedDict):
    code: NotRequired[str]
    description: NotRequired[str]
    info: NotRequired[str]
    severity: NotRequired[str]
    category: NotRequired[str]
    causes: NotRequired[list[str]]
    error_identifiers: NotRequired[Any]
