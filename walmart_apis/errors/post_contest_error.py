from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_items_dispute_duplicates_contest403_error1 import V3ItemsDisputeDuplicatesContest403Error1
from ..models.v3_items_dispute_duplicates_contest404_error1 import V3ItemsDisputeDuplicatesContest404Error1
from ..models.v3_items_dispute_duplicates_contest500_error1 import V3ItemsDisputeDuplicatesContest500Error1

PostContestErrorBody: TypeAlias = (
    V3ItemsDisputeDuplicatesContest403Error1
    | V3ItemsDisputeDuplicatesContest404Error1
    | V3ItemsDisputeDuplicatesContest500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _PostContestError:
    def map(self, status_code: int, content: bytes) -> PostContestErrorBody:
        match status_code:
            case 403:
                return decode_json[V3ItemsDisputeDuplicatesContest403Error1](content)
            case 404:
                return decode_json[V3ItemsDisputeDuplicatesContest404Error1](content)
            case 500:
                return decode_json[V3ItemsDisputeDuplicatesContest500Error1](content)
            case _:
                return RawError(status_code, content)


post_contest_error_mapper: Final[ErrorMapper[PostContestErrorBody]] = _PostContestError()
