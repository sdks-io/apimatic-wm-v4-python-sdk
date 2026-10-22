from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .strategy1 import Strategy1, Strategy1Dict


class V3RepricerStrategyResponse(SdkBaseModel):
    repricer_strategy: Optional[str] = Field(default=UNSET, alias="repricerStrategy")
    """Specifies the name of the strategy collection. This value is used to group and manage related repricing
    strategies.<br><b style='color:green;'>Market availability: US | CA | MX</span></b>"""

    strategy_collection_id: Optional[str] = Field(default=UNSET, alias="strategyCollectionId")
    """Unique identifier used to group and manage repricing strategies across different resources.<br><b
    style='color:green;'>Market availability: US | CA | MX</span></b>"""

    enabled: Optional[bool] = UNSET
    """Indicates the current status of the strategy collection.<br><b style='color:green;'>Market availability: US | CA
    | MX</span></b>"""

    enable_repricer_for_promotion: Optional[bool] = Field(default=UNSET, alias="enableRepricerForPromotion")
    """Indicates whether the item is eligible for promotional repricing. Set this to true to enable repricing for
    promotional items.<br><b style='color:green;'>Market availability: US | MX</span></b>"""

    restore_seller_price_without_target: Optional[bool] = Field(default=UNSET, alias="restoreSellerPriceWithoutTarget")
    """Reprices the item price back to the last submitted price if no competitor price is found.<br><b
    style='color:green;'>Market availability: US only</span></b>"""

    enable_buybox_meet_external: Optional[bool] = Field(default=UNSET, alias="enableBuyboxMeetExternal")
    """Indicates whether to match external competitor prices to beat the Buy Box price. This is only applicable for Buy
    Box strategies.<br><b style='color:green;'>Market availability: US | MX</span></b>"""

    compare_with3p_offer_only: Optional[bool] = Field(default=UNSET, alias="compareWith3pOfferOnly")
    """Indicates whether to compare only against 3P offers.<br><b style='color:green;'>Market availability: US
    only</span></b>"""

    strategies: Optional[list[Strategy1]] = UNSET
    """Defines one or more repricing strategies to apply.<br><b style='color:green;'>Market availability: US | CA |
    MX</span></b>"""


class V3RepricerStrategyResponseDict(TypedDict):
    repricer_strategy: NotRequired[str]
    strategy_collection_id: NotRequired[str]
    enabled: NotRequired[bool]
    enable_repricer_for_promotion: NotRequired[bool]
    restore_seller_price_without_target: NotRequired[bool]
    enable_buybox_meet_external: NotRequired[bool]
    compare_with3p_offer_only: NotRequired[bool]
    strategies: NotRequired[list[Strategy1Dict]]
