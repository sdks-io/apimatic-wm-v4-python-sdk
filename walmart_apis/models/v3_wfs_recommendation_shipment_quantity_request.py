from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V3WfsRecommendationShipmentQuantityRequest(SdkBaseModel):
    """Provide either ``listOfGtins`` or ``listOfSkus``."""

    list_of_gtins: Optional[list[str]] = Field(default=UNSET, alias="listOfGtins")
    """List of GTINs to request recommended shipment quantities for."""

    list_of_skus: Optional[list[str]] = Field(default=UNSET, alias="listOfSkus")
    """List of SKUs to request recommended shipment quantities for."""


class V3WfsRecommendationShipmentQuantityRequestDict(TypedDict):
    list_of_gtins: NotRequired[list[str]]
    list_of_skus: NotRequired[list[str]]
