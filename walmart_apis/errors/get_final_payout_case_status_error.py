from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

GetFinalPayoutCaseStatusErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _GetFinalPayoutCaseStatusError:
    def map(self, response: HttpResponse) -> GetFinalPayoutCaseStatusErrorBody:
        match response.status_code:
            case 400 | 401 | 404 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


get_final_payout_case_status_error_mapper: Final[
    ErrorMapper[GetFinalPayoutCaseStatusErrorBody]
] = _GetFinalPayoutCaseStatusError()
