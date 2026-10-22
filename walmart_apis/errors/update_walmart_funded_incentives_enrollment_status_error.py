from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_token400_error1 import V3Token400Error1

UpdateWalmartFundedIncentivesEnrollmentStatusErrorBody: TypeAlias = V3Token400Error1 | RawError


@dataclass(frozen=True, slots=True)
class _UpdateWalmartFundedIncentivesEnrollmentStatusError:
    def map(self, status_code: int, content: bytes) -> UpdateWalmartFundedIncentivesEnrollmentStatusErrorBody:
        match status_code:
            case 403 | 500:
                return decode_json[V3Token400Error1](content)
            case _:
                return RawError(status_code, content)


update_walmart_funded_incentives_enrollment_status_error_mapper: Final[
    ErrorMapper[UpdateWalmartFundedIncentivesEnrollmentStatusErrorBody]
] = _UpdateWalmartFundedIncentivesEnrollmentStatusError()
