from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

SendTestNotificationErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _SendTestNotificationError:
    def map(self, response: HttpResponse) -> SendTestNotificationErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return RawError(response)
            case _:
                return RawError(response)


send_test_notification_error_mapper: Final[ErrorMapper[SendTestNotificationErrorBody]] = _SendTestNotificationError()
