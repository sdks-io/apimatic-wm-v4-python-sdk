from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SellerAccountableOtdDrivers(SdkBaseModel):
    """Seller accountable drivers, which impacting the on time delivery rate"""

    late_shipment_rate: Optional[float] = Field(default=UNSET, alias="lateShipmentRate")
    """Rate of orders impacted due to late shipment"""

    carrier_edd_later_than_edd_rate: Optional[float] = Field(default=UNSET, alias="carrierEDDLaterThanEDDRate")
    """Rate of orders delivered later than estimated delivery date"""

    late_handover_to_carrier_rate: Optional[float] = Field(default=UNSET, alias="lateHandoverToCarrierRate")
    """Rate of orders impacted due to late handover to carrier"""

    no_carrier_scan_rate: Optional[float] = Field(default=UNSET, alias="noCarrierScanRate")
    """Rate of orders impacted due to no carrier scan"""

    carrier_method_mismatch_rate: Optional[float] = Field(default=UNSET, alias="carrierMethodMismatchRate")
    """Rate of orders impacted due to shipping method mismatch"""

    ship_location_mismatch_rate: Optional[float] = Field(default=UNSET, alias="shipLocationMismatchRate")
    """Rate of orders impacted due to ship location mismatch"""


class SellerAccountableOtdDriversDict(TypedDict):
    late_shipment_rate: NotRequired[float]
    carrier_edd_later_than_edd_rate: NotRequired[float]
    late_handover_to_carrier_rate: NotRequired[float]
    no_carrier_scan_rate: NotRequired[float]
    carrier_method_mismatch_rate: NotRequired[float]
    ship_location_mismatch_rate: NotRequired[float]
