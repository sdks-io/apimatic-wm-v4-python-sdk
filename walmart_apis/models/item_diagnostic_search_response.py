from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .active_item_issues import ActiveItemIssues, ActiveItemIssuesDict
from .diagnostic_pagination import DiagnosticPagination, DiagnosticPaginationDict


class ItemDiagnosticSearchResponse(SdkBaseModel):
    """Search response containing paginated item-level diagnostics and pagination metadata.

    Each item's ``issues`` array contains ``issueType`` values as lightweight lookup keys. Partners should use the
    dedicated ``GET /item-issues/issue-types`` endpoint to retrieve complete issue metadata (name, description,
    category, fixability, help links) and cache it locally (recommended TTL: 24 hours) to enrich search results."""

    pagination: Optional[DiagnosticPagination] = UNSET
    """Pagination metadata for navigating through search results.

    Includes ``hasNextPage`` and ``hasPreviousPage`` boolean flags for convenient pagination control in UIs."""

    data: Optional[list[ActiveItemIssues]] = UNSET
    """Paginated list of item-level diagnostics. Each item appears once per unique ``offerId`` with all campaign
    associations. Empty array when no items match the search criteria."""


class ItemDiagnosticSearchResponseDict(TypedDict):
    pagination: NotRequired[DiagnosticPaginationDict]
    data: NotRequired[list[ActiveItemIssuesDict]]
