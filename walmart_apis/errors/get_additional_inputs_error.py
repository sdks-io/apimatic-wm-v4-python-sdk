from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

GetAdditionalInputsErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _GetAdditionalInputsError:
    def map(self, response: HttpResponse) -> GetAdditionalInputsErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


get_additional_inputs_error_mapper: Final[ErrorMapper[GetAdditionalInputsErrorBody]] = _GetAdditionalInputsError()
