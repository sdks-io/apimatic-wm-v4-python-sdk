from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .box_item8 import BoxItem8, BoxItem8Dict
from .from_address3 import FromAddress3, FromAddress3Dict
from .package_dimension import PackageDimension, PackageDimensionDict


class V3ShippingMultiPackageLabelsRequest(SdkBaseModel):
    package_dimensions: list[PackageDimension] = Field(alias="packageDimensions")
    """Package Dimensions"""

    box_items: list[BoxItem8] = Field(alias="boxItems")
    """Box Items, 1 total quantity supported for multiple packages"""

    from_address: FromAddress3 = Field(alias="fromAddress")
    """From address"""

    purchase_order_id: str = Field(alias="purchaseOrderId")
    """Purchase order ID. <br/><b>Applicable to SWW and WPS.</span></b>"""

    carrier_name: str = Field(alias="carrierName")
    """Carrier name. The only supported carrier is 'FedEx'. <br/><b>Applicable to SWW only.</span></b>"""

    carrier_service_type: str = Field(alias="carrierServiceType")
    """Carrier service type. Supported values are - 'FEDEX_INTERNATIONAL_PRIORITY' for single fedExPak/fedExEnvelope
    package types, 'FEDEX_INTERNATIONAL_ECONOMY' and 'FEDEX_INTERNATIONAL_GROUND'. <br/><b>Applicable to SWW
    only.</span></b>"""


class V3ShippingMultiPackageLabelsRequestDict(TypedDict):
    package_dimensions: list[PackageDimensionDict]
    box_items: list[BoxItem8Dict]
    from_address: FromAddress3Dict
    purchase_order_id: str
    carrier_name: str
    carrier_service_type: str
