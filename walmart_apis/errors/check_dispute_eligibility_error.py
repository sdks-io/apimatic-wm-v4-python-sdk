from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

CheckDisputeEligibilityErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _CheckDisputeEligibilityError:
    def map(self, response: HttpResponse) -> CheckDisputeEligibilityErrorBody:
        match response.status_code:
            case 400 | 401 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


check_dispute_eligibility_error_mapper: Final[
    ErrorMapper[CheckDisputeEligibilityErrorBody]
] = _CheckDisputeEligibilityError()
