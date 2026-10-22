from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OperationType(str, Enum):
    """Type of operation to perform on campaign items. Allowed values: ``ADD`` or ``REMOVE``."""

    ADD = "ADD"
    REMOVE = "REMOVE"

    __str__ = str.__str__


OperationTypeOrStr: TypeAlias = Annotated[OperationType | str, open_enum_validator(OperationType)]
