from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

GetAnnualStatementOptsErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _GetAnnualStatementOptsError:
    def map(self, response: HttpResponse) -> GetAnnualStatementOptsErrorBody:
        match response.status_code:
            case 400 | 401 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


get_annual_statement_opts_error_mapper: Final[
    ErrorMapper[GetAnnualStatementOptsErrorBody]
] = _GetAnnualStatementOptsError()
