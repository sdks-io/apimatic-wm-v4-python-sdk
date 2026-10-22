from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LagTimeResponse(SdkBaseModel):
    sku: str
    """A seller-provided Product ID. The response will have a decoded value of the SKU."""

    fulfillment_lag_time: int = Field(alias="fulfillmentLagTime")
    """The number of days between when the item is ordered and when it is shipped."""


class LagTimeResponseDict(TypedDict):
    sku: str
    fulfillment_lag_time: int
