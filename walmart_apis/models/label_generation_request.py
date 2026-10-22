from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .box_dimensions1 import BoxDimensions1, BoxDimensions1Dict
from .box_item import BoxItem, BoxItemDict
from .enums.add_on import AddOnOrStr
from .from_address import FromAddress, FromAddressDict
from .return_address import ReturnAddress, ReturnAddressDict


class LabelGenerationRequest(SdkBaseModel):
    package_type: str = Field(alias="packageType")
    """Package Type. This value maps to 'packageTypeShortName' from Supported carrier package types API response."""

    box_dimensions: BoxDimensions1 = Field(alias="boxDimensions")
    """Box dimensions and weight for the shipping package."""

    box_items: list[BoxItem] = Field(alias="boxItems")
    """Box Items"""

    from_address: Optional[FromAddress] = Field(default=UNSET, alias="fromAddress")
    """From address"""

    purchase_order_id: str = Field(alias="purchaseOrderId")
    """Purchase order ID"""

    carrier_name: str = Field(alias="carrierName")
    """Carrier name. This value maps to 'shortName' from Supported carriers API response. Currently FedEx and USPS are
    supported carriers."""

    carrier_service_type: str = Field(alias="carrierServiceType")
    """Carrier service type. This value maps to 'serviceTypes.name' from Shipping Estimates API response"""

    add_ons: Optional[list[AddOnOrStr]] = Field(default=UNSET, alias="addOns")
    """Add-ons type. Add-ons can be opted during label generation for a shipping. Supported values for add-ons are
    INSURANCE and SIGNATURE. We support standard SIGNATURE Type for now."""

    return_address: Optional[ReturnAddress] = Field(default=UNSET, alias="returnAddress")
    """Return Address. This is only mandatory field for yanwen"""

    has_battery: Optional[bool] = Field(default=UNSET, alias="hasBattery")
    """hasBattery flag. Pass 'true' if the shipment consists of battery. This is a mandatory field for yanwen."""

    hazmat: Optional[bool] = UNSET
    """hazmat flag. Pass 'true' if the shipment consists of hazardous material."""

    account_type: Optional[str] = Field(default=UNSET, alias="accountType")
    """Account Type. This is a mandatory field in case of BYOA"""


class LabelGenerationRequestDict(TypedDict):
    package_type: str
    box_dimensions: BoxDimensions1Dict
    box_items: list[BoxItemDict]
    from_address: NotRequired[FromAddressDict]
    purchase_order_id: str
    carrier_name: str
    carrier_service_type: str
    add_ons: NotRequired[list[AddOnOrStr]]
    return_address: NotRequired[ReturnAddressDict]
    has_battery: NotRequired[bool]
    hazmat: NotRequired[bool]
    account_type: NotRequired[str]
