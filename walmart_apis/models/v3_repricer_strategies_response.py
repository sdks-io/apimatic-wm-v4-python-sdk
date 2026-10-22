from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .strategy_collection import StrategyCollection, StrategyCollectionDict


class V3RepricerStrategiesResponse(SdkBaseModel):
    total_elements: Optional[int] = Field(default=UNSET, alias="totalElements")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    strategy_collections: Optional[list[StrategyCollection]] = Field(default=UNSET, alias="strategyCollections")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class V3RepricerStrategiesResponseDict(TypedDict):
    total_elements: NotRequired[int]
    strategy_collections: NotRequired[list[StrategyCollectionDict]]
