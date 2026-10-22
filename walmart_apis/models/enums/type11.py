from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type11(str, Enum):
    """Document category; one of PROOF_OF_DAMAGED_ITEM, INVOICE, OTHER, PPOD."""

    PROOF_OF_DAMAGED_ITEM = "PROOF_OF_DAMAGED_ITEM"
    INVOICE = "INVOICE"
    OTHER = "OTHER"
    PPOD = "PPOD"

    __str__ = str.__str__


Type11OrStr: TypeAlias = Annotated[Type11 | str, open_enum_validator(Type11)]
