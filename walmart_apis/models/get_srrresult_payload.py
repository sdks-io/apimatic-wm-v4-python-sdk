from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.cumulative_rate_trend4 import CumulativeRateTrend4OrStr
from .enums.risk_level import RiskLevelOrStr
from .seller_accountable_srr_drivers import SellerAccountableSrrDrivers, SellerAccountableSrrDriversDict


class GetSrrresultPayload(SdkBaseModel):
    report_duration: Optional[int] = Field(default=UNSET, alias="reportDuration")
    """Past number of days the metrics calculated"""

    updated_timestamp: Optional[str] = Field(default=UNSET, alias="updatedTimestamp")
    """Timestamp when metrics are calculated in ISO format"""

    cumulative_rate: Optional[float] = Field(default=UNSET, alias="cumulativeRate")
    """Cumulative seller response rate"""

    cumulative_rate_trend: Optional[CumulativeRateTrend4OrStr] = Field(default=UNSET, alias="cumulativeRateTrend")
    """Cumulative seller response rate trend"""

    impacted_customer_count: Optional[int] = Field(default=UNSET, alias="impactedCustomerCount")
    """Number of customers impacted"""

    standard: Optional[str] = UNSET
    """Minimum seller accountable seller response rate required as per Walmart standards"""

    risk_level: Optional[RiskLevelOrStr] = Field(default=UNSET, alias="riskLevel")
    """Risk level as per Walmart standards"""

    seller_accountable_drivers: Optional[SellerAccountableSrrDrivers] = Field(
        default=UNSET, alias="sellerAccountableDrivers"
    )
    """Seller accountable drivers, which impacting the seller response rate"""


class GetSrrresultPayloadDict(TypedDict):
    report_duration: NotRequired[int]
    updated_timestamp: NotRequired[str]
    cumulative_rate: NotRequired[float]
    cumulative_rate_trend: NotRequired[CumulativeRateTrend4OrStr]
    impacted_customer_count: NotRequired[int]
    standard: NotRequired[str]
    risk_level: NotRequired[RiskLevelOrStr]
    seller_accountable_drivers: NotRequired[SellerAccountableSrrDriversDict]
