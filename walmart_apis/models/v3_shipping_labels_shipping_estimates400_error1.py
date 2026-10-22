from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error_identifiers11 import ErrorIdentifiers11, ErrorIdentifiers11Dict


class V3ShippingLabelsShippingEstimates400Error1(SdkBaseModel):
    code: Optional[str] = UNSET
    """error code.

    <b style="color: green;">Market availability: US | CA | MX</b>"""

    field: Optional[str] = UNSET
    """field.

    <b style="color: green;">Market availability: US | CA | MX</b>"""

    description: Optional[str] = UNSET
    """error description.

    <b style="color: green;">Market availability: US | CA | MX</b>"""

    info: Optional[str] = UNSET
    """error info.

    <b style="color: green;">Market availability: US | CA | MX</b>"""

    severity: Optional[str] = UNSET
    """error severity.

    <b style="color: green;">Market availability: US | CA | MX</b>"""

    category: Optional[str] = UNSET
    """error category.

    <b style="color: green;">Market availability: US | CA | MX</b>"""

    error_identifiers: Optional[ErrorIdentifiers11] = Field(default=UNSET, alias="errorIdentifiers")
    """error Identifiers.

    <b style="color: green;">Market availability: US | CA | MX</b>"""


class V3ShippingLabelsShippingEstimates400Error1Dict(TypedDict):
    code: NotRequired[str]
    field: NotRequired[str]
    description: NotRequired[str]
    info: NotRequired[str]
    severity: NotRequired[str]
    category: NotRequired[str]
    error_identifiers: NotRequired[ErrorIdentifiers11Dict]
