from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Reward(SdkBaseModel):
    """Specifies the list of rewards.<br><b style='color:green;'>Market availability: US | CA</b>"""

    reward: Optional[str] = UNSET
    """Specifies name of the eligible reward.<br><b style='color:green;'>Market availability: US | CA</b>"""

    is_reward_active: Optional[bool] = Field(default=UNSET, alias="isRewardActive")
    """Indicates reward active status.<br><b style='color:green;'>Market availability: US | CA</b>"""

    is_reward_override: Optional[bool] = Field(default=UNSET, alias="isRewardOverride")
    """Indicates if the reward has been overridden.<br><b style='color:green;'>Market availability: US | CA</b>"""

    reward_override_action: Optional[str] = Field(default=UNSET, alias="rewardOverrideAction")
    """Specifies the reward override action (approve or deny).<br><b style='color:green;'>Market availability: US |
    CA</b>"""


class RewardDict(TypedDict):
    reward: NotRequired[str]
    is_reward_active: NotRequired[bool]
    is_reward_override: NotRequired[bool]
    reward_override_action: NotRequired[str]
