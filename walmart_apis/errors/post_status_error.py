from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_items_dispute_duplicates_status403_error1 import V3ItemsDisputeDuplicatesStatus403Error1
from ..models.v3_items_dispute_duplicates_status404_error1 import V3ItemsDisputeDuplicatesStatus404Error1
from ..models.v3_items_dispute_duplicates_status500_error1 import V3ItemsDisputeDuplicatesStatus500Error1

PostStatusErrorBody: TypeAlias = (
    V3ItemsDisputeDuplicatesStatus403Error1
    | V3ItemsDisputeDuplicatesStatus404Error1
    | V3ItemsDisputeDuplicatesStatus500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _PostStatusError:
    def map(self, status_code: int, content: bytes) -> PostStatusErrorBody:
        match status_code:
            case 403:
                return decode_json[V3ItemsDisputeDuplicatesStatus403Error1](content)
            case 404:
                return decode_json[V3ItemsDisputeDuplicatesStatus404Error1](content)
            case 500:
                return decode_json[V3ItemsDisputeDuplicatesStatus500Error1](content)
            case _:
                return RawError(status_code, content)


post_status_error_mapper: Final[ErrorMapper[PostStatusErrorBody]] = _PostStatusError()
