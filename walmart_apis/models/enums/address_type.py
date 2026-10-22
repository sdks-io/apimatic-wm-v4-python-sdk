from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AddressType(str, Enum):
    """Type of address to which shipping has to be covered as part of mentioned region, sub region and states."""

    PO_BOX = "PO_BOX"
    MILITARY = "MILITARY"
    STREET = "STREET"

    __str__ = str.__str__


AddressTypeOrStr: TypeAlias = Annotated[AddressType | str, open_enum_validator(AddressType)]
