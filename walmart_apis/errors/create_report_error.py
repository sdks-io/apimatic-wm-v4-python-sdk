from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

CreateReportErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _CreateReportError:
    def map(self, response: HttpResponse) -> CreateReportErrorBody:
        match response.status_code:
            case 400 | 403 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


create_report_error_mapper: Final[ErrorMapper[CreateReportErrorBody]] = _CreateReportError()
