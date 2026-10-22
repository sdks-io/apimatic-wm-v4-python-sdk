from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .max_unit_value9 import MaxUnitValue9, MaxUnitValue9Dict
from .max_value9 import MaxValue9, MaxValue9Dict
from .min_unit_value9 import MinUnitValue9, MinUnitValue9Dict
from .min_value9 import MinValue9, MinValue9Dict
from .per_unit_value9 import PerUnitValue9, PerUnitValue9Dict
from .value9 import Value9, Value9Dict


class ComparisonPrice7(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: Global</b>"""

    value: Optional[Value9] = UNSET
    """<br><b style='color:green;'>Market availability: Global</b>"""

    uom_type: Optional[str] = Field(default=UNSET, alias="uomType")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    min_value: Optional[MinValue9] = Field(default=UNSET, alias="minValue")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    max_value: Optional[MaxValue9] = Field(default=UNSET, alias="maxValue")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    per_unit_value: Optional[PerUnitValue9] = Field(default=UNSET, alias="perUnitValue")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    min_unit_value: Optional[MinUnitValue9] = Field(default=UNSET, alias="minUnitValue")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    max_unit_value: Optional[MaxUnitValue9] = Field(default=UNSET, alias="maxUnitValue")
    """<br><b style='color:green;'>Market availability: Global</b>"""


class ComparisonPrice7Dict(TypedDict):
    value: NotRequired[Value9Dict]
    uom_type: NotRequired[str]
    min_value: NotRequired[MinValue9Dict]
    max_value: NotRequired[MaxValue9Dict]
    per_unit_value: NotRequired[PerUnitValue9Dict]
    min_unit_value: NotRequired[MinUnitValue9Dict]
    max_unit_value: NotRequired[MaxUnitValue9Dict]
