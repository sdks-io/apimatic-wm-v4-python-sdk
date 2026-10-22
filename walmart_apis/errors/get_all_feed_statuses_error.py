from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.feed_record_response import FeedRecordResponse

GetAllFeedStatusesErrorBody: TypeAlias = FeedRecordResponse | RawError


@dataclass(frozen=True, slots=True)
class _GetAllFeedStatusesError:
    def map(self, status_code: int, content: bytes) -> GetAllFeedStatusesErrorBody:
        match status_code:
            case 404 | 500:
                return decode_json[FeedRecordResponse](content)
            case _:
                return RawError(status_code, content)


get_all_feed_statuses_error_mapper: Final[ErrorMapper[GetAllFeedStatusesErrorBody]] = _GetAllFeedStatusesError()
