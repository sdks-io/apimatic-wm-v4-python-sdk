from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    async_json_decoder,
    form_body,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..errors.token_api_error import TokenApiErrorBody, token_api_error_mapper
from ..models.enums.grant_type1 import GrantType1, GrantType1OrStr
from ..models.oauth_token_model import OauthTokenModel
from ..models.token_detail_response import TokenDetailResponse
from ..server.server import Server


class Authorization:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = AuthorizationWithRawResponse(client, server)

    def get_token_detail(
        self,
        wm_sec_access_token: str,
        wm_market: str,
        content_type: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TokenDetailResponse:
        """This process retrieves the access permissions granted by sellers to applications in the context of OAuth 2.0.
        The scope encompasses various API categories, each with its respective access levels, for example Reports: View
        Only, Item: Full Access, etc. <br><b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call <strong style="color: green;">**Market
                availability: Global**</strong>
            wm_market: Available marketplace location: us (USA), mx (Mexico), ca (Canada) or cl (Chile) <strong
                style="color: green;">**Market availability: Global**</strong>
            content_type: Content type of the request body. <strong style="color: green;">**Market availability:
                Global**</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID <strong style="color: green;">**Market availability: Global**</strong>
            wm_svc_name: Walmart Service Name <strong style="color: green;">**Market availability: Global**</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">**Market availability: Global**</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_token_detail(
                wm_sec_access_token,
                wm_market,
                content_type,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def token_api(
        self,
        wm_market: str,
        authorization: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_partner_id: str | None = None,
        wm_consumer_channel_type: str | None = None,
        grant_type: GrantType1OrStr = GrantType1.CLIENT_CREDENTIALS,
        code: str | None = "65CA5DA313A549D49D15D3119D9AD85D",
        redirect_uri: str | None = "https://example-client-app.com",
        refresh_token: str | None = "APXcIoTpKMH9OQN.....",
        request_options: RequestOptionsOrDict | None = None,
    ) -> OauthTokenModel:
        """<p>This endpoint issues access tokens required for authenticating API requests. It supports multiple OAuth
        2.0 grant types to accommodate various integration scenarios.</p> <b style='color:green;'>Market availability:
        Global</b><br/><h3>Supported Grant Types</h3><table><tr><th>Grant Type</th><th>Description</th><th>How to get
        the credentials</th></tr><tr><td>authorization_code</td><td>Exchanges an authorization code for an access
        token.</td><td>Used in app integration only via the OAuth consent screen. This is applicable to the <strong>US
        market only</strong>. Refer to <a href=/global-marketplace/docs/oauth-20-authorization>OAuth 2.0
        authorization</a> for more details.</td></tr><tr><td>client_credentials</td><td>Issues a token using client ID
        and secret.</td><td>For <strong>sellers</strong>: Obtain client_id and client_secret from the <strong>Developer
        Portal</strong>.<br/>For <strong>solution providers</strong>: Obtain credentials from sellers via <a
        href=/global-marketplace/docs/delegated-access-auth>Delegated Access
        authorization</a>.</td></tr><tr><td>refresh_token</td><td>Issues a new access token using a refresh
        token.</td><td>Provided during the authorization_code flow. This is applicable to the <strong>US market
        only</strong>. Refer to <a href=/global-marketplace/docs/oauth-20-authorization>OAuth 2.0 authorization</a> for
        more details.</td></tr></table><br/><b>Note:<br/></b> Use authorization_code and refresh_token <b>only for
        app-based integrations.</b> These grant types are currently <b>supported only in the US
        market</b>.<br/><br/><h3>Token Lifetimes</h3><table><tr><th>Token Type</th><th>Duration</th></tr><tr><td>Access
        Token</td><td>15 minutes <i>(900 seconds)</i></td></tr><tr><td>Refresh Token</td><td>1 year <i>(365
        days)</i></td></tr></table>

        Args:
            wm_market: Available marketplace location: us (USA), mx (Mexico), ca (Canada) or cl (Chile) <strong
                style="color: green;">**Market availability: Global**</strong>
            authorization: Basic authorization header. Base 64 encodes the Client ID and Client Secret retrieved in step
                two of the integration steps. <strong style="color: green;">**Market availability: Global**</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID <strong style="color: green;">**Market availability: Global**</strong>
            wm_svc_name: Walmart Service Name <strong style="color: green;">**Market availability: Global**</strong>
            wm_partner_id: Partner Id registered in Walmart marketplace to identify a seller. <br /> This field is
                required when **grant_type: authorization_code** and **grant_type: refresh_token** <strong style="color:
                green;">**Market availability: Global**</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">**Market availability: Global**</strong>
            grant_type: Type of grant requested. <br /> **Available grant types:** authorization_code, refresh_token and
                client_credentials <strong style="color: green;">**Market availability: Global**</strong>
            code: Authorization code obtained by your client app when the seller authorizes your app to access the
                seller resource. <br /> This field is required when **grant_type: authorization_code** <strong
                style="color: green;">**Market availability: Global**</strong>
            redirect_uri: This should be same as one of your client app URIs provided while registering the app. <br />
                This field is required when **grant_type: authorization_code** <strong style="color: green;">**Market
                availability: Global**</strong>
            refresh_token: Refresh token received as response of Authentication API with authorization_code grant type,
                to be used to refresh the access token. The token lifetime is 1 year. <strong style="color:
                green;">**Market availability: Global**</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad request Unauthorized request Internal Server Error ``error`` is ``V3Token400Error1 |
                V3Token401Error1 | V3Token500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.token_api(
                wm_market,
                authorization,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_partner_id=wm_partner_id,
                wm_consumer_channel_type=wm_consumer_channel_type,
                grant_type=grant_type,
                code=code,
                redirect_uri=redirect_uri,
                refresh_token=refresh_token,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AuthorizationWithRawResponse:
        return self._with_raw_response


class AsyncAuthorization:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncAuthorizationWithRawResponse(client, server)

    async def get_token_detail(
        self,
        wm_sec_access_token: str,
        wm_market: str,
        content_type: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TokenDetailResponse:
        """This process retrieves the access permissions granted by sellers to applications in the context of OAuth 2.0.
        The scope encompasses various API categories, each with its respective access levels, for example Reports: View
        Only, Item: Full Access, etc. <br><b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call <strong style="color: green;">**Market
                availability: Global**</strong>
            wm_market: Available marketplace location: us (USA), mx (Mexico), ca (Canada) or cl (Chile) <strong
                style="color: green;">**Market availability: Global**</strong>
            content_type: Content type of the request body. <strong style="color: green;">**Market availability:
                Global**</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID <strong style="color: green;">**Market availability: Global**</strong>
            wm_svc_name: Walmart Service Name <strong style="color: green;">**Market availability: Global**</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">**Market availability: Global**</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_token_detail(
                wm_sec_access_token,
                wm_market,
                content_type,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def token_api(
        self,
        wm_market: str,
        authorization: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_partner_id: str | None = None,
        wm_consumer_channel_type: str | None = None,
        grant_type: GrantType1OrStr = GrantType1.CLIENT_CREDENTIALS,
        code: str | None = "65CA5DA313A549D49D15D3119D9AD85D",
        redirect_uri: str | None = "https://example-client-app.com",
        refresh_token: str | None = "APXcIoTpKMH9OQN.....",
        request_options: RequestOptionsOrDict | None = None,
    ) -> OauthTokenModel:
        """<p>This endpoint issues access tokens required for authenticating API requests. It supports multiple OAuth
        2.0 grant types to accommodate various integration scenarios.</p> <b style='color:green;'>Market availability:
        Global</b><br/><h3>Supported Grant Types</h3><table><tr><th>Grant Type</th><th>Description</th><th>How to get
        the credentials</th></tr><tr><td>authorization_code</td><td>Exchanges an authorization code for an access
        token.</td><td>Used in app integration only via the OAuth consent screen. This is applicable to the <strong>US
        market only</strong>. Refer to <a href=/global-marketplace/docs/oauth-20-authorization>OAuth 2.0
        authorization</a> for more details.</td></tr><tr><td>client_credentials</td><td>Issues a token using client ID
        and secret.</td><td>For <strong>sellers</strong>: Obtain client_id and client_secret from the <strong>Developer
        Portal</strong>.<br/>For <strong>solution providers</strong>: Obtain credentials from sellers via <a
        href=/global-marketplace/docs/delegated-access-auth>Delegated Access
        authorization</a>.</td></tr><tr><td>refresh_token</td><td>Issues a new access token using a refresh
        token.</td><td>Provided during the authorization_code flow. This is applicable to the <strong>US market
        only</strong>. Refer to <a href=/global-marketplace/docs/oauth-20-authorization>OAuth 2.0 authorization</a> for
        more details.</td></tr></table><br/><b>Note:<br/></b> Use authorization_code and refresh_token <b>only for
        app-based integrations.</b> These grant types are currently <b>supported only in the US
        market</b>.<br/><br/><h3>Token Lifetimes</h3><table><tr><th>Token Type</th><th>Duration</th></tr><tr><td>Access
        Token</td><td>15 minutes <i>(900 seconds)</i></td></tr><tr><td>Refresh Token</td><td>1 year <i>(365
        days)</i></td></tr></table>

        Args:
            wm_market: Available marketplace location: us (USA), mx (Mexico), ca (Canada) or cl (Chile) <strong
                style="color: green;">**Market availability: Global**</strong>
            authorization: Basic authorization header. Base 64 encodes the Client ID and Client Secret retrieved in step
                two of the integration steps. <strong style="color: green;">**Market availability: Global**</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID <strong style="color: green;">**Market availability: Global**</strong>
            wm_svc_name: Walmart Service Name <strong style="color: green;">**Market availability: Global**</strong>
            wm_partner_id: Partner Id registered in Walmart marketplace to identify a seller. <br /> This field is
                required when **grant_type: authorization_code** and **grant_type: refresh_token** <strong style="color:
                green;">**Market availability: Global**</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">**Market availability: Global**</strong>
            grant_type: Type of grant requested. <br /> **Available grant types:** authorization_code, refresh_token and
                client_credentials <strong style="color: green;">**Market availability: Global**</strong>
            code: Authorization code obtained by your client app when the seller authorizes your app to access the
                seller resource. <br /> This field is required when **grant_type: authorization_code** <strong
                style="color: green;">**Market availability: Global**</strong>
            redirect_uri: This should be same as one of your client app URIs provided while registering the app. <br />
                This field is required when **grant_type: authorization_code** <strong style="color: green;">**Market
                availability: Global**</strong>
            refresh_token: Refresh token received as response of Authentication API with authorization_code grant type,
                to be used to refresh the access token. The token lifetime is 1 year. <strong style="color:
                green;">**Market availability: Global**</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad request Unauthorized request Internal Server Error ``error`` is ``V3Token400Error1 |
                V3Token401Error1 | V3Token500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.token_api(
                wm_market,
                authorization,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_partner_id=wm_partner_id,
                wm_consumer_channel_type=wm_consumer_channel_type,
                grant_type=grant_type,
                code=code,
                redirect_uri=redirect_uri,
                refresh_token=refresh_token,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncAuthorizationWithRawResponse:
        return self._with_raw_response


class AuthorizationWithRawResponse(BaseRawResponse[RawClient, Server]):
    def get_token_detail(
        self,
        wm_sec_access_token: str,
        wm_market: str,
        content_type: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TokenDetailResponse, RawError]:
        """This process retrieves the access permissions granted by sellers to applications in the context of OAuth 2.0.
        The scope encompasses various API categories, each with its respective access levels, for example Reports: View
        Only, Item: Full Access, etc. <br><b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call <strong style="color: green;">**Market
                availability: Global**</strong>
            wm_market: Available marketplace location: us (USA), mx (Mexico), ca (Canada) or cl (Chile) <strong
                style="color: green;">**Market availability: Global**</strong>
            content_type: Content type of the request body. <strong style="color: green;">**Market availability:
                Global**</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID <strong style="color: green;">**Market availability: Global**</strong>
            wm_svc_name: Walmart Service Name <strong style="color: green;">**Market availability: Global**</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">**Market availability: Global**</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/token/detail"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_MARKET", wm_market),
                param[str]("Content-Type", content_type),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            decoder=json_decoder[TokenDetailResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def token_api(
        self,
        wm_market: str,
        authorization: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_partner_id: str | None = None,
        wm_consumer_channel_type: str | None = None,
        grant_type: GrantType1OrStr = GrantType1.CLIENT_CREDENTIALS,
        code: str | None = "65CA5DA313A549D49D15D3119D9AD85D",
        redirect_uri: str | None = "https://example-client-app.com",
        refresh_token: str | None = "APXcIoTpKMH9OQN.....",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OauthTokenModel, TokenApiErrorBody]:
        """<p>This endpoint issues access tokens required for authenticating API requests. It supports multiple OAuth
        2.0 grant types to accommodate various integration scenarios.</p> <b style='color:green;'>Market availability:
        Global</b><br/><h3>Supported Grant Types</h3><table><tr><th>Grant Type</th><th>Description</th><th>How to get
        the credentials</th></tr><tr><td>authorization_code</td><td>Exchanges an authorization code for an access
        token.</td><td>Used in app integration only via the OAuth consent screen. This is applicable to the <strong>US
        market only</strong>. Refer to <a href=/global-marketplace/docs/oauth-20-authorization>OAuth 2.0
        authorization</a> for more details.</td></tr><tr><td>client_credentials</td><td>Issues a token using client ID
        and secret.</td><td>For <strong>sellers</strong>: Obtain client_id and client_secret from the <strong>Developer
        Portal</strong>.<br/>For <strong>solution providers</strong>: Obtain credentials from sellers via <a
        href=/global-marketplace/docs/delegated-access-auth>Delegated Access
        authorization</a>.</td></tr><tr><td>refresh_token</td><td>Issues a new access token using a refresh
        token.</td><td>Provided during the authorization_code flow. This is applicable to the <strong>US market
        only</strong>. Refer to <a href=/global-marketplace/docs/oauth-20-authorization>OAuth 2.0 authorization</a> for
        more details.</td></tr></table><br/><b>Note:<br/></b> Use authorization_code and refresh_token <b>only for
        app-based integrations.</b> These grant types are currently <b>supported only in the US
        market</b>.<br/><br/><h3>Token Lifetimes</h3><table><tr><th>Token Type</th><th>Duration</th></tr><tr><td>Access
        Token</td><td>15 minutes <i>(900 seconds)</i></td></tr><tr><td>Refresh Token</td><td>1 year <i>(365
        days)</i></td></tr></table>

        Args:
            wm_market: Available marketplace location: us (USA), mx (Mexico), ca (Canada) or cl (Chile) <strong
                style="color: green;">**Market availability: Global**</strong>
            authorization: Basic authorization header. Base 64 encodes the Client ID and Client Secret retrieved in step
                two of the integration steps. <strong style="color: green;">**Market availability: Global**</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID <strong style="color: green;">**Market availability: Global**</strong>
            wm_svc_name: Walmart Service Name <strong style="color: green;">**Market availability: Global**</strong>
            wm_partner_id: Partner Id registered in Walmart marketplace to identify a seller. <br /> This field is
                required when **grant_type: authorization_code** and **grant_type: refresh_token** <strong style="color:
                green;">**Market availability: Global**</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">**Market availability: Global**</strong>
            grant_type: Type of grant requested. <br /> **Available grant types:** authorization_code, refresh_token and
                client_credentials <strong style="color: green;">**Market availability: Global**</strong>
            code: Authorization code obtained by your client app when the seller authorizes your app to access the
                seller resource. <br /> This field is required when **grant_type: authorization_code** <strong
                style="color: green;">**Market availability: Global**</strong>
            redirect_uri: This should be same as one of your client app URIs provided while registering the app. <br />
                This field is required when **grant_type: authorization_code** <strong style="color: green;">**Market
                availability: Global**</strong>
            refresh_token: Refresh token received as response of Authentication API with authorization_code grant type,
                to be used to refresh the access token. The token lifetime is 1 year. <strong style="color:
                green;">**Market availability: Global**</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/token"),
            headers=[
                param[str]("WM_MARKET", wm_market),
                param[str]("Authorization", authorization),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_PARTNER.ID", wm_partner_id),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=form_body(
                param[GrantType1OrStr]("grant_type", grant_type),
                param[str | None]("code", code),
                param[str | None]("redirect_uri", redirect_uri),
                param[str | None]("refresh_token", refresh_token),
            ),
            decoder=json_decoder[OauthTokenModel],
            error_mapper=token_api_error_mapper,
            request_options=request_options,
        )


class AsyncAuthorizationWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def get_token_detail(
        self,
        wm_sec_access_token: str,
        wm_market: str,
        content_type: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TokenDetailResponse, RawError]:
        """This process retrieves the access permissions granted by sellers to applications in the context of OAuth 2.0.
        The scope encompasses various API categories, each with its respective access levels, for example Reports: View
        Only, Item: Full Access, etc. <br><b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call <strong style="color: green;">**Market
                availability: Global**</strong>
            wm_market: Available marketplace location: us (USA), mx (Mexico), ca (Canada) or cl (Chile) <strong
                style="color: green;">**Market availability: Global**</strong>
            content_type: Content type of the request body. <strong style="color: green;">**Market availability:
                Global**</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID <strong style="color: green;">**Market availability: Global**</strong>
            wm_svc_name: Walmart Service Name <strong style="color: green;">**Market availability: Global**</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">**Market availability: Global**</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/token/detail"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_MARKET", wm_market),
                param[str]("Content-Type", content_type),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            decoder=async_json_decoder[TokenDetailResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def token_api(
        self,
        wm_market: str,
        authorization: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_partner_id: str | None = None,
        wm_consumer_channel_type: str | None = None,
        grant_type: GrantType1OrStr = GrantType1.CLIENT_CREDENTIALS,
        code: str | None = "65CA5DA313A549D49D15D3119D9AD85D",
        redirect_uri: str | None = "https://example-client-app.com",
        refresh_token: str | None = "APXcIoTpKMH9OQN.....",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OauthTokenModel, TokenApiErrorBody]:
        """<p>This endpoint issues access tokens required for authenticating API requests. It supports multiple OAuth
        2.0 grant types to accommodate various integration scenarios.</p> <b style='color:green;'>Market availability:
        Global</b><br/><h3>Supported Grant Types</h3><table><tr><th>Grant Type</th><th>Description</th><th>How to get
        the credentials</th></tr><tr><td>authorization_code</td><td>Exchanges an authorization code for an access
        token.</td><td>Used in app integration only via the OAuth consent screen. This is applicable to the <strong>US
        market only</strong>. Refer to <a href=/global-marketplace/docs/oauth-20-authorization>OAuth 2.0
        authorization</a> for more details.</td></tr><tr><td>client_credentials</td><td>Issues a token using client ID
        and secret.</td><td>For <strong>sellers</strong>: Obtain client_id and client_secret from the <strong>Developer
        Portal</strong>.<br/>For <strong>solution providers</strong>: Obtain credentials from sellers via <a
        href=/global-marketplace/docs/delegated-access-auth>Delegated Access
        authorization</a>.</td></tr><tr><td>refresh_token</td><td>Issues a new access token using a refresh
        token.</td><td>Provided during the authorization_code flow. This is applicable to the <strong>US market
        only</strong>. Refer to <a href=/global-marketplace/docs/oauth-20-authorization>OAuth 2.0 authorization</a> for
        more details.</td></tr></table><br/><b>Note:<br/></b> Use authorization_code and refresh_token <b>only for
        app-based integrations.</b> These grant types are currently <b>supported only in the US
        market</b>.<br/><br/><h3>Token Lifetimes</h3><table><tr><th>Token Type</th><th>Duration</th></tr><tr><td>Access
        Token</td><td>15 minutes <i>(900 seconds)</i></td></tr><tr><td>Refresh Token</td><td>1 year <i>(365
        days)</i></td></tr></table>

        Args:
            wm_market: Available marketplace location: us (USA), mx (Mexico), ca (Canada) or cl (Chile) <strong
                style="color: green;">**Market availability: Global**</strong>
            authorization: Basic authorization header. Base 64 encodes the Client ID and Client Secret retrieved in step
                two of the integration steps. <strong style="color: green;">**Market availability: Global**</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID <strong style="color: green;">**Market availability: Global**</strong>
            wm_svc_name: Walmart Service Name <strong style="color: green;">**Market availability: Global**</strong>
            wm_partner_id: Partner Id registered in Walmart marketplace to identify a seller. <br /> This field is
                required when **grant_type: authorization_code** and **grant_type: refresh_token** <strong style="color:
                green;">**Market availability: Global**</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">**Market availability: Global**</strong>
            grant_type: Type of grant requested. <br /> **Available grant types:** authorization_code, refresh_token and
                client_credentials <strong style="color: green;">**Market availability: Global**</strong>
            code: Authorization code obtained by your client app when the seller authorizes your app to access the
                seller resource. <br /> This field is required when **grant_type: authorization_code** <strong
                style="color: green;">**Market availability: Global**</strong>
            redirect_uri: This should be same as one of your client app URIs provided while registering the app. <br />
                This field is required when **grant_type: authorization_code** <strong style="color: green;">**Market
                availability: Global**</strong>
            refresh_token: Refresh token received as response of Authentication API with authorization_code grant type,
                to be used to refresh the access token. The token lifetime is 1 year. <strong style="color:
                green;">**Market availability: Global**</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/token"),
            headers=[
                param[str]("WM_MARKET", wm_market),
                param[str]("Authorization", authorization),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_PARTNER.ID", wm_partner_id),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=form_body(
                param[GrantType1OrStr]("grant_type", grant_type),
                param[str | None]("code", code),
                param[str | None]("redirect_uri", redirect_uri),
                param[str | None]("refresh_token", refresh_token),
            ),
            decoder=async_json_decoder[OauthTokenModel],
            error_mapper=token_api_error_mapper,
            request_options=request_options,
        )
