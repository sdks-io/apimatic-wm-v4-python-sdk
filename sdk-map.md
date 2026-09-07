<!-- Generated file — do not edit; regenerated with the SDK. -->

# SDK map — Walmart APIs (Python)

> A generated table of contents for this SDK. Consult this map and its sub-pages to learn signatures, error types, and server/auth wiring **by lookup**. Model shapes and enum values are *not* duplicated here — the map names the module declaring each type; read the shape there. Every name is the emitted spelling, so a wrong one fails at import rather than working silently.

|  |  |
| --- | --- |
| SDK display name | Walmart APIs |
| Root package | `walmart_apis` |
| Distribution name | `walmart-apis` |
| Requires | Python 3.10 or later |
| API spec version | `v4` |
| Generator | APIMatic |

Staleness check: the API spec version above changes when the SDK is regenerated from a new spec, and the package version is what `pip show` reports for the installed SDK. If a lookup here fails at import, re-read the module named in the row.

All `Source` paths on this map and its sub-pages are relative to the **SDK root** — the directory holding this file and `pyproject.toml` — never to the page that carries them. Open them as-is from the SDK root; if the SDK sits under a subdirectory of a larger repo, prefix that subdirectory.

---

## Getting a client

### Synchronous client

```python
from walmart_apis import WalmartApisClient
from walmart_apis.auth import SellerAuthAuthorizationCodeScope, SellerAuthClientCredentialsScope, WalletAuthScope
from walmart_apis.core import AuthorizationCodeCredentials, BasicAuthCredentials, ClientCredentials


def prompt(url: str) -> str:
    return input(f"Open {url}, then paste the code: ")


client = WalmartApisClient(
    seller_auth_authorization_code=AuthorizationCodeCredentials[SellerAuthAuthorizationCodeScope](
        client_id="YOUR_CLIENT_ID", redirect_uri="YOUR_REDIRECT_URI", prompt_for_authorization_code=prompt
    ),
    seller_auth_client_credentials=ClientCredentials[SellerAuthClientCredentialsScope](
        client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET"
    ),
    basic_client_auth=BasicAuthCredentials(username="YOUR_USERNAME", password="YOUR_PASSWORD"),
    wallet_auth=ClientCredentials[WalletAuthScope](client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET"),
    environment="production",
)

# TODO: call endpoints here -- see api-reference.md

client.close()
```

Alternatively, scope it — `with WalmartApisClient(...) as client:` closes the pool on exit.

### Asynchronous client

