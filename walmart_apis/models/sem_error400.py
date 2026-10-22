from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SemError400(SdkBaseModel):
    code: Optional[str] = UNSET
    """A unique identifier for the type of error. This helps in quickly recognizing and categorizing the specific
    issue."""

    description: Optional[str] = UNSET
    """A detailed message explaining what caused the error. This provides more context about the issue."""

    info: Optional[str] = UNSET
    """A brief summary of the error, often used for a quick understanding of the issue."""

    severity: Optional[str] = UNSET
    """Indicates the criticality of the error. Common values include ``ERROR``, ``WARNING``, or ``INFO``."""

    category: Optional[str] = UNSET
    """Classifies the error into a specific group or type, which helps in organizing and managing different types of
    issues."""


class SemError400Dict(TypedDict):
    code: NotRequired[str]
    description: NotRequired[str]
    info: NotRequired[str]
    severity: NotRequired[str]
    category: NotRequired[str]
