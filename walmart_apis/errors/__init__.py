from .bulk_update_item_status_error import BulkUpdateItemStatusErrorBody, bulk_update_item_status_error_mapper
from .create_campaign_error import CreateCampaignErrorBody, create_campaign_error_mapper
from .create_label_error import CreateLabelErrorBody, create_label_error_mapper
from .create_label_mps_error import CreateLabelMpsErrorBody, create_label_mps_error_mapper
from .create_strategy_error import CreateStrategyErrorBody, create_strategy_error_mapper
from .delete_campaign_error import DeleteCampaignErrorBody, delete_campaign_error_mapper
from .delete_strategy_error import DeleteStrategyErrorBody, delete_strategy_error_mapper
from .discard_label_error import DiscardLabelErrorBody, discard_label_error_mapper
from .download_claim_documents_error import DownloadClaimDocumentsErrorBody, download_claim_documents_error_mapper
from .download_tax_form_error import DownloadTaxFormErrorBody, download_tax_form_error_mapper
from .generate_report_error import GenerateReportErrorBody, generate_report_error_mapper
from .get_all_assets_error import GetAllAssetsErrorBody, get_all_assets_error_mapper
from .get_all_feed_statuses_error import GetAllFeedStatusesErrorBody, get_all_feed_statuses_error_mapper
from .get_all_incentives_error import GetAllIncentivesErrorBody, get_all_incentives_error_mapper
from .get_assortment_recommendation_trends_error import (
    GetAssortmentRecommendationTrendsErrorBody,
    get_assortment_recommendation_trends_error_mapper,
)
from .get_assortment_recommendation_variants_error import (
    GetAssortmentRecommendationVariantsErrorBody,
    get_assortment_recommendation_variants_error_mapper,
)
from .get_assortment_recommendations_error import (
    GetAssortmentRecommendationsErrorBody,
    get_assortment_recommendations_error_mapper,
)
from .get_billing_history_error import GetBillingHistoryErrorBody, get_billing_history_error_mapper
from .get_campaign_details_error import GetCampaignDetailsErrorBody, get_campaign_details_error_mapper
from .get_campaign_level_summary_error import GetCampaignLevelSummaryErrorBody, get_campaign_level_summary_error_mapper
from .get_categories_list_error import GetCategoriesListErrorBody, get_categories_list_error_mapper
from .get_categorization_details_of_assortment_recommendations_error import (
    GetCategorizationDetailsOfAssortmentRecommendationsErrorBody,
    get_categorization_details_of_assortment_recommendations_error_mapper,
)
from .get_claim_details_error import GetClaimDetailsErrorBody, get_claim_details_error_mapper
from .get_claim_history_error import GetClaimHistoryErrorBody, get_claim_history_error_mapper
from .get_eligible_items_error import GetEligibleItemsErrorBody, get_eligible_items_error_mapper
from .get_feed_item_status_error import GetFeedItemStatusErrorBody, get_feed_item_status_error_mapper
from .get_fulfill_with_wfsrecommendations_error import (
    GetFulfillWithWfsrecommendationsErrorBody,
    get_fulfill_with_wfsrecommendations_error_mapper,
)
from .get_inventory_error import GetInventoryErrorBody, get_inventory_error_mapper
from .get_irp_categories_error import GetIrpCategoriesErrorBody, get_irp_categories_error_mapper
from .get_irp_items_error import GetIrpItemsErrorBody, get_irp_items_error_mapper
from .get_issue_types_error import GetIssueTypesErrorBody, get_issue_types_error_mapper
from .get_item_level_summary_error import GetItemLevelSummaryErrorBody, get_item_level_summary_error_mapper
from .get_item_recommendations_error import GetItemRecommendationsErrorBody, get_item_recommendations_error_mapper
from .get_lag_time_error import GetLagTimeErrorBody, get_lag_time_error_mapper
from .get_listing_quality_score_error import GetListingQualityScoreErrorBody, get_listing_quality_score_error_mapper
from .get_multi_node_inventory_for_all_sku_and_all_ship_nodes_error import (
    GetMultiNodeInventoryForAllSkuAndAllShipNodesErrorBody,
    get_multi_node_inventory_for_all_sku_and_all_ship_nodes_error_mapper,
)
from .get_multi_node_inventory_for_sku_and_all_shipnodes_error import (
    GetMultiNodeInventoryForSkuAndAllShipnodesErrorBody,
    get_multi_node_inventory_for_sku_and_all_shipnodes_error_mapper,
)
from .get_pro_seller_badge_info_error import GetProSellerBadgeInfoErrorBody, get_pro_seller_badge_info_error_mapper
from .get_promotional_prices_error import GetPromotionalPricesErrorBody, get_promotional_prices_error_mapper
from .get_recon_report_error import GetReconReportErrorBody, get_recon_report_error_mapper
from .get_recon_report_v1_error import GetReconReportV1ErrorBody, get_recon_report_v1_error_mapper
from .get_repricer_feed_error import GetRepricerFeedErrorBody, get_repricer_feed_error_mapper
from .get_restock_recommendations_error import (
    GetRestockRecommendationsErrorBody,
    get_restock_recommendations_error_mapper,
)
from .get_returns_error import GetReturnsErrorBody, get_returns_error_mapper
from .get_seller_incentives_info_error import GetSellerIncentivesInfoErrorBody, get_seller_incentives_info_error_mapper
from .get_seo_recommendations_error import GetSeoRecommendationsErrorBody, get_seo_recommendations_error_mapper
from .get_shipment_quantity_recommendations_error import (
    GetShipmentQuantityRecommendationsErrorBody,
    get_shipment_quantity_recommendations_error_mapper,
)
from .get_shipping_estimate_error import GetShippingEstimateErrorBody, get_shipping_estimate_error_mapper
from .get_strategies_error import GetStrategiesErrorBody, get_strategies_error_mapper
from .get_tag_templates_error import GetTagTemplatesErrorBody, get_tag_templates_error_mapper
from .get_tax_forms_error import GetTaxFormsErrorBody, get_tax_forms_error_mapper
from .get_unpublished_item_count_error import GetUnpublishedItemCountErrorBody, get_unpublished_item_count_error_mapper
from .get_unpublished_items_error import GetUnpublishedItemsErrorBody, get_unpublished_items_error_mapper
from .get_unpublished_recommendations_error import (
    GetUnpublishedRecommendationsErrorBody,
    get_unpublished_recommendations_error_mapper,
)
from .get_wfsinventory_error import GetWfsinventoryErrorBody, get_wfsinventory_error_mapper
from .get_wsr_item_report_error import GetWsrItemReportErrorBody, get_wsr_item_report_error_mapper
from .get_wsr_performance_report_error import GetWsrPerformanceReportErrorBody, get_wsr_performance_report_error_mapper
from .items_details_for_listing_error import ItemsDetailsForListingErrorBody, items_details_for_listing_error_mapper
from .list_claims_error import ListClaimsErrorBody, list_claims_error_mapper
from .post_contest_error import PostContestErrorBody, post_contest_error_mapper
from .post_status_error import PostStatusErrorBody, post_status_error_mapper
from .price_and_promotion_bulk_uploads_error import (
    PriceAndPromotionBulkUploadsErrorBody,
    price_and_promotion_bulk_uploads_error_mapper,
)
from .price_bulk_uploads_error import PriceBulkUploadsErrorBody, price_bulk_uploads_error_mapper
from .reduced_referral_fee_incentives_enrollment_error import (
    ReducedReferralFeeIncentivesEnrollmentErrorBody,
    reduced_referral_fee_incentives_enrollment_error_mapper,
)
from .refund_request_error import RefundRequestErrorBody, refund_request_error_mapper
from .reject_assortment_recommendations_error import (
    RejectAssortmentRecommendationsErrorBody,
    reject_assortment_recommendations_error_mapper,
)
from .return_order_cursor_error import ReturnOrderCursorErrorBody, return_order_cursor_error_mapper
from .rich_media_operation_error import RichMediaOperationErrorBody, rich_media_operation_error_mapper
from .scan_form_error import ScanFormErrorBody, scan_form_error_mapper
from .search_campaign_recommendations_error import (
    SearchCampaignRecommendationsErrorBody,
    search_campaign_recommendations_error_mapper,
)
from .search_item_issues_error import SearchItemIssuesErrorBody, search_item_issues_error_mapper
from .stop_campaign_error import StopCampaignErrorBody, stop_campaign_error_mapper
from .submit_additional_info_error import SubmitAdditionalInfoErrorBody, submit_additional_info_error_mapper
from .submit_claim_error import SubmitClaimErrorBody, submit_claim_error_mapper
from .token_api_error import TokenApiErrorBody, token_api_error_mapper
from .update_campaign_error import UpdateCampaignErrorBody, update_campaign_error_mapper
from .update_inventory_for_an_item_error import (
    UpdateInventoryForAnItemErrorBody,
    update_inventory_for_an_item_error_mapper,
)
from .update_multi_node_inventory_error import (
    UpdateMultiNodeInventoryErrorBody,
    update_multi_node_inventory_error_mapper,
)
from .update_price_error import UpdatePriceErrorBody, update_price_error_mapper
from .update_promotional_prices_error import UpdatePromotionalPricesErrorBody, update_promotional_prices_error_mapper
from .update_seo_recommendations_error import UpdateSeoRecommendationsErrorBody, update_seo_recommendations_error_mapper
from .update_strategy_error import UpdateStrategyErrorBody, update_strategy_error_mapper
from .update_walmart_funded_incentives_enrollment_status_error import (
    UpdateWalmartFundedIncentivesEnrollmentStatusErrorBody,
    update_walmart_funded_incentives_enrollment_status_error_mapper,
)
from .walmart_funded_incentives_enrollment_error import (
    WalmartFundedIncentivesEnrollmentErrorBody,
    walmart_funded_incentives_enrollment_error_mapper,
)
from .walmart_plus_enrollment_error import WalmartPlusEnrollmentErrorBody, walmart_plus_enrollment_error_mapper

