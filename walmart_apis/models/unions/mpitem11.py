from __future__ import annotations

from typing import TypeAlias

from ..price_feed_price_item import PriceFeedPriceItem, PriceFeedPriceItemDict
from ..price_feed_promo_discount_item import PriceFeedPromoDiscountItem, PriceFeedPromoDiscountItemDict

Mpitem11: TypeAlias = list[PriceFeedPriceItem] | list[PriceFeedPromoDiscountItem]

Mpitem11Dict: TypeAlias = list[PriceFeedPriceItemDict] | list[PriceFeedPromoDiscountItemDict]
