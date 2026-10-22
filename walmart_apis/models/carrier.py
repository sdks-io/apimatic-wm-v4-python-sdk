from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Carrier(SdkBaseModel):
    """carriers"""

    carrier_id: Optional[str] = Field(default=UNSET, alias="carrierId")
    """The carrier ID. A unique identifier for the carrier."""

    short_name: Optional[str] = Field(default=UNSET, alias="shortName")
    """The carrier short name."""

    carrier_name: Optional[str] = Field(default=UNSET, alias="carrierName")
    """The carrier name."""


class CarrierDict(TypedDict):
    carrier_id: NotRequired[str]
    short_name: NotRequired[str]
    carrier_name: NotRequired[str]
