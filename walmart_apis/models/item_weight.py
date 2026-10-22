from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ItemWeight(SdkBaseModel):
    """itemWeight.<br><b style='color:green;'>Market availability: US</b>"""

    unit_of_measure: Optional[str] = Field(default=UNSET, alias="unitOfMeasure")
    """Unit of measure for the quantity.<br><b style='color:green;'>Market availability: US</b>"""

    measurement_value: Optional[float] = Field(default=UNSET, alias="measurementValue")
    """Numeric value for the quantity in the specified unit of measure.<br><b style='color:green;'>Market availability:
    US</b>"""


class ItemWeightDict(TypedDict):
    unit_of_measure: NotRequired[str]
    measurement_value: NotRequired[float]
