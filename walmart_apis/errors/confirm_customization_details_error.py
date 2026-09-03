from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

ConfirmCustomizationDetailsErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _ConfirmCustomizationDetailsError:
    def map(self, response: HttpResponse) -> ConfirmCustomizationDetailsErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


confirm_customization_details_error_mapper: Final[
    ErrorMapper[ConfirmCustomizationDetailsErrorBody]
] = _ConfirmCustomizationDetailsError()
