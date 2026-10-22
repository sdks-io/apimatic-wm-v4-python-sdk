from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.locale import Locale, LocaleDict


class MpitemFeedHeader(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: Global</b>"""

    business_unit: str = Field(alias="businessUnit")
    """Business unit identifier matching the target market. For example, use WALMART_US for the US market.<br><b
    style='color:green;'>Market availability: US</b>"""

    sub_category: str = Field(alias="subCategory")
    """ItemFeed subcategory for price update.<br><b style='color:green;'>Market availability: CA | MX | CL</b>"""

    mart: str
    """The mart ID for the various markets are WALMART_CA for CA, WALMART_MEXICO for MX, and WALMART_CHILE for
    CL..<br><b style='color:green;'>Market availability: CA | MX | CL</b>"""

    feed_type: str = Field(alias="feedType")
    """The type of feed for this request.<br><b style='color:green;'>Market availability: CA | MX | CL</b>"""

    process_mode: Optional[str] = Field(default=UNSET, alias="processMode")
    """The feed processing behavior. Use REPLACE to overwrite existing values.<br><b style='color:green;'>Market
    availability: CA | MX | CL</b>"""

    locale: Locale
    """The market specific locale. Allowed values by market include: en for US, es for MX and CL, and en and fr for
    CA.<br><b style='color:green;'>Market availability: Global</b>"""

    version: str
    """The feed schema version. The values vary by region. 2.0.20240126-12_25_52-api for US, 5.0.20250801-18_47_55 for
    CA, MX and CL.<br><b style='color:green;'>Market availability: Global</b>"""

    subset: str
    """Origin of the data. Use External for partner submitted feeds.<br><b style='color:green;'>Market availability: CA
    | MX | CL</b>"""

    tenant: str
    """The tenant identifier for the marketplace. For example, use WALMART_CA for CA, WALMART_MEXICO for MX, and
    WALMART_CHILE for CL.<br><b style='color:green;'>Market availability: CA | MX | CL</b>"""


class MpitemFeedHeaderDict(TypedDict):
    business_unit: str
    sub_category: str
    mart: str
    feed_type: str
    process_mode: NotRequired[str]
    locale: LocaleDict
    version: str
    subset: str
    tenant: str
