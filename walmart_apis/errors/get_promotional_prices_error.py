from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_token500_error1 import V3Token500Error1

GetPromotionalPricesErrorBody: TypeAlias = V3Token500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _GetPromotionalPricesError:
    def map(self, status_code: int, content: bytes) -> GetPromotionalPricesErrorBody:
        match status_code:
            case 401:
                return decode_json[V3Token500Error1](content)
            case _:
                return RawError(status_code, content)


get_promotional_prices_error_mapper: Final[ErrorMapper[GetPromotionalPricesErrorBody]] = _GetPromotionalPricesError()
