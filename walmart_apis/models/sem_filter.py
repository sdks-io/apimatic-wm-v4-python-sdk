from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SemFilter(SdkBaseModel):
    """Filtering criteria"""

    field: str
    """Field by which the filtering is to be done."""

    values: list[str]
    """List of values for the specified field."""


class SemFilterDict(TypedDict):
    field: str
    values: list[str]
