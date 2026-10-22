from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .comparison_price import ComparisonPrice, ComparisonPriceDict
from .enums.name7 import Name7OrStr


class AddOn8(SdkBaseModel):
    """List of add-ons returned for the estimate."""

    name: Name7OrStr
    """Name of the add-on type."""

    charge: ComparisonPrice
    """Charge of add-on type."""

    declared_value: Optional[ComparisonPrice] = Field(default=UNSET, alias="declaredValue")
    """Declared value of shipment. This value is applicable in case of INSURANCE add-on type only."""

    ref_link: Optional[str] = Field(default=UNSET, alias="refLink")
    """Reference link for the add-on type."""

    status: Optional[str] = UNSET
    """Status of the add-on type."""


class AddOn8Dict(TypedDict):
    name: Name7OrStr
    charge: ComparisonPriceDict
    declared_value: NotRequired[ComparisonPriceDict]
    ref_link: NotRequired[str]
    status: NotRequired[str]
