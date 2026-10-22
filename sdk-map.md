<!-- Generated file — do not edit; regenerated with the SDK. -->

# SDK map — Walmart APIs (Python)

> A generated table of contents for this SDK. Consult this map and its sub-pages to learn signatures, error types, and server/auth wiring **by lookup**. Model shapes and enum values are *not* duplicated here — the map names the module declaring each type; read the shape there. Every name is the emitted spelling, so a wrong one fails at import rather than working silently.

|  |  |
| --- | --- |
| SDK display name | Walmart APIs |
| Root package | `walmart_apis` |
| Distribution name | `apimatic-wm-v4-sdk` |
| Requires | Python 3.10 or later |
| API spec version | `1.0` |
| Generator | APIMatic |

Staleness check: the API spec version above changes when the SDK is regenerated from a new spec, and the package version is what `pip show` reports for the installed SDK. If a lookup here fails at import, re-read the module named in the row.

All `Source` paths on this map and its sub-pages are relative to the **SDK root** — the directory holding this file and `pyproject.toml` — never to the page that carries them. Open them as-is from the SDK root; if the SDK sits under a subdirectory of a larger repo, prefix that subdirectory.

---

## Getting a client

### Synchronous client

```python
from walmart_apis import WalmartApisClient
from walmart_apis.core import BasicAuthCredentials

client = WalmartApisClient(
    basic_auth=BasicAuthCredentials(username="YOUR_USERNAME", password="YOUR_PASSWORD"),
    bearer_auth="YOUR_BEARER_TOKEN",
    access_token="YOUR_API_KEY",
    environment="production",
)

# TODO: call endpoints here -- see api-reference.md

client.close()
```

Alternatively, scope it — `with WalmartApisClient(...) as client:` closes the pool on exit.

### Asynchronous client

```python
from asyncio import run

from walmart_apis import AsyncWalmartApisClient
from walmart_apis.core import BasicAuthCredentials


async def main() -> None:
    client = AsyncWalmartApisClient(
        basic_auth=BasicAuthCredentials(username="YOUR_USERNAME", password="YOUR_PASSWORD"),
        bearer_auth="YOUR_BEARER_TOKEN",
        access_token="YOUR_API_KEY",
        environment="production",
    )
    # TODO: call endpoints here, awaiting each -- see api-reference.md
    await client.aclose()


run(main())
```

Alternatively, scope it — `async with AsyncWalmartApisClient(...) as client:` closes the pool on exit.

`AsyncClient` (`walmart_apis/async_client.py`) mirrors `Client` method for method, each endpoint method a coroutine. It takes the same keywords, except that each client accepts only its own transport and — where the **Async Type** column differs — only its own flavor.

`Client` and `AsyncClient` are aliases of `WalmartApisClient` and `AsyncWalmartApisClient` — the names tracebacks and `repr()` show; all four import from the root.

`close()` / `aclose()` closes the transport even when you supplied one via `custom_http_client=` / `custom_async_http_client=`, and a closed client cannot be reused.

Every API group is a property on the client (e.g. `client.assortment_recommendations`). Every constructor argument is optional and keyword-only. Sources: `walmart_apis/client.py`, `walmart_apis/async_client.py`:

| Keyword | Sync Type | Async Type | Default |
| --- | --- | --- | --- |
| `environment` | `Environment` | `Environment` | `"production"` |
| `base_url` | `str \| None` | `str \| None` | `None` |
| `timeout` | `float` | `float` | `30.0` seconds |
| `retry_options` | `int \| RetryOptionsOrDict \| None` | `int \| RetryOptionsOrDict \| None` | `None` |
| `logging_options` | `LoggingOptionsOrDict \| None` | `LoggingOptionsOrDict \| None` | `None` |
| `custom_http_client` | `HttpClient \| None` | — | `None` |
| `custom_async_http_client` | — | `AsyncHttpClient \| None` | `None` |
| `basic_auth` | `BasicAuthCredentialsOrDict \| None` | `BasicAuthCredentialsOrDict \| None` | `None` |
| `bearer_auth` | `str \| None` | `str \| None` | `None` |
| `access_token` | `str \| None` | `str \| None` | `None` |

