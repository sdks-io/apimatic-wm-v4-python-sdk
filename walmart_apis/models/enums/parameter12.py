from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Parameter12(str, Enum):
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | BRAND | To filter based on list of brands which are associated with the assortment recommendations. This is
        allowed when the categorization type is CATEGORY | string |
    | CATEGORY | To filter based on list of categories which are associated with the assortment recommendations. This is
        allowed when the categorization type is BRAND | string |"""

    CATEGORY = "CATEGORY"
    BRAND = "BRAND"

    __str__ = str.__str__


Parameter12OrStr: TypeAlias = Annotated[Parameter12 | str, open_enum_validator(Parameter12)]
