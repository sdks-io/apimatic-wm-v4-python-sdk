from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Issues(SdkBaseModel):
    """Items status included in the response list."""

    product_id: Optional[str] = Field(default=UNSET, alias="productId")
    """ProductId of the Item"""

    product_id_type: Optional[str] = Field(default=UNSET, alias="productIdType")
    """ProductIdType of the item"""


class IssuesDict(TypedDict):
    product_id: NotRequired[str]
    product_id_type: NotRequired[str]
