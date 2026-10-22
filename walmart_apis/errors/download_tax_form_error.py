from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v1_settings_downloadtaxformprofile400_error1 import V1SettingsDownloadtaxformprofile400Error1
from ..models.v1_settings_downloadtaxformprofile404_error1 import V1SettingsDownloadtaxformprofile404Error1
from ..models.v1_settings_downloadtaxformprofile500_error1 import V1SettingsDownloadtaxformprofile500Error1
from ..models.v1_settings_downloadtaxformprofile502_error1 import V1SettingsDownloadtaxformprofile502Error1

DownloadTaxFormErrorBody: TypeAlias = (
    V1SettingsDownloadtaxformprofile400Error1
    | V1SettingsDownloadtaxformprofile404Error1
    | V1SettingsDownloadtaxformprofile500Error1
    | V1SettingsDownloadtaxformprofile502Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _DownloadTaxFormError:
    def map(self, status_code: int, content: bytes) -> DownloadTaxFormErrorBody:
        match status_code:
            case 400:
                return decode_json[V1SettingsDownloadtaxformprofile400Error1](content)
            case 404:
                return decode_json[V1SettingsDownloadtaxformprofile404Error1](content)
            case 500:
                return decode_json[V1SettingsDownloadtaxformprofile500Error1](content)
            case 502:
                return decode_json[V1SettingsDownloadtaxformprofile502Error1](content)
            case _:
                return RawError(status_code, content)


download_tax_form_error_mapper: Final[ErrorMapper[DownloadTaxFormErrorBody]] = _DownloadTaxFormError()
