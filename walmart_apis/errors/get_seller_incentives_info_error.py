from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_insights_seller_incentives500_error1 import V3InsightsSellerIncentives500Error1
from ..models.v3_token400_error1 import V3Token400Error1

GetSellerIncentivesInfoErrorBody: TypeAlias = V3Token400Error1 | V3InsightsSellerIncentives500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _GetSellerIncentivesInfoError:
    def map(self, status_code: int, content: bytes) -> GetSellerIncentivesInfoErrorBody:
        match status_code:
            case 401 | 403:
                return decode_json[V3Token400Error1](content)
            case 500:
                return decode_json[V3InsightsSellerIncentives500Error1](content)
            case _:
                return RawError(status_code, content)


get_seller_incentives_info_error_mapper: Final[
    ErrorMapper[GetSellerIncentivesInfoErrorBody]
] = _GetSellerIncentivesInfoError()
