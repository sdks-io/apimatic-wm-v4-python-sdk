from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

CreateConfirmDeliveryDetailsErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _CreateConfirmDeliveryDetailsError:
    def map(self, response: HttpResponse) -> CreateConfirmDeliveryDetailsErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


create_confirm_delivery_details_error_mapper: Final[
    ErrorMapper[CreateConfirmDeliveryDetailsErrorBody]
] = _CreateConfirmDeliveryDetailsError()
