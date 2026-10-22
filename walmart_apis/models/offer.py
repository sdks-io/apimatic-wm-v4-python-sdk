from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fast_shipping_speed import FastShippingSpeed, FastShippingSpeedDict
from .price2 import Price2, Price2Dict
from .publish_and_transactable import PublishAndTransactable, PublishAndTransactableDict
from .shipping_speed import ShippingSpeed, ShippingSpeedDict


class Offer(SdkBaseModel):
    total_issue: Optional[int] = Field(default=UNSET, alias="totalIssue")
    issue_count: Optional[int] = Field(default=UNSET, alias="issueCount")
    price: Optional[Price2] = UNSET
    shipping_speed: Optional[ShippingSpeed] = Field(default=UNSET, alias="shippingSpeed")
    publish_and_transactable: Optional[PublishAndTransactable] = Field(default=UNSET, alias="publishAndTransactable")
    fast_shipping_speed: Optional[FastShippingSpeed] = Field(default=UNSET, alias="fastShippingSpeed")
    free_shipping_speed: Optional[FastShippingSpeed] = Field(default=UNSET, alias="freeShippingSpeed")


class OfferDict(TypedDict):
    total_issue: NotRequired[int]
    issue_count: NotRequired[int]
    price: NotRequired[Price2Dict]
    shipping_speed: NotRequired[ShippingSpeedDict]
    publish_and_transactable: NotRequired[PublishAndTransactableDict]
    fast_shipping_speed: NotRequired[FastShippingSpeedDict]
    free_shipping_speed: NotRequired[FastShippingSpeedDict]
