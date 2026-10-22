from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.sem_error_response400 import SemErrorResponse400

GetBillingHistoryErrorBody: TypeAlias = SemErrorResponse400 | RawError


@dataclass(frozen=True, slots=True)
class _GetBillingHistoryError:
    def map(self, status_code: int, content: bytes) -> GetBillingHistoryErrorBody:
        match status_code:
            case 400 | 500:
                return decode_json[SemErrorResponse400](content)
            case _:
                return RawError(status_code, content)


get_billing_history_error_mapper: Final[ErrorMapper[GetBillingHistoryErrorBody]] = _GetBillingHistoryError()
