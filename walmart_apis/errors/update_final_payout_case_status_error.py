from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

UpdateFinalPayoutCaseStatusErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _UpdateFinalPayoutCaseStatusError:
    def map(self, response: HttpResponse) -> UpdateFinalPayoutCaseStatusErrorBody:
        match response.status_code:
            case 400 | 404 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


update_final_payout_case_status_error_mapper: Final[
    ErrorMapper[UpdateFinalPayoutCaseStatusErrorBody]
] = _UpdateFinalPayoutCaseStatusError()
