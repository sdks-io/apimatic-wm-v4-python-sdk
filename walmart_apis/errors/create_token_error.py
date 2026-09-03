from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.oauth_error_model import OauthErrorModel

CreateTokenErrorBody: TypeAlias = OauthErrorModel | RawError


@dataclass(frozen=True, slots=True)
class _CreateTokenError:
    def map(self, response: HttpResponse) -> CreateTokenErrorBody:
        match response.status_code:
            case 400 | 401 | 429 | 500:
                return decode_json[OauthErrorModel](response)
            case _:
                return RawError(response)


create_token_error_mapper: Final[ErrorMapper[CreateTokenErrorBody]] = _CreateTokenError()
