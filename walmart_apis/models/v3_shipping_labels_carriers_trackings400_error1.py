from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error_identifiers2 import ErrorIdentifiers2, ErrorIdentifiers2Dict


class V3ShippingLabelsCarriersTrackings400Error1(SdkBaseModel):
    code: Optional[str] = UNSET
    """error code.

    <b style="color: green;">Market availability: CL only</b>"""

    field: Optional[str] = UNSET
    """field.

    <b style="color: green;">Market availability: CL only</b>"""

    description: Optional[str] = UNSET
    """error description.

    <b style="color: green;">Market availability: CL only</b>"""

    info: Optional[str] = UNSET
    """error info.

    <b style="color: green;">Market availability: CL only</b>"""

    severity: Optional[str] = UNSET
    """error severity.

    <b style="color: green;">Market availability: CL only</b>"""

    category: Optional[str] = UNSET
    """error category.

    <b style="color: green;">Market availability: CL only</b>"""

    error_identifiers: Optional[ErrorIdentifiers2] = Field(default=UNSET, alias="errorIdentifiers")
    """error Identifiers.

    <b style="color: green;">Market availability: CL only</b>"""


class V3ShippingLabelsCarriersTrackings400Error1Dict(TypedDict):
    code: NotRequired[str]
    field: NotRequired[str]
    description: NotRequired[str]
    info: NotRequired[str]
    severity: NotRequired[str]
    category: NotRequired[str]
    error_identifiers: NotRequired[ErrorIdentifiers2Dict]
