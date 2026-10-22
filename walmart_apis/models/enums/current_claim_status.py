from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CurrentClaimStatus(str, Enum):
    INITIATED = "INITIATED"
    IN_REVIEW = "IN_REVIEW"
    NEED_INFO = "NEED_INFO"
    APPROVED = "APPROVED"
    PAYMENT_INITIATED = "PAYMENT_INITIATED"
    PAID_OUT = "PAID_OUT"
    REJECTED = "REJECTED"

    __str__ = str.__str__


CurrentClaimStatusOrStr: TypeAlias = Annotated[CurrentClaimStatus | str, open_enum_validator(CurrentClaimStatus)]
