from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProcessMode(str, Enum):
    """This is applicable only for promotions"""

    UPSERT = "UPSERT"
    DELETE = "DELETE"

    __str__ = str.__str__


ProcessModeOrStr: TypeAlias = Annotated[ProcessMode | str, open_enum_validator(ProcessMode)]
