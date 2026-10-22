from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CarrierPackageResponse(SdkBaseModel):
    """Carrier package type details."""

    id: Optional[str] = UNSET
    """The carrier package ID."""

    package_type_short_name: Optional[str] = Field(default=UNSET, alias="packageTypeShortName")
    """The carrier package short name."""

    package_type_display_name: Optional[str] = Field(default=UNSET, alias="packageTypeDisplayName")
    """The carrier package display name."""

    length: Optional[int] = UNSET
    """The package length. The Unit is determined by dimensionUnit."""

    width: Optional[int] = UNSET
    """The package width. The Unit is determined by dimensionUnit."""

    height: Optional[int] = UNSET
    """The package height. The Unit is determined by dimensionUnit."""

    dimension_unit: Optional[str] = Field(default=UNSET, alias="dimensionUnit")
    """The package dimension unit."""


class CarrierPackageResponseDict(TypedDict):
    id: NotRequired[str]
    package_type_short_name: NotRequired[str]
    package_type_display_name: NotRequired[str]
    length: NotRequired[int]
    width: NotRequired[int]
    height: NotRequired[int]
    dimension_unit: NotRequired[str]
