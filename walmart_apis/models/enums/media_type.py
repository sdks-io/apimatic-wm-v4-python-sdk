from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MediaType(str, Enum):
    """Type of rich media asset. Determines the structure of the ``richMediaAsset`` object."""

    VIDEO = "VIDEO"
    IMAGES360 = "IMAGES360"

    __str__ = str.__str__


MediaTypeOrStr: TypeAlias = Annotated[MediaType | str, open_enum_validator(MediaType)]
