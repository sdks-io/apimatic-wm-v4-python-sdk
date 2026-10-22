from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .campaign_recommendations_filter import CampaignRecommendationsFilter, CampaignRecommendationsFilterDict
from .campaign_recommendations_page import CampaignRecommendationsPage, CampaignRecommendationsPageDict
from .recommendations_sort import RecommendationsSort, RecommendationsSortDict


class CampaignRecommendationsSearchRequest(SdkBaseModel):
    """Request DTO for searching campaign-level recommendations.

    All fields are optional. The request body itself is also optional — when absent, sensible defaults are applied:
    - ``page.offset``: 0
    - ``page.limit``: 10
    - No filters, no sorting

    **Filter behavior**: Filters are combined using the AND operator. Multiple values within a single filter act as
    OR."""

    page: Optional[CampaignRecommendationsPage] = UNSET
    """Pagination configuration for campaign recommendations.

    **Defaults when page is not provided**: ``offset=0``, ``limit=10``

    Both ``offset`` and ``limit`` are required when the ``page`` object is provided."""

    sort: Optional[RecommendationsSort] = UNSET
    """Sorting configuration for ordering search results.

    Both ``field`` and ``order`` are required when the ``sort`` object is provided."""

    filters: Optional[list[CampaignRecommendationsFilter]] = UNSET
    """List of filters to narrow down results. Multiple filters are combined using the AND operator. Each filter field
    must be specified only once (no duplicates)."""


class CampaignRecommendationsSearchRequestDict(TypedDict):
    page: NotRequired[CampaignRecommendationsPageDict]
    sort: NotRequired[RecommendationsSortDict]
    filters: NotRequired[list[CampaignRecommendationsFilterDict]]
