from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

GetOrderMetricsErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _GetOrderMetricsError:
    def map(self, response: HttpResponse) -> GetOrderMetricsErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


get_order_metrics_error_mapper: Final[ErrorMapper[GetOrderMetricsErrorBody]] = _GetOrderMetricsError()
