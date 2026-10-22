from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.sem_error_response400 import SemErrorResponse400

GetItemRecommendationsErrorBody: TypeAlias = SemErrorResponse400 | RawError


@dataclass(frozen=True, slots=True)
class _GetItemRecommendationsError:
    def map(self, status_code: int, content: bytes) -> GetItemRecommendationsErrorBody:
        match status_code:
            case 400 | 500:
                return decode_json[SemErrorResponse400](content)
            case _:
                return RawError(status_code, content)


get_item_recommendations_error_mapper: Final[
    ErrorMapper[GetItemRecommendationsErrorBody]
] = _GetItemRecommendationsError()
