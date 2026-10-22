from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sem_campaign_report import SemCampaignReport, SemCampaignReportDict
from .sem_pagination import SemPagination, SemPaginationDict


class SemCampaignLevelReportResponse(SdkBaseModel):
    pagination: Optional[SemPagination] = UNSET
    """Pagination details"""

    data: Optional[list[SemCampaignReport]] = UNSET
    """List of campaigns with performance data"""


class SemCampaignLevelReportResponseDict(TypedDict):
    pagination: NotRequired[SemPaginationDict]
    data: NotRequired[list[SemCampaignReportDict]]
