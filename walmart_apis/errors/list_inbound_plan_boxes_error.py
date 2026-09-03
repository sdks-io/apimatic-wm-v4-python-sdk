from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.common_error_list import CommonErrorList

ListInboundPlanBoxesErrorBody: TypeAlias = CommonErrorList | RawError


@dataclass(frozen=True, slots=True)
class _ListInboundPlanBoxesError:
    def map(self, response: HttpResponse) -> ListInboundPlanBoxesErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[CommonErrorList](response)
            case _:
                return RawError(response)


list_inbound_plan_boxes_error_mapper: Final[ErrorMapper[ListInboundPlanBoxesErrorBody]] = _ListInboundPlanBoxesError()
