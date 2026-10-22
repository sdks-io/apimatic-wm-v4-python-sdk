from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CategorizationType(str, Enum):
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | BRAND | To get list of brands which are associated with the assortment recommendations | string |
    | CATEGORY | To get list of categories which are associated with the assortment recommendations | string |"""

    BRAND = "BRAND"
    CATEGORY = "CATEGORY"

    __str__ = str.__str__


CategorizationTypeOrStr: TypeAlias = Annotated[CategorizationType | str, open_enum_validator(CategorizationType)]
