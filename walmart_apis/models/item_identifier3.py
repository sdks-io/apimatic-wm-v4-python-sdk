from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ItemIdentifier3(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: Global</b>"""

    sku: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: Global</b>"""

    offer_id: Optional[str] = Field(default=UNSET, alias="offerId")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    item_id: Optional[str] = Field(default=UNSET, alias="itemId")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    wpid: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: Global</b>"""

    product_type: Optional[str] = Field(default=UNSET, alias="productType")
    """<br><b style='color:green;'>Market availability: Global</b>"""


class ItemIdentifier3Dict(TypedDict):
    sku: NotRequired[str]
    offer_id: NotRequired[str]
    item_id: NotRequired[str]
    wpid: NotRequired[str]
    product_type: NotRequired[str]
