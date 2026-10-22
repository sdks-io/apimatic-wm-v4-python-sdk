from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error3 import Error3, Error3Dict


class ItemPriceResponse(SdkBaseModel):
    errors: Optional[list[Error3]] = UNSET
    status_code: Optional[int] = Field(default=UNSET, alias="statusCode")
    mart: Optional[str] = UNSET
    """Marketplace name. Example: Walmart-US"""

    sku: Optional[str] = UNSET
    """An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item."""

    message: Optional[str] = UNSET
    """A message of acknowledgement for a price update"""


class ItemPriceResponseDict(TypedDict):
    errors: NotRequired[list[Error3Dict]]
    status_code: NotRequired[int]
    mart: NotRequired[str]
    sku: NotRequired[str]
    message: NotRequired[str]
