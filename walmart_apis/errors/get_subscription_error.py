from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetSubscriptionErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetSubscriptionError:
    def map(self, response: HttpResponse) -> GetSubscriptionErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return RawError(response)
            case _:
                return RawError(response)


get_subscription_error_mapper: Final[ErrorMapper[GetSubscriptionErrorBody]] = _GetSubscriptionError()
