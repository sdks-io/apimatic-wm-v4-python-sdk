from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Item1(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US</b>"""

    item_id: Optional[str] = Field(default=UNSET, alias="itemId")
    """<br><b style='color:green;'>Market availability: US</b>"""

    product_name: Optional[str] = Field(default=UNSET, alias="productName")
    """<br><b style='color:green;'>Market availability: US</b>"""

    product_url: Optional[str] = Field(default=UNSET, alias="productUrl")
    """<br><b style='color:green;'>Market availability: US</b>"""

    product_image_url: Optional[str] = Field(default=UNSET, alias="productImageUrl")
    """<br><b style='color:green;'>Market availability: US</b>"""

    sku_id: Optional[str] = Field(default=UNSET, alias="skuId")
    """<br><b style='color:green;'>Market availability: US</b>"""

    current_price: Optional[float] = Field(default=UNSET, alias="currentPrice")
    """<br><b style='color:green;'>Market availability: US</b>"""

    target_price: Optional[float] = Field(default=UNSET, alias="targetPrice")
    """<br><b style='color:green;'>Market availability: US</b>"""

    shipping_price: Optional[float] = Field(default=UNSET, alias="shippingPrice")
    """<br><b style='color:green;'>Market availability: US</b>"""

    incentive_type: Optional[str] = Field(default=UNSET, alias="incentiveType")
    """<br><b style='color:green;'>Market availability: US</b>"""

    base_referral_fee: Optional[float] = Field(default=UNSET, alias="baseReferralFee")
    """<br><b style='color:green;'>Market availability: US</b>"""

    reduced_referral_fee: Optional[float] = Field(default=UNSET, alias="reducedReferralFee")
    """<br><b style='color:green;'>Market availability: US</b>"""

    enrollment_type: Optional[str] = Field(default=UNSET, alias="enrollmentType")
    """<br><b style='color:green;'>Market availability: US</b>"""

    enrollment_date: Optional[str] = Field(default=UNSET, alias="enrollmentDate")
    """<br><b style='color:green;'>Market availability: US</b>"""

    incentive_status: Optional[str] = Field(default=UNSET, alias="incentiveStatus")
    """<br><b style='color:green;'>Market availability: US</b>"""

    inventory_count: Optional[float] = Field(default=UNSET, alias="inventoryCount")
    """<br><b style='color:green;'>Market availability: US</b>"""

    start_date: Optional[str] = Field(default=UNSET, alias="startDate")
    """<br><b style='color:green;'>Market availability: US</b>"""

    expiration_date: Optional[str] = Field(default=UNSET, alias="expirationDate")
    """<br><b style='color:green;'>Market availability: US</b>"""

    incentive_id: Optional[str] = Field(default=UNSET, alias="incentiveId")
    """<br><b style='color:green;'>Market availability: US</b>"""


class Item1Dict(TypedDict):
    item_id: NotRequired[str]
    product_name: NotRequired[str]
    product_url: NotRequired[str]
    product_image_url: NotRequired[str]
    sku_id: NotRequired[str]
    current_price: NotRequired[float]
    target_price: NotRequired[float]
    shipping_price: NotRequired[float]
    incentive_type: NotRequired[str]
    base_referral_fee: NotRequired[float]
    reduced_referral_fee: NotRequired[float]
    enrollment_type: NotRequired[str]
    enrollment_date: NotRequired[str]
    incentive_status: NotRequired[str]
    inventory_count: NotRequired[float]
    start_date: NotRequired[str]
    expiration_date: NotRequired[str]
    incentive_id: NotRequired[str]
