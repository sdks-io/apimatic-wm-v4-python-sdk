from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .comparison_price import ComparisonPrice, ComparisonPriceDict
from .enums.name import NameOrStr


class AddOnsResponse(SdkBaseModel):
    """List of add-ons returned for the estimate."""

    name: NameOrStr
    """Name of the AddOn type."""

    charge: ComparisonPrice
    """Charge of add-on type."""

    declared_value: Optional[ComparisonPrice] = Field(default=UNSET, alias="declaredValue")
    """Declared value of shipment. This value is applicable in case of INSURANCE add-on type only."""

    ref_link: Optional[str] = Field(default=UNSET, alias="refLink")
    """Reference link for the add-on type."""

    status: Optional[str] = UNSET
    """Status of the add-on type."""


class AddOnsResponseDict(TypedDict):
    name: NameOrStr
    charge: ComparisonPriceDict
    declared_value: NotRequired[ComparisonPriceDict]
    ref_link: NotRequired[str]
    status: NotRequired[str]
