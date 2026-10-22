from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .competitor4 import Competitor4, Competitor4Dict
from .enums.demand_sales_trends4 import DemandSalesTrends4OrStr
from .enums.free_shipping import FreeShippingOrStr
from .enums.item_availability_status4 import ItemAvailabilityStatus4OrStr
from .enums.sales_insights import SalesInsightsOrStr
from .walmart4 import Walmart4, Walmart4Dict


class ItemDetails3(SdkBaseModel):
    """Details of the recommended item."""

    title: Optional[str] = UNSET
    """Title of the recommended item. <br><b style='color:green;'>Market availability: US | CA | MX</span></b>"""

    brand: Optional[str] = UNSET
    """Brand of the recommended item. <br><b style='color:green;'>Market availability: US | CA | MX</span></b>"""

    category: Optional[str] = UNSET
    """Category of the recommended item. <br><b style='color:green;'>Market availability: US | CA | MX</span></b>"""

    product_type: Optional[str] = Field(default=UNSET, alias="productType")
    """Indicates the product type of an item that can be used to set up this item using Item Setup APIs or Item setup
    bulk upload. <br><b style='color:green;'>Market availability: US only</span></b>"""

    gtin: Optional[str] = UNSET
    """GTIN of the recommended item. <br><b style='color:green;'>Market availability: US | CA | MX</span></b>"""

    upc: Optional[str] = UNSET
    """Universal Product Code (UPC) of the recommended item. <br><b style='color:green;'>Market availability: US | CA |
    MX</span></b>"""

    sku: Optional[str] = UNSET
    """Stock Keeping Unit (SKU) of the recommended item. <br><b style='color:green;'>Market availability: CA |
    MX</span></b>"""

    isbn: Optional[str] = UNSET
    """ISBN of the recommended item. <br><b style='color:green;'>Market availability: US only</span></b>"""

    ean: Optional[str] = UNSET
    """European Article Number (EAN) of the recommended item. <br><b style='color:green;'>Market availability: US
    only</span></b>"""

    item_availability_status: Optional[ItemAvailabilityStatus4OrStr] = Field(
        default=UNSET, alias="itemAvailabilityStatus"
    )
    """Item availability status of the recommended item. <br><b style='color:green;'>Market availability: US | CA |
    MX</span></b>

    | Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | EXISTING_IN_WALMART | Indicates that item is existing in Walmart. | string |
    | NEW_TO_WALMART | Indicates that item is new to Walmart. | string |"""

    potential_sales: Optional[str] = Field(default=UNSET, alias="potentialSales")
    """Indicates the potential revenue the recommended item can bring in over a year. This field does not promise the
    numbers indicated. <br><b style='color:green;'>Market availability: US | CA | MX</span></b>"""

    potential_sales_rank: Optional[str] = Field(default=UNSET, alias="potentialSalesRank")
    """Rank of an item, from 1 to 10 (1 being highest), that indicates the relative potential sales of a product in a
    category. This is an estimate based on customer demand, historical category sales and other data points. <br><b
    style='color:green;'>Market availability: US | CA | MX</span></b>"""

    sales_insights: Optional[SalesInsightsOrStr] = Field(default=UNSET, alias="salesInsights")
    """Tags that indicate why an item is in demand, helping sellers quickly assess customer interest and competitive
    signal. <br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    is_top_go_get_item: Optional[bool] = Field(default=UNSET, alias="isTopGoGetItem")
    """Top Go‑Get Items are customer favorite items sellers are recommended to prioritize and bring to their Walmart
    Catalog. <br><b style='color:green;'>Market availability: US | CA | MX</span></b>"""

    shopping_trends: OptionalNullable[list[str]] = Field(default=UNSET, alias="shoppingTrends")
    """This field is deprecated."""

    demand_sales_trends: Optional[DemandSalesTrends4OrStr] = Field(default=UNSET, alias="demandSalesTrends")
    """Indicates the months of the year when high demand is observed for the recommended item. The sequence of month is
    in the decreasing order of the high demand. The values are comma separated. <br><b style='color:green;'>Market
    availability: US only</span></b>

    | Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC | Months of the year. | string |"""

    search_keywords: Optional[list[str]] = Field(default=UNSET, alias="searchKeywords")
    """List of the most popular keywords that people have searched for, where the item shows up in the result set.
    <br><b style='color:green;'>Market availability: US only</span></b>"""

    offer_count: Optional[float] = Field(default=UNSET, alias="offerCount")
    """Total number offers for this Item on Walmart. <br><b style='color:green;'>Market availability: US
    only</span></b>"""

    free_shipping: Optional[FreeShippingOrStr] = Field(default=UNSET, alias="freeShipping")
    """Indicates if the shipping is free for a recommended item which is a buy box winner. <br><b
    style='color:green;'>Market availability: US | CA | MX</span></b>"""

    rating: Optional[float] = UNSET
    """Average rating of the recommended item. <br><b style='color:green;'>Market availability: US only</span></b>"""

    rating_count: Optional[float] = Field(default=UNSET, alias="ratingCount")
    """Total number of ratings for the recommended item. <br><b style='color:green;'>Market availability: US
    only</span></b>"""

    primary_variant_item_id: Optional[str] = Field(default=UNSET, alias="primaryVariantItemId")
    """Primary variant item ID. <br><b style='color:green;'>Market availability: US only</span></b>"""

    has_variants: Optional[bool] = Field(default=UNSET, alias="hasVariants")
    """Indicates to ensure whether the item has variants or not. If it is <br><b style='color:green;'>Market
    availability: US only</span></b>"""

    walmart: Optional[Walmart4] = UNSET
    """Walmart's item information. <br><b style='color:green;'>Market availability: US | CA | MX</span></b>"""

    competitors: Optional[list[Competitor4]] = UNSET
    """Competitor's item information."""


class ItemDetails3Dict(TypedDict):
    title: NotRequired[str]
    brand: NotRequired[str]
    category: NotRequired[str]
    product_type: NotRequired[str]
    gtin: NotRequired[str]
    upc: NotRequired[str]
    sku: NotRequired[str]
    isbn: NotRequired[str]
    ean: NotRequired[str]
    item_availability_status: NotRequired[ItemAvailabilityStatus4OrStr]
    potential_sales: NotRequired[str]
    potential_sales_rank: NotRequired[str]
    sales_insights: NotRequired[SalesInsightsOrStr]
    is_top_go_get_item: NotRequired[bool]
    shopping_trends: NotRequired[list[str] | None]
    demand_sales_trends: NotRequired[DemandSalesTrends4OrStr]
    search_keywords: NotRequired[list[str]]
    offer_count: NotRequired[float]
    free_shipping: NotRequired[FreeShippingOrStr]
    rating: NotRequired[float]
    rating_count: NotRequired[float]
    primary_variant_item_id: NotRequired[str]
    has_variants: NotRequired[bool]
    walmart: NotRequired[Walmart4Dict]
    competitors: NotRequired[list[Competitor4Dict]]
