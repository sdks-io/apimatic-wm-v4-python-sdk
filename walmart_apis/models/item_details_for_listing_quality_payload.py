from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .quality_score import QualityScore, QualityScoreDict
from .score_details import ScoreDetails, ScoreDetailsDict
from .stats import Stats, StatsDict


class ItemDetailsForListingQualityPayload(SdkBaseModel):
    product_id: Optional[str] = Field(default=UNSET, alias="productId")
    score_details: Optional[ScoreDetails] = Field(default=UNSET, alias="scoreDetails")
    wfs_enabled: Optional[str] = Field(default=UNSET, alias="wfsEnabled")
    priority: Optional[str] = UNSET
    product_name: Optional[str] = Field(default=UNSET, alias="productName")
    item_id: Optional[str] = Field(default=UNSET, alias="itemId")
    seller_id: Optional[str] = Field(default=UNSET, alias="sellerId")
    page_views: Optional[str] = Field(default=UNSET, alias="pageViews")
    stats: Optional[Stats] = UNSET
    image_ur_l: Optional[str] = Field(default=UNSET, alias="imageUrL")
    quality_score: Optional[QualityScore] = Field(default=UNSET, alias="qualityScore")
    offer_id: Optional[str] = Field(default=UNSET, alias="offerId")
    sku: Optional[str] = UNSET
    category: Optional[str] = UNSET
    post_purchase_issues: Optional[str] = Field(default=UNSET, alias="postPurchaseIssues")
    product_type: Optional[str] = Field(default=UNSET, alias="productType")
    condition: Optional[str] = UNSET
    fast_shipping_regions_count: Optional[int] = Field(default=UNSET, alias="fastShippingRegionsCount")
    free_shipping_regions_count: Optional[int] = Field(default=UNSET, alias="freeShippingRegionsCount")
    fast_shipping_flag: Optional[int] = Field(default=UNSET, alias="fastShippingFlag")
    free_shipping_flag: Optional[int] = Field(default=UNSET, alias="freeShippingFlag")
    last30_days_conversion_rate: Optional[float] = Field(default=UNSET, alias="last30DaysConversionRate")
    last30_days_page_views: Optional[int] = Field(default=UNSET, alias="last30DaysPageViews")
    gmv: Optional[float] = UNSET
    is_customer_favorites: Optional[bool] = Field(default=UNSET, alias="isCustomerFavorites")
    is_in_stock: Optional[bool] = Field(default=UNSET, alias="isInStock")
    is_fast_and_free_shipping: Optional[bool] = Field(default=UNSET, alias="isFastAndFreeShipping")


class ItemDetailsForListingQualityPayloadDict(TypedDict):
    product_id: NotRequired[str]
    score_details: NotRequired[ScoreDetailsDict]
    wfs_enabled: NotRequired[str]
    priority: NotRequired[str]
    product_name: NotRequired[str]
    item_id: NotRequired[str]
    seller_id: NotRequired[str]
    page_views: NotRequired[str]
    stats: NotRequired[StatsDict]
    image_ur_l: NotRequired[str]
    quality_score: NotRequired[QualityScoreDict]
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
