from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .issue17 import Issue17, Issue17Dict


class Issue16(SdkBaseModel):
    score: Optional[float] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    is_editable: Optional[bool] = Field(default=UNSET, alias="isEditable")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    attribute_value: Optional[str] = Field(default=UNSET, alias="attributeValue")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    is_spec_attribute: Optional[bool] = Field(default=UNSET, alias="isSpecAttribute")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    attribute_name: Optional[str] = Field(default=UNSET, alias="attributeName")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    issue_count: Optional[int] = Field(default=UNSET, alias="issueCount")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    issues: Optional[list[Issue17]] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class Issue16Dict(TypedDict):
    score: NotRequired[float]
    is_editable: NotRequired[bool]
    attribute_value: NotRequired[str]
    is_spec_attribute: NotRequired[bool]
    attribute_name: NotRequired[str]
    issue_count: NotRequired[int]
    issues: NotRequired[list[Issue17Dict]]
