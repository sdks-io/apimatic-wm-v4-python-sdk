from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.common_error_list import CommonErrorList

UpdateShipmentTrackingDetailsErrorBody: TypeAlias = CommonErrorList | RawError


@dataclass(frozen=True, slots=True)
class _UpdateShipmentTrackingDetailsError:
    def map(self, response: HttpResponse) -> UpdateShipmentTrackingDetailsErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[CommonErrorList](response)
            case _:
                return RawError(response)


update_shipment_tracking_details_error_mapper: Final[
    ErrorMapper[UpdateShipmentTrackingDetailsErrorBody]
] = _UpdateShipmentTrackingDetailsError()
