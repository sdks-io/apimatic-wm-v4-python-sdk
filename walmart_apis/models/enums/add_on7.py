from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AddOn7(str, Enum):
    """AddOns Type. AddOns can be opted during label generation for a shipping. Supported values for AddOns are
    INSURANCE and SIGNATURE. We support standard SIGNATURE Type for now."""

    SIGNATURE = "SIGNATURE"
    INSURANCE = "INSURANCE"

    __str__ = str.__str__


AddOn7OrStr: TypeAlias = Annotated[AddOn7 | str, open_enum_validator(AddOn7)]
