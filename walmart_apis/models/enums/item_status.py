from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ItemStatus(str, Enum):
    """Current status of the item in IRP."""

    COMPLETE = "COMPLETE"
    ELIGIBLE = "ELIGIBLE"
    ENROLLED = "ENROLLED"

    __str__ = str.__str__


ItemStatusOrStr: TypeAlias = Annotated[ItemStatus | str, open_enum_validator(ItemStatus)]
