from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .supplier_item_orderable import SupplierItemOrderable, SupplierItemOrderableDict
from .unions.visible import Visible, VisibleDict


class SupplierItemPayload(SdkBaseModel):
    orderable: SupplierItemOrderable = Field(alias="Orderable")
    visible: Visible = Field(alias="Visible")
    """The visible block for rich media. The expected structure depends on ``SupplierItemFeedHeader.subCategory``.
    Discriminator is based on ``SupplierItemFeedHeader.subCategory``"""


class SupplierItemPayloadDict(TypedDict):
    orderable: SupplierItemOrderableDict
    visible: VisibleDict
