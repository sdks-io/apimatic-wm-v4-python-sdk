from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .box_dimensions2 import BoxDimensions2, BoxDimensions2Dict
from .estimates_box_item import EstimatesBoxItem, EstimatesBoxItemDict
from .shipment_location import ShipmentLocation, ShipmentLocationDict
from .to_shipment_location import ToShipmentLocation, ToShipmentLocationDict


class EstimateShipmentRequestDto(SdkBaseModel):
    box_dimensions: BoxDimensions2 = Field(alias="boxDimensions")
    deliver_by_date: Optional[str] = Field(default=UNSET, alias="deliverByDate")
    """Estimated delivery date."""

    ship_by_date: Optional[str] = Field(default=UNSET, alias="shipByDate")
    """ShipBy date."""

    from_address: ShipmentLocation = Field(alias="fromAddress")
    """From address - Seller's fulfilment center address."""

    to_address: ToShipmentLocation = Field(alias="toAddress")
    """To Address - Customer's Delivery Address"""

    carriers: Optional[list[str]] = UNSET
    """Carriers List. This value maps to 'shortName' from All carriers API response.If not provided, it will fetch
    response for all service types."""

    package_type: str = Field(alias="packageType")
    """Package Type. This value maps to 'packageTypeShortName' from All carrier package types API response."""

    include_services_not_meeting_delivery_promise: Optional[bool] = Field(
        default=UNSET, alias="includeServicesNotMeetingDeliveryPromise"
    )
    """Delivery promise date flag. Pass 'false' if only services meeting promised delivery dates needs to be fetched,
    else 'true' to fetch all supported delivery dates"""

    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    """Purchase Order Id. This is a mandatory field for India(IN) to United States(US) shipping."""

    box_items: Optional[list[EstimatesBoxItem]] = Field(default=UNSET, alias="boxItems")
    """Box items. This is a mandatory field for India(IN) to United States(US) shipping"""

    add_ons: Optional[bool] = Field(default=UNSET, alias="addOns")
    """addOns flag. Pass 'true' to fetch all addOns cost and we support two add ons type: SIGNATURE and INSURANCE. To
    get Insurance Estimate, please provide purchaseOrderId and boxItems details. By default, The value of addOns will be
    false."""

    has_battery: Optional[bool] = Field(default=UNSET, alias="hasBattery")
    """hasBattery flag. Pass 'true' if the shipment consists of battery. This is a mandatory field for yanwen."""


class EstimateShipmentRequestDtoDict(TypedDict):
    box_dimensions: BoxDimensions2Dict
    deliver_by_date: NotRequired[str]
    ship_by_date: NotRequired[str]
    from_address: ShipmentLocationDict
    to_address: ToShipmentLocationDict
    carriers: NotRequired[list[str]]
    package_type: str
    include_services_not_meeting_delivery_promise: NotRequired[bool]
    purchase_order_id: NotRequired[str]
    box_items: NotRequired[list[EstimatesBoxItemDict]]
    add_ons: NotRequired[bool]
    has_battery: NotRequired[bool]
