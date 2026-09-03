from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

ListSettlementDetailsErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _ListSettlementDetailsError:
    def map(self, response: HttpResponse) -> ListSettlementDetailsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


list_settlement_details_error_mapper: Final[ErrorMapper[ListSettlementDetailsErrorBody]] = _ListSettlementDetailsError()
