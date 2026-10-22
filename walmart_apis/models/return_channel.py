from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ReturnChannel(SdkBaseModel):
    """The channel via order return got initiated.<br><b style='color:green;'>Market availability: US</b>"""

    channel_name: Optional[str] = Field(default=UNSET, alias="channelName")
    """Valid values are: ONLINE, IN_STORE, and CUSTOMER_CARE.<br><b style='color:green;'>Market availability: US</b>"""


class ReturnChannelDict(TypedDict):
    channel_name: NotRequired[str]
