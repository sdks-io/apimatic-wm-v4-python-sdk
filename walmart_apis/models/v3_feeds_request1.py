from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .program_action11 import ProgramAction11, ProgramAction11Dict
from .program_action_feed_header11 import ProgramActionFeedHeader11, ProgramActionFeedHeader11Dict


class V3FeedsRequest1(SdkBaseModel):
    program_action_feed_header: Optional[ProgramActionFeedHeader11] = Field(
        default=UNSET, alias="ProgramActionFeedHeader"
    )
    """ProgramAction feed header details. <br><b style='color:green;'>Market availability: US</span></b>"""

    program_action: Optional[list[ProgramAction11]] = Field(default=UNSET, alias="ProgramAction")
    """This includes all the SKU IDs and the type of shipping configuration to migrate. <br><b
    style='color:green;'>Market availability: US</span></b>"""


class V3FeedsRequest1Dict(TypedDict):
    program_action_feed_header: NotRequired[ProgramActionFeedHeader11Dict]
    program_action: NotRequired[list[ProgramAction11Dict]]