The types those columns name — where each imports from and, for a credentials dict, its keys:

| Type | Import from | Shape |
| --- | --- | --- |
| `Environment` | `walmart_apis.server` | `Literal` of the Environments table's names |
| `RetryOptionsOrDict` | `walmart_apis.core` | a retry count, `RetryOptions`, or a dict: `max_retries: int` · `initial_delay: float` · `backoff_factor: float` · `max_delay: float` · `max_jitter: float` · `status_codes_to_retry: frozenset[int]` · `http_methods_to_retry: frozenset[HttpMethod]` |
| `LoggingOptionsOrDict` | `walmart_apis.core` | `LoggingOptions` or a dict: `log_request_headers: bool` · `log_response_headers: bool` · `log_request_body: bool` · `body_size_limit: int` · `redaction_placeholder: str` · `unmask_headers: AbstractSet[str]` · `mask_headers: AbstractSet[str]` · `mask_keys: AbstractSet[str]` |
| `HttpClient` | `walmart_apis.core` | protocol — `send(request: HttpRequest) -> HttpResponse` · `close()`; `send` returns once the head has arrived and never reads the body, and raises `TransportError` (from `core`) when no response arrives — anything else it raises is never retried |
| `BasicAuthCredentialsOrDict` | `walmart_apis.core` | `BasicAuthCredentials` or a dict: `username: str` · `password: str` |
| `AsyncHttpClient` | `walmart_apis.core` | protocol — `async send(request: HttpRequest) -> AsyncHttpResponse` · `async aclose()`; the same obligation, awaited |

### Retries — on by default

`retry_options` left at `None` applies the default `RetryOptions` policy below, so an unconfigured client **retries**: a request whose method is in `http_methods_to_retry` is sent again when it gets a status in `status_codes_to_retry`, or no response at all, and the last outcome reaches you only once its retries are spent. A body that cannot be re-sent byte for byte — a streamed file upload — is never retried. `retry_options=0` (or `{"max_retries": 0}`) turns retrying off; a bare count sets `max_retries` and leaves every other field at its default.

`RetryOptions` fields (source: `walmart_apis/core/retries.py`). Pass only the fields you change; each one left out takes its default:

| Field | Type | Default |
| --- | --- | --- |
| `max_retries` | `int` | `3` |
| `initial_delay` | `float` (seconds) | `1.0` |
| `backoff_factor` | `float` | `2.0` |
| `max_delay` | `float` (seconds) | `60.0` |
| `max_jitter` | `float` (seconds) | `0.5` |
| `status_codes_to_retry` | `frozenset[int]` | `frozenset({408, 429, 500, 502, 503, 504})` |
| `http_methods_to_retry` | `frozenset[HttpMethod]` | `frozenset({"GET", "HEAD", "PUT", "OPTIONS"})` |

The wait before retry *n* is `initial_delay × backoff_factor^(n−1)` plus up to `max_jitter` of random delay, the sum capped at `max_delay`; a `Retry-After` header replaces it, trimmed to `max_delay`.

A single call overrides two of these through `request_options` (`walmart_apis/core/request_options.py`): `max_retries` and `status_codes_to_retry`, each merged over the client's policy field by field — `request_options={"max_retries": 0}` turns retrying off for that one call and leaves every other call alone.

### Logging — off by default

Every HTTP exchange is written through the standard `logging` module under the `walmart_apis` logger, and the SDK configures nothing itself. Set that logger's level to turn it on: INFO writes the request line and a 2xx response line, WARNING a non-2xx response line and each retry, ERROR a call that ends in an exception, and DEBUG the header dumps and the request body that the flags below turn on. Or set `WALMART_APIS_LOG=info|debug` before the process starts: it sets the level, turns the three flags on for `debug`, and adds a stderr handler only where nothing listens.

`LoggingOptions` fields (source: `walmart_apis/core/logging.py`). Pass only the fields you change; each one left out takes its default, and a name set you pass replaces its default:

| Field | Type | Default |
| --- | --- | --- |
| `log_request_headers` | `bool` | `False` |
| `log_response_headers` | `bool` | `False` |
| `log_request_body` | `bool` | `False` |
| `body_size_limit` | `int` (bytes) | `32768` |
| `redaction_placeholder` | `str` | `"REDACTED"` |
| `unmask_headers` | `AbstractSet[str]` | `frozenset()` |
| `mask_headers` | `AbstractSet[str]` | `frozenset()` |
| `mask_keys` | `AbstractSet[str]` | `frozenset({"sig", "signature", "access_token", "apikey", "api_key", "client_secret", "password", "refresh_token", "code", "assertion", "client_assertion"})` |

A single call is quietened through `request_options` (`walmart_apis/core/request_options.py`): `log_level`, a `logging` level constant, is a floor below which that call's records are not written; it never turns a dump or the body on. A header value prints `REDACTED` unless its name is on the runtime's safe list, a query value unless its key is a paging name, and a form field whose key is in `mask_keys` always; a JSON body prints as sent; a response body is never logged.

---

## Error-handling model (read once — applies to every operation)

Every operation is reached in two response modes:

- **Parsed call.** Returns the decoded payload and raises `ApiError` on an error status, with the decoded body on `.error` and the status on `.status_code`.
- **Raw call.** Reached through `.with_raw_response`; returns `ApiResult` — `Success` or `Failure` — and never raises for an API error. Read `.payload` on a `Success` or `.error` on a `Failure`; both carry `.status_code` and `.headers`.

What `.error` holds is fixed per operation. There are two cases:

- **Case A — typed error.** The operation documents at least one error status, so `walmart_apis/errors/` declares a union alias over the bodies those statuses map to — `RawError` is always its last arm, for any undocumented status — and `.error` is annotated with that alias. Narrow it with `isinstance`. The operation blocks name the alias and the status each arm maps from.
- **Case B — raw error.** The operation documents no error status; `.error` is `RawError` (`walmart_apis/core/results.py`): `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any`.

Core runtime types (`walmart_apis/core/`) — public members with their **declared types**, verbatim from source:

| Type | Public members | Source |
| --- | --- | --- |
| `ApiError` — raised by every parsed call; `.error` is a Case A alias from `walmart_apis/errors/` or `RawError` | `error: E` · `status_code: int` · `headers: Mapping[str, str]` | `walmart_apis/core/exceptions.py` |
| `ApiResult[T, E]` — returned by every raw call; the `Success[T] \| Failure[E]` union | `payload: T` (on `Success`) · `error: E` (on `Failure`) · `status_code: int` · `headers: Mapping[str, str]` (both on either) | `walmart_apis/core/results.py` |
| `RawError` | `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` | `walmart_apis/core/results.py` |

Typed error bodies (the arms of a Case A alias) are ordinary models — no special handling. The operation's **Type sources** table gives the module that declares each one; read field names, declared types and JSON aliases there, as for any other model.

```python
try:
    response = client.assortment_recommendations.get_assortment_recommendation_trends(
        "some example string",
        WmGlobalVersion._3_1,
        "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
        "b3261d2d-028a-4ef7-8602-633c23200af6",
        "Walmart Service Name",
        WmMarket1.US,
        trend_types="PRICE_TRENDS,DEMAND_TRENDS",
    )
except ApiError as e:
    # Case A — typed error: e.error is GetAssortmentRecommendationTrendsErrorBody
    if isinstance(e.error, ErrorResponse1):
        # Handle 400, 500
        print(e.error)
    if isinstance(e.error, RawError):
        # Any other error status
        print(e.status_code, e.error.text())
```

**Raw (`.with_raw_response`) variants: present on every operation** — the same call returns `ApiResult` instead of raising, with the same body on `Failure.error`. Of **117 operations**, **85 are Case A (typed)** and **32 are Case B (raw)**.

---

## Operations — by controller (29 pages, 117 operations)

Each links to a sub-page with one block per operation, headed by its full accessor path: the HTTP verb and route (for a mock, a raw request or a provider-side log — never reconstruct it from the method name), the sync parsed signature with its required positional parameters, each parameter's role and — where it differs — wire name, both return types, and its error case — **Case A** names the alias and the status each arm maps from, **Case B** names `RawError`. Every block also carries a **Type sources** table — every *generated* type it names, with the module that declares it. A runtime type — a file alias, a date/time or byte converter — is not listed there.

