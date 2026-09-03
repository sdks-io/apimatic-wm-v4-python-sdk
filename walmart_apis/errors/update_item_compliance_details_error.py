from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.common_error_list import CommonErrorList

UpdateItemComplianceDetailsErrorBody: TypeAlias = CommonErrorList | RawError


@dataclass(frozen=True, slots=True)
class _UpdateItemComplianceDetailsError:
    def map(self, response: HttpResponse) -> UpdateItemComplianceDetailsErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[CommonErrorList](response)
            case _:
                return RawError(response)


update_item_compliance_details_error_mapper: Final[
    ErrorMapper[UpdateItemComplianceDetailsErrorBody]
] = _UpdateItemComplianceDetailsError()