__all__ = [
    "BulkUpdateItemStatusErrorBody",
    "CreateCampaignErrorBody",
    "CreateLabelErrorBody",
    "CreateLabelMpsErrorBody",
    "CreateStrategyErrorBody",
    "DeleteCampaignErrorBody",
    "DeleteStrategyErrorBody",
    "DiscardLabelErrorBody",
    "DownloadClaimDocumentsErrorBody",
    "DownloadTaxFormErrorBody",
    "GenerateReportErrorBody",
    "GetAllAssetsErrorBody",
    "GetAllFeedStatusesErrorBody",
    "GetAllIncentivesErrorBody",
    "GetAssortmentRecommendationTrendsErrorBody",
    "GetAssortmentRecommendationVariantsErrorBody",
    "GetAssortmentRecommendationsErrorBody",
    "GetBillingHistoryErrorBody",
    "GetCampaignDetailsErrorBody",
    "GetCampaignLevelSummaryErrorBody",
    "GetCategoriesListErrorBody",
    "GetCategorizationDetailsOfAssortmentRecommendationsErrorBody",
    "GetClaimDetailsErrorBody",
    "GetClaimHistoryErrorBody",
    "GetEligibleItemsErrorBody",
    "GetFeedItemStatusErrorBody",
    "GetFulfillWithWfsrecommendationsErrorBody",
    "GetInventoryErrorBody",
    "GetIrpCategoriesErrorBody",
    "GetIrpItemsErrorBody",
    "GetIssueTypesErrorBody",
    "GetItemLevelSummaryErrorBody",
    "GetItemRecommendationsErrorBody",
    "GetLagTimeErrorBody",
    "GetListingQualityScoreErrorBody",
    "GetMultiNodeInventoryForAllSkuAndAllShipNodesErrorBody",
    "GetMultiNodeInventoryForSkuAndAllShipnodesErrorBody",
    "GetProSellerBadgeInfoErrorBody",
    "GetPromotionalPricesErrorBody",
    "GetReconReportErrorBody",
    "GetReconReportV1ErrorBody",
    "GetRepricerFeedErrorBody",
    "GetRestockRecommendationsErrorBody",
    "GetReturnsErrorBody",
    "GetSellerIncentivesInfoErrorBody",
    "GetSeoRecommendationsErrorBody",
    "GetShipmentQuantityRecommendationsErrorBody",
    "GetShippingEstimateErrorBody",
    "GetStrategiesErrorBody",
    "GetTagTemplatesErrorBody",
    "GetTaxFormsErrorBody",
    "GetUnpublishedItemCountErrorBody",
    "GetUnpublishedItemsErrorBody",
    "GetUnpublishedRecommendationsErrorBody",
    "GetWfsinventoryErrorBody",
    "GetWsrItemReportErrorBody",
    "GetWsrPerformanceReportErrorBody",
    "ItemsDetailsForListingErrorBody",
    "ListClaimsErrorBody",
    "PostContestErrorBody",
    "PostStatusErrorBody",
    "PriceAndPromotionBulkUploadsErrorBody",
    "PriceBulkUploadsErrorBody",
    "ReducedReferralFeeIncentivesEnrollmentErrorBody",
    "RefundRequestErrorBody",
    "RejectAssortmentRecommendationsErrorBody",
    "ReturnOrderCursorErrorBody",
    "RichMediaOperationErrorBody",
    "ScanFormErrorBody",
    "SearchCampaignRecommendationsErrorBody",
    "SearchItemIssuesErrorBody",
    "StopCampaignErrorBody",
    "SubmitAdditionalInfoErrorBody",
    "SubmitClaimErrorBody",
    "TokenApiErrorBody",
    "UpdateCampaignErrorBody",
    "UpdateInventoryForAnItemErrorBody",
    "UpdateMultiNodeInventoryErrorBody",
    "UpdatePriceErrorBody",
    "UpdatePromotionalPricesErrorBody",
    "UpdateSeoRecommendationsErrorBody",
    "UpdateStrategyErrorBody",
    "UpdateWalmartFundedIncentivesEnrollmentStatusErrorBody",
    "WalmartFundedIncentivesEnrollmentErrorBody",
    "WalmartPlusEnrollmentErrorBody",
    "bulk_update_item_status_error_mapper",
    "create_campaign_error_mapper",
    "create_label_error_mapper",
    "create_label_mps_error_mapper",
    "create_strategy_error_mapper",
    "delete_campaign_error_mapper",
    "delete_strategy_error_mapper",
    "discard_label_error_mapper",
    "download_claim_documents_error_mapper",
    "download_tax_form_error_mapper",
    "generate_report_error_mapper",
    "get_all_assets_error_mapper",
    "get_all_feed_statuses_error_mapper",
    "get_all_incentives_error_mapper",
    "get_assortment_recommendation_trends_error_mapper",
    "get_assortment_recommendation_variants_error_mapper",
    "get_assortment_recommendations_error_mapper",
    "get_billing_history_error_mapper",
    "get_campaign_details_error_mapper",
    "get_campaign_level_summary_error_mapper",
    "get_categories_list_error_mapper",
    "get_categorization_details_of_assortment_recommendations_error_mapper",
    "get_claim_details_error_mapper",
    "get_claim_history_error_mapper",
    "get_eligible_items_error_mapper",
    "get_feed_item_status_error_mapper",
    "get_fulfill_with_wfsrecommendations_error_mapper",
    "get_inventory_error_mapper",
    "get_irp_categories_error_mapper",
    "get_irp_items_error_mapper",
    "get_issue_types_error_mapper",
    "get_item_level_summary_error_mapper",
    "get_item_recommendations_error_mapper",
    "get_lag_time_error_mapper",
    "get_listing_quality_score_error_mapper",
    "get_multi_node_inventory_for_all_sku_and_all_ship_nodes_error_mapper",
    "get_multi_node_inventory_for_sku_and_all_shipnodes_error_mapper",
    "get_pro_seller_badge_info_error_mapper",
    "get_promotional_prices_error_mapper",
    "get_recon_report_error_mapper",
    "get_recon_report_v1_error_mapper",
    "get_repricer_feed_error_mapper",
    "get_restock_recommendations_error_mapper",
    "get_returns_error_mapper",
    "get_seller_incentives_info_error_mapper",
    "get_seo_recommendations_error_mapper",
    "get_shipment_quantity_recommendations_error_mapper",
    "get_shipping_estimate_error_mapper",
    "get_strategies_error_mapper",
    "get_tag_templates_error_mapper",
    "get_tax_forms_error_mapper",
    "get_unpublished_item_count_error_mapper",
    "get_unpublished_items_error_mapper",
    "get_unpublished_recommendations_error_mapper",
    "get_wfsinventory_error_mapper",
    "get_wsr_item_report_error_mapper",
    "get_wsr_performance_report_error_mapper",
    "items_details_for_listing_error_mapper",
    "list_claims_error_mapper",
    "post_contest_error_mapper",
    "post_status_error_mapper",
    "price_and_promotion_bulk_uploads_error_mapper",
    "price_bulk_uploads_error_mapper",
    "reduced_referral_fee_incentives_enrollment_error_mapper",
    "refund_request_error_mapper",
    "reject_assortment_recommendations_error_mapper",
    "return_order_cursor_error_mapper",
    "rich_media_operation_error_mapper",
    "scan_form_error_mapper",
    "search_campaign_recommendations_error_mapper",
    "search_item_issues_error_mapper",
    "stop_campaign_error_mapper",
    "submit_additional_info_error_mapper",
    "submit_claim_error_mapper",
    "token_api_error_mapper",
    "update_campaign_error_mapper",
    "update_inventory_for_an_item_error_mapper",
    "update_multi_node_inventory_error_mapper",
    "update_price_error_mapper",
    "update_promotional_prices_error_mapper",
    "update_seo_recommendations_error_mapper",
    "update_strategy_error_mapper",
    "update_walmart_funded_incentives_enrollment_status_error_mapper",
    "walmart_funded_incentives_enrollment_error_mapper",
    "walmart_plus_enrollment_error_mapper",
]