```python
from asyncio import run, to_thread

from walmart_apis import AsyncWalmartApisClient
from walmart_apis.auth import SellerAuthAuthorizationCodeScope, SellerAuthClientCredentialsScope, WalletAuthScope
from walmart_apis.core import AsyncAuthorizationCodeCredentials, BasicAuthCredentials, ClientCredentials


async def prompt(url: str) -> str:
    print(f"Open {url}")
    return await to_thread(input, "Paste the code: ")


async def main() -> None:
    client = AsyncWalmartApisClient(
        seller_auth_authorization_code=AsyncAuthorizationCodeCredentials[SellerAuthAuthorizationCodeScope](
            client_id="YOUR_CLIENT_ID", redirect_uri="YOUR_REDIRECT_URI", prompt_for_authorization_code=prompt
        ),
        seller_auth_client_credentials=ClientCredentials[SellerAuthClientCredentialsScope](
            client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET"
        ),
        basic_client_auth=BasicAuthCredentials(username="YOUR_USERNAME", password="YOUR_PASSWORD"),
        wallet_auth=ClientCredentials[WalletAuthScope](client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET"),
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

Every API group is a property on the client (e.g. `client.authorization`). Every constructor argument is optional and keyword-only. Sources: `walmart_apis/client.py`, `walmart_apis/async_client.py`:

| Keyword | Sync Type | Async Type | Default |
| --- | --- | --- | --- |
| `environment` | `Environment` | `Environment` | `"production"` |
| `timeout` | `float` | `float` | `30.0` seconds |
| `server_config` | `ServerConfigOrDict \| None` | `ServerConfigOrDict \| None` | `None` |
| `custom_http_client` | `HttpClient \| None` | — | `None` |
| `custom_async_http_client` | — | `AsyncHttpClient \| None` | `None` |
| `seller_auth_authorization_code` | `AuthorizationCodeCredentialsOrDict[SellerAuthAuthorizationCodeScope] \| None` | `AsyncAuthorizationCodeCredentialsOrDict[SellerAuthAuthorizationCodeScope] \| None` | `None` |
| `seller_auth_authorization_code_token_source` | `RefreshableTokenSource[AuthorizationCodeCredentials[SellerAuthAuthorizationCodeScope]] \| None` | `AsyncRefreshableTokenSource[AsyncAuthorizationCodeCredentials[SellerAuthAuthorizationCodeScope]] \| None` | `None` |
| `seller_auth_client_credentials` | `ClientCredentialsOrDict[SellerAuthClientCredentialsScope] \| None` | `ClientCredentialsOrDict[SellerAuthClientCredentialsScope] \| None` | `None` |
| `seller_auth_client_credentials_token_source` | `TokenSource[ClientCredentials[SellerAuthClientCredentialsScope]] \| None` | `AsyncTokenSource[ClientCredentials[SellerAuthClientCredentialsScope]] \| None` | `None` |
| `basic_client_auth` | `BasicAuthCredentialsOrDict \| None` | `BasicAuthCredentialsOrDict \| None` | `None` |
| `wallet_auth` | `ClientCredentialsOrDict[WalletAuthScope] \| None` | `ClientCredentialsOrDict[WalletAuthScope] \| None` | `None` |
| `wallet_auth_token_source` | `TokenSource[ClientCredentials[WalletAuthScope]] \| None` | `AsyncTokenSource[ClientCredentials[WalletAuthScope]] \| None` | `None` |

The types those columns name — where each imports from and, for a credentials dict, its keys:

| Type | Import from | Shape |
| --- | --- | --- |
| `Environment` | `walmart_apis.server` | `Literal` of the Environments table's names |
| `ServerConfigOrDict` | `walmart_apis.server` | keys as the Servers & auth tables read |
| `HttpClient` | `walmart_apis.core` | protocol — `send(request: HttpRequest) -> HttpResponse` · `close()` |
| `AuthorizationCodeCredentialsOrDict` | `walmart_apis.core` | `AuthorizationCodeCredentials` or a dict: `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AuthorizationCodePrompt` |
| `SellerAuthAuthorizationCodeScope` | `walmart_apis.auth` | `Enum` of the declared scopes |
| `RefreshableTokenSource` | `walmart_apis.core` | protocol — `fetch(credentials) -> OAuthTokenRefreshable` · `refresh(credentials, refresh_token) -> OAuthTokenRefreshable \| None` |
| `AuthorizationCodeCredentials` | `walmart_apis.core` | `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AuthorizationCodePrompt` |
| `ClientCredentialsOrDict` | `walmart_apis.core` | `ClientCredentials` or a dict: `client_id: str` · `client_secret: str` · `scopes: list[Scope] \| None` |
| `SellerAuthClientCredentialsScope` | `walmart_apis.auth` | `Enum` of the declared scopes |
| `TokenSource` | `walmart_apis.core` | protocol — `fetch(credentials) -> OAuthToken` |
| `ClientCredentials` | `walmart_apis.core` | `client_id: str` · `client_secret: str` · `scopes: list[Scope] \| None` |
| `BasicAuthCredentialsOrDict` | `walmart_apis.core` | `BasicAuthCredentials` or a dict: `username: str` · `password: str` |
| `WalletAuthScope` | `walmart_apis.auth` | `Enum` of the declared scopes |
| `AsyncHttpClient` | `walmart_apis.core` | protocol — `async send(request: HttpRequest) -> HttpResponse` · `async aclose()` |
| `AsyncAuthorizationCodeCredentialsOrDict` | `walmart_apis.core` | `AsyncAuthorizationCodeCredentials` or a dict: `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AsyncAuthorizationCodePrompt` |
| `AsyncRefreshableTokenSource` | `walmart_apis.core` | protocol — `async fetch(credentials) -> OAuthTokenRefreshable` · `async refresh(credentials, refresh_token) -> OAuthTokenRefreshable \| None` |
| `AsyncAuthorizationCodeCredentials` | `walmart_apis.core` | `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AsyncAuthorizationCodePrompt` |
| `AsyncTokenSource` | `walmart_apis.core` | protocol — `async fetch(credentials) -> OAuthToken` |

---

## Error-handling model (read once — applies to every operation)

Every operation is reached in two response modes:

- **Parsed call.** Returns the decoded payload and raises `ApiError` on an error status, with the decoded body on `.error` and the status on `.status_code`.
- **Raw call.** Reached through `.with_raw_response`; returns `ApiResult` — `Success` or `Failure` — and never raises for an API error. Read `.payload` on a `Success` or `.error` on a `Failure`; both carry `.response`.

What `.error` holds is fixed per operation. There are two cases:

- **Case A — typed error.** The operation documents at least one error status, so `walmart_apis/errors/` declares a union alias over the bodies those statuses map to — `RawError` is always its last arm, for any undocumented status — and `.error` is annotated with that alias. Narrow it with `isinstance`. The operation blocks name the alias and the status each arm maps from.
- **Case B — raw error.** The operation documents no error status; `.error` is `RawError` (`walmart_apis/core/results.py`): `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` · `response: HttpResponse`.

Core runtime types (`walmart_apis/core/`) — public members with their **declared types**, verbatim from source:

| Type | Public members | Source |
| --- | --- | --- |
| `ApiError` — raised by every parsed call; `.error` is a Case A alias from `walmart_apis/errors/` or `RawError` | `error: E` · `status_code: int` · `response: HttpResponse` | `walmart_apis/core/exceptions.py` |
| `ApiResult[T, E]` — returned by every raw call; the `Success[T] \| Failure[E]` union | `payload: T` (on `Success`) · `error: E` (on `Failure`) · `response: HttpResponse` (on both) | `walmart_apis/core/results.py` |
| `RawError` | `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` · `response: HttpResponse` | `walmart_apis/core/results.py` |

Typed error bodies (the arms of a Case A alias) are ordinary models — no special handling. The operation's **Type sources** table gives the module that declares each one; read field names, declared types and JSON aliases there, as for any other model.

```python
from walmart_apis.core import ApiError, RawError
from walmart_apis.models import AuthorizeError

