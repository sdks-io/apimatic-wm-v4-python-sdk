from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ItemStatus5(str, Enum):
    """IRP status of the items."""

    ENROLLED = "ENROLLED"
    ELIGIBLE = "ELIGIBLE"
    COMPLETE = "COMPLETE"

    __str__ = str.__str__


ItemStatus5OrStr: TypeAlias = Annotated[ItemStatus5 | str, open_enum_validator(ItemStatus5)]
