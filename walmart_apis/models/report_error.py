from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ReportError(SdkBaseModel):
    code: str
    """Error code"""

    description: str
    """Error description"""

    severity: str
    """Error severity"""

    category: str
    """Error category"""

    error_identifiers: str = Field(alias="errorIdentifiers")
    """Error Identifiers"""


class ReportErrorDict(TypedDict):
    code: str
    description: str
    severity: str
    category: str
    error_identifiers: str
