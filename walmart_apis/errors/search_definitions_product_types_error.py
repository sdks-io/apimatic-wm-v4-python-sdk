from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

SearchDefinitionsProductTypesErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _SearchDefinitionsProductTypesError:
    def map(self, response: HttpResponse) -> SearchDefinitionsProductTypesErrorBody:
        match response.status_code:
            case 400 | 403 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


search_definitions_product_types_error_mapper: Final[
    ErrorMapper[SearchDefinitionsProductTypesErrorBody]
] = _SearchDefinitionsProductTypesError()
