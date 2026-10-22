from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubCategory(str, Enum):
    """Rich media sub-category that determines the required Visible block. Allowed values: ``video``,
    ``360_spin_image``."""

    VIDEO = "video"
    _360_SPIN_IMAGE = "360_spin_image"

    __str__ = str.__str__


SubCategoryOrStr: TypeAlias = Annotated[SubCategory | str, open_enum_validator(SubCategory)]
