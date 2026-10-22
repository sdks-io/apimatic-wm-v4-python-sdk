from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.sem_error_response400 import SemErrorResponse400

DeleteCampaignErrorBody: TypeAlias = SemErrorResponse400 | RawError


@dataclass(frozen=True, slots=True)
class _DeleteCampaignError:
    def map(self, status_code: int, content: bytes) -> DeleteCampaignErrorBody:
        match status_code:
            case 400 | 404 | 500:
                return decode_json[SemErrorResponse400](content)
            case _:
                return RawError(status_code, content)


delete_campaign_error_mapper: Final[ErrorMapper[DeleteCampaignErrorBody]] = _DeleteCampaignError()
