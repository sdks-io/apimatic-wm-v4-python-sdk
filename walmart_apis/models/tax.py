from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .excess_tax import ExcessTax, ExcessTaxDict
from .tax_per_unit import TaxPerUnit, TaxPerUnitDict


class Tax(SdkBaseModel):
    tax_name: Optional[str] = Field(default=UNSET, alias="taxName")
    """Name of the tax.<br><b style='color:green;'>Market availability: US,MX</b>"""

    excess_tax: Optional[ExcessTax] = Field(default=UNSET, alias="excessTax")
    """Amount of excess tax in the order line.<br><b style='color:green;'>Market availability: US </b>"""

    tax_per_unit: Optional[TaxPerUnit] = Field(default=UNSET, alias="taxPerUnit")
    """Price of One unit of item, in this order line.<br><b style='color:green;'>Market availability: US</b>"""


class TaxDict(TypedDict):
    tax_name: NotRequired[str]
    excess_tax: NotRequired[ExcessTaxDict]
    tax_per_unit: NotRequired[TaxPerUnitDict]
