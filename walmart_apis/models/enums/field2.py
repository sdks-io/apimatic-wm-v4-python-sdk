from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Field2(str, Enum):
    """Field by which the filtering is to be done.

    **Supported fields**:
    - ``issues``: Filter by specific issue types (For example, ``ITEM_OUT_OF_STOCK``, ``TITLE_TOO_LONG``)
    - ``issueCategory``: Filter by issue severity category (``LIMITED``, ``BLOCKED``, ``NO_ISSUES``)
    - ``itemId``: Filter by Walmart item IDs (numeric strings). Currently filters within items in active SEM campaigns.
        *In a future release, this will also support items not yet associated with any campaign.*"""

    ISSUES = "issues"
    ISSUE_CATEGORY = "issueCategory"
    ITEM_ID = "itemId"

    __str__ = str.__str__


Field2OrStr: TypeAlias = Annotated[Field2 | str, open_enum_validator(Field2)]
