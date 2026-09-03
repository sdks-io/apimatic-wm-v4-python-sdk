from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

SendInvoiceErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _SendInvoiceError:
    def map(self, response: HttpResponse) -> SendInvoiceErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


send_invoice_error_mapper: Final[ErrorMapper[SendInvoiceErrorBody]] = _SendInvoiceError()
