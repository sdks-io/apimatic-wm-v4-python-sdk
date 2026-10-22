from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Issues1(SdkBaseModel):
    """Items status included in the response list."""

    product_id: Optional[str] = Field(default=UNSET, alias="productId")
    """The unique Product ID assigned to the item.

    <strong style="color: green;">**Market availability: US only**</strong>"""

    product_id_type: Optional[str] = Field(default=UNSET, alias="productIdType")
    """The Product ID type of the item.

    <strong style="color: green;">**Market availability: US only**</strong>"""


class Issues1Dict(TypedDict):
    product_id: NotRequired[str]
    product_id_type: NotRequired[str]
