from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ItemStatus10(str, Enum):
    """IRP status of the items.<br><b style='color:green;'>Market availability: US only</b>"""

    ENROLLED = "ENROLLED"
    ELIGIBLE = "ELIGIBLE"
    COMPLETE = "COMPLETE"

    __str__ = str.__str__


ItemStatus10OrStr: TypeAlias = Annotated[ItemStatus10 | str, open_enum_validator(ItemStatus10)]
