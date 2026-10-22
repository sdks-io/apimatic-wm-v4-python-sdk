from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error3 import Error3, Error3Dict
from .results4 import Results4, Results4Dict


class V3Feeds404Error2(SdkBaseModel):
    errors: Optional[list[Error3]] = UNSET
    total_results: Optional[int] = Field(default=UNSET, alias="totalResults")
    """Total number of feeds returned."""

    offset: Optional[int] = UNSET
    """The object response to the starting number, where 0 is the first available."""

    limit: Optional[int] = UNSET
    """The number of items to be returned."""

    results: Optional[Results4] = UNSET
    """Specifies the feed status results."""


class V3Feeds404Error2Dict(TypedDict):
    errors: NotRequired[list[Error3Dict]]
    total_results: NotRequired[int]
    offset: NotRequired[int]
    limit: NotRequired[int]
    results: NotRequired[Results4Dict]
