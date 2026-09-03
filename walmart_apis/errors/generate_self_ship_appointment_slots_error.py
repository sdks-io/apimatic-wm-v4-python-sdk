from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.common_error_list import CommonErrorList

GenerateSelfShipAppointmentSlotsErrorBody: TypeAlias = CommonErrorList | RawError


@dataclass(frozen=True, slots=True)
class _GenerateSelfShipAppointmentSlotsError:
    def map(self, response: HttpResponse) -> GenerateSelfShipAppointmentSlotsErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[CommonErrorList](response)
            case _:
                return RawError(response)


generate_self_ship_appointment_slots_error_mapper: Final[
    ErrorMapper[GenerateSelfShipAppointmentSlotsErrorBody]
] = _GenerateSelfShipAppointmentSlotsError()
