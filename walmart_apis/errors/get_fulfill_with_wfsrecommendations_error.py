from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_response2 import ErrorResponse2

GetFulfillWithWfsrecommendationsErrorBody: TypeAlias = ErrorResponse2 | RawError


@dataclass(frozen=True, slots=True)
class _GetFulfillWithWfsrecommendationsError:
    def map(self, status_code: int, content: bytes) -> GetFulfillWithWfsrecommendationsErrorBody:
        match status_code:
            case 400 | 500:
                return decode_json[ErrorResponse2](content)
            case _:
                return RawError(status_code, content)


get_fulfill_with_wfsrecommendations_error_mapper: Final[
    ErrorMapper[GetFulfillWithWfsrecommendationsErrorBody]
] = _GetFulfillWithWfsrecommendationsError()
