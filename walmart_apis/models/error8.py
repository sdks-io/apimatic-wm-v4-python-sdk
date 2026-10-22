from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Error8(SdkBaseModel):
    code: Optional[str] = UNSET
    """A unique identifier for the type of error. This helps in quickly recognizing and categorizing the specific
    issue."""

    description: Optional[str] = UNSET
    """A detailed message explaining what caused the error. This provides more context about the issue."""

    category: Optional[str] = UNSET
    """Classifies the error into a specific group or type, which helps in organizing and managing different types of
    issues."""

    severity: Optional[str] = UNSET
    """Indicates the criticality of the error. Common values include ERROR, WARNING, or INFO."""


class Error8Dict(TypedDict):
    code: NotRequired[str]
    description: NotRequired[str]
    category: NotRequired[str]
    severity: NotRequired[str]
