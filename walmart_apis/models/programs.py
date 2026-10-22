from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .walmart_funded_incentives_enrollment import (
    WalmartFundedIncentivesEnrollment,
    WalmartFundedIncentivesEnrollmentDict,
)


class Programs(SdkBaseModel):
    walmart_funded_incentives_enrollment: Optional[WalmartFundedIncentivesEnrollment] = Field(
        default=UNSET, alias="WalmartFundedIncentivesEnrollment"
    )
    """<br><b style='color:green;'>Market availability: US</b>"""


class ProgramsDict(TypedDict):
    walmart_funded_incentives_enrollment: NotRequired[WalmartFundedIncentivesEnrollmentDict]
