from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

CreateSubscriptionErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _CreateSubscriptionError:
    def map(self, response: HttpResponse) -> CreateSubscriptionErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return RawError(response)
            case _:
                return RawError(response)


create_subscription_error_mapper: Final[ErrorMapper[CreateSubscriptionErrorBody]] = _CreateSubscriptionError()
