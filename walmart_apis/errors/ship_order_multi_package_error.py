from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

ShipOrderMultiPackageErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _ShipOrderMultiPackageError:
    def map(self, response: HttpResponse) -> ShipOrderMultiPackageErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500 | 503:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


ship_order_multi_package_error_mapper: Final[
    ErrorMapper[ShipOrderMultiPackageErrorBody]
] = _ShipOrderMultiPackageError()
