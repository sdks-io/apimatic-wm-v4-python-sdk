from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.oauth_error_model import OauthErrorModel
from ..models.registration_error import RegistrationError

RegisterClientErrorBody: TypeAlias = RegistrationError | OauthErrorModel | RawError


@dataclass(frozen=True, slots=True)
class _RegisterClientError:
    def map(self, response: HttpResponse) -> RegisterClientErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[RegistrationError](response)
            case 429 | 500:
                return decode_json[OauthErrorModel](response)
            case _:
                return RawError(response)


register_client_error_mapper: Final[ErrorMapper[RegisterClientErrorBody]] = _RegisterClientError()
