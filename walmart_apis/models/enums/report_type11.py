from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ReportType11(str, Enum):
    """Specifies the type of report to be generated. Example: ITEM for Item Report."""

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
    SEM_PERFORMANCE = "SEM_PERFORMANCE"

    __str__ = str.__str__


ReportType11OrStr: TypeAlias = Annotated[ReportType11 | str, open_enum_validator(ReportType11)]
