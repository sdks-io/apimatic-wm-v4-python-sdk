from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Field3(str, Enum):
    """Field by which the filtering is to be done.

    **Supported fields**:
    - ``campaignIds``: Filter by specific campaign identifiers
    - ``recommendationType``: Filter by recommendation type (``BUDGET``, ``BIDDING_STRATEGY``)"""

    CAMPAIGN_IDS = "campaignIds"
    RECOMMENDATION_TYPE = "recommendationType"

    __str__ = str.__str__


Field3OrStr: TypeAlias = Annotated[Field3 | str, open_enum_validator(Field3)]
