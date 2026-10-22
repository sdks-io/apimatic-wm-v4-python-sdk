from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PriceDisplayCodes(SdkBaseModel):
    is_clearance: Optional[bool] = Field(default=UNSET, alias="isClearance")
    hide_price_for_soi: Optional[Any] = Field(default=UNSET, alias="hidePriceForSOI")
    submap_type: Optional[Any] = Field(default=UNSET, alias="submapType")
    is_rollback: Optional[bool] = Field(default=UNSET, alias="isRollback")
    is_reduced_price: Optional[bool] = Field(default=UNSET, alias="isReducedPrice")
    is_eligible_for_associate_discount: Optional[Any] = Field(default=UNSET, alias="isEligibleForAssociateDiscount")
    is_strikethrough: Optional[bool] = Field(default=UNSET, alias="isStrikethrough")


class PriceDisplayCodesDict(TypedDict):
    is_clearance: NotRequired[bool]
    hide_price_for_soi: NotRequired[Any]
    submap_type: NotRequired[Any]
    is_rollback: NotRequired[bool]
    is_reduced_price: NotRequired[bool]
    is_eligible_for_associate_discount: NotRequired[Any]
    is_strikethrough: NotRequired[bool]
