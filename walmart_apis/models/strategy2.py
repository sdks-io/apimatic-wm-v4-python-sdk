from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.adjustment_type2 import AdjustmentType2OrStr
from .enums.strategy_type import StrategyTypeOrStr


class Strategy2(SdkBaseModel):
    strategy_type: Optional[StrategyTypeOrStr] = Field(default=UNSET, alias="strategyType")
    """Strategy type supported for markets is Buy Box Price(for us and mx), External Price(for US, MX and CA),
    Competitive Price(for us and mx).<br><b style="color:green;">Market availability: US | CA | MX</b>"""

    adjustment_type: Optional[AdjustmentType2OrStr] = Field(default=UNSET, alias="adjustmentType")
    """Specifies how price adjustment is applied. UNIT for a fixed amount or PERCENTAGE for a percentage-based
    change.<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    adjustment_value: Optional[float] = Field(default=UNSET, alias="adjustmentValue")
    """Defines the value by which price is adjusted, based on the selected adjustment value.<br><b
    style='color:green;'>Market availability: US | CA | MX</b>"""


class Strategy2Dict(TypedDict):
    strategy_type: NotRequired[StrategyTypeOrStr]
    adjustment_type: NotRequired[AdjustmentType2OrStr]
    adjustment_value: NotRequired[float]
