from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.common_error_list import CommonErrorList

GetInboundPlanErrorBody: TypeAlias = CommonErrorList | RawError


@dataclass(frozen=True, slots=True)
class _GetInboundPlanError:
    def map(self, response: HttpResponse) -> GetInboundPlanErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[CommonErrorList](response)
            case _:
                return RawError(response)


get_inbound_plan_error_mapper: Final[ErrorMapper[GetInboundPlanErrorBody]] = _GetInboundPlanError()
