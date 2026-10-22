from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .estimate import Estimate, EstimateDict


class EstimateShipmentResponseWrapper(SdkBaseModel):
    """Response payload containing the list of shipping cost estimates."""

    estimates: Optional[list[Estimate]] = UNSET
    """List of estimates."""

    alert_message: Optional[str] = Field(default=UNSET, alias="alertMessage")
    """Alert message displayed when there are issues fetching estimates for the carrier service type."""


class EstimateShipmentResponseWrapperDict(TypedDict):
    estimates: NotRequired[list[EstimateDict]]
    alert_message: NotRequired[str]
