from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta_data_response import MetaDataResponse, MetaDataResponseDict
from .record import Record, RecordDict


class Payload1(SdkBaseModel):
    """Payload in the response having the details about the item recommendations."""

    recommendation_type: Literal["ITEM"] = Field(default="ITEM", alias="recommendationType")
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ITEM | To get list of recommended items | string |"""

    meta: Optional[MetaDataResponse] = UNSET
    """Meta information for the response."""

    records: Optional[list[Record]] = UNSET
    """Information related to the item recommendations."""


class Payload1Dict(TypedDict):
    recommendation_type: Literal["ITEM"]
    meta: NotRequired[MetaDataResponseDict]
    records: NotRequired[list[RecordDict]]
