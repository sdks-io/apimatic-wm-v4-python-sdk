from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.box_dimension_unit4 import BoxDimensionUnit4OrStr
from .enums.box_weight_unit4 import BoxWeightUnit4OrStr


class BoxDimensions4(SdkBaseModel):
    """Box Dimensions"""

    box_dimension_unit: Optional[BoxDimensionUnit4OrStr] = Field(default=UNSET, alias="boxDimensionUnit")
    """Box Dimension Unit [CM, IN]. Mandatory for CUSTOM_PACKAGE type, otherwise not required. <br/><b>Applicable to SWW
    and WPS.</span></b>"""

    box_weight_unit: BoxWeightUnit4OrStr = Field(alias="boxWeightUnit")
    """Box Weight Unit [LB, KG]. <br/><b>Applicable to SWW and WPS.</span></b>"""

    box_weight: float = Field(alias="boxWeight")
    """Box Weight. <br/><b>Applicable to SWW and WPS.</span></b>"""

    box_length: Optional[float] = Field(default=UNSET, alias="boxLength")
    """Box Length. Mandatory for CUSTOM_PACKAGE type, otherwise not required. <br/><b>Applicable to SWW and
    WPS.</span></b>"""

    box_width: Optional[float] = Field(default=UNSET, alias="boxWidth")
    """Box Width. Mandatory for CUSTOM_PACKAGE type, otherwise not required. <br/><b>Applicable to SWW and
    WPS.</span></b>"""

    box_height: Optional[float] = Field(default=UNSET, alias="boxHeight")
    """Box Height. Mandatory for CUSTOM_PACKAGE type, otherwise not required. <br/><b>Applicable to SWW and
    WPS.</span></b>"""


class BoxDimensions4Dict(TypedDict):
    box_dimension_unit: NotRequired[BoxDimensionUnit4OrStr]
    box_weight_unit: BoxWeightUnit4OrStr
    box_weight: float
    box_length: NotRequired[float]
    box_width: NotRequired[float]
    box_height: NotRequired[float]
