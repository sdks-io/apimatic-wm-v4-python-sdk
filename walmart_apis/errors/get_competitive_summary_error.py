from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error3 import Error3

GetCompetitiveSummaryErrorBody: TypeAlias = list[Error3] | RawError


@dataclass(frozen=True, slots=True)
class _GetCompetitiveSummaryError:
    def map(self, response: HttpResponse) -> GetCompetitiveSummaryErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[list[Error3]](response)
            case _:
                return RawError(response)


get_competitive_summary_error_mapper: Final[ErrorMapper[GetCompetitiveSummaryErrorBody]] = _GetCompetitiveSummaryError()
