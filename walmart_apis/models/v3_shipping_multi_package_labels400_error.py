from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error_identifiers1 import ErrorIdentifiers1, ErrorIdentifiers1Dict


class V3ShippingMultiPackageLabels400Error(SdkBaseModel):
    code: Optional[str] = UNSET
    """error code.

    <b style="color: green;">Market availability: MX | CL | US</b>"""

    field: Optional[str] = UNSET
    """field.

    <b style="color: green;">Market availability: MX | CL | US</b>"""

    description: Optional[str] = UNSET
    """error description.

    <b style="color: green;">Market availability: MX | CL | US</b>"""

    info: Optional[str] = UNSET
    """error info.

    <b style="color: green;">Market availability: MX | CL | US</b>"""

    severity: Optional[str] = UNSET
    """error severity.

    <b style="color: green;">Market availability: MX | CL | US</b>"""

    category: Optional[str] = UNSET
    """error category.

    <b style="color: green;">Market availability: MX | CL | US</b>"""

    error_identifiers: Optional[ErrorIdentifiers1] = Field(default=UNSET, alias="errorIdentifiers")
    """error Identifiers.

    <b style="color: green;">Market availability: MX | CL | US</b>"""


class V3ShippingMultiPackageLabels400ErrorDict(TypedDict):
    code: NotRequired[str]
    field: NotRequired[str]
    description: NotRequired[str]
    info: NotRequired[str]
    severity: NotRequired[str]
    category: NotRequired[str]
    error_identifiers: NotRequired[ErrorIdentifiers1Dict]
