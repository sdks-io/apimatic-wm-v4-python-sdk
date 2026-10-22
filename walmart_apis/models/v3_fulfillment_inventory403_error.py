from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V3FulfillmentInventory403Error(SdkBaseModel):
    code: Optional[str] = UNSET
    field: Optional[str] = UNSET
    description: Optional[str] = UNSET
    info: Optional[str] = UNSET
    severity: Optional[str] = UNSET
    category: Optional[str] = UNSET
    causes: Optional[list[str]] = UNSET
    """Causes of the error."""

    error_identifiers: Optional[Any] = Field(default=UNSET, alias="errorIdentifiers")
    """Error Identifiers of the error."""


class V3FulfillmentInventory403ErrorDict(TypedDict):
    code: NotRequired[str]
    field: NotRequired[str]
    description: NotRequired[str]
    info: NotRequired[str]
    severity: NotRequired[str]
    category: NotRequired[str]
    causes: NotRequired[list[str]]
    error_identifiers: NotRequired[Any]
