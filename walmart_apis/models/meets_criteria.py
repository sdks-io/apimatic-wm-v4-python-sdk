from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MeetsCriteria(SdkBaseModel):
    """Shows whether the seller has met the requirements for the badge."""

    is_orders_criteria_met: Optional[bool] = Field(default=UNSET, alias="isOrdersCriteriaMet")
    """Indicates whether the seller has met the minimum number of orders required."""

    is_delivery_defect_criteria_met: Optional[bool] = Field(default=UNSET, alias="isDeliveryDefectCriteriaMet")
    """Indicates whether the seller has a low delivery defect, meeting the threshold for the badge."""

    is_cancellation_criteria_met: Optional[bool] = Field(default=UNSET, alias="isCancellationCriteriaMet")
    """Indicates whether the seller has a low cancellation rate, meeting the threshold for the badge."""

    is_listing_quality_catalog_criteria_met: Optional[bool] = Field(
        default=UNSET, alias="isListingQualityCatalogCriteriaMet"
    )
    """Indicates whether the seller is meeting the trending catalog requirement."""

    is_active_days_criteria_met: Optional[bool] = Field(default=UNSET, alias="isActiveDaysCriteriaMet")
    """Indicates whether the seller has met the minimum number of active days required."""


class MeetsCriteriaDict(TypedDict):
    is_orders_criteria_met: NotRequired[bool]
    is_delivery_defect_criteria_met: NotRequired[bool]
    is_cancellation_criteria_met: NotRequired[bool]
    is_listing_quality_catalog_criteria_met: NotRequired[bool]
    is_active_days_criteria_met: NotRequired[bool]
