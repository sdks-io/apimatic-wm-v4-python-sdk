from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .incentives_enrollment import IncentivesEnrollment, IncentivesEnrollmentDict


class Programs1(SdkBaseModel):
    incentives_enrollment: Optional[IncentivesEnrollment] = Field(default=UNSET, alias="IncentivesEnrollment")


class Programs1Dict(TypedDict):
    incentives_enrollment: NotRequired[IncentivesEnrollmentDict]
