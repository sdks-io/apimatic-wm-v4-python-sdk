from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.replace_all import ReplaceAllOrStr
from .pricing import Pricing, PricingDict


class Price5(SdkBaseModel):
    offer_id: Optional[str] = Field(default=UNSET, alias="offerId")
    """This is applicable only for promotions"""

    sku: str
    replace_all: Optional[ReplaceAllOrStr] = Field(default=UNSET, alias="replaceAll")
    """This is applicable only for promotions"""

    pricing: list[Pricing]
    definitions: Optional[Any] = UNSET


class Price5Dict(TypedDict):
    offer_id: NotRequired[str]
    sku: str
    replace_all: NotRequired[ReplaceAllOrStr]
    pricing: list[PricingDict]
    definitions: NotRequired[Any]
