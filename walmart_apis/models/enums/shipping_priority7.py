from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ShippingPriority7(str, Enum):
    """Shipping priority will help system decide the carrier service for fulfillment in case there are multiple shipping
    options available for customers with different carrier services in terms of shipping cost and speed. <br><b
    style='color:green;'>Market availability: US</span></b>"""

    SLOWEST = "SLOWEST"
    FASTEST = "FASTEST"

    __str__ = str.__str__


ShippingPriority7OrStr: TypeAlias = Annotated[ShippingPriority7 | str, open_enum_validator(ShippingPriority7)]
