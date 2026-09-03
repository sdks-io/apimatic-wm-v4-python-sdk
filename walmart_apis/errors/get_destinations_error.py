from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetDestinationsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetDestinationsError:
    def map(self, response: HttpResponse) -> GetDestinationsErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return RawError(response)
            case _:
                return RawError(response)


get_destinations_error_mapper: Final[ErrorMapper[GetDestinationsErrorBody]] = _GetDestinationsError()
