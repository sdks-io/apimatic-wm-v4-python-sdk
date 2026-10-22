from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class NonAccountableCancellationsDrivers(SdkBaseModel):
    """Non Accountable drivers, which impacting the cancellations rate"""

    customer_req_rate: Optional[float] = Field(default=UNSET, alias="customerReqRate")
    """Rate of orders cancelled due customer request"""

    customer_fraud_rate: Optional[float] = Field(default=UNSET, alias="customerFraudRate")
    """Rate of orders cancelled due customer fraud"""

    miscellaneous_rate: Optional[float] = Field(default=UNSET, alias="miscellaneousRate")
    """Rate of orders cancelled due to miscellaneous reasons"""


class NonAccountableCancellationsDriversDict(TypedDict):
    customer_req_rate: NotRequired[float]
    customer_fraud_rate: NotRequired[float]
    miscellaneous_rate: NotRequired[float]
