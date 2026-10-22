from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .program_action import ProgramAction, ProgramActionDict
from .program_action_feed_header import ProgramActionFeedHeader, ProgramActionFeedHeaderDict


class V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequest(SdkBaseModel):
    program_action_feed_header: Optional[ProgramActionFeedHeader] = Field(
        default=UNSET, alias="ProgramActionFeedHeader"
    )
    """<br><b style='color:green;'>Market availability: US</b>"""

    program_action: Optional[list[ProgramAction]] = Field(default=UNSET, alias="ProgramAction")


class V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequestDict(TypedDict):
    program_action_feed_header: NotRequired[ProgramActionFeedHeaderDict]
    program_action: NotRequired[list[ProgramActionDict]]
