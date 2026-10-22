from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.field3 import Field3OrStr


class CampaignRecommendationsFilter(SdkBaseModel):
    """Filter configuration to narrow down campaign recommendation results.

    **Validation Rules**:
    - Both ``field`` and ``values`` are required when a filter is provided
    - Each filter field must be specified only once (no duplicate fields)
    - Filter values must contain at least one value
    - Multiple values within a filter act as an OR condition
    - Multiple filters are combined using the AND operator."""

    field: Field3OrStr
    """Field by which the filtering is to be done.

    **Supported fields**:
    - ``campaignIds``: Filter by specific campaign identifiers
    - ``recommendationType``: Filter by recommendation type (``BUDGET``, ``BIDDING_STRATEGY``)"""

    values: list[str]
    """List of values for the specified field. Multiple values act as an OR condition within the filter.

    **Valid values by field**:
    - ``campaignIds``: Numeric string campaign IDs
    - ``recommendationType``: ``BUDGET``, ``BIDDING_STRATEGY``"""


class CampaignRecommendationsFilterDict(TypedDict):
    field: Field3OrStr
    values: list[str]
