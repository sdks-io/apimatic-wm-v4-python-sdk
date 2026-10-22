from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Op2(str, Enum):
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    EQUALS = "equals"
    BETWEEN = "between"

    __str__ = str.__str__


Op2OrStr: TypeAlias = Annotated[Op2 | str, open_enum_validator(Op2)]
