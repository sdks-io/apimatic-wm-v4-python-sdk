from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

GetFasterPayoutEligibilityErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _GetFasterPayoutEligibilityError:
    def map(self, response: HttpResponse) -> GetFasterPayoutEligibilityErrorBody:
        match response.status_code:
            case 400 | 401 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


get_faster_payout_eligibility_error_mapper: Final[
    ErrorMapper[GetFasterPayoutEligibilityErrorBody]
] = _GetFasterPayoutEligibilityError()
