from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.status11 import Status11OrStr
from .item9 import Item9, Item9Dict


class V3GrowthReviewsAcceleratorItemsStatusRequest(SdkBaseModel):
    status: Status11OrStr
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ENROLL | To enroll items into the program | string |
    | DISENROLL | To opt out items from the program | string |
    <br><b style='color:green;'>Market availability: US only</b>"""

    items: list[Item9]
    """Items<br><b style='color:green;'>Market availability: US only</b>"""


class V3GrowthReviewsAcceleratorItemsStatusRequestDict(TypedDict):
    status: Status11OrStr
    items: list[Item9Dict]
