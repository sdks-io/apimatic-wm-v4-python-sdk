from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_unpublished_items_payload import GetUnpublishedItemsPayload, GetUnpublishedItemsPayloadDict
from .total_gmv_amount import TotalGmvAmount, TotalGmvAmountDict


class GetUnpublishedItem(SdkBaseModel):
    payload: Optional[list[GetUnpublishedItemsPayload]] = UNSET
    total_count: Optional[int] = Field(default=UNSET, alias="totalCount")
    """total number of unpublished items"""

    total_gmv_amount: Optional[TotalGmvAmount] = Field(default=UNSET, alias="totalGmvAmount")
    """Gross Merchandise Value of the total result set"""


class GetUnpublishedItemDict(TypedDict):
    payload: NotRequired[list[GetUnpublishedItemsPayloadDict]]
    total_count: NotRequired[int]
    total_gmv_amount: NotRequired[TotalGmvAmountDict]
