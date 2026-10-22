from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ReportType(str, Enum):
    """Type of report for which the request is created. Example, ITEM for Item Report."""

    ITEM = "ITEM"
    INVENTORY = "INVENTORY"
    CANCELLATION = "CANCELLATION"
    DELIVERY_DEFECT = "DELIVERY_DEFECT"
    ITEM_PERFORMANCE = "ITEM_PERFORMANCE"
    PROMO = "PROMO"
    RETURN_OVERRIDES = "RETURN_OVERRIDES"
    CPA = "CPA"
    SHIPPING_CONFIGURATION = "SHIPPING_CONFIGURATION"
    SHIPPING_PROGRAM = "SHIPPING_PROGRAM"
    BUYBOX = "BUYBOX"
    ASSORTMENT_RECOMMENDATIONS = "ASSORTMENT_RECOMMENDATIONS"
    LAGTIME = "LAGTIME"
    INVENTORY_RECOMMENDATIONS = "INVENTORY_RECOMMENDATIONS"

    __str__ = str.__str__


ReportTypeOrStr: TypeAlias = Annotated[ReportType | str, open_enum_validator(ReportType)]
