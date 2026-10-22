from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .program_action1 import ProgramAction1, ProgramAction1Dict
from .program_action_feed_header import ProgramActionFeedHeader, ProgramActionFeedHeaderDict


class V3FeedsFeedTypeIncentiveEnrollmentRequest(SdkBaseModel):
    program_action_feed_header: Optional[ProgramActionFeedHeader] = Field(
        default=UNSET, alias="ProgramActionFeedHeader"
    )
    """<br><b style='color:green;'>Market availability: US</b>"""

    program_action: Optional[list[ProgramAction1]] = Field(default=UNSET, alias="ProgramAction")


class V3FeedsFeedTypeIncentiveEnrollmentRequestDict(TypedDict):
    program_action_feed_header: NotRequired[ProgramActionFeedHeaderDict]
    program_action: NotRequired[list[ProgramAction1Dict]]
