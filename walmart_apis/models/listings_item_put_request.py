from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.requirements import RequirementsOrStr


class ListingsItemPutRequest(SdkBaseModel):
    product_type: str = Field(alias="productType")
    """Walmart product type for the listing"""

    requirements: Optional[RequirementsOrStr] = UNSET
    attributes: Any
    """JSON object of product attributes matching the product type definition schema"""


class ListingsItemPutRequestDict(TypedDict):
    product_type: str
    requirements: NotRequired[RequirementsOrStr]
    attributes: Any
