from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RejectionCodes1(str, Enum):
    """List of rejection codes. <br><b style='color:green;'>Market availability: US, CA, MX</span></b>

    | Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | NOT_SELLING_THESE_ITEMS<br><b style='color:green;'>Market availability: US, CA, MX</span></b> | As a seller, I
        don’t intend to sell these items on Walmart | string |
    | NOT_SELLING_THESE_BRANDS<br><b style='color:green;'>Market availability: US, CA, MX</span></b> | As a seller, I
        don’t intend to sell these brands on Walmart | string |
    | NOT_SELLING_THESE_CATEGORIES<br><b style='color:green;'>Market availability: US only</span></b> | As a seller, I
        don’t intend to sell these categories on Walmart | string |
    | LIMITED_TO_OTHER_MARKETPLACE<br><b style='color:green;'>Market availability: US, CA, MX</span></b> | As a seller,
        I intend to sell the rejected items only on other marketplaces | string |
    | ALREADY_SELLING_ON_WALMART<br><b style='color:green;'>Market availability: US, CA, MX</span></b> | I am already
        selling these items on Walmart | string |
    | OTHER_REASON<br><b style='color:green;'>Market availability: US, CA, MX</span></b> | Other reason for rejecting
        the items. customRejectionMessage is mandatory to pass if rejectionCode is OTHER_REASON. | string |"""

    NOT_SELLING_THESE_ITEMS = "NOT_SELLING_THESE_ITEMS"
    NOT_SELLING_THESE_BRANDS = "NOT_SELLING_THESE_BRANDS"
    NOT_SELLING_THESE_CATEGORIES = "NOT_SELLING_THESE_CATEGORIES"
    LIMITED_TO_OTHER_MARKETPLACE = "LIMITED_TO_OTHER_MARKETPLACE"
    ALREADY_SELLING_ON_WALMART = "ALREADY_SELLING_ON_WALMART"
    OTHER_REASON = "OTHER_REASON"

    __str__ = str.__str__


RejectionCodes1OrStr: TypeAlias = Annotated[RejectionCodes1 | str, open_enum_validator(RejectionCodes1)]
