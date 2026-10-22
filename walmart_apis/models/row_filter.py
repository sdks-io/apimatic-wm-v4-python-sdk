from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RowFilter(SdkBaseModel):
    type_: str = Field(alias="type")
    values: list[str]
    column_name: str = Field(alias="columnName")


class RowFilterDict(TypedDict):
    type_: str
    values: list[str]
    column_name: str
