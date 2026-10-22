from __future__ import annotations

from typing import Literal

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.order1 import Order1OrStr


class RecommendationsSort(SdkBaseModel):
    """Sorting configuration for ordering search results.

    Both ``field`` and ``order`` are required when the ``sort`` object is provided."""

    field: Literal["adspend"] = "adspend"
    """Field by which the results should be sorted."""

    order: Order1OrStr
    """Sort direction."""


class RecommendationsSortDict(TypedDict):
    field: Literal["adspend"]
    order: Order1OrStr
