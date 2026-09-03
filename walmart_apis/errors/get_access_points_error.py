from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

GetAccessPointsErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _GetAccessPointsError:
    def map(self, response: HttpResponse) -> GetAccessPointsErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


get_access_points_error_mapper: Final[ErrorMapper[GetAccessPointsErrorBody]] = _GetAccessPointsError()
