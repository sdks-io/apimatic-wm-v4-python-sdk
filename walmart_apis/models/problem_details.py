from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ProblemDetails(SdkBaseModel):
    """Problem details for HTTP APIs, as defined by RFC 9457 (https://www.rfc-editor.org/rfc/rfc9457)."""

    type_: str = Field(alias="type")
    """A URI that identifies the problem type."""

    title: str
    """A short, human-readable summary of the problem type."""

    status: int
    """The HTTP status code returned by the origin server for this occurrence."""

    detail: Optional[str] = UNSET
    """A human-readable explanation specific to this occurrence of the problem."""

    instance: Optional[str] = UNSET
    """A URI reference that identifies the specific occurrence of the problem."""

    code: Optional[str] = UNSET
    """A Walmart-specific error code for legacy compatibility."""


class ProblemDetailsDict(TypedDict):
    type_: str
    title: str
    status: int
    detail: NotRequired[str]
    instance: NotRequired[str]
    code: NotRequired[str]
