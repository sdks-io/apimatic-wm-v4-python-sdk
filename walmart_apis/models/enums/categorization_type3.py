from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CategorizationType3(str, Enum):
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | BRAND | To get list of brands which are associated with the assortment recommendations | string |
    | CATEGORY | To get list of categories which are associated with the assortment recommendations | string |

    <br><b style='color:green;'>Market availability: US | CA | MX</span></b>"""

    BRAND = "BRAND"
    CATEGORY = "CATEGORY"

    __str__ = str.__str__


CategorizationType3OrStr: TypeAlias = Annotated[CategorizationType3 | str, open_enum_validator(CategorizationType3)]
