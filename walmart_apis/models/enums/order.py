from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Order(str, Enum):
    """Sorting order.

    **Default**: DESC, <br><b style='color:green;'>Market availability: US only</b>"""

    ASC = "ASC"
    DESC = "DESC"

    __str__ = str.__str__


OrderOrStr: TypeAlias = Annotated[Order | str, open_enum_validator(Order)]
