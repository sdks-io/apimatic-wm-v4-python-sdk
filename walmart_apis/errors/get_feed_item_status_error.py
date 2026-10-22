from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_feeds404_error21 import V3Feeds404Error21
from ..models.v3_feeds500_error21 import V3Feeds500Error21

GetFeedItemStatusErrorBody: TypeAlias = V3Feeds404Error21 | V3Feeds500Error21 | RawError


@dataclass(frozen=True, slots=True)
class _GetFeedItemStatusError:
    def map(self, status_code: int, content: bytes) -> GetFeedItemStatusErrorBody:
        match status_code:
            case 404:
                return decode_json[V3Feeds404Error21](content)
            case 500:
                return decode_json[V3Feeds500Error21](content)
            case _:
                return RawError(status_code, content)


get_feed_item_status_error_mapper: Final[ErrorMapper[GetFeedItemStatusErrorBody]] = _GetFeedItemStatusError()
