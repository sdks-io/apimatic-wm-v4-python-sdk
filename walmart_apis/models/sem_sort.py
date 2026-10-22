from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SemSort(SdkBaseModel):
    """Sorting criteria"""

    field: str
    """Field to sort by."""

    order: str
    """Sort direction. Allowed values: ASC, DESC."""


class SemSortDict(TypedDict):
    field: str
    order: str
