from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

GetInventorySummariesErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _GetInventorySummariesError:
    def map(self, response: HttpResponse) -> GetInventorySummariesErrorBody:
        match response.status_code:
            case 400 | 403 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


get_inventory_summaries_error_mapper: Final[ErrorMapper[GetInventorySummariesErrorBody]] = _GetInventorySummariesError()
