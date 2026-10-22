from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .filter1 import Filter1, Filter1Dict
from .search1 import Search1, Search1Dict
from .sort1 import Sort1, Sort1Dict


class V3GrowthReviewsAcceleratorItemsRequest(SdkBaseModel):
    search: Optional[list[Search1]] = UNSET
    """Defines the search criteria for filtering items. This allows searching by product name or SKU to match specific
    items in the marketplace.<br><b style='color:green;'>Market availability: US only</b>"""

    filter: Filter1
    """Specifies the filter request.<br><b style='color:green;'>Market availability: US only</b>"""

    sort: Optional[list[Sort1]] = UNSET
    """Specifies the sort request.<br><b style='color:green;'>Market availability: US only</b>"""


class V3GrowthReviewsAcceleratorItemsRequestDict(TypedDict):
    search: NotRequired[list[Search1Dict]]
    filter: Filter1Dict
    sort: NotRequired[list[Sort1Dict]]
