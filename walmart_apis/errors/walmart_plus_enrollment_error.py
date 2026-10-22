from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_feeds_feed_type_program_actions_request_type_walmart_plus_sff400_error1 import (
    V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSff400Error1,
)
from ..models.v3_feeds_feed_type_program_actions_request_type_walmart_plus_sff500_error1 import (
    V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSff500Error1,
)

WalmartPlusEnrollmentErrorBody: TypeAlias = (
    V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSff400Error1
    | V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSff500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _WalmartPlusEnrollmentError:
    def map(self, status_code: int, content: bytes) -> WalmartPlusEnrollmentErrorBody:
        match status_code:
            case 400:
                return decode_json[V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSff400Error1](content)
            case 500:
                return decode_json[V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSff500Error1](content)
            case _:
                return RawError(status_code, content)


walmart_plus_enrollment_error_mapper: Final[ErrorMapper[WalmartPlusEnrollmentErrorBody]] = _WalmartPlusEnrollmentError()
