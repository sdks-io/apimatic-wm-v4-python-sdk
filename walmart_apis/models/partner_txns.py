from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PartnerTxns(SdkBaseModel):
    net_payable: Optional[float] = Field(default=UNSET, alias="netPayable")
    advance_payment: Optional[float] = Field(default=UNSET, alias="advancePayment")


class PartnerTxnsDict(TypedDict):
    net_payable: NotRequired[float]
    advance_payment: NotRequired[float]
