from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SellerAccountableVtrDrivers(SdkBaseModel):
    """Seller accountable drivers, which impacting the valid tracking rate"""

    misleading_tracking_rate: Optional[float] = Field(default=UNSET, alias="misleadingTrackingRate")
    """Total rate of orders with misleading tracking information"""

    non_integrated_carrier_rate: Optional[float] = Field(default=UNSET, alias="nonIntegratedCarrierRate")
    """Total rate of orders with non Integrated Carriers"""

    invalid_tracking_id_rate: Optional[float] = Field(default=UNSET, alias="invalidTrackingIdRate")
    """Total rate of orders with invalid tracking Id"""

    invalid_tracking_url_rate: Optional[float] = Field(default=UNSET, alias="invalidTrackingUrlRate")
    """Total rate of orders with invalid tracking url"""

    no_carrier_scan_rate: Optional[float] = Field(default=UNSET, alias="noCarrierScanRate")
    """Total rate of orders with no Carrier Scan"""


class SellerAccountableVtrDriversDict(TypedDict):
    misleading_tracking_rate: NotRequired[float]
    non_integrated_carrier_rate: NotRequired[float]
    invalid_tracking_id_rate: NotRequired[float]
    invalid_tracking_url_rate: NotRequired[float]
    no_carrier_scan_rate: NotRequired[float]
