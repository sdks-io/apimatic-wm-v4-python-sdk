from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .box_dimensions3 import BoxDimensions3, BoxDimensions3Dict
from .box_item6 import BoxItem6, BoxItem6Dict
from .enums.add_on7 import AddOn7OrStr
from .from_address2 import FromAddress2, FromAddress2Dict
from .return_address1 import ReturnAddress1, ReturnAddress1Dict


class V3ShippingLabelsRequest(SdkBaseModel):
    package_type: str = Field(alias="packageType")
    """The package type. For example, CUSTOM_PACKAGE', 'FEDEX_ENVELOPE', or 'FEDEX_PAK'.

    <b style="color: green;">Market availability: Global"""

    box_dimensions: BoxDimensions3 = Field(alias="boxDimensions")
    """Dimensions and weight of the package being shipped. Used together with packageType. For FEDEX_PAK or
    FEDEX_ENVELOPE, length/height/width are predetermined by the carrier and only weight is required. For
    CUSTOM_PACKAGE, all dimensions and weight are required.

    <b style="color: green;">Market availability: Global</b>"""

    box_items: list[BoxItem6] = Field(alias="boxItems")
    """boxItems - this is a list of items that seller will be shipping in this package, all the items should be part of
    the purchaseOrder entered, lineId & SKU are used to identify the exact item being shipped. Quantity tells us how
    many of that item we are shipping, it should be <= the remaining unshipping quantity of the PO

    <b style="color: green;">Market availability: Global"""

    from_address: Optional[FromAddress2] = Field(default=UNSET, alias="fromAddress")
    """Defines the origin address from which the order will be shipped. This represents the seller’s fulfillment center
    location.

    <b style="color: green;">Market availability: US | CA | MX</b>"""

    purchase_order_id: str = Field(alias="purchaseOrderId")
    """Purchase Order Id.

    <b>Applicable to SWW and WPS.</b>

    <b style="color: green;">Market availability: US | CA | MX</b>"""

    carrier_name: str = Field(alias="carrierName")
    """The carrier name.

    For US: This value maps to the 'shortName' parameter from a Supported carriers API response.

    Supported values for US: FedEx and USPS.

    Supported values for MX and CA: FedEx.

    Supported values for CA: MailAmericas.

    Supported values for CL: CBT sellers can use 'MailAmericas'. Domestic sellers can use 'Enviame'.

    <b>Applicable to SWW.</b>



    <b style="color: green;">Market availability: US | CA | MX | CL </b>"""

    carrier_service_type: str = Field(alias="carrierServiceType")
    """The carrier service type.

    For US: This value maps to 'serviceTypes.name' parameter from Shipping Estimates API response

    Supported values for MX: 'FEDEX_INTERNATIONAL_PRIORITY' for fedExPak/fedExEnvelope package types,
    'FEDEX_INTERNATIONAL_ECONOMY', and 'FEDEX_INTERNATIONAL_GROUND'

    Supported values for CA: 'FEDEX_INTERNATIONAL_PRIORITY' for single fedExPak/fedExEnvelope package types,
    'FEDEX_INTERNATIONAL_ECONOMY', and 'FEDEX_INTERNATIONAL_GROUND'

    Supported values for CL: 'US_CL_MAIL_AMERICAS' and 'CN_CL_MAIL_AMERICAS'.

    <b>Applicable to SWW.</b>



    <strong style="color: green;">Market availability: Global</strong>"""

    add_ons: Optional[list[AddOn7OrStr]] = Field(default=UNSET, alias="addOns")
    """AddOns Type. AddOns can be opted during label generation for a shipping. Supported values for AddOns are
    INSURANCE and SIGNATURE. We support standard SIGNATURE Type for now.

    <b style="color: green;">Market availability: US only</b>"""

    return_address: Optional[ReturnAddress1] = Field(default=UNSET, alias="returnAddress")
    """Return Address. This parameter is mandatory for orders using ``Yanwen`` for the carrier.

    <b style="color: green;">Market availability: US only</b>"""

    has_battery: Optional[bool] = Field(default=UNSET, alias="hasBattery")
    """The status for if the order contains a battery. This is mandatory for order using ``Yanwen`` as the carrier.
    Possible values, ``true`` or ``false``.

    <b style="color: green;">Market availability: US only</b>"""

    hazmat: Optional[bool] = UNSET
    """The status for if the shipment contains hazardous material. Possible values, ``true`` or ``false``.

    <b style="color: green;">Market availability: US only</b>"""

    account_type: Optional[str] = Field(default=UNSET, alias="accountType")
    """Account Type - BYOA (bring your own account), this is an US only initiative where sellers can bring their own
    FedEx accounts for creating labels instead of using the walmart ones.

    <b style="color: green;">Market availability: US only</b>"""

    label_size: Optional[str] = Field(default=UNSET, alias="labelSize")
    """The size of the label. For example, A6,A8, LETTER_SIZE, or A4 for PDF response.

     Supported values for CL: 'LETTER_SIZE', 'A4', 'A6', 'A8' for MailAmericas

     Supported values for CA: A6, LETTER_SIZE or A4 for PDF response



    <b style="color: green;">Market availability: CA | CL</b>"""


class V3ShippingLabelsRequestDict(TypedDict):
    package_type: str
    box_dimensions: BoxDimensions3Dict
    box_items: list[BoxItem6Dict]
    from_address: NotRequired[FromAddress2Dict]
    purchase_order_id: str
    carrier_name: str
    carrier_service_type: str
    add_ons: NotRequired[list[AddOn7OrStr]]
    return_address: NotRequired[ReturnAddress1Dict]
    has_battery: NotRequired[bool]
    hazmat: NotRequired[bool]
    account_type: NotRequired[str]
    label_size: NotRequired[str]
