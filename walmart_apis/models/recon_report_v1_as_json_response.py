from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .jsonobject import Jsonobject, JsonobjectDict


class ReconReportV1AsJsonResponse(SdkBaseModel):
    report_data: Optional[list[Jsonobject]] = Field(default=UNSET, alias="reportData")
    """content of the CSV file in the list format, each element in the list represents the row in CSV file."""

    next_offset: Optional[int] = Field(default=UNSET, alias="nextOffset")
    """this field will be used in subsequent calls to fetch next set of records."""

    total_records: Optional[int] = Field(default=UNSET, alias="totalRecords")
    """records returned in the current response."""

    description: Optional[str] = UNSET
    """total number of lines in the the file."""


class ReconReportV1AsJsonResponseDict(TypedDict):
    report_data: NotRequired[list[JsonobjectDict]]
    next_offset: NotRequired[int]
    total_records: NotRequired[int]
    description: NotRequired[str]
