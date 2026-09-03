from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

GetSolicitationActionsForOrderErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _GetSolicitationActionsForOrderError:
    def map(self, response: HttpResponse) -> GetSolicitationActionsForOrderErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


get_solicitation_actions_for_order_error_mapper: Final[
    ErrorMapper[GetSolicitationActionsForOrderErrorBody]
] = _GetSolicitationActionsForOrderError()
