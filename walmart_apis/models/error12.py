from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Error12(SdkBaseModel):
    code: Optional[str] = UNSET
    """A unique identifier for the type of error. This helps in quickly recognizing and categorizing the specific
    issue.<br><b style='color:green;'>Market availability: US only</b>"""

    description: Optional[str] = UNSET
    """A detailed message explaining what caused the error. This provides more context about the issue.<br><b
    style='color:green;'>Market availability: US only</b>"""

    category: Optional[str] = UNSET
    """Classifies the error into a specific group or type, which helps in organizing and managing different types of
    issues.<br><b style='color:green;'>Market availability: US only</b>"""

    severity: Optional[str] = UNSET
    """Indicates the criticality of the error. Common values include ERROR, WARNING, or INFO.<br><b
    style='color:green;'>Market availability: US only</b>"""


class Error12Dict(TypedDict):
    code: NotRequired[str]
    description: NotRequired[str]
    category: NotRequired[str]
    severity: NotRequired[str]
