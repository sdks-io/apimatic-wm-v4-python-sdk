from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.common_error_list import CommonErrorList

ScheduleSelfShipAppointmentErrorBody: TypeAlias = CommonErrorList | RawError


@dataclass(frozen=True, slots=True)
class _ScheduleSelfShipAppointmentError:
    def map(self, response: HttpResponse) -> ScheduleSelfShipAppointmentErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[CommonErrorList](response)
            case _:
                return RawError(response)


schedule_self_ship_appointment_error_mapper: Final[
    ErrorMapper[ScheduleSelfShipAppointmentErrorBody]
] = _ScheduleSelfShipAppointmentError()
