from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ReturnLine(SdkBaseModel):
    """Array of return lines.<br><b style='color:green;'>Market availability: US</b>"""

    return_order_line_number: Optional[int] = Field(default=UNSET, alias="returnOrderLineNumber")
    """Identifier of the return label.<br><b style='color:green;'>Market availability: US</b>"""


class ReturnLineDict(TypedDict):
    return_order_line_number: NotRequired[int]
