from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.authorize_error import AuthorizeError
from ..models.oauth_error_model import OauthErrorModel

AuthorizeErrorBody: TypeAlias = AuthorizeError | OauthErrorModel | RawError


@dataclass(frozen=True, slots=True)
class _AuthorizeError:
    def map(self, response: HttpResponse) -> AuthorizeErrorBody:
        match response.status_code:
            case 400:
                return decode_json[AuthorizeError](response)
            case 429 | 500:
                return decode_json[OauthErrorModel](response)
            case _:
                return RawError(response)


authorize_error_mapper: Final[ErrorMapper[AuthorizeErrorBody]] = _AuthorizeError()
