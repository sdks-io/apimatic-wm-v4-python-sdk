from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.sem_error_response400 import SemErrorResponse400

UpdateCampaignErrorBody: TypeAlias = SemErrorResponse400 | RawError


@dataclass(frozen=True, slots=True)
class _UpdateCampaignError:
    def map(self, status_code: int, content: bytes) -> UpdateCampaignErrorBody:
        match status_code:
            case 400 | 404 | 500:
                return decode_json[SemErrorResponse400](content)
            case _:
                return RawError(status_code, content)


update_campaign_error_mapper: Final[ErrorMapper[UpdateCampaignErrorBody]] = _UpdateCampaignError()
