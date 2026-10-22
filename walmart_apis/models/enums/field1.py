from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Field1(str, Enum):
    """Attribute on which filter needs to be applied.

    **Supported fields**:
    - ``campaignId``: Filter by campaign identifier(s)
    - ``adGroupId``: Filter by ad group identifier(s)
    - ``creativeId``: Filter by creative identifier(s)"""

    CAMPAIGN_ID = "campaignId"
    AD_GROUP_ID = "adGroupId"
    CREATIVE_ID = "creativeId"

    __str__ = str.__str__


Field1OrStr: TypeAlias = Annotated[Field1 | str, open_enum_validator(Field1)]
