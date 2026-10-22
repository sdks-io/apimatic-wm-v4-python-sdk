from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .from_address5 import FromAddress5, FromAddress5Dict


class V3ShippingScanFormRequest(SdkBaseModel):
    scan_form_id: str = Field(alias="scanFormId")
    """Client-generated unique identifier for this scan form. Acts as a natural idempotency key — submitting a second
    POST with the same scanFormId returns 409 Conflict without creating a duplicate. Use a deterministic value (e.g.,
    sellerId + shipOnDate + shipNode) to enable safe retries on network failure.

    <b style="color: green;">Market availability: US only</b>"""

    carrier_name: str = Field(alias="carrierName")
    """Carrier short name for the scan form request. This value maps to shortName from the supported carriers API
    response.

    <b style="color: green;">Market availability: US only</b>"""

    ship_on_date: str = Field(alias="shipOnDate")
    """Ship-on date for the scan form. This is the date when the shipment is scheduled for carrier pickup. Format:
    yyyy-MM-dd.

    <b style="color: green;">Market availability: US only</b>"""

    from_address: FromAddress5 = Field(alias="fromAddress")
    """Origin (ship-from) address used for the scan form.

    <b style="color: green;">Market availability: US only</b>"""

    tracking_numbers: list[str] = Field(alias="trackingNumbers")
    """List of tracking numbers to include in the scan form. Maximum 200 tracking numbers per scan form (USPS limit).

    <b style="color: green;">Market availability: US only</b>"""

    carrier_service_type: Optional[str] = Field(default=UNSET, alias="carrierServiceType")
    """Carrier service type. This value maps to serviceTypes.name from the shipping estimates API response.

    <b style="color: green;">Market availability: US only</b>"""

    document_format: str = Field(alias="documentFormat")
    """Requested scan form output format. Allowed values: PDF, ZPL, PNG, BLOB. Default is PDF.

    <b style="color: green;">Market availability: US only</b>"""


class V3ShippingScanFormRequestDict(TypedDict):
    scan_form_id: str
    carrier_name: str
    ship_on_date: str
    from_address: FromAddress5Dict
    tracking_numbers: list[str]
    carrier_service_type: NotRequired[str]
    document_format: str
