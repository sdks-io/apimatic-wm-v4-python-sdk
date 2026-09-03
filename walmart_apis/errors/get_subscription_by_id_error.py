from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetSubscriptionByIdErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetSubscriptionByIdError:
    def map(self, response: HttpResponse) -> GetSubscriptionByIdErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return RawError(response)
            case _:
                return RawError(response)


get_subscription_by_id_error_mapper: Final[ErrorMapper[GetSubscriptionByIdErrorBody]] = _GetSubscriptionByIdError()
