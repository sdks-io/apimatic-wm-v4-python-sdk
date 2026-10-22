from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BoxItem8(SdkBaseModel):
    """Box Items"""

    sku: str
    """sku of an item. <br/><b>Applicable to SWW and WPS.</span></b>"""

    quantity: int
    """Quantity of Item. <br/><b>Applicable to SWW and WPS.</span></b>"""

    country_of_origin: Optional[str] = Field(default=UNSET, alias="countryOfOrigin")
    """Country of origin (country code) of item.<br/><b>Applicable to SWW and WPS.</span></b>

    <b style="color: green;">Market availability: MX</b>"""

    line_number: str = Field(alias="lineNumber")
    """primeLineNo from CA order's response. <br/><b>Applicable to SWW and WPS.</span></b>"""


class BoxItem8Dict(TypedDict):
    sku: str
    quantity: int
    country_of_origin: NotRequired[str]
    line_number: str
