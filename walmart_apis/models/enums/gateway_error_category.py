from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GatewayErrorCategory(str, Enum):
    INTERNAL_DATA_ERROR = "INTERNAL_DATA_ERROR"
    EXTERNAL_DATA_ERROR = "EXTERNAL_DATA_ERROR"
    SYSTEM_ERROR = "SYSTEM_ERROR"

    __str__ = str.__str__


GatewayErrorCategoryOrStr: TypeAlias = Annotated[GatewayErrorCategory | str, open_enum_validator(GatewayErrorCategory)]
