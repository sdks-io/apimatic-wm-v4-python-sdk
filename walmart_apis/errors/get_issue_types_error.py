from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_response import ErrorResponse
from ..models.error_response429 import ErrorResponse429

GetIssueTypesErrorBody: TypeAlias = ErrorResponse | ErrorResponse429 | RawError


@dataclass(frozen=True, slots=True)
class _GetIssueTypesError:
    def map(self, status_code: int, content: bytes) -> GetIssueTypesErrorBody:
        match status_code:
            case 401 | 403 | 500 | 503:
                return decode_json[ErrorResponse](content)
            case 429:
                return decode_json[ErrorResponse429](content)
            case _:
                return RawError(status_code, content)


get_issue_types_error_mapper: Final[ErrorMapper[GetIssueTypesErrorBody]] = _GetIssueTypesError()
