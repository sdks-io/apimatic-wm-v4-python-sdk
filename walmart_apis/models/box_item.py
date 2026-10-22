from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BoxItem(SdkBaseModel):
    """Box Items"""

    sku: str
    """sku of an item"""

    quantity: int
    """Quantity of Item"""

    line_number: str = Field(alias="lineNumber")
    """PO Line Number"""

    product_name: Optional[str] = Field(default=UNSET, alias="productName")
    """Name of the Product. This is a mandatory field if carrier is opted as 'Yanwen' and also for India(IN) to United
    States(US) shipping"""

    product_name_in_locale: Optional[str] = Field(default=UNSET, alias="productNameInLocale")
    """Name of the Product in Mandarin. This is a mandatory field if carrier is opted as 'Yanwen'"""

    hs_code: Optional[str] = Field(default=UNSET, alias="hsCode")
    """HS Code. This is a mandatory field for India(IN) to United States(US) shipping"""

    origin_state: Optional[str] = Field(default=UNSET, alias="originState")
    """Origin State. This is a mandatory field for India(IN) to United States(US) shipping"""

    origin_city: Optional[str] = Field(default=UNSET, alias="originCity")
    """Origin City. This is a mandatory field for India(IN) to United States(US) shipping"""

    country_of_origin: Optional[str] = Field(default=UNSET, alias="countryOfOrigin")
    """Country of Origin. This is a mandatory field for India(IN) to United States(US) shipping"""


class BoxItemDict(TypedDict):
    sku: str
    quantity: int
    line_number: str
    product_name: NotRequired[str]
    product_name_in_locale: NotRequired[str]
    hs_code: NotRequired[str]
    origin_state: NotRequired[str]
    origin_city: NotRequired[str]
    country_of_origin: NotRequired[str]
