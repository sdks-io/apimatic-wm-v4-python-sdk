from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SellerAccountableSrrDrivers(SdkBaseModel):
    """Seller accountable drivers, which impacting the seller response rate"""

    miscellaneous_rate: Optional[float] = Field(default=UNSET, alias="miscellaneousRate")
    """Seller response rate for miscellaneous customer enquires"""

    cancellation_rate: Optional[float] = Field(default=UNSET, alias="cancellationRate")
    """Seller response rate for customer enquires regarding cancellations"""

    feedback_rate: Optional[float] = Field(default=UNSET, alias="feedbackRate")
    """Seller response rate for customer feedback"""

    item_issue_rate: Optional[float] = Field(default=UNSET, alias="itemIssueRate")
    """Seller response rate for customer enquires regarding item issues"""

    returns_refunds_rate: Optional[float] = Field(default=UNSET, alias="returnsRefundsRate")
    """Seller response rate for customer enquires regarding returns and refunds"""

    track_order_rate: Optional[float] = Field(default=UNSET, alias="trackOrderRate")
    """Seller response rate for customer enquires regarding order tracking"""


class SellerAccountableSrrDriversDict(TypedDict):
    miscellaneous_rate: NotRequired[float]
    cancellation_rate: NotRequired[float]
    feedback_rate: NotRequired[float]
    item_issue_rate: NotRequired[float]
    returns_refunds_rate: NotRequired[float]
    track_order_rate: NotRequired[float]
