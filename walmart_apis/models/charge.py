from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .charge_per_unit import ChargePerUnit, ChargePerUnitDict
from .tax import Tax, TaxDict
from .variant_info import VariantInfo, VariantInfoDict


class Charge(SdkBaseModel):
    charge_category: Optional[str] = Field(default=UNSET, alias="chargeCategory")
    """The category type. (e.g., 'PRODUCT' or 'FEE').<br><b style='color:green;'>Market availability:US</b>"""

    charge_type: Optional[str] = Field(default=UNSET, alias="chargeType")
    """The category type. (e.g., 'PRODUCT' or 'FEE').<br><b style='color:green;'>Market availability: MX | CA |
    CL</b>"""

    charge_name: Optional[str] = Field(default=UNSET, alias="chargeName")
    """If chargeType is PRODUCT, chargeName is Item Price. If chargeType is SHIPPING, chargeName is Shipping.<br><b
    style='color:green;'>Market availability: US | MX</b>"""

    charge_per_unit: Optional[ChargePerUnit] = Field(default=UNSET, alias="chargePerUnit")
    """Price of One unit of item, in this order line.<br><b style='color:green;'>Market availability:US</b>"""

    is_discount: Optional[bool] = Field(default=UNSET, alias="isDiscount")
    """Is this charge a discount, which then needs to be subtracted from the refund.<br><b style='color:green;'>Market
    availability: US</b>"""

    is_billable: Optional[bool] = Field(default=UNSET, alias="isBillable")
    """Should this charge be included in the refund computation.<br><b style='color:green;'>Market availability:
    US</b>"""

    tax: Optional[list[Tax]] = UNSET
    """Taxes for each charge.<br><b style='color:green;'>Market availability: US | MX</b>"""

    references: Optional[list[VariantInfo]] = UNSET
    """Used only for 1P.<br><b style='color:green;'>Market availability: US | MX</b>"""


class ChargeDict(TypedDict):
    charge_category: NotRequired[str]
    charge_type: NotRequired[str]
    charge_name: NotRequired[str]
    charge_per_unit: NotRequired[ChargePerUnitDict]
    is_discount: NotRequired[bool]
    is_billable: NotRequired[bool]
    tax: NotRequired[list[TaxDict]]
    references: NotRequired[list[VariantInfoDict]]
