from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.cumulative_rate_trend import CumulativeRateTrendOrStr
from .enums.risk_level import RiskLevelOrStr
from .enums.shipping_method import ShippingMethodOrStr
from .non_accountable_vtr_drivers import NonAccountableVtrDrivers, NonAccountableVtrDriversDict
from .seller_accountable_vtr_drivers import SellerAccountableVtrDrivers, SellerAccountableVtrDriversDict


class GetVtrResultPayload(SdkBaseModel):
    report_duration: Optional[int] = Field(default=UNSET, alias="reportDuration")
    """Past number of days the metrics calculated"""

    updated_timestamp: Optional[str] = Field(default=UNSET, alias="updatedTimestamp")
    """Timestamp when metrics are calculated in ISO format"""

    shipping_method: Optional[ShippingMethodOrStr] = Field(default=UNSET, alias="shippingMethod")
    """shipping methods used to calculate these metrics"""

    cumulative_rate: Optional[float] = Field(default=UNSET, alias="cumulativeRate")
    """Cumulative valid tracking rate"""

    cumulative_rate_trend: Optional[CumulativeRateTrendOrStr] = Field(default=UNSET, alias="cumulativeRateTrend")
    """Cumulative valid tracking rate trend"""

    impacted_customer_count: Optional[int] = Field(default=UNSET, alias="impactedCustomerCount")
    """Number of customers impacted"""

    standard: Optional[str] = UNSET
    """Minimum seller accountable valid tracking rate required as per Walmart standards"""

    risk_level: Optional[RiskLevelOrStr] = Field(default=UNSET, alias="riskLevel")
    """Risk level as per Walmart standards"""

    seller_accountable_drivers: Optional[SellerAccountableVtrDrivers] = Field(
        default=UNSET, alias="sellerAccountableDrivers"
    )
    """Seller accountable drivers, which impacting the valid tracking rate"""

    non_accountable_drivers: Optional[NonAccountableVtrDrivers] = Field(default=UNSET, alias="nonAccountableDrivers")
    """Non Accountable drivers, which impacting the valid tracking rate"""


class GetVtrResultPayloadDict(TypedDict):
    report_duration: NotRequired[int]
    updated_timestamp: NotRequired[str]
    shipping_method: NotRequired[ShippingMethodOrStr]
    cumulative_rate: NotRequired[float]
    cumulative_rate_trend: NotRequired[CumulativeRateTrendOrStr]
    impacted_customer_count: NotRequired[int]
    standard: NotRequired[str]
    risk_level: NotRequired[RiskLevelOrStr]
    seller_accountable_drivers: NotRequired[SellerAccountableVtrDriversDict]
    non_accountable_drivers: NotRequired[NonAccountableVtrDriversDict]
