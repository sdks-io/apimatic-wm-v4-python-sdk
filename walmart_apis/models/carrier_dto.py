from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CarrierDto(SdkBaseModel):
    """Defines the carrier configurations used for shipping, like carrier name and carrier service."""

    carrier_name: Optional[str] = Field(default=UNSET, alias="carrierName")
    """Name of the carrier to use for shipping."""

    carrier_service: Optional[str] = Field(default=UNSET, alias="carrierService")
    """Service name of the carrier to use for shipping"""


class CarrierDtoDict(TypedDict):
    carrier_name: NotRequired[str]
    carrier_service: NotRequired[str]
