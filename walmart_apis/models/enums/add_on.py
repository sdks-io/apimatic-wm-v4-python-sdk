from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AddOn(str, Enum):
    """Add-ons Type. Add-ons can be opted during label generation for a shipping. Supported values for add-ons are
    INSURANCE and SIGNATURE. We support standard SIGNATURE Type for now."""

    SIGNATURE = "SIGNATURE"
    INSURANCE = "INSURANCE"

    __str__ = str.__str__


AddOnOrStr: TypeAlias = Annotated[AddOn | str, open_enum_validator(AddOn)]
