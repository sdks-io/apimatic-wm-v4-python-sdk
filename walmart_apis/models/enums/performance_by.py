from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PerformanceBy(str, Enum):
    """Aggregation level for metrics. Determines which identifier fields are populated in response.

    - **CAMPAIGN**: Only ``campaignId`` populated (``adGroupId``, ``creativeId`` will be null)
    - **ADGROUP**: ``campaignId`` and ``adGroupId`` populated (``creativeId`` will be null)
    - **CREATIVE**: All IDs populated (``campaignId``, ``adGroupId``, ``creativeId``)

    **Default**: ``CREATIVE`` (when not specified)"""

    CAMPAIGN = "CAMPAIGN"
    ADGROUP = "ADGROUP"
    CREATIVE = "CREATIVE"

    __str__ = str.__str__


PerformanceByOrStr: TypeAlias = Annotated[PerformanceBy | str, open_enum_validator(PerformanceBy)]
