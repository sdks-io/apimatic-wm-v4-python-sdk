from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BoxItem6(SdkBaseModel):
    """Box Items"""

    sku: str
    """The item sku.

    <b style="color: green;">Market availability: Global"""

    quantity: int
    """Number of items.

    <b style="color: green;">Market availability: Global"""

    line_number: str = Field(alias="lineNumber")
    """PO Line Number

    <b style="color: green;">Market availability: Global"""

    product_name: Optional[str] = Field(default=UNSET, alias="productName")
    """The name of the product. This parameter is required if carrier is opted as 'Yanwen' and also for shipping from
    India(IN) to United-States(US).

    <b style="color: green;">Market availability: US only"""

    product_name_in_locale: Optional[str] = Field(default=UNSET, alias="productNameInLocale")
    """The name of the product in Mandarin. This parameter is required if carrier is opted as 'Yanwen'.

    <b style="color: green;">Market availability: US only"""

    hs_code: Optional[str] = Field(default=UNSET, alias="hsCode")
    """HS Code. This is a mandatory field for India (IN) to United States (US) shipping

    <b style="color: green;">Market availability: US only</b>"""

    origin_state: Optional[str] = Field(default=UNSET, alias="originState")
    """Origin State. This is a mandatory field for India (IN) to United States (US) shipping

    <b style="color: green;">Market availability: US only</b>"""

    origin_city: Optional[str] = Field(default=UNSET, alias="originCity")
    """Origin City. This is a mandatory field for India (IN) to United States (US) shipping

    <b style="color: green;">Market availability: US only</b>"""

    country_of_origin: Optional[str] = Field(default=UNSET, alias="countryOfOrigin")
    """Country of Origin. This is a mandatory field for India (IN) to United States (US) shipping

    <b style="color: green;">Market availability: US | CA | MX</b>"""


class BoxItem6Dict(TypedDict):
    sku: str
    quantity: int
    line_number: str
    product_name: NotRequired[str]
    product_name_in_locale: NotRequired[str]
    hs_code: NotRequired[str]
    origin_state: NotRequired[str]
    origin_city: NotRequired[str]
    country_of_origin: NotRequired[str]
