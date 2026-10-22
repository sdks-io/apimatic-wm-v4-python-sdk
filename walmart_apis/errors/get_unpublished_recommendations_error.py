from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_response2 import ErrorResponse2

GetUnpublishedRecommendationsErrorBody: TypeAlias = ErrorResponse2 | RawError


@dataclass(frozen=True, slots=True)
class _GetUnpublishedRecommendationsError:
    def map(self, status_code: int, content: bytes) -> GetUnpublishedRecommendationsErrorBody:
        match status_code:
            case 400 | 500:
                return decode_json[ErrorResponse2](content)
            case _:
                return RawError(status_code, content)


get_unpublished_recommendations_error_mapper: Final[
    ErrorMapper[GetUnpublishedRecommendationsErrorBody]
] = _GetUnpublishedRecommendationsError()
