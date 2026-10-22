from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_token400_error1 import V3Token400Error1
from ..models.v3_token401_error1 import V3Token401Error1
from ..models.v3_token500_error1 import V3Token500Error1

TokenApiErrorBody: TypeAlias = V3Token400Error1 | V3Token401Error1 | V3Token500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _TokenApiError:
    def map(self, status_code: int, content: bytes) -> TokenApiErrorBody:
        match status_code:
            case 400:
                return decode_json[V3Token400Error1](content)
            case 401:
                return decode_json[V3Token401Error1](content)
            case 500:
                return decode_json[V3Token500Error1](content)
            case _:
                return RawError(status_code, content)


token_api_error_mapper: Final[ErrorMapper[TokenApiErrorBody]] = _TokenApiError()
