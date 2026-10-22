from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BiddingStrategyType(str, Enum):
    """Bidding strategy type for the campaign."""

    TARGET_ROAS = "TARGET_ROAS"
    MAXIMIZE_TRAFFIC = "MAXIMIZE_TRAFFIC"

    __str__ = str.__str__


BiddingStrategyTypeOrStr: TypeAlias = Annotated[BiddingStrategyType | str, open_enum_validator(BiddingStrategyType)]
