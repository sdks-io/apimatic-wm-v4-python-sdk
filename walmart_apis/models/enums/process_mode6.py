from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProcessMode6(str, Enum):
    """<br><b style='color:green;'>Market availability: Global</b>"""

    UPSERT = "UPSERT"
    DELETE = "DELETE"

    __str__ = str.__str__


ProcessMode6OrStr: TypeAlias = Annotated[ProcessMode6 | str, open_enum_validator(ProcessMode6)]
