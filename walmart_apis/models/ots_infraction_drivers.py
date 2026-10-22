from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class OtsInfractionDrivers(SdkBaseModel):
    """Individual drivers of on time shipment rate"""

    marked_as_shipped_late_rate: Optional[float] = Field(default=UNSET, alias="markedAsShippedLateRate")
    """Marked as shipped later rate"""

    late_handover_to_carrier_rate: Optional[float] = Field(default=UNSET, alias="lateHandoverToCarrierRate")
    """Late handover to carrier rate"""


class OtsInfractionDriversDict(TypedDict):
    marked_as_shipped_late_rate: NotRequired[float]
    late_handover_to_carrier_rate: NotRequired[float]
