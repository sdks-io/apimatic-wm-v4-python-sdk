from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

ListFinancialEventsErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _ListFinancialEventsError:
    def map(self, response: HttpResponse) -> ListFinancialEventsErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


list_financial_events_error_mapper: Final[ErrorMapper[ListFinancialEventsErrorBody]] = _ListFinancialEventsError()
