from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MediaOperations(str, Enum):
    """Operation type. Allowed values: ``Delink`` and ``null``(empty). Set to ``Delink`` to remove the GTIN association
    from this asset. Set to ``null`` (empty) for create/edit operations."""

    DELINK = "Delink"

    __str__ = str.__str__


MediaOperationsOrStr: TypeAlias = Annotated[MediaOperations | str, open_enum_validator(MediaOperations)]
