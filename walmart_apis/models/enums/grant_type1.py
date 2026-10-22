from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GrantType1(str, Enum):
    """Type of grant requested. <br /> **Available grant types:** authorization_code, refresh_token and
    client_credentials

    <strong style="color: green;">**Market availability: Global**</strong>"""

    AUTHORIZATION_CODE = "authorization_code"
    REFRESH_TOKEN = "refresh_token"
    CLIENT_CREDENTIALS = "client_credentials"

    __str__ = str.__str__


GrantType1OrStr: TypeAlias = Annotated[GrantType1 | str, open_enum_validator(GrantType1)]
