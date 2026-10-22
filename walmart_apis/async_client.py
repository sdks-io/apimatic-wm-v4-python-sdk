from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.assortment_recommendations import AsyncAssortmentRecommendations
from .apis.authorization import AsyncAuthorization
from .apis.disputes import AsyncDisputes
from .apis.feeds_api import AsyncFeedsApi
from .apis.insight_api import AsyncInsightApi
from .apis.inventory_api import AsyncInventoryApi
from .apis.lag_time_api import AsyncLagTimeApi
from .apis.notifications import AsyncNotifications
from .apis.on_request_report import AsyncOnRequestReport
from .apis.on_request_report_api import AsyncOnRequestReportApi
from .apis.prices import AsyncPrices
from .apis.promotions import AsyncPromotions
from .apis.recommendations_api import AsyncRecommendationsApi
from .apis.report_scheduler import AsyncReportScheduler
from .apis.reports_api import AsyncReportsApi
from .apis.returns_refund import AsyncReturnsRefund
from .apis.reviews import AsyncReviews
from .apis.rich_media import AsyncRichMedia
from .apis.sem_campaign_management import AsyncSemCampaignManagement
from .apis.sem_catalog import AsyncSemCatalog
from .apis.sem_item_diagnostics import AsyncSemItemDiagnostics
from .apis.sem_reporting import AsyncSemReporting
from .apis.seo_recommendations import AsyncSeoRecommendations
from .apis.ship_with_walmart import AsyncShipWithWalmart
from .apis.shipment_protection import AsyncShipmentProtection
from .apis.simplified_shipping_settings import AsyncSimplifiedShippingSettings
from .apis.tax_form_apis import AsyncTaxFormApis
from .apis.walmart_seller_fulfilled import AsyncWalmartSellerFulfilled
from .apis.wsr_attribution_reports import AsyncWsrAttributionReports
from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseWalmartApisClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyHeaderScheme,
    AsyncHttpClient,
    AsyncHttpx2Client,
    AsyncRawClient,
    BasicAuthCredentials,
    BasicAuthCredentialsOrDict,
    BasicAuthScheme,
    BearerAuthScheme,
    LoggingOptionsOrDict,
    RetryOptionsOrDict,
    no_auth,
    param,
)
from .server.environment import Environment


class AsyncWalmartApisClient(BaseWalmartApisClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        retry_options: int | RetryOptionsOrDict | None = None,
        logging_options: LoggingOptionsOrDict | None = None,
        custom_async_http_client: AsyncHttpClient | None = None,
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
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpx2Client(timeout=timeout)
            ),
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
        self._auth = AsyncAuthSchemes(
            basic_auth=BasicAuthScheme(BasicAuthCredentials.coerce(basic_auth)) if basic_auth is not None else no_auth,
            bearer_auth=BearerAuthScheme(bearer_auth) if bearer_auth is not None else no_auth,
            access_token=(
                ApiKeyHeaderScheme("WM_SEC.ACCESS_TOKEN", access_token) if access_token is not None else no_auth
            ),
        )

    @cached_property
    def assortment_recommendations(self) -> AsyncAssortmentRecommendations:
        return AsyncAssortmentRecommendations(self._raw_client, self._server)

    @cached_property
    def authorization(self) -> AsyncAuthorization:
        return AsyncAuthorization(self._raw_client, self._server)

    @cached_property
    def disputes(self) -> AsyncDisputes:
        return AsyncDisputes(self._raw_client, self._server)

    @cached_property
    def feeds_api(self) -> AsyncFeedsApi:
        return AsyncFeedsApi(self._raw_client, self._server, self._auth)

    @cached_property
    def insight_api(self) -> AsyncInsightApi:
        return AsyncInsightApi(self._raw_client, self._server, self._auth)

    @cached_property
    def inventory_api(self) -> AsyncInventoryApi:
        return AsyncInventoryApi(self._raw_client, self._server, self._auth)

    @cached_property
    def lag_time_api(self) -> AsyncLagTimeApi:
        return AsyncLagTimeApi(self._raw_client, self._server, self._auth)

    @cached_property
    def notifications(self) -> AsyncNotifications:
        return AsyncNotifications(self._raw_client, self._server, self._auth)

    @cached_property
    def on_request_report(self) -> AsyncOnRequestReport:
        return AsyncOnRequestReport(self._raw_client, self._server, self._auth)

    @cached_property
    def on_request_report_api(self) -> AsyncOnRequestReportApi:
        return AsyncOnRequestReportApi(self._raw_client, self._server, self._auth)

    @cached_property
    def prices(self) -> AsyncPrices:
        return AsyncPrices(self._raw_client, self._server, self._auth)

    @cached_property
    def promotions(self) -> AsyncPromotions:
        return AsyncPromotions(self._raw_client, self._server)

    @cached_property
    def recommendations_api(self) -> AsyncRecommendationsApi:
        return AsyncRecommendationsApi(self._raw_client, self._server)

    @cached_property
    def report_scheduler(self) -> AsyncReportScheduler:
        return AsyncReportScheduler(self._raw_client, self._server, self._auth)

    @cached_property
    def reports_api(self) -> AsyncReportsApi:
        return AsyncReportsApi(self._raw_client, self._server, self._auth)

    @cached_property
    def returns_refund(self) -> AsyncReturnsRefund:
        return AsyncReturnsRefund(self._raw_client, self._server, self._auth)

    @cached_property
    def reviews(self) -> AsyncReviews:
        return AsyncReviews(self._raw_client, self._server, self._auth)

    @cached_property
    def rich_media(self) -> AsyncRichMedia:
        return AsyncRichMedia(self._raw_client, self._server, self._auth)

    @cached_property
    def sem_campaign_management(self) -> AsyncSemCampaignManagement:
        return AsyncSemCampaignManagement(self._raw_client, self._server, self._auth)

    @cached_property
    def sem_catalog(self) -> AsyncSemCatalog:
        return AsyncSemCatalog(self._raw_client, self._server, self._auth)

    @cached_property
    def sem_item_diagnostics(self) -> AsyncSemItemDiagnostics:
        return AsyncSemItemDiagnostics(self._raw_client, self._server, self._auth)

    @cached_property
    def sem_reporting(self) -> AsyncSemReporting:
        return AsyncSemReporting(self._raw_client, self._server, self._auth)

    @cached_property
    def seo_recommendations(self) -> AsyncSeoRecommendations:
        return AsyncSeoRecommendations(self._raw_client, self._server, self._auth)

    @cached_property
    def ship_with_walmart(self) -> AsyncShipWithWalmart:
        return AsyncShipWithWalmart(self._raw_client, self._server, self._auth)

    @cached_property
    def shipment_protection(self) -> AsyncShipmentProtection:
        return AsyncShipmentProtection(self._raw_client, self._server)

    @cached_property
    def simplified_shipping_settings(self) -> AsyncSimplifiedShippingSettings:
        return AsyncSimplifiedShippingSettings(self._raw_client, self._server)

    @cached_property
    def tax_form_apis(self) -> AsyncTaxFormApis:
        return AsyncTaxFormApis(self._raw_client, self._server, self._auth)

    @cached_property
    def wsr_attribution_reports(self) -> AsyncWsrAttributionReports:
        return AsyncWsrAttributionReports(self._raw_client, self._server, self._auth)

    @cached_property
    def walmart_seller_fulfilled(self) -> AsyncWalmartSellerFulfilled:
        return AsyncWalmartSellerFulfilled(self._raw_client, self._server)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncWalmartApisClient
