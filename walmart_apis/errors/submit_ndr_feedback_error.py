from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

SubmitNdrFeedbackErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _SubmitNdrFeedbackError:
    def map(self, response: HttpResponse) -> SubmitNdrFeedbackErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


submit_ndr_feedback_error_mapper: Final[ErrorMapper[SubmitNdrFeedbackErrorBody]] = _SubmitNdrFeedbackError()
