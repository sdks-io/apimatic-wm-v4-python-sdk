from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .filter import Filter, FilterDict
from .query import Query, QueryDict


class ItemDetailsLqrequestPayload(SdkBaseModel):
    query: Optional[Query] = UNSET
    filters: Optional[list[Filter]] = UNSET


class ItemDetailsLqrequestPayloadDict(TypedDict):
    query: NotRequired[QueryDict]
    filters: NotRequired[list[FilterDict]]
