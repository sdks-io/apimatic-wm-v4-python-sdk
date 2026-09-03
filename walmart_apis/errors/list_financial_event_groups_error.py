from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

ListFinancialEventGroupsErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _ListFinancialEventGroupsError:
    def map(self, response: HttpResponse) -> ListFinancialEventGroupsErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


list_financial_event_groups_error_mapper: Final[
    ErrorMapper[ListFinancialEventGroupsErrorBody]
] = _ListFinancialEventGroupsError()
