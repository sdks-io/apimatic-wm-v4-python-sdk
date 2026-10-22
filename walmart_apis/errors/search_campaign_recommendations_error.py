from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_response import ErrorResponse
from ..models.error_response429 import ErrorResponse429

SearchCampaignRecommendationsErrorBody: TypeAlias = ErrorResponse | ErrorResponse429 | RawError


@dataclass(frozen=True, slots=True)
class _SearchCampaignRecommendationsError:
    def map(self, status_code: int, content: bytes) -> SearchCampaignRecommendationsErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500 | 503:
                return decode_json[ErrorResponse](content)
            case 429:
                return decode_json[ErrorResponse429](content)
            case _:
                return RawError(status_code, content)


search_campaign_recommendations_error_mapper: Final[
    ErrorMapper[SearchCampaignRecommendationsErrorBody]
] = _SearchCampaignRecommendationsError()
