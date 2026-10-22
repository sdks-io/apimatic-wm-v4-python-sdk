from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.box_dimension_unit2 import BoxDimensionUnit2OrStr
from .enums.box_weight_unit2 import BoxWeightUnit2OrStr


class BoxDimensions2(SdkBaseModel):
    box_length: Optional[float] = Field(default=UNSET, alias="boxLength")
    box_width: Optional[float] = Field(default=UNSET, alias="boxWidth")
    box_height: Optional[float] = Field(default=UNSET, alias="boxHeight")
    box_weight: float = Field(alias="boxWeight")
    box_dimension_unit: Optional[BoxDimensionUnit2OrStr] = Field(default=UNSET, alias="boxDimensionUnit")
    box_weight_unit: BoxWeightUnit2OrStr = Field(alias="boxWeightUnit")


class BoxDimensions2Dict(TypedDict):
    box_length: NotRequired[float]
    box_width: NotRequired[float]
    box_height: NotRequired[float]
    box_weight: float
    box_dimension_unit: NotRequired[BoxDimensionUnit2OrStr]
    box_weight_unit: BoxWeightUnit2OrStr
