from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .quality_score2 import QualityScore2, QualityScore2Dict
from .score_details2 import ScoreDetails2, ScoreDetails2Dict
from .stats2 import Stats2, Stats2Dict


class Payload11(SdkBaseModel):
    product_id: Optional[str] = Field(default=UNSET, alias="productId")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    score_details: Optional[ScoreDetails2] = Field(default=UNSET, alias="scoreDetails")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    wfs_enabled: Optional[str] = Field(default=UNSET, alias="wfsEnabled")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    priority: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    product_name: Optional[str] = Field(default=UNSET, alias="productName")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    item_id: Optional[str] = Field(default=UNSET, alias="itemId")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    seller_id: Optional[str] = Field(default=UNSET, alias="sellerId")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    page_views: Optional[str] = Field(default=UNSET, alias="pageViews")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    stats: Optional[Stats2] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    image_ur_l: Optional[str] = Field(default=UNSET, alias="imageUrL")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    quality_score: Optional[QualityScore2] = Field(default=UNSET, alias="qualityScore")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    offer_id: Optional[str] = Field(default=UNSET, alias="offerId")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    sku: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    category: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    post_purchase_issues: Optional[str] = Field(default=UNSET, alias="postPurchaseIssues")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    product_type: Optional[str] = Field(default=UNSET, alias="productType")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    condition: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    fast_shipping_regions_count: Optional[int] = Field(default=UNSET, alias="fastShippingRegionsCount")
    """<br><b style='color:green;'>Market availability: US</b>"""

    free_shipping_regions_count: Optional[int] = Field(default=UNSET, alias="freeShippingRegionsCount")
    """<br><b style='color:green;'>Market availability: US</b>"""

    fast_shipping_flag: Optional[int] = Field(default=UNSET, alias="fastShippingFlag")
    """<br><b style='color:green;'>Market availability: US</b>"""

    free_shipping_flag: Optional[int] = Field(default=UNSET, alias="freeShippingFlag")
    """<br><b style='color:green;'>Market availability: US</b>"""

    last30_days_conversion_rate: Optional[float] = Field(default=UNSET, alias="last30DaysConversionRate")
    """<br><b style='color:green;'>Market availability: US</b>"""

    last30_days_page_views: Optional[int] = Field(default=UNSET, alias="last30DaysPageViews")
    """<br><b style='color:green;'>Market availability: US</b>"""

    gmv: Optional[float] = UNSET
    """<br><b style='color:green;'>Market availability: US</b>"""

    is_customer_favorites: Optional[bool] = Field(default=UNSET, alias="isCustomerFavorites")
    """<br><b style='color:green;'>Market availability: US</b>"""

    is_in_stock: Optional[bool] = Field(default=UNSET, alias="isInStock")
    """<br><b style='color:green;'>Market availability: US</b>"""

    is_fast_and_free_shipping: Optional[bool] = Field(default=UNSET, alias="isFastAndFreeShipping")
    """<br><b style='color:green;'>Market availability: US</b>"""


class Payload11Dict(TypedDict):
    product_id: NotRequired[str]
    score_details: NotRequired[ScoreDetails2Dict]
    wfs_enabled: NotRequired[str]
    priority: NotRequired[str]
    product_name: NotRequired[str]
    item_id: NotRequired[str]
    seller_id: NotRequired[str]
    page_views: NotRequired[str]
    stats: NotRequired[Stats2Dict]
    image_ur_l: NotRequired[str]
    quality_score: NotRequired[QualityScore2Dict]
    offer_id: NotRequired[str]
    sku: NotRequired[str]
    category: NotRequired[str]
    post_purchase_issues: NotRequired[str]
    product_type: NotRequired[str]
    condition: NotRequired[str]
    fast_shipping_regions_count: NotRequired[int]
    free_shipping_regions_count: NotRequired[int]
    fast_shipping_flag: NotRequired[int]
    free_shipping_flag: NotRequired[int]
    last30_days_conversion_rate: NotRequired[float]
    last30_days_page_views: NotRequired[int]
    gmv: NotRequired[float]
    is_customer_favorites: NotRequired[bool]
    is_in_stock: NotRequired[bool]
    is_fast_and_free_shipping: NotRequired[bool]