try:
    client.authorization.authorize(
        response_type, client_id, redirect_uri, scope, state, code_challenge, code_challenge_method
    )
except ApiError as e:
    # Case A — typed error: e.error is AuthorizeErrorBody
    if isinstance(e.error, AuthorizeError):
        # Handle 400
        print(e.error)
    if isinstance(e.error, RawError):
        # Any other error status
        print(e.status_code, e.error.text())
```

**Raw (`.with_raw_response`) variants: present on every operation** — the same call returns `ApiResult` instead of raising, with the same body on `Failure.error`. Of **174 operations**, **174 are Case A (typed)** and **0 are Case B (raw)**.

---

## Operations — by controller (30 pages, 174 operations)

Each links to a sub-page with one block per operation, headed by its full accessor path: the HTTP verb and route (for a mock, a raw request or a provider-side log — never reconstruct it from the method name), the sync parsed signature with its required positional parameters, each parameter's role and — where it differs — wire name, both return types, and its error case — **Case A** names the alias and the status each arm maps from, **Case B** names `RawError`. Every block also carries a **Type sources** table — every type it names, with the module that declares it.

**Each block states what is specific to its operation. Everything below holds for every operation, and blocks never restate it — silence means the default applies.**

| Applies to every operation | Stated where |
| --- | --- |
| **Four spellings, one signature** — the same method name and parameters on `Client` and `AsyncClient`, each also reachable through `.with_raw_response`; the async twin is a coroutine to `await`, with the same return types and error case, and where the **Async Type** column differs, pass the type it names | Getting a client |
| **Parsed raises, raw returns** — `ApiError` versus `ApiResult` | Error-handling model |
| **Case B error is always `RawError`** — also the last arm of every Case A alias, where a block's **Error arms** bullet ends in it | Error-handling model |
| **A trailing `request_options`** — keyword-only and optional, for per-call overrides such as a timeout or extra headers; every signature ends with it | here (`walmart_apis/core/request_options.py`) |
| **Each operation names its own server** — this SDK declares several, so every block carries a **Server** bullet with the server's key in `server_config=` | its block |
| **Parameter names are literal** — signatures are generated code verbatim, and everything behind the bare `*` must be passed by name | here |
| **A parameter's wire name is its Python name** — sent as-is on the path, query string, header or body, unless the block's **Params** bullet carries a wire name beside the role | here |

**The operation's behavioural prose lives on the operation itself**, as the method's docstring in the module named at the top of its page, and again in `api-reference.md` with a per-parameter description and a usage sample. Blocks here give you the contract — names, types, shapes, errors. Where an operation's *semantics* decide what you must pass, that is what the docstring settles; read it there rather than filling it in from memory.

Sub-pages chunk per `###` block: each block is self-contained given the table above, and assumes this page is loaded beside it.

