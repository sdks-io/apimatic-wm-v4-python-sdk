from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class ProgramActionFeedHeader(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US</b>"""

    request_id: Optional[str] = Field(default=UNSET, alias="requestId")
    """<br><b style='color:green;'>Market availability: US</b>"""

    request_batch_id: Optional[str] = Field(default=UNSET, alias="requestBatchId")
    """<br><b style='color:green;'>Market availability: US</b>"""

    process_mode: Optional[str] = Field(default=UNSET, alias="processMode")
    """<br><b style='color:green;'>Market availability: US</b>"""

    subset: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: US</b>"""

    selling_channel: Optional[str] = Field(default=UNSET, alias="sellingChannel")
    """<br><b style='color:green;'>Market availability: US</b>"""

    version: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: US</b>"""

    locale: Optional[str] = UNSET
    """en.<br><b style='color:green;'>Market availability: US</b>"""

    feed_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="feedDate")
    """<br><b style='color:green;'>Market availability: US</b>"""

    feed_type: Optional[str] = Field(default=UNSET, alias="feedType")
    """<br><b style='color:green;'>Market availability: US</b>"""


class ProgramActionFeedHeaderDict(TypedDict):
    request_id: NotRequired[str]
    request_batch_id: NotRequired[str]
    process_mode: NotRequired[str]
    subset: NotRequired[str]
    selling_channel: NotRequired[str]
    version: NotRequired[str]
    locale: NotRequired[str]
    feed_date: NotRequired[RFC3339DateTime]
    feed_type: NotRequired[str]
