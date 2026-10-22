from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error_response4 import ErrorResponse4, ErrorResponse4Dict
from .estimate_shipment_response_wrapper import EstimateShipmentResponseWrapper, EstimateShipmentResponseWrapperDict


class CommonResponseEstimateShipmentResponseWrapper(SdkBaseModel):
    data: Optional[EstimateShipmentResponseWrapper] = UNSET
    """Response payload containing the list of shipping cost estimates."""

    errors: Optional[list[ErrorResponse4]] = UNSET
    """List of error details describing why the request failed."""


class CommonResponseEstimateShipmentResponseWrapperDict(TypedDict):
    data: NotRequired[EstimateShipmentResponseWrapperDict]
    errors: NotRequired[list[ErrorResponse4Dict]]
