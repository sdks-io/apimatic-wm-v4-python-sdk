from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.assortment_recommendations import AssortmentRecommendations
from .apis.authorization import Authorization
from .apis.disputes import Disputes
from .apis.feeds_api import FeedsApi
from .apis.insight_api import InsightApi
from .apis.inventory_api import InventoryApi
from .apis.lag_time_api import LagTimeApi
from .apis.notifications import Notifications
from .apis.on_request_report import OnRequestReport
from .apis.on_request_report_api import OnRequestReportApi
from .apis.prices import Prices
from .apis.promotions import Promotions
from .apis.recommendations_api import RecommendationsApi
from .apis.report_scheduler import ReportScheduler
from .apis.reports_api import ReportsApi
from .apis.returns_refund import ReturnsRefund
from .apis.reviews import Reviews
from .apis.rich_media import RichMedia
from .apis.sem_campaign_management import SemCampaignManagement
from .apis.sem_catalog import SemCatalog
from .apis.sem_item_diagnostics import SemItemDiagnostics
from .apis.sem_reporting import SemReporting
from .apis.seo_recommendations import SeoRecommendations
from .apis.ship_with_walmart import ShipWithWalmart
from .apis.shipment_protection import ShipmentProtection
from .apis.simplified_shipping_settings import SimplifiedShippingSettings
from .apis.tax_form_apis import TaxFormApis
from .apis.walmart_seller_fulfilled import WalmartSellerFulfilled
from .apis.wsr_attribution_reports import WsrAttributionReports
from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseWalmartApisClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyHeaderScheme,
    BasicAuthCredentials,
    BasicAuthCredentialsOrDict,
    BasicAuthScheme,
    BearerAuthScheme,
    HttpClient,
    Httpx2Client,
    LoggingOptionsOrDict,
    RawClient,
    RetryOptionsOrDict,
    no_auth,
    param,
)
from .server.environment import Environment


class WalmartApisClient(BaseWalmartApisClient[RawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        retry_options: int | RetryOptionsOrDict | None = None,
        logging_options: LoggingOptionsOrDict | None = None,
        custom_http_client: HttpClient | None = None,
        basic_auth: BasicAuthCredentialsOrDict | None = None,
        bearer_auth: str | None = None,
        access_token: str | None = None,
    ) -> None:
        super().__init__(
            environment=environment,
            base_url=base_url,
            timeout=timeout,
            retry_options=retry_options,
            logging_options=logging_options,
        )
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else Httpx2Client(timeout=timeout),
            retry_options=self._retry_options,
            logging_options=self._logging_options,
            global_headers=[
                param[str]("User-Agent", "WalmartApisClient/1.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "1.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AuthSchemes(
            basic_auth=BasicAuthScheme(BasicAuthCredentials.coerce(basic_auth)) if basic_auth is not None else no_auth,
            bearer_auth=BearerAuthScheme(bearer_auth) if bearer_auth is not None else no_auth,
            access_token=(
                ApiKeyHeaderScheme("WM_SEC.ACCESS_TOKEN", access_token) if access_token is not None else no_auth
            ),
        )

    @cached_property
    def assortment_recommendations(self) -> AssortmentRecommendations:
        return AssortmentRecommendations(self._raw_client, self._server)

    @cached_property
    def authorization(self) -> Authorization:
        return Authorization(self._raw_client, self._server, self._auth)

    @cached_property
    def disputes(self) -> Disputes:
        return Disputes(self._raw_client, self._server)

    @cached_property
    def feeds_api(self) -> FeedsApi:
        return FeedsApi(self._raw_client, self._server, self._auth)

    @cached_property
    def insight_api(self) -> InsightApi:
        return InsightApi(self._raw_client, self._server, self._auth)

    @cached_property
    def inventory_api(self) -> InventoryApi:
        return InventoryApi(self._raw_client, self._server, self._auth)

    @cached_property
    def lag_time_api(self) -> LagTimeApi:
        return LagTimeApi(self._raw_client, self._server, self._auth)

    @cached_property
    def notifications(self) -> Notifications:
        return Notifications(self._raw_client, self._server, self._auth)

    @cached_property
    def on_request_report(self) -> OnRequestReport:
        return OnRequestReport(self._raw_client, self._server, self._auth)

    @cached_property
    def on_request_report_api(self) -> OnRequestReportApi:
        return OnRequestReportApi(self._raw_client, self._server, self._auth)

    @cached_property
    def prices(self) -> Prices:
        return Prices(self._raw_client, self._server, self._auth)

    @cached_property
    def promotions(self) -> Promotions:
        return Promotions(self._raw_client, self._server)

    @cached_property
    def recommendations_api(self) -> RecommendationsApi:
        return RecommendationsApi(self._raw_client, self._server)

    @cached_property
    def report_scheduler(self) -> ReportScheduler:
        return ReportScheduler(self._raw_client, self._server, self._auth)

    @cached_property
    def reports_api(self) -> ReportsApi:
        return ReportsApi(self._raw_client, self._server, self._auth)

    @cached_property
    def returns_refund(self) -> ReturnsRefund:
        return ReturnsRefund(self._raw_client, self._server, self._auth)

    @cached_property
    def reviews(self) -> Reviews:
        return Reviews(self._raw_client, self._server, self._auth)

    @cached_property
    def rich_media(self) -> RichMedia:
        return RichMedia(self._raw_client, self._server, self._auth)

    @cached_property
    def sem_campaign_management(self) -> SemCampaignManagement:
        return SemCampaignManagement(self._raw_client, self._server, self._auth)

    @cached_property
    def sem_catalog(self) -> SemCatalog:
        return SemCatalog(self._raw_client, self._server, self._auth)

    @cached_property
    def sem_item_diagnostics(self) -> SemItemDiagnostics:
        return SemItemDiagnostics(self._raw_client, self._server, self._auth)

    @cached_property
    def sem_reporting(self) -> SemReporting:
        return SemReporting(self._raw_client, self._server, self._auth)

    @cached_property
    def seo_recommendations(self) -> SeoRecommendations:
        return SeoRecommendations(self._raw_client, self._server, self._auth)

    @cached_property
    def ship_with_walmart(self) -> ShipWithWalmart:
        return ShipWithWalmart(self._raw_client, self._server, self._auth)

    @cached_property
    def shipment_protection(self) -> ShipmentProtection:
        return ShipmentProtection(self._raw_client, self._server)

    @cached_property
    def simplified_shipping_settings(self) -> SimplifiedShippingSettings:
        return SimplifiedShippingSettings(self._raw_client, self._server)

    @cached_property
    def tax_form_apis(self) -> TaxFormApis:
        return TaxFormApis(self._raw_client, self._server, self._auth)

    @cached_property
    def wsr_attribution_reports(self) -> WsrAttributionReports:
        return WsrAttributionReports(self._raw_client, self._server, self._auth)

    @cached_property
    def walmart_seller_fulfilled(self) -> WalmartSellerFulfilled:
        return WalmartSellerFulfilled(self._raw_client, self._server)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = WalmartApisClient