**Each block states what is specific to its operation. Everything below holds for every operation, and blocks never restate it — silence means the default applies.**

| Applies to every operation | Stated where |
| --- | --- |
| **Four spellings, one signature** — the same method name and parameters on `Client` and `AsyncClient`, each also reachable through `.with_raw_response`; the async twin is a coroutine to `await`, with the same return types and error case, and where the **Async Type** column differs, pass the type it names | Getting a client |
| **Parsed raises, raw returns** — `ApiError` versus `ApiResult` | Error-handling model |
| **Case B error is always `RawError`** — also the last arm of every Case A alias, where a block's **Error arms** bullet ends in it | Error-handling model |
| **A trailing `request_options`** — keyword-only and optional, for per-call overrides such as a timeout, extra headers, `max_retries`, `status_codes_to_retry` or `log_level`; every signature ends with it | here (`walmart_apis/core/request_options.py`), Retries, Logging |
| **Base URL is the selected environment's** — this SDK's only server, one URL per `environment=`; override it with `base_url="https://…"` | Servers & auth |
| **Parameter names are literal** — signatures are generated code verbatim, and everything behind the bare `*` must be passed by name | here |
| **A parameter's wire name is its Python name** — sent as-is on the path, query string, header or body, unless the block's **Params** bullet carries a wire name beside the role | here |

**The operation's behavioural prose lives on the operation itself**, as the method's docstring in the module named at the top of its page, and again in `api-reference.md` with a per-parameter description and a usage sample. Blocks here give you the contract — names, types, shapes, errors. Where an operation's *semantics* decide what you must pass, that is what the docstring settles; read it there rather than filling it in from memory.

Sub-pages chunk per `###` block: each block is self-contained given the table above, and assumes this page is loaded beside it.

