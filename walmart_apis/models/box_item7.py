from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BoxItem7(SdkBaseModel):
    """Box Items"""

    sku: Optional[str] = UNSET
    """The stock keeping unit of an item.

    <b style="color: green;">Market availability: Global</b>"""

    quantity: Optional[int] = UNSET
    """Quantity of the item.

    <b style="color: green;">Market availability: Global</b>"""

    line_number: Optional[str] = Field(default=UNSET, alias="lineNumber")
    """PO line number.

    <b style="color: green;">Market availability: Global</b>"""

    product_name: Optional[str] = Field(default=UNSET, alias="productName")
    """The name of the product. This parameter is required if carrier is opted as 'Yanwen' and also for shipping from
    India(IN) to United-States(US).

    <b style="color: green;">Market availability: US only</b>"""

    product_name_in_locale: Optional[str] = Field(default=UNSET, alias="productNameInLocale")
    """The name of the product in Mandarin. This parameter is required if carrier is opted as 'Yanwen'

    <b style="color: green;">Market availability: US only</b>"""

    hs_code: Optional[str] = Field(default=UNSET, alias="hsCode")
    """The HS code, Harmonized System code, is a six-digit numerical identifier used for classifying traded products
    worldwide. This is a mandatory field for India (IN) to United States (US) shipping

    <strong style="color: green;">Market availability: US only</strong>"""

    origin_state: Optional[str] = Field(default=UNSET, alias="originState")
    """Origin state. This field is mandatory for shipments from India (IN) to the United States (US).

    <b style="color: green;">Market availability: US only</b>"""

    origin_city: Optional[str] = Field(default=UNSET, alias="originCity")
    """Origin city. This field is mandatory for shipments from India (IN) to the United States (US).

    <b style="color: green;">Market availability: US only</b>"""

    country_of_origin: Optional[str] = Field(default=UNSET, alias="countryOfOrigin")
    """Country of origin. This field is mandatory for shipments from India (IN) to the United States (US).

    <b style="color: green;">Market availability: US only</b>"""


class BoxItem7Dict(TypedDict):
    sku: NotRequired[str]
    quantity: NotRequired[int]
    line_number: NotRequired[str]
    product_name: NotRequired[str]
    product_name_in_locale: NotRequired[str]
    hs_code: NotRequired[str]
    origin_state: NotRequired[str]
    origin_city: NotRequired[str]
    country_of_origin: NotRequired[str]
