from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Parameter1(str, Enum):
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | BRAND | To filter based on list of brands which are associated with the assortment recommendations | string |
    | CATEGORY | To filter based on list of categories which are associated with the assortment recommendations | string
        |
    | PRODUCT_TYPE | To filter based on list of product types which are associated with the assortment recommendations |
        string |"""

    BRAND = "BRAND"
    CATEGORY = "CATEGORY"
    PRODUCT_TYPE = "PRODUCT_TYPE"

    __str__ = str.__str__


Parameter1OrStr: TypeAlias = Annotated[Parameter1 | str, open_enum_validator(Parameter1)]
