from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Data8(SdkBaseModel):
    """Carrier package type details."""

    id: Optional[str] = UNSET
    """The carrier package Id

    <b style="color: green;">Market availability: Global</b>"""

    package_type_short_name: Optional[str] = Field(default=UNSET, alias="packageTypeShortName")
    """The carrier package short name

    <b style="color: green;">Market availability: Global</b>"""

    package_type_display_name: Optional[str] = Field(default=UNSET, alias="packageTypeDisplayName")
    """The carrier package display name

    <b style="color: green;">Market availability: Global</b>"""

    length: Optional[float] = UNSET
    """The package length. The Unit is determined by dimensionUnit.

    <b style="color: green;">Market availability: Global</b>"""

    width: Optional[float] = UNSET
    """The package width. The Unit is determined by dimensionUnit.

    <b style="color: green;">Market availability: Global</b>"""

    height: Optional[float] = UNSET
    """The package height. The Unit is determined by dimensionUnit.

    <b style="color: green;">Market availability: Global</b>"""

    dimension_unit: Optional[str] = Field(default=UNSET, alias="dimensionUnit")
    """The package dimension unit.

    <b style="color: green;">Market availability: Global</b>"""


class Data8Dict(TypedDict):
    id: NotRequired[str]
    package_type_short_name: NotRequired[str]
    package_type_display_name: NotRequired[str]
    length: NotRequired[float]
    width: NotRequired[float]
    height: NotRequired[float]
    dimension_unit: NotRequired[str]
