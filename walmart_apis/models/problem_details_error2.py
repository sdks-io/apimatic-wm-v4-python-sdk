from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ProblemDetailsError2(SdkBaseModel):
    """RFC 9457 Problem Details for HTTP APIs"""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """A URI reference that identifies the problem type."""

    title: Optional[str] = UNSET
    """A short, human-readable summary of the problem type."""

    status: Optional[int] = UNSET
    """The HTTP status code."""

    detail: Optional[str] = UNSET
    """A human-readable explanation specific to this occurrence of the problem."""

    instance: Optional[str] = UNSET
    """A URI reference that identifies the specific occurrence of the problem."""


class ProblemDetailsError2Dict(TypedDict):
    type_: NotRequired[str]
    title: NotRequired[str]
    status: NotRequired[int]
    detail: NotRequired[str]
    instance: NotRequired[str]
