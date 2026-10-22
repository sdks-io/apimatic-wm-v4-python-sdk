from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.status1 import Status1OrStr
from .items_request import ItemsRequest, ItemsRequestDict


class BulkItemStatusUpdateRequest(SdkBaseModel):
    status: Status1OrStr
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ENROLL | To enroll items into the program | string |
    | DISENROLL | To opt out items from the program | string |"""

    items: list[ItemsRequest]
    """Items"""


class BulkItemStatusUpdateRequestDict(TypedDict):
    status: Status1OrStr
    items: list[ItemsRequestDict]
