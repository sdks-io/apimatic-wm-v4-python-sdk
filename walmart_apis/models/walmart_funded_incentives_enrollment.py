from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class WalmartFundedIncentivesEnrollment(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US</b>"""

    walmart_funded_incentives_enrollment: Optional[str] = Field(
        default=UNSET, alias="walmartFundedIncentivesEnrollment"
    )
    """<br><b style='color:green;'>Market availability: US</b>"""


class WalmartFundedIncentivesEnrollmentDict(TypedDict):
    walmart_funded_incentives_enrollment: NotRequired[str]
