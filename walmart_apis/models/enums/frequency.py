from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Frequency(str, Enum):
    """Specifies the frequency at which the report should be generated. For example, if set to YEARLY, the report will
    be generated once every year."""

    HOURLY = "HOURLY"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"
    YEARLY = "YEARLY"

    __str__ = str.__str__


FrequencyOrStr: TypeAlias = Annotated[Frequency | str, open_enum_validator(Frequency)]
