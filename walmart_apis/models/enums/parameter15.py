from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Parameter15(str, Enum):
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | BRAND <br><b style='color:green;'>Market availability: US, CA, MX</span></b> | To filter based on list of brands
        which are associated with the assortment recommendations | string |
    | CATEGORY <br><b style='color:green;'>Market availability: US, CA, MX</span></b> | To filter based on list of
        categories which are associated with the assortment recommendations | string |
    | PRODUCT_TYPE <br><b style='color:green;'>Market availability: US only</span></b> | To filter based on list of
        product types which are associated with the assortment recommendations | string |"""

    BRAND = "BRAND"
    CATEGORY = "CATEGORY"
    PRODUCT_TYPE = "PRODUCT_TYPE"

    __str__ = str.__str__


Parameter15OrStr: TypeAlias = Annotated[Parameter15 | str, open_enum_validator(Parameter15)]
