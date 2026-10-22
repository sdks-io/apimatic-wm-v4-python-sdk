from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .partner_program_acc_summary import PartnerProgramAccSummary, PartnerProgramAccSummaryDict
from .partner_program_transaction_details import PartnerProgramTransactionDetails, PartnerProgramTransactionDetailsDict
from .seller_info import SellerInfo, SellerInfoDict


class PartnerProgramStatementDo(SdkBaseModel):
    outstanding_mca_balance: Optional[float] = Field(default=UNSET, alias="outstandingMCABalance")
    seller_info: Optional[SellerInfo] = Field(default=UNSET, alias="sellerInfo")
    account_summary: Optional[PartnerProgramAccSummary] = Field(default=UNSET, alias="accountSummary")
    transaction_details: Optional[PartnerProgramTransactionDetails] = Field(default=UNSET, alias="transactionDetails")


class PartnerProgramStatementDoDict(TypedDict):
    outstanding_mca_balance: NotRequired[float]
    seller_info: NotRequired[SellerInfoDict]
    account_summary: NotRequired[PartnerProgramAccSummaryDict]
    transaction_details: NotRequired[PartnerProgramTransactionDetailsDict]
