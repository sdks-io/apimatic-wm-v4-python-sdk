from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TemplateType(str, Enum):
    NON_MACRO = "NON_MACRO"

    __str__ = str.__str__


TemplateTypeOrStr: TypeAlias = Annotated[TemplateType | str, open_enum_validator(TemplateType)]
