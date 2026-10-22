from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PromotionSettingAction1(str, Enum):
    """| Market | Translation |
    | --- | ----------- |
    | US | ["Create", "Delete","Replace All"]|
    <br><b style='color:green;'>Market availability: US"""

    CREATE = "Create"
    DELETE = "Delete"
    REPLACE_ALL = "Replace All"

    __str__ = str.__str__


PromotionSettingAction1OrStr: TypeAlias = Annotated[
    PromotionSettingAction1 | str, open_enum_validator(PromotionSettingAction1)
]
