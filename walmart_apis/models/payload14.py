from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .additional_attributes3 import AdditionalAttributes3, AdditionalAttributes3Dict
from .item_identifier3 import ItemIdentifier3, ItemIdentifier3Dict
from .max_sales_retail_price2 import MaxSalesRetailPrice2, MaxSalesRetailPrice2Dict
from .min_advt_price2 import MinAdvtPrice2, MinAdvtPrice2Dict
from .pricing_list2 import PricingList2, PricingList2Dict
from .rebate2 import Rebate2, Rebate2Dict


class Payload14(SdkBaseModel):
    item_identifier: ItemIdentifier3 = Field(alias="itemIdentifier")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    pricing_list: PricingList2 = Field(alias="pricingList")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    max_sales_retail_price: Optional[MaxSalesRetailPrice2] = Field(default=UNSET, alias="maxSalesRetailPrice")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    min_advt_price: Optional[MinAdvtPrice2] = Field(default=UNSET, alias="minAdvtPrice")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    rebate: Optional[Rebate2] = UNSET
    """<br><b style='color:green;'>Market availability: Global</b>"""

    additional_attributes: Optional[AdditionalAttributes3] = Field(default=UNSET, alias="additionalAttributes")
    """<br><b style='color:green;'>Market availability: Global</b>"""


class Payload14Dict(TypedDict):
    item_identifier: ItemIdentifier3Dict
    pricing_list: PricingList2Dict
    max_sales_retail_price: NotRequired[MaxSalesRetailPrice2Dict]
    min_advt_price: NotRequired[MinAdvtPrice2Dict]
    rebate: NotRequired[Rebate2Dict]
    additional_attributes: NotRequired[AdditionalAttributes3Dict]
