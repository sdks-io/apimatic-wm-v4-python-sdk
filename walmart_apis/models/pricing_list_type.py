from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .pricing_type import PricingType, PricingTypeDict


class PricingListType(SdkBaseModel):
    replace_all: Optional[bool] = Field(default=UNSET, alias="replaceAll")
    pricing: list[PricingType]


class PricingListTypeDict(TypedDict):
    replace_all: NotRequired[bool]
    pricing: list[PricingTypeDict]
