from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Item111(SdkBaseModel):
    """Items.<br><b style='color:green;'>Market availability: US only</b>"""

    item_id: Optional[str] = Field(default=UNSET, alias="itemId")
    """Specifies the item identifier.<br><b style='color:green;'>Market availability: US only</b>"""

    error_code: Optional[str] = Field(default=UNSET, alias="errorCode")
    """A unique identifier for the type of error. This helps in quickly recognizing and categorizing the specific
    issue.<br><b style='color:green;'>Market availability: US only</b>"""

    error_description: Optional[str] = Field(default=UNSET, alias="errorDescription")
    """A detailed message explaining what caused the error. This provides more context about the issue.<br><b
    style='color:green;'>Market availability: US only</b>"""

    category: Optional[str] = UNSET
    """Classifies the error into a specific group or type, which helps in organizing and managing different types of
    issues.<br><b style='color:green;'>Market availability: US only</b>"""

    severity: Optional[str] = UNSET
    """Indicates the criticality of the error. Common values include ERROR, WARNING, or INFO.<br><b
    style='color:green;'>Market availability: US only</b>"""


class Item111Dict(TypedDict):
    item_id: NotRequired[str]
    error_code: NotRequired[str]
    error_description: NotRequired[str]
    category: NotRequired[str]
    severity: NotRequired[str]
