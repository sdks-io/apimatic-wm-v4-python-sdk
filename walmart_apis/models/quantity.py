from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Quantity(SdkBaseModel):
    """Total quantity returned in this return line.>"""

    unit_of_measure: str = Field(alias="unitOfMeasure")
    """The unit of measure in the item's weight (e.g., 'EACH' or 'EA')"""

    measurement_value: int = Field(alias="measurementValue")
    """The quantity of the unit of measure for the item"""


class QuantityDict(TypedDict):
    unit_of_measure: str
    measurement_value: int
