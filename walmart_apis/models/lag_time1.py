from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .additional_attributes import AdditionalAttributes, AdditionalAttributesDict


class LagTime1(SdkBaseModel):
    sku: str
    """A seller-provided Product ID. The response will have a decoded value of the SKU."""

    fulfillment_lag_time: Optional[int] = Field(default=UNSET, alias="fulfillmentLagTime")
    """The number of days between when the item is ordered and when it is shipped."""

    additional_attributes: Optional[list[AdditionalAttributes]] = Field(default=UNSET, alias="additionalAttributes")


class LagTime1Dict(TypedDict):
    sku: str
    fulfillment_lag_time: NotRequired[int]
    additional_attributes: NotRequired[list[AdditionalAttributesDict]]
