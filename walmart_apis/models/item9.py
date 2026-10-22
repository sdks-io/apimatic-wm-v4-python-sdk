from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Item9(SdkBaseModel):
    """Items"""

    item_id: str = Field(alias="itemId")
    """Specifies the item identifier.<br><b style='color:green;'>Market availability: US only</b>"""

    target_reviews: Optional[int] = Field(default=UNSET, alias="targetReviews")
    """Custom target number of reviews requested to be collected for the item. Default is 5.<br><b
    style='color:green;'>Market availability: US only</b>"""


class Item9Dict(TypedDict):
    item_id: str
    target_reviews: NotRequired[int]
