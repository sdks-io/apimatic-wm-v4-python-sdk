from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ImpactOption(SdkBaseModel):
    """A single recommendation option with its projected performance impact."""

    value: Optional[float] = UNSET
    """The recommended value for this option (For example, suggested daily budget amount in USD)."""

    adspend_change: Optional[float] = Field(default=UNSET, alias="adspendChange")
    """Projected change in ad spend (in USD) if this option is applied."""

    clicks_change: Optional[int] = Field(default=UNSET, alias="clicksChange")
    """Projected change in number of clicks if this option is applied."""

    impressions_change: Optional[int] = Field(default=UNSET, alias="impressionsChange")
    """Projected change in number of impressions if this option is applied."""

    is_recommended: Optional[bool] = Field(default=UNSET, alias="isRecommended")
    """``true`` if this is the primary recommended option. Only one option within a ``RecommendedValueImpact`` will have
    ``isRecommended: true``."""


class ImpactOptionDict(TypedDict):
    value: NotRequired[float]
    adspend_change: NotRequired[float]
    clicks_change: NotRequired[int]
    impressions_change: NotRequired[int]
    is_recommended: NotRequired[bool]
