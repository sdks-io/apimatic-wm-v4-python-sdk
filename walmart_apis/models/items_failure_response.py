from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ItemsFailureResponse(SdkBaseModel):
    """Items."""

    item_id: Optional[str] = Field(default=UNSET, alias="itemId")
    """Specifies the item identifier."""

    error_code: Optional[str] = Field(default=UNSET, alias="errorCode")
    """A unique identifier for the type of error. This helps in quickly recognizing and categorizing the specific
    issue."""

    error_description: Optional[str] = Field(default=UNSET, alias="errorDescription")
    """A detailed message explaining what caused the error. This provides more context about the issue."""

    category: Optional[str] = UNSET
    """Classifies the error into a specific group or type, which helps in organizing and managing different types of
    issues."""

    severity: Optional[str] = UNSET
    """Indicates the criticality of the error. Common values include ERROR, WARNING, or INFO."""


class ItemsFailureResponseDict(TypedDict):
    item_id: NotRequired[str]
    error_code: NotRequired[str]
    error_description: NotRequired[str]
    category: NotRequired[str]
    severity: NotRequired[str]
