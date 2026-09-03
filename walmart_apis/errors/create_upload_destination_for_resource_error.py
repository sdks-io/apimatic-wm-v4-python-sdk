from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

CreateUploadDestinationForResourceErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _CreateUploadDestinationForResourceError:
    def map(self, response: HttpResponse) -> CreateUploadDestinationForResourceErrorBody:
        match response.status_code:
            case 400 | 403 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


create_upload_destination_for_resource_error_mapper: Final[
    ErrorMapper[CreateUploadDestinationForResourceErrorBody]
] = _CreateUploadDestinationForResourceError()
