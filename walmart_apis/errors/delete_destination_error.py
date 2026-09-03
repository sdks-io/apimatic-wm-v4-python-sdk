from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DeleteDestinationErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteDestinationError:
    def map(self, response: HttpResponse) -> DeleteDestinationErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return RawError(response)
            case _:
                return RawError(response)


delete_destination_error_mapper: Final[ErrorMapper[DeleteDestinationErrorBody]] = _DeleteDestinationError()
