from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_insights_prosellerbadge400_error1 import V3InsightsProsellerbadge400Error1
from ..models.v3_insights_prosellerbadge500_error1 import V3InsightsProsellerbadge500Error1
from ..models.v3_token400_error1 import V3Token400Error1

GetProSellerBadgeInfoErrorBody: TypeAlias = (
    V3InsightsProsellerbadge400Error1 | V3Token400Error1 | V3InsightsProsellerbadge500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _GetProSellerBadgeInfoError:
    def map(self, status_code: int, content: bytes) -> GetProSellerBadgeInfoErrorBody:
        match status_code:
            case 400:
                return decode_json[V3InsightsProsellerbadge400Error1](content)
            case 401 | 403:
                return decode_json[V3Token400Error1](content)
            case 500:
                return decode_json[V3InsightsProsellerbadge500Error1](content)
            case _:
                return RawError(status_code, content)


get_pro_seller_badge_info_error_mapper: Final[
    ErrorMapper[GetProSellerBadgeInfoErrorBody]
] = _GetProSellerBadgeInfoError()
