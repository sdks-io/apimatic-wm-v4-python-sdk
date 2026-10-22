from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .box_dimensions5 import BoxDimensions5, BoxDimensions5Dict
from .box_item10 import BoxItem10, BoxItem10Dict
from .from_address4 import FromAddress4, FromAddress4Dict
from .to_address1 import ToAddress1, ToAddress1Dict


class V3ShippingLabelsShippingEstimatesRequest(SdkBaseModel):
    box_dimensions: BoxDimensions5 = Field(alias="boxDimensions")
    """Dimensions and weight of the package being shipped. For CUSTOM_PACKAGE, all dimensions and weight are
    required."""

    deliver_by_date: Optional[str] = Field(default=UNSET, alias="deliverByDate")
    """Estimated delivery date."""

    ship_by_date: Optional[str] = Field(default=UNSET, alias="shipByDate")
    """ShipBy date."""

    from_address: FromAddress4 = Field(alias="fromAddress")
    """From address - Seller's fulfillment center address."""

    to_address: ToAddress1 = Field(alias="toAddress")
    """To Address - Customer's delivery address."""

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

    purchase_order_id: str = Field(alias="purchaseOrderId")
    """An unique identifier associated with the seller's purchase order."""

    box_items: list[BoxItem10] = Field(alias="boxItems")
    """boxItems - A list of items that the seller will be shipping in this package. Each item must correspond to a line
    item in the specified purchaseOrder. The lineId and SKU fields are used to uniquely identify the specific item being
    shipped."""

    add_ons: Optional[bool] = Field(default=UNSET, alias="addOns")
    """addOns flag. Pass 'true' to fetch all addOns cost and we support two add ons type: SIGNATURE and INSURANCE. To
    get Insurance Estimate, please provide purchaseOrderId and boxItems details. By default, The value of addOns will be
    false."""

    has_battery: Optional[bool] = Field(default=UNSET, alias="hasBattery")
    """hasBattery flag. Pass 'true' if the shipment consists of battery. This is a mandatory field for yanwen."""


class V3ShippingLabelsShippingEstimatesRequestDict(TypedDict):
    box_dimensions: BoxDimensions5Dict
    deliver_by_date: NotRequired[str]
    ship_by_date: NotRequired[str]
    from_address: FromAddress4Dict
    to_address: ToAddress1Dict
    carriers: NotRequired[list[str]]
    package_type: str
    include_services_not_meeting_delivery_promise: NotRequired[bool]
    purchase_order_id: str
    box_items: list[BoxItem10Dict]
    add_ons: NotRequired[bool]
    has_battery: NotRequired[bool]
