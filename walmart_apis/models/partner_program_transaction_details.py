from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .adjustment_aggregate import AdjustmentAggregate, AdjustmentAggregateDict
from .partner_txns import PartnerTxns, PartnerTxnsDict
from .sale_refund_aggr import SaleRefundAggr, SaleRefundAggrDict
from .wfs_aggr import WfsAggr, WfsAggrDict


class PartnerProgramTransactionDetails(SdkBaseModel):
    sale_aggregate: Optional[SaleRefundAggr] = Field(default=UNSET, alias="saleAggregate")
    refund_details: Optional[SaleRefundAggr] = Field(default=UNSET, alias="refundDetails")
    adjustment_aggregate: Optional[AdjustmentAggregate] = Field(default=UNSET, alias="adjustmentAggregate")
    wfs: Optional[WfsAggr] = UNSET
    partner_txns: Optional[PartnerTxns] = Field(default=UNSET, alias="partnerTxns")


class PartnerProgramTransactionDetailsDict(TypedDict):
    sale_aggregate: NotRequired[SaleRefundAggrDict]
    refund_details: NotRequired[SaleRefundAggrDict]
    adjustment_aggregate: NotRequired[AdjustmentAggregateDict]
    wfs: NotRequired[WfsAggrDict]
    partner_txns: NotRequired[PartnerTxnsDict]
