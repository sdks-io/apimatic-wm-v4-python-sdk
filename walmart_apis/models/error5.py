from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error_identifiers import ErrorIdentifiers, ErrorIdentifiersDict


class Error5(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: Global</b>"""

    code: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: Global</b>"""

    field: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: Global</b>"""

    description: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: Global</b>"""

    info: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: Global</b>"""

    severity: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: Global</b>"""

    category: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: Global</b>"""

    error_identifiers: Optional[ErrorIdentifiers] = Field(default=UNSET, alias="errorIdentifiers")
    """<br><b style='color:green;'>Market availability: Global</b>"""


class Error5Dict(TypedDict):
    code: NotRequired[str]
    field: NotRequired[str]
    description: NotRequired[str]
    info: NotRequired[str]
    severity: NotRequired[str]
    category: NotRequired[str]
    error_identifiers: NotRequired[ErrorIdentifiersDict]
