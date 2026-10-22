from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.rejection_codes1 import RejectionCodes1OrStr
from .filter_criteria5 import FilterCriteria5, FilterCriteria5Dict


class V3GrowthAssortmentRecommendationsRejectionsRequest(SdkBaseModel):
    recommendation_type: Literal["ITEM"] = Field(default="ITEM", alias="recommendationType")
    """<br><b style='color:green;'>Market availability: US | CA | MX</span></b>

    | Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ITEM | To reject list of recommended items | string |"""

    filter_criteria: Optional[FilterCriteria5] = Field(default=UNSET, alias="filterCriteria")
    """Different type of filters can be passed in this object.<br><b style='color:green;'>Market availability: US | CA |
    MX</span></b>"""

    item_recommendation_unique_ids: Optional[list[str]] = Field(default=UNSET, alias="itemRecommendationUniqueIds")
    """List of item recommendation unique ids to reject. The size of the list should not exceed 100. You cannot add
    filter criteria along with the itemRecommendationUniqueIds list <br><b style='color:green;'>Market availability: US
    | CA | MX</span></b>"""

    rejection_codes: RejectionCodes1OrStr = Field(alias="rejectionCodes")
    """List of rejection codes. <br><b style='color:green;'>Market availability: US, CA, MX</span></b>

    | Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | NOT_SELLING_THESE_ITEMS<br><b style='color:green;'>Market availability: US, CA, MX</span></b> | As a seller, I
        don’t intend to sell these items on Walmart | string |
    | NOT_SELLING_THESE_BRANDS<br><b style='color:green;'>Market availability: US, CA, MX</span></b> | As a seller, I
        don’t intend to sell these brands on Walmart | string |
    | NOT_SELLING_THESE_CATEGORIES<br><b style='color:green;'>Market availability: US only</span></b> | As a seller, I
        don’t intend to sell these categories on Walmart | string |
    | LIMITED_TO_OTHER_MARKETPLACE<br><b style='color:green;'>Market availability: US, CA, MX</span></b> | As a seller,
        I intend to sell the rejected items only on other marketplaces | string |
    | ALREADY_SELLING_ON_WALMART<br><b style='color:green;'>Market availability: US, CA, MX</span></b> | I am already
        selling these items on Walmart | string |
    | OTHER_REASON<br><b style='color:green;'>Market availability: US, CA, MX</span></b> | Other reason for rejecting
        the items. customRejectionMessage is mandatory to pass if rejectionCode is OTHER_REASON. | string |"""

    custom_rejection_message: Optional[str] = Field(default=UNSET, alias="customRejectionMessage")
    """Custom rejection message if the rejection code is OTHER_REASON. This is required only when the rejectionCodes has
    OTHER_REASON in the list. Maximum length of the message is 500. <br><b style='color:green;'>Market availability: US
    | CA | MX</span></b>"""


class V3GrowthAssortmentRecommendationsRejectionsRequestDict(TypedDict):
    recommendation_type: Literal["ITEM"]
    filter_criteria: NotRequired[FilterCriteria5Dict]
    item_recommendation_unique_ids: NotRequired[list[str]]
    rejection_codes: RejectionCodes1OrStr
    custom_rejection_message: NotRequired[str]
