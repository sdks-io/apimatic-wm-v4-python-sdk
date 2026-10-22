from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class WsrErrorDetail(SdkBaseModel):
    """Individual error detail"""

    code: Optional[str] = UNSET
    """Error code of the response.

    **Common Codes**:
    - ``SA_4000``: Bad request / validation error
    - ``SA_4001``: Unauthorized
    - ``SA_4003``: Forbidden
    - ``SA_5000``: Internal server error"""

    description: Optional[str] = UNSET
    """Human-readable description of the error"""


class WsrErrorDetailDict(TypedDict):
    code: NotRequired[str]
    description: NotRequired[str]
