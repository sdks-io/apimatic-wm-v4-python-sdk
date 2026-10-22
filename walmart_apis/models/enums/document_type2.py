from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DocumentType2(str, Enum):
    PROOF_OF_DAMAGED_ITEM = "PROOF_OF_DAMAGED_ITEM"
    INVOICE = "INVOICE"
    OTHER = "OTHER"
    PPOD = "PPOD"

    __str__ = str.__str__


DocumentType2OrStr: TypeAlias = Annotated[DocumentType2 | str, open_enum_validator(DocumentType2)]
