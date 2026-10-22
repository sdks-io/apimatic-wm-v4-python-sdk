from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .sem_filter import SemFilter, SemFilterDict


class SemItemEligibilityRequest(SdkBaseModel):
    filters: list[SemFilter]
    """List of filters to apply when checking eligibility."""


class SemItemEligibilityRequestDict(TypedDict):
    filters: list[SemFilterDict]
