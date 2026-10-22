from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Jsonobject(SdkBaseModel):
    """content of the CSV file in the list format, each element in the list represents the row in CSV file."""

    empty: Optional[bool] = UNSET


class JsonobjectDict(TypedDict):
    empty: NotRequired[bool]
