from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MediaType1(str, Enum):
    """Media type as recorded for this specific item linkage."""

    VIDEO = "VIDEO"
    IMAGES360 = "IMAGES360"

    __str__ = str.__str__


MediaType1OrStr: TypeAlias = Annotated[MediaType1 | str, open_enum_validator(MediaType1)]
