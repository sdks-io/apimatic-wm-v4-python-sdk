from __future__ import annotations

from typing import TypeAlias

from ..price_feed_promo_discount_item import PriceFeedPromoDiscountItem, PriceFeedPromoDiscountItemDict
from ..promotion_feed_price_item import PromotionFeedPriceItem, PromotionFeedPriceItemDict

Mpitem111: TypeAlias = list[PromotionFeedPriceItem] | list[PriceFeedPromoDiscountItem]

Mpitem111Dict: TypeAlias = list[PromotionFeedPriceItemDict] | list[PriceFeedPromoDiscountItemDict]
