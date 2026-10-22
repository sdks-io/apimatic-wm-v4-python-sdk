from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.adjustment_type import AdjustmentTypeOrStr
from .enums.strategy_type1 import StrategyType1OrStr


class Strategy1(SdkBaseModel):
    strategy_type: Optional[StrategyType1OrStr] = Field(default=UNSET, alias="strategyType")
    """Strategy type supported for markets is Buy Box Price(for us and mx),External Price(for us and mx, ca),Competitive
    Price(for us and mx).<br><b style="color:green;">Market availability: US | CA | MX</b>"""

    adjustment_type: Optional[AdjustmentTypeOrStr] = Field(default=UNSET, alias="adjustmentType")
    """Specifies how price adjustment is applied. UNIT for a fixed amount or PERCENTAGE for a percentage-based
    change.<br><b style='color:green;'>Market availability: US | CA | MX</span></b>"""

    adjustment_value: Optional[float] = Field(default=UNSET, alias="adjustmentValue")
    """Defines the value by which price is adjusted, based on the selected adjustment value.<br><b
    style='color:green;'>Market availability: US | CA | MX</span></b>"""


class Strategy1Dict(TypedDict):
    strategy_type: NotRequired[StrategyType1OrStr]
    adjustment_type: NotRequired[AdjustmentTypeOrStr]
    adjustment_value: NotRequired[float]
