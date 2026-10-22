from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .label import Label, LabelDict
from .return_line import ReturnLine, ReturnLineDict


class ReturnLineGroup(SdkBaseModel):
    group_no: Optional[int] = Field(default=UNSET, alias="groupNo")
    """Sequence of group numbers where each returnLineGroups will represent one or more return lines.<br><b
    style='color:green;'>Market availability: US</b>"""

    return_lines: Optional[list[ReturnLine]] = Field(default=UNSET, alias="returnLines")
    """Array of return lines.<br><b style='color:green;'>Market availability: US</b>"""

    labels: Optional[list[Label]] = UNSET
    """Array of labels.<br><b style='color:green;'>Market availability: US</b>"""

    return_expected_flag: Optional[bool] = Field(default=UNSET, alias="returnExpectedFlag")
    """Is customer required to send this item back to return center.<br><b style='color:green;'>Market availability:
    US</b>"""


class ReturnLineGroupDict(TypedDict):
    group_no: NotRequired[int]
    return_lines: NotRequired[list[ReturnLineDict]]
    labels: NotRequired[list[LabelDict]]
    return_expected_flag: NotRequired[bool]
