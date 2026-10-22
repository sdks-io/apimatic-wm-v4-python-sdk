from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SaleRefundAggr(SdkBaseModel):
    product_price: Optional[float] = Field(default=UNSET, alias="productPrice")
    shipping: Optional[float] = UNSET
    net_tax_collected: Optional[float] = Field(default=UNSET, alias="netTaxCollected")
    product_tax_collected: Optional[float] = Field(default=UNSET, alias="productTaxCollected")
    shipping_tax_collected: Optional[float] = Field(default=UNSET, alias="shippingTaxCollected")
    net_tax_withheld: Optional[float] = Field(default=UNSET, alias="netTaxWithheld")
    product_tax_withheld: Optional[float] = Field(default=UNSET, alias="productTaxWithheld")
    shipping_tax_withheld: Optional[float] = Field(default=UNSET, alias="shippingTaxWithheld")
    net_fee_collected: Optional[float] = Field(default=UNSET, alias="netFeeCollected")
    net_fee_withheld: Optional[float] = Field(default=UNSET, alias="netFeeWithheld")
    net_comm: Optional[float] = Field(default=UNSET, alias="netComm")
    net_payable: Optional[float] = Field(default=UNSET, alias="netPayable")
    above_cap: Optional[float] = Field(default=UNSET, alias="aboveCap")
    wfs_shipping: Optional[float] = Field(default=UNSET, alias="wfsShipping")
    wfs_shippping_tax: Optional[float] = Field(default=UNSET, alias="wfsShipppingTax")
    total_base_commission: Optional[float] = Field(default=UNSET, alias="totalBaseCommission")
    commission_savings: Optional[float] = Field(default=UNSET, alias="commissionSavings")


class SaleRefundAggrDict(TypedDict):
    product_price: NotRequired[float]
    shipping: NotRequired[float]
    net_tax_collected: NotRequired[float]
    product_tax_collected: NotRequired[float]
    shipping_tax_collected: NotRequired[float]
    net_tax_withheld: NotRequired[float]
    product_tax_withheld: NotRequired[float]
    shipping_tax_withheld: NotRequired[float]
    net_fee_collected: NotRequired[float]
    net_fee_withheld: NotRequired[float]
    net_comm: NotRequired[float]
    net_payable: NotRequired[float]
    above_cap: NotRequired[float]
    wfs_shipping: NotRequired[float]
    wfs_shippping_tax: NotRequired[float]
    total_base_commission: NotRequired[float]
    commission_savings: NotRequired[float]
