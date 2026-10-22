from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item_weight import ItemWeight, ItemWeightDict


class Item2(SdkBaseModel):
    """An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item.<br><b
    style='color:green;'>Market availability: Global</b>"""

    condition: Optional[str] = UNSET
    """Information about the condition of the product.<br><b style='color:green;'>Market availability: US</b>"""

    offer_id: Optional[str] = Field(default=UNSET, alias="offerId")
    """The offerId associated.<br><b style='color:green;'>Market availability: MX | CA</b>"""

    product_name: Optional[str] = Field(default=UNSET, alias="productName")
    """The name of the product associated with the line item.<br><b style='color:green;'>Market availability:
    Global</b>"""

    sku: Optional[str] = UNSET
    """An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by
    the seller in the XSD file to refer to each item. Special characters hyphen (-), space ( ), and period (.) are not
    allowed.

    .<b style='color:green;'>Market availability: MX | CA</b>"""

    item_weight: Optional[ItemWeight] = Field(default=UNSET, alias="itemWeight")
    """itemWeight.<br><b style='color:green;'>Market availability: US</b>"""


class Item2Dict(TypedDict):
    condition: NotRequired[str]
    offer_id: NotRequired[str]
    product_name: NotRequired[str]
    sku: NotRequired[str]
    item_weight: NotRequired[ItemWeightDict]
