from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IncentivesEnrollment(SdkBaseModel):
    referral_fee_incentive_enrollment: Optional[str] = Field(default=UNSET, alias="referralFeeIncentiveEnrollment")
    """<br><b style='color:green;'>Market availability: US</b>"""

    incentive_type: Optional[str] = Field(default=UNSET, alias="incentiveType")
    """<br><b style='color:green;'>Market availability: US</b>"""

    incentive_id: Optional[str] = Field(default=UNSET, alias="incentiveId")
    """<br><b style='color:green;'>Market availability: US</b>"""


class IncentivesEnrollmentDict(TypedDict):
    referral_fee_incentive_enrollment: NotRequired[str]
    incentive_type: NotRequired[str]
    incentive_id: NotRequired[str]
