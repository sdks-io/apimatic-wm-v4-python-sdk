from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .campaign_suggestion import CampaignSuggestion, CampaignSuggestionDict
from .diagnostic_pagination import DiagnosticPagination, DiagnosticPaginationDict


class CampaignRecommendationsSearchResponse(SdkBaseModel):
    """Search response containing paginated campaign-level recommendations and pagination metadata.

    Each campaign in the ``data`` array includes its current settings (bidding strategy, target ROAS, daily budget) and
    an array of actionable recommendations with projected performance impact."""

    pagination: Optional[DiagnosticPagination] = UNSET
    """Pagination metadata for navigating through search results.

    Includes ``hasNextPage`` and ``hasPreviousPage`` boolean flags for convenient pagination control in UIs."""

    data: Optional[list[CampaignSuggestion]] = UNSET
    """Paginated list of campaign-level suggestions. Each campaign appears once with all its recommendations. Empty
    array when no campaigns match the search criteria."""


class CampaignRecommendationsSearchResponseDict(TypedDict):
    pagination: NotRequired[DiagnosticPaginationDict]
    data: NotRequired[list[CampaignSuggestionDict]]
