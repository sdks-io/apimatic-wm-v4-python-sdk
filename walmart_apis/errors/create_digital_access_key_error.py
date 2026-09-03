from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

CreateDigitalAccessKeyErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _CreateDigitalAccessKeyError:
    def map(self, response: HttpResponse) -> CreateDigitalAccessKeyErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


create_digital_access_key_error_mapper: Final[
    ErrorMapper[CreateDigitalAccessKeyErrorBody]
] = _CreateDigitalAccessKeyError()