| Controller | Class | Ops | Page |
| --- | --- | --- | --- |
| `client.assortment_recommendations` | `AssortmentRecommendations` / `AsyncAssortmentRecommendations` | 5 | [map/operations/assortment_recommendations.md](map/operations/assortment_recommendations.md) |
| `client.authorization` | `Authorization` / `AsyncAuthorization` | 2 | [map/operations/authorization.md](map/operations/authorization.md) |
| `client.disputes` | `Disputes` / `AsyncDisputes` | 2 | [map/operations/disputes.md](map/operations/disputes.md) |
| `client.feeds_api` | `FeedsApi` / `AsyncFeedsApi` | 3 | [map/operations/feeds_api.md](map/operations/feeds_api.md) |
| `client.insight_api` | `InsightApi` / `AsyncInsightApi` | 7 | [map/operations/insight_api.md](map/operations/insight_api.md) |
| `client.inventory_api` | `InventoryApi` / `AsyncInventoryApi` | 7 | [map/operations/inventory_api.md](map/operations/inventory_api.md) |
| `client.lag_time_api` | `LagTimeApi` / `AsyncLagTimeApi` | 2 | [map/operations/lag_time_api.md](map/operations/lag_time_api.md) |
| `client.notifications` | `Notifications` / `AsyncNotifications` | 6 | [map/operations/notifications.md](map/operations/notifications.md) |
| `client.on_request_report` | `OnRequestReport` / `AsyncOnRequestReport` | 1 | [map/operations/on_request_report.md](map/operations/on_request_report.md) |
| `client.on_request_report_api` | `OnRequestReportApi` / `AsyncOnRequestReportApi` | 3 | [map/operations/on_request_report_api.md](map/operations/on_request_report_api.md) |
| `client.prices` | `Prices` / `AsyncPrices` | 11 | [map/operations/prices.md](map/operations/prices.md) |
| `client.promotions` | `Promotions` / `AsyncPromotions` | 3 | [map/operations/promotions.md](map/operations/promotions.md) |
| `client.recommendations_api` | `RecommendationsApi` / `AsyncRecommendationsApi` | 4 | [map/operations/recommendations_api.md](map/operations/recommendations_api.md) |
| `client.report_scheduler` | `ReportScheduler` / `AsyncReportScheduler` | 4 | [map/operations/report_scheduler.md](map/operations/report_scheduler.md) |
| `client.reports_api` | `ReportsApi` / `AsyncReportsApi` | 7 | [map/operations/reports_api.md](map/operations/reports_api.md) |
| `client.returns_refund` | `ReturnsRefund` / `AsyncReturnsRefund` | 3 | [map/operations/returns_refund.md](map/operations/returns_refund.md) |
| `client.reviews` | `Reviews` / `AsyncReviews` | 3 | [map/operations/reviews.md](map/operations/reviews.md) |
| `client.rich_media` | `RichMedia` / `AsyncRichMedia` | 2 | [map/operations/rich_media.md](map/operations/rich_media.md) |
| `client.sem_campaign_management` | `SemCampaignManagement` / `AsyncSemCampaignManagement` | 6 | [map/operations/sem_campaign_management.md](map/operations/sem_campaign_management.md) |
| `client.sem_catalog` | `SemCatalog` / `AsyncSemCatalog` | 2 | [map/operations/sem_catalog.md](map/operations/sem_catalog.md) |
| `client.sem_item_diagnostics` | `SemItemDiagnostics` / `AsyncSemItemDiagnostics` | 2 | [map/operations/sem_item_diagnostics.md](map/operations/sem_item_diagnostics.md) |
| `client.sem_reporting` | `SemReporting` / `AsyncSemReporting` | 3 | [map/operations/sem_reporting.md](map/operations/sem_reporting.md) |
| `client.seo_recommendations` | `SeoRecommendations` / `AsyncSeoRecommendations` | 2 | [map/operations/seo_recommendations.md](map/operations/seo_recommendations.md) |
| `client.ship_with_walmart` | `ShipWithWalmart` / `AsyncShipWithWalmart` | 10 | [map/operations/ship_with_walmart.md](map/operations/ship_with_walmart.md) |
| `client.shipment_protection` | `ShipmentProtection` / `AsyncShipmentProtection` | 6 | [map/operations/shipment_protection.md](map/operations/shipment_protection.md) |
| `client.simplified_shipping_settings` | `SimplifiedShippingSettings` / `AsyncSimplifiedShippingSettings` | 5 | [map/operations/simplified_shipping_settings.md](map/operations/simplified_shipping_settings.md) |
| `client.tax_form_apis` | `TaxFormApis` / `AsyncTaxFormApis` | 2 | [map/operations/tax_form_apis.md](map/operations/tax_form_apis.md) |
| `client.wsr_attribution_reports` | `WsrAttributionReports` / `AsyncWsrAttributionReports` | 3 | [map/operations/wsr_attribution_reports.md](map/operations/wsr_attribution_reports.md) |
| `client.walmart_seller_fulfilled` | `WalmartSellerFulfilled` / `AsyncWalmartSellerFulfilled` | 1 | [map/operations/walmart_seller_fulfilled.md](map/operations/walmart_seller_fulfilled.md) |

---

## Models — where they live, how to build them

**Shapes live only in the source.** Every module under `walmart_apis/models/` declares one type plus its input companion, and every module under `walmart_apis/errors/` one alias plus the mapper that builds it; no two share a name. Take a type's module from the operation's **Type sources** table. When no retrieved chunk names it, the module is the type name in snake_case under the kind's directory below (`AccountConfigs10` ↔ `account_configs10.py`; an error alias drops its `Body` suffix: `GetReturnsErrorBody` ↔ `get_returns_error.py`). Never grep for a type.

| Group | Count | Directory (module = `<type_name>.py`) |
| --- | --- | --- |
| Models (`SdkBaseModel` pydantic classes) | 959 | `walmart_apis/models/` |
| Enums (`Enum` over `str`) — Python member names + wire values | 188 | `walmart_apis/models/enums/` |
| Unions (discriminated) — `TypeAlias` over the arms, tagged via `WireDiscriminator(…)` | 1 | `walmart_apis/models/unions/` |
| Unions (plain) — `TypeAlias` over the arms | 7 | `walmart_apis/models/unions/` |
| Error aliases (one per Case A operation) | 85 | `walmart_apis/errors/` |

