from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

CreateProductReviewAndSellerFeedbackSolicitationErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _CreateProductReviewAndSellerFeedbackSolicitationError:
    def map(self, response: HttpResponse) -> CreateProductReviewAndSellerFeedbackSolicitationErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


create_product_review_and_seller_feedback_solicitation_error_mapper: Final[
    ErrorMapper[CreateProductReviewAndSellerFeedbackSolicitationErrorBody]
] = _CreateProductReviewAndSellerFeedbackSolicitationError()