| Controller | Ops | Page |
| --- | --- | --- |
| `client.authorization` | 3 | [map/operations/authorization.md](map/operations/authorization.md) |
| `client.catalog` | 2 | [map/operations/catalog.md](map/operations/catalog.md) |
| `client.data_kiosk` | 5 | [map/operations/data_kiosk.md](map/operations/data_kiosk.md) |
| `client.disputes` | 1 | [map/operations/disputes.md](map/operations/disputes.md) |
| `client.feeds` | 5 | [map/operations/feeds.md](map/operations/feeds.md) |
| `client.final_payout` | 2 | [map/operations/final_payout.md](map/operations/final_payout.md) |
| `client.finances` | 4 | [map/operations/finances.md](map/operations/finances.md) |
| `client.fulfillment_outbound` | 7 | [map/operations/fulfillment_outbound.md](map/operations/fulfillment_outbound.md) |
| `client.inventory` | 4 | [map/operations/inventory.md](map/operations/inventory.md) |
| `client.listings_items` | 5 | [map/operations/listings_items.md](map/operations/listings_items.md) |
| `client.listings_restrictions` | 1 | [map/operations/listings_restrictions.md](map/operations/listings_restrictions.md) |
| `client.merchant_fulfillment` | 5 | [map/operations/merchant_fulfillment.md](map/operations/merchant_fulfillment.md) |
| `client.orders` | 14 | [map/operations/orders.md](map/operations/orders.md) |
| `client.payouts` | 5 | [map/operations/payouts.md](map/operations/payouts.md) |
| `client.product_type_definitions` | 2 | [map/operations/product_type_definitions.md](map/operations/product_type_definitions.md) |
| `client.reconciliation` | 3 | [map/operations/reconciliation.md](map/operations/reconciliation.md) |
| `client.report_schedules` | 4 | [map/operations/report_schedules.md](map/operations/report_schedules.md) |
| `client.reports` | 7 | [map/operations/reports.md](map/operations/reports.md) |
| `client.sellers` | 2 | [map/operations/sellers.md](map/operations/sellers.md) |
| `client.settlement` | 3 | [map/operations/settlement.md](map/operations/settlement.md) |
| `client.uploads` | 1 | [map/operations/uploads.md](map/operations/uploads.md) |
| `client.wfs_inventory` | 1 | [map/operations/wfs_inventory.md](map/operations/wfs_inventory.md) |
| `client.messaging` | 11 | [map/operations/messaging.md](map/operations/messaging.md) |
| `client.notifications` | 9 | [map/operations/notifications.md](map/operations/notifications.md) |
| `client.product_fees` | 3 | [map/operations/product_fees.md](map/operations/product_fees.md) |
| `client.product_pricing` | 8 | [map/operations/product_pricing.md](map/operations/product_pricing.md) |
| `client.sales` | 1 | [map/operations/sales.md](map/operations/sales.md) |
| `client.shipping` | 9 | [map/operations/shipping.md](map/operations/shipping.md) |
| `client.solicitations` | 2 | [map/operations/solicitations.md](map/operations/solicitations.md) |
| `client.wfs_inbound` | 45 | [map/operations/wfs_inbound.md](map/operations/wfs_inbound.md) |

---

## Models — where they live, how to build them

**Shapes live only in the source.** Every module under `walmart_apis/models/` declares one type plus its input companion, and every module under `walmart_apis/errors/` one alias plus the mapper that builds it; no two share a name. Take a type's module from the operation's **Type sources** table. When no retrieved chunk names it, the module is the type name in snake_case under the kind's directory below (`AccessPoint` ↔ `access_point.py`; an error alias drops its `Body` suffix: `CreateWarrantyErrorBody` ↔ `create_warranty_error.py`). Never grep for a type.

