from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.box_dimension_unit3 import BoxDimensionUnit3OrStr
from .enums.box_weight_unit3 import BoxWeightUnit3OrStr


class BoxDimensions3(SdkBaseModel):
    """Dimensions and weight of the package being shipped. Used together with packageType. For FEDEX_PAK or
    FEDEX_ENVELOPE, length/height/width are predetermined by the carrier and only weight is required. For
    CUSTOM_PACKAGE, all dimensions and weight are required.

    <b style="color: green;">Market availability: Global</b>"""

    box_length: Optional[float] = Field(default=UNSET, alias="boxLength")
    """The length of the package. Required when packageType is CUSTOM_PACKAGE, not required for other standard package
    types (Example: FEDEX_ENVELOPE, FEDEX_PAK) where dimensions are predetermined by the carrier. The Unit is determined
    by boxDimensionUnit.

    <b style="color: green;">Market availability: Global</b>"""

    box_width: Optional[float] = Field(default=UNSET, alias="boxWidth")
    """The width of the package. Required when packageType is CUSTOM_PACKAGE; not required for other standard package
    types (Example: FEDEX_ENVELOPE, FEDEX_PAK) where dimensions are predetermined by the carrier. The Unit is determined
    by boxDimensionUnit.

    <b style="color: green;">Market availability: Global</b>"""

    box_height: Optional[float] = Field(default=UNSET, alias="boxHeight")
    """The height of the package. Required when packageType is CUSTOM_PACKAGE; not required for other standard package
    types (Example: FEDEX_ENVELOPE, FEDEX_PAK) where dimensions are predetermined by the carrier. The Unit is determined
    by boxDimensionUnit.

    <b style="color: green;">Market availability: Global</b>"""

    box_weight: float = Field(alias="boxWeight")
    """The weight of the package. Required for all package types. The Unit is determined by boxWeightUnit.

    <b style="color: green;">Market availability: Global</b>"""

    box_dimension_unit: Optional[BoxDimensionUnit3OrStr] = Field(default=UNSET, alias="boxDimensionUnit")
    """The unit of measurement for the package length, width, and height. Allowed values: IN (inches), FT (feet), CM
    (centimeters).

    <b style="color: green;">Market availability: Global</b>"""

    box_weight_unit: BoxWeightUnit3OrStr = Field(alias="boxWeightUnit")
    """The unit of measurement for the package weight. Allowed values: LB (pounds), KG (kilograms), OZ (ounces).

    <b style="color: green;">Market availability: Global</b>"""


class BoxDimensions3Dict(TypedDict):
    box_length: NotRequired[float]
    box_width: NotRequired[float]
    box_height: NotRequired[float]
    box_weight: float
    box_dimension_unit: NotRequired[BoxDimensionUnit3OrStr]
    box_weight_unit: BoxWeightUnit3OrStr
