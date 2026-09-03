from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetDestinationErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetDestinationError:
    def map(self, response: HttpResponse) -> GetDestinationErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return RawError(response)
            case _:
                return RawError(response)


get_destination_error_mapper: Final[ErrorMapper[GetDestinationErrorBody]] = _GetDestinationError()
