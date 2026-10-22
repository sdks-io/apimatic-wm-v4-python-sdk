from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class StatusQuantity(SdkBaseModel):
    unit_of_measurement: Optional[str] = Field(default=UNSET, alias="unitOfMeasurement")
    """The unit of measurement for status quantity (e.g., EACH)"""

    amount: Optional[str] = UNSET
    """The amount for the status quantity"""


class StatusQuantityDict(TypedDict):
    unit_of_measurement: NotRequired[str]
    amount: NotRequired[str]
