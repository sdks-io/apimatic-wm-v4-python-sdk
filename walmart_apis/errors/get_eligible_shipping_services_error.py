from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

GetEligibleShippingServicesErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _GetEligibleShippingServicesError:
    def map(self, response: HttpResponse) -> GetEligibleShippingServicesErrorBody:
        match response.status_code:
            case 400 | 403 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


get_eligible_shipping_services_error_mapper: Final[
    ErrorMapper[GetEligibleShippingServicesErrorBody]
] = _GetEligibleShippingServicesError()
