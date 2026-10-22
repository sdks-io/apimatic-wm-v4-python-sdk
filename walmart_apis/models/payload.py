from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.claim_type import ClaimTypeOrStr


class Payload(SdkBaseModel):
    """Claim details."""

    purchase_order_no: str = Field(alias="purchaseOrderNo")
    """Marketplace purchase-order number associated with the item in this claim."""

    purchase_order_line_no: str = Field(alias="purchaseOrderLineNo")
    """Line number within the purchase order that maps to the claimed SKU."""

    sales_order_no: str = Field(alias="salesOrderNo")
    """Customer sales-order number for the shipment."""

    sales_order_line_no: str = Field(alias="salesOrderLineNo")
    """Line number within the sales order that maps to the claimed SKU."""

    fulfiller_line_id: str = Field(alias="fulfillerLineId")
    """Identifier for the fulfiller’s line item in the warehouse/fulfillment center manifest."""

    quantity: int
    """Number of units being claimed for this line."""

    return_order_id: str = Field(alias="returnOrderId")
    """Return-order ID that triggered or is linked to the claim."""

    claim_type: ClaimTypeOrStr = Field(alias="claimType")
    """Claim category: LIT (lost in transit), LAD (lost after delivery), or DAMAGED."""

    notes: Optional[str] = UNSET
    """Free-form claim notes from the seller."""


class PayloadDict(TypedDict):
    purchase_order_no: str
    purchase_order_line_no: str
    sales_order_no: str
    sales_order_line_no: str
    fulfiller_line_id: str
    quantity: int
    return_order_id: str
    claim_type: ClaimTypeOrStr
    notes: NotRequired[str]