| Group | Count | Directory (module = `<type_name>.py`) |
| --- | --- | --- |
| Models (`SdkBaseModel` pydantic classes) | 410 | `walmart_apis/models/` |
| Enums (`Enum` over `str` / `int`) — Python member names + wire values | 119 | `walmart_apis/models/enums/` |
| Error aliases (one per Case A operation) | 174 | `walmart_apis/errors/` |

Conventions: a model is a `SdkBaseModel` (pydantic) class; a field whose wire name differs from its Python name carries it as `Field(alias=…)` (`access_point_id` ↔ `"accessPointId"`) — read the alias off the field rather than deriving it. An omittable field is annotated `Optional[T]` and defaults to `UNSET`, and one that may also be explicitly null is `OptionalNullable[T]`; both come from `core` and neither is `typing.Optional` — there is no `None` arm unless the spec declared the property nullable, so passing `None` to the first is a type error rather than a value that serializes.

Every model and enum also has an **input companion**, exported beside it from the same package (`AccessPoint` ↔ `AccessPointDict`). Wherever a signature names the companion you may pass either the model instance or a plain dict with the same keys, whichever reads better at the call site. An enum is a real `Enum` subclass over `str` / `int`; its companion is spelled `<Name>OrStr` or `<Name>OrInt` (`AccountStatus` ↔ `AccountStatusOrStr`) and additionally accepts a wire value this SDK version does not know.

Import paths by content type (`from <package> import <Name>`):

| Contents | Import from |
| --- | --- |
| Client (root) | `walmart_apis` |
| Operation controllers | `walmart_apis.apis` |
| Models | `walmart_apis.models` |
| Enums | `walmart_apis.models.enums` |
| Error aliases | `walmart_apis.errors` |
| Core runtime (`ApiError`, `ApiResult`, `RawError`, …) | `walmart_apis.core` |

---

## Servers & auth

**OAuth2 (authorization code).** Pass `seller_auth_authorization_code` your client id, redirect URI and authorization code; authorization is at `/auth/v4/authorize` and tokens come from `/auth/v4/token`, both on the `default` server. Scopes are the `SellerAuthAuthorizationCodeScope` alias.

**OAuth2 (client credentials).** Pass `seller_auth_client_credentials` your client id and secret; tokens come from `/auth/v4/token` on the `default` server. Scopes are the `SellerAuthClientCredentialsScope` alias.

**Basic auth.** Pass `basic_client_auth={"username": …, "password": …}`, or a `BasicAuthCredentials`.

**OAuth2 (client credentials).** Pass `wallet_auth` your client id and secret; tokens come from `/auth/token` on the `default1` server. Scopes are the `WalletAuthScope` alias.

Operation blocks name their scheme in an **Auth** bullet; an operation whose spec declares no scheme carries no such bullet.

- `AND` — every scheme listed must be configured for the call to succeed.
- `OR` — any one of the schemes listed can be used; the first one you configured is the one sent, in the order listed.

A scheme you did not configure is skipped silently rather than raising, and the request is sent anyway — so an authentication failure can mean no credential was sent rather than a bad one.

**Environments.** `environment=` selects the target environment (`walmart_apis/server/environment.py`):

| Environment | Hosting |
| --- | --- |
| `"production"` *(default)* | Production |
| `"environment2"` | Sandbox |
| `"environment3"` | mock |

**2 servers.** Base-URL templates and override points (`walmart_apis/server/server_config.py`):

| Server | `"production"` base URL | `"environment2"` base URL | `"environment3"` base URL | Override point |
| --- | --- | --- | --- | --- |
| `default` | `https://marketplace.walmart.com/seller` | `https://sandbox.marketplace.walmart.com/seller` | `https://walmart-apis-mock-server.onrender.com/seller` | `{"default": {"production": {"base_url": …}}}` (and the other environments) |
| `default1` | `https://marketplace.walmart.com/seller/v1` | `https://sandbox.marketplace.walmart.com/seller/v1` | `https://walmart-apis-mock-server.onrender.com/seller/v1` | `{"default1": {"production": {"base_url": …}}}` (and the other environments) |

Pick a row with `environment=`, and override any of these by passing `server_config=` a dict nested exactly as the columns above read — `{"default": {"production": {"base_url": …}}}` — with each row's variables sitting beside its `base_url`.

