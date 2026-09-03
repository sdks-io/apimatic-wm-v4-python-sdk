from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

SearchTransactionsErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _SearchTransactionsError:
    def map(self, response: HttpResponse) -> SearchTransactionsErrorBody:
        match response.status_code:
            case 400 | 401 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


search_transactions_error_mapper: Final[ErrorMapper[SearchTransactionsErrorBody]] = _SearchTransactionsError()
