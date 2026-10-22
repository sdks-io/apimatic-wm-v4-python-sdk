from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.box_dimension_unit1 import BoxDimensionUnit1OrStr
from .enums.box_weight_unit import BoxWeightUnitOrStr


class BoxDimensions1(SdkBaseModel):
    """Box dimensions and weight for the shipping package."""

    box_length: Optional[float] = Field(default=UNSET, alias="boxLength")
    """Length of the package. Required when packageType is CUSTOM_PACKAGE; not required for other standard package types
    (e.g., FEDEX_ENVELOPE, FEDEX_PAK) where dimensions are predetermined by the carrier. The Unit is determined by
    boxDimensionUnit."""

    box_width: Optional[float] = Field(default=UNSET, alias="boxWidth")
    """Width of the package. Required when packageType is CUSTOM_PACKAGE; not required for other standard package types
    (e.g., FEDEX_ENVELOPE, FEDEX_PAK) where dimensions are predetermined by the carrier. The Unit is determined by
    boxDimensionUnit."""

    box_height: Optional[float] = Field(default=UNSET, alias="boxHeight")
    """Height of the package. Required when packageType is CUSTOM_PACKAGE; not required for other standard package types
    (e.g., FEDEX_ENVELOPE, FEDEX_PAK) where dimensions are predetermined by the carrier. The Unit is determined by
    boxDimensionUnit."""

    box_weight: float = Field(alias="boxWeight")
    """Weight of the package. Required for all package types. The Unit is determined by boxWeightUnit."""

    box_dimension_unit: Optional[BoxDimensionUnit1OrStr] = Field(default=UNSET, alias="boxDimensionUnit")
    """Unit of measurement for the package length, width, and height. Allowed values: IN (inches), FT (feet), CM
    (centimeters). Required when packageType is CUSTOM_PACKAGE; not required for other standard package types (e.g.,
    FEDEX_ENVELOPE, FEDEX_PAK) where dimensions are predetermined by the carrier."""

    box_weight_unit: BoxWeightUnitOrStr = Field(alias="boxWeightUnit")
    """Unit of measurement for the package weight. Allowed values: LB (pounds), KG (kilograms), OZ (ounces)."""


class BoxDimensions1Dict(TypedDict):
    box_length: NotRequired[float]
    box_width: NotRequired[float]
    box_height: NotRequired[float]
    box_weight: float
    box_dimension_unit: NotRequired[BoxDimensionUnit1OrStr]
    box_weight_unit: BoxWeightUnitOrStr
