from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .competitor_item_info import CompetitorItemInfo, CompetitorItemInfoDict
from .enums.demand_sales_trends import DemandSalesTrendsOrStr
from .enums.free_shipping1 import FreeShipping1OrStr
from .enums.item_availability_status import ItemAvailabilityStatusOrStr
from .enums.sales_insights import SalesInsightsOrStr
from .variant_info import VariantInfo, VariantInfoDict
from .walmart_item_info import WalmartItemInfo, WalmartItemInfoDict


class ItemDetails4(SdkBaseModel):
    """Details of the recommended item.<br><b style='color:green;'>Market availability: US only</span></b>"""

    title: Optional[str] = UNSET
    """Title of the recommended item"""

    brand: Optional[str] = UNSET
    """Brand of the recommended item"""

    category: Optional[str] = UNSET
    """Category of the recommended item"""

    product_type: Optional[str] = Field(default=UNSET, alias="productType")
    """Indicates the product type of an item that can be used to set up this item using Item Setup APIs or Item setup
    bulk upload."""

    gtin: Optional[str] = UNSET
    """GTIN of the recommended item"""

    upc: Optional[str] = UNSET
    """Universal Product Code (UPC) of the recommended item."""

    isbn: Optional[str] = UNSET
    """ISBN of the recommended item"""

    ean: Optional[str] = UNSET
    """European Article Number (EAN) of the recommended item."""

    item_availability_status: Optional[ItemAvailabilityStatusOrStr] = Field(
        default=UNSET, alias="itemAvailabilityStatus"
    )
    """Item availability status of the recommended item.

    | Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | EXISTING_IN_WALMART | Indicates that item is existing in Walmart. | string |
    | NEW_TO_WALMART | Indicates that item is new to Walmart. | string |"""

    potential_sales: Optional[str] = Field(default=UNSET, alias="potentialSales")
    """Indicates the potential revenue the recommended item can bring in over a year. This field does not promise the
    numbers indicated."""

    potential_sales_rank: Optional[str] = Field(default=UNSET, alias="potentialSalesRank")
    """Rank of an item, from 1 to 10 (1 being highest), that indicates the relative potential sales of a product in a
    category. This is an estimate based on customer demand, historical category sales and other data points."""

    is_top_go_get_item: Optional[bool] = Field(default=UNSET, alias="isTopGoGetItem")
    """Top Go‑Get Items are customer favorite items sellers are recommended to prioritize and bring to their Walmart
    Catalog."""

    sales_insights: Optional[SalesInsightsOrStr] = Field(default=UNSET, alias="salesInsights")
    """Tags that indicate why an item is in demand, helping sellers quickly assess customer interest and competitive
    signal. <br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    shopping_trends: OptionalNullable[list[str]] = Field(default=UNSET, alias="shoppingTrends")
    """This field is deprecated."""

    demand_sales_trends: Optional[DemandSalesTrendsOrStr] = Field(default=UNSET, alias="demandSalesTrends")
    """Indicates the months of the year when high demand is observed for the recommended item. The sequence of month is
    in the decreasing order of the high demand. The values are comma separated.

    | Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC | Months of the year. | string |"""

    search_keywords: Optional[list[str]] = Field(default=UNSET, alias="searchKeywords")
    """List of the most popular keywords that people have searched for, where the item shows up in the result set."""

    offer_count: Optional[float] = Field(default=UNSET, alias="offerCount")
    """Total number offers for this Item on Walmart."""

    free_shipping: Optional[FreeShipping1OrStr] = Field(default=UNSET, alias="freeShipping")
    """Indicates if the shipping is free for a recommended item which is a buy box winner."""

    rating: Optional[float] = UNSET
    """Average rating of the recommended item."""

    rating_count: Optional[float] = Field(default=UNSET, alias="ratingCount")
    """Total number of ratings for the recommended item."""

    is_primary_variant: Optional[bool] = Field(default=UNSET, alias="isPrimaryVariant")
    """Indicates whether the item is a primary variant."""

    variant_info: Optional[list[VariantInfo]] = Field(default=UNSET, alias="variantInfo")
    """List of variant details of the item."""

    walmart: Optional[WalmartItemInfo] = UNSET
    """Walmart's item information"""

    competitors: Optional[list[CompetitorItemInfo]] = UNSET
    """Competitor's item information"""


class ItemDetails4Dict(TypedDict):
    title: NotRequired[str]
    brand: NotRequired[str]
    category: NotRequired[str]
    product_type: NotRequired[str]
    gtin: NotRequired[str]
    upc: NotRequired[str]
    isbn: NotRequired[str]
    ean: NotRequired[str]
    item_availability_status: NotRequired[ItemAvailabilityStatusOrStr]
    potential_sales: NotRequired[str]
    potential_sales_rank: NotRequired[str]
    is_top_go_get_item: NotRequired[bool]
    sales_insights: NotRequired[SalesInsightsOrStr]
    shopping_trends: NotRequired[list[str] | None]
    demand_sales_trends: NotRequired[DemandSalesTrendsOrStr]
    search_keywords: NotRequired[list[str]]
    offer_count: NotRequired[float]
    free_shipping: NotRequired[FreeShipping1OrStr]
    rating: NotRequired[float]
    rating_count: NotRequired[float]
    is_primary_variant: NotRequired[bool]
    variant_info: NotRequired[list[VariantInfoDict]]
    walmart: NotRequired[WalmartItemInfoDict]
    competitors: NotRequired[list[CompetitorItemInfoDict]]
