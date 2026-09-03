from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

InitiateFasterPayoutErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _InitiateFasterPayoutError:
    def map(self, response: HttpResponse) -> InitiateFasterPayoutErrorBody:
        match response.status_code:
            case 400 | 401 | 409 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


initiate_faster_payout_error_mapper: Final[ErrorMapper[InitiateFasterPayoutErrorBody]] = _InitiateFasterPayoutError()
