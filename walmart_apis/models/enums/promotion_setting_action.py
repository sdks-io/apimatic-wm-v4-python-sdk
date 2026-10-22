from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PromotionSettingAction(str, Enum):
    """| Market | Translation |
    | --- | ----------- |
    | CA | ["Create", "Delete","Replace All"]|
    | MX & CL | ["Crear", "Eliminar","Reemplazar todo"]|

    <br><b style='color:green;'>Market availability: CA | MX | CL"""

    CREATE = "Create"
    DELETE = "Delete"
    REPLACE_ALL = "Replace All"
    CREAR = "Crear"
    ELIMINAR = "Eliminar"
    REEMPLAZAR_TODO = "Reemplazar todo"

    __str__ = str.__str__


PromotionSettingActionOrStr: TypeAlias = Annotated[
    PromotionSettingAction | str, open_enum_validator(PromotionSettingAction)
]
