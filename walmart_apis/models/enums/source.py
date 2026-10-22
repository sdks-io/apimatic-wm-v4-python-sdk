from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Source(str, Enum):
    """Originating source of the rich media asset. Possible values: ``MARKETPLACE_PARTNER``, ``SELLER_API``"""

    MARKETPLACE_PARTNER = "MARKETPLACE_PARTNER"
    SELLER_API = "SELLER_API"

    __str__ = str.__str__


SourceOrStr: TypeAlias = Annotated[Source | str, open_enum_validator(Source)]
