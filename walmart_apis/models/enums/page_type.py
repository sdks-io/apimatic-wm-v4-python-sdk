from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PageType(str, Enum):
    """The type of page this template is for (For example, ``ITEM``, ``BRANDSHOP``).

    <span style="color:green">**Market availability: Global**</span>"""

    ITEM = "ITEM"
    BRANDSHOP = "BRANDSHOP"

    __str__ = str.__str__


PageTypeOrStr: TypeAlias = Annotated[PageType | str, open_enum_validator(PageType)]
