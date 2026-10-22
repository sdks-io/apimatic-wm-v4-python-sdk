from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ItemStatus9(str, Enum):
    """Current status of the item in IRP.<br><b style='color:green;'>Market availability: US only</b>"""

    COMPLETE = "COMPLETE"
    ELIGIBLE = "ELIGIBLE"
    ENROLLED = "ENROLLED"

    __str__ = str.__str__


ItemStatus9OrStr: TypeAlias = Annotated[ItemStatus9 | str, open_enum_validator(ItemStatus9)]
