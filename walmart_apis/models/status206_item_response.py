from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Status206ItemResponse(SdkBaseModel):
    """list of ItemResponses"""

    product_id: Optional[str] = Field(default=UNSET, alias="productId")
    """Product id"""

    product_id_type: Optional[str] = Field(default=UNSET, alias="productIdType")
    """Product id type"""

    status: Optional[str] = UNSET
    """Status of the product."""

    last_updated_date: Optional[str] = Field(default=UNSET, alias="lastUpdatedDate")
    """The time at which the product was terminated."""


class Status206ItemResponseDict(TypedDict):
    product_id: NotRequired[str]
    product_id_type: NotRequired[str]
    status: NotRequired[str]
    last_updated_date: NotRequired[str]
