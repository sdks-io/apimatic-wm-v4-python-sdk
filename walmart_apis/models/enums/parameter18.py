from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Parameter18(str, Enum):
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | BRAND <br><b style='color:green;'>Market availability: US | CA | MX</span></b>| To filter based on list of brands
        which are associated with the assortment recommendations. This is allowed when the categorization type is
        CATEGORY | string |
    | CATEGORY <br><b style='color:green;'>Market availability: US | CA | MX</span></b> | To filter based on list of
        categories which are associated with the assortment recommendations. This is allowed when the categorization
        type is BRAND | string |"""

    CATEGORY = "CATEGORY"
    BRAND = "BRAND"

    __str__ = str.__str__


Parameter18OrStr: TypeAlias = Annotated[Parameter18 | str, open_enum_validator(Parameter18)]
