from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .row_filter import RowFilter, RowFilterDict


class Filters(SdkBaseModel):
    email: Optional[str] = UNSET
    row_filters: Optional[list[RowFilter]] = Field(default=UNSET, alias="rowFilters")


class FiltersDict(TypedDict):
    email: NotRequired[str]
    row_filters: NotRequired[list[RowFilterDict]]