Conventions: a model is a `SdkBaseModel` (pydantic) class; a field whose wire name differs from its Python name carries it as `Field(alias=…)` (`shipping_priority` ↔ `"shippingPriority"`) — read the alias off the field rather than deriving it. An omittable field is annotated `Optional[T]` and defaults to `UNSET`, and one that may also be explicitly null is `OptionalNullable[T]`; both come from `core` and neither is `typing.Optional` — there is no `None` arm unless the spec declared the property nullable, so passing `None` to the first is a type error rather than a value that serializes.

Every model, enum and union also has an **input companion**, exported beside it from the same package (`AccountConfigs10` ↔ `AccountConfigs10Dict`). Wherever a signature names the companion you may pass either the model instance or a plain dict with the same keys, whichever reads better at the call site. An enum is a real `Enum` subclass over `str`; its companion is spelled `<Name>OrStr` or `<Name>OrInt` (`Accept` ↔ `AcceptOrStr`) and additionally accepts a wire value this SDK version does not know. A union is a `TypeAlias` over its arms — a discriminated one names the wire key its arms are told apart by, so build the arm you mean and the union supplies the tag for any arm whose own schema does not declare it.

Import paths by content type (`from <package> import <Name>`):

| Contents | Import from |
| --- | --- |
| Client (root) | `walmart_apis` |
| Operation controllers | `walmart_apis.apis` |
| Models | `walmart_apis.models` |
| Enums | `walmart_apis.models.enums` |
| Unions | `walmart_apis.models.unions`, `walmart_apis.models` |
| Error aliases | `walmart_apis.errors` |
| Core runtime (`ApiError`, `ApiResult`, `RawError`, …) | `walmart_apis.core` |

---

## Servers & auth

**Basic auth.** Pass `basic_auth={"username": …, "password": …}`, or a `BasicAuthCredentials`.

**Bearer token.** Pass `bearer_auth="<token>"`.

**API key (header `WM_SEC.ACCESS_TOKEN`).** Pass `access_token="<api_key>"`; sent as the `WM_SEC.ACCESS_TOKEN` request header.

Operation blocks name their scheme in an **Auth** bullet; an operation whose spec declares no scheme carries no such bullet.

- `AND` — every scheme listed must be configured for the call to succeed.
- `OR` — any one of the schemes listed can be used; the first one you configured is the one sent, in the order listed.

A scheme you did not configure is skipped silently rather than raising, and the request is sent anyway — so an authentication failure can mean no credential was sent rather than a bad one.

**Environments.** `environment=` selects the target environment (`walmart_apis/server/environment.py`); this SDK's one server (`walmart_apis/server/server_config.py`) has a base URL per environment:

| Environment | Base URL | Hosting | Override point |
| --- | --- | --- | --- |
| `"production"` *(default)* | `https://marketplace.walmartapis.com` | Production URL, Specifies the production URL., Specifies the production URL., Production URL, Specifies the production URL., Specifies the production URL., Refers to the URL used for accessing the production server., Specifies the production URL., Refers to the URL used for accessing the production server., Production URL, Production URL, Production server for all APIs., Production URL, Production URL, Production URL, Base URL for production requests., Production URL, Production URL, Production URL, Refers to the URL used for accessing the production server. | `base_url="https://…"` |
| `"environment2"` | `https://sandbox.walmartapis.com` | Sandbox URL, Specifies the sandbox URL., Specifies the sandbox URL., Sandbox URL, Specifies the sandbox URL., Specifies the sandbox URL., Refers to the URL used for accessing the sandbox server., Specifies the sandbox URL., Refers to the URL used for accessing the sandbox server., Sandbox URL, Sandbox URL, Sandbox URL, Sandbox URL, Sandbox URL, Base URL for sandbox requests., Sandbox URL, Sandbox URL, Sandbox URL, Refers to the URL used for accessing the sandbox server. | `base_url="https://…"` |

Pick a row with `environment=`.

