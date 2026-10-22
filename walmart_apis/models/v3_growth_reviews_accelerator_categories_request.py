from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.item_status10 import ItemStatus10OrStr


class V3GrowthReviewsAcceleratorCategoriesRequest(SdkBaseModel):
    item_status: Optional[ItemStatus10OrStr] = Field(default=UNSET, alias="itemStatus")
    """IRP status of the items.<br><b style='color:green;'>Market availability: US only</b>"""


class V3GrowthReviewsAcceleratorCategoriesRequestDict(TypedDict):
    item_status: NotRequired[ItemStatus10OrStr]
