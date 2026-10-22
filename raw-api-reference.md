# Raw Reference

**Raw** endpoints, reached through `with_raw_response`, return `ApiResult[T, E]` and never raise for an API error. For the parsed endpoints, see [API Reference](api-reference.md).

> Source: [WalmartApisClient](walmart_apis/client.py)

## AssortmentRecommendations

> Source: [AssortmentRecommendations](walmart_apis/apis/assortment_recommendations.py)

<details>
<summary><code>def get_assortment_recommendation_trends(recommendation_unique_id: str, wm_global_version: WmGlobalVersionOrStr, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, *, trend_types: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3GrowthAssortmentRecommendationsTrendsResponse, GetAssortmentRecommendationTrendsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

You can fetch the monthly and weekly trends for both demand and price, for the assortment recommendations that are recommended for you. <br><b style='color:green;'>Market availability: US only</span></b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.assortment_recommendations.with_raw_response.get_assortment_recommendation_trends(
    "some example string",
    WmGlobalVersion._3_1,
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    trend_types="PRICE_TRENDS,DEMAND_TRENDS",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3GrowthAssortmentRecommendationsTrendsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAssortmentRecommendationTrendsErrorBody
```

**Async**

```python
result = await async_client.assortment_recommendations.with_raw_response.get_assortment_recommendation_trends(
    "some example string",
    WmGlobalVersion._3_1,
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    trend_types="PRICE_TRENDS,DEMAND_TRENDS",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3GrowthAssortmentRecommendationsTrendsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAssortmentRecommendationTrendsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>recommendation_unique_id</code> | <code>str</code> | Unique ID that is returned in the response of the get recommendations API or in the on-request bulk CSV file. <br><b style='color:green;'>Market availability: US only</span></b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. Required for authenticating requests to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>trend_types</code> | <code>str \| None</code> | Comma separated list of trends.<br><b style='color:green;'>Market availability: US only</span></b><br><br> \| Attribute \| Description \| Data Type \|<br>\| --- \| ----------- \| ------- \|<br>\| PRICE_TRENDS \| Indicates the price trends for the recommended item in the marketplace currency for rolling 52-weeks/12-months. The data may not be available for all weeks/months. \| string \|<br>\| DEMAND_TRENDS \| Indicates the demand trends for the recommended item for 52-weeks/12-months. \| string \|<br>**Default**: <code>None</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3GrowthAssortmentRecommendationsTrendsResponse](walmart_apis/models/v3_growth_assortment_recommendations_trends_response.py), [GetAssortmentRecommendationTrendsErrorBody](walmart_apis/errors/get_assortment_recommendation_trends_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3GrowthAssortmentRecommendationsTrendsResponse](walmart_apis/models/v3_growth_assortment_recommendations_trends_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetAssortmentRecommendationTrendsErrorBody](walmart_apis/errors/get_assortment_recommendation_trends_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 500 | <code>[ErrorResponse1](walmart_apis/models/error_response1.py)</code> |
| 403 | <code>[V3Token500Error1](walmart_apis/models/v3_token500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_assortment_recommendation_variants(primary_variant_item_id: str, wm_global_version: WmGlobalVersionOrStr, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, *, next_cursor: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3GrowthAssortmentRecommendationsVariantsResponse, GetAssortmentRecommendationVariantsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

You can fetch variant items corresponding to a recommended primary variant item. <br><b style='color:green;'>Market availability: US only</span></b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.assortment_recommendations.with_raw_response.get_assortment_recommendation_variants(
    "some example string",
    WmGlobalVersion._3_1,
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    next_cursor="*",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3GrowthAssortmentRecommendationsVariantsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAssortmentRecommendationVariantsErrorBody
```

**Async**

```python
result = await async_client.assortment_recommendations.with_raw_response.get_assortment_recommendation_variants(
    "some example string",
    WmGlobalVersion._3_1,
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    next_cursor="*",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3GrowthAssortmentRecommendationsVariantsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAssortmentRecommendationVariantsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>primary_variant_item_id</code> | <code>str</code> | Primary variant item ID that is returned in the response of get recommendations API or in the on-request bulk CSV file. <br><b style='color:green;'>Market availability: US only</span></b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. Required for authenticating requests to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>next_cursor</code> | <code>str \| None</code> | Used for pagination when more than 200 records are retrieved. The nextCursor value of the response includes a marker which needs to be passed in next call which retrieves the next page of results. <br><b style='color:green;'>Market availability: US only</span></b><br>**Default**: <code>None</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3GrowthAssortmentRecommendationsVariantsResponse](walmart_apis/models/v3_growth_assortment_recommendations_variants_response.py), [GetAssortmentRecommendationVariantsErrorBody](walmart_apis/errors/get_assortment_recommendation_variants_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3GrowthAssortmentRecommendationsVariantsResponse](walmart_apis/models/v3_growth_assortment_recommendations_variants_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetAssortmentRecommendationVariantsErrorBody](walmart_apis/errors/get_assortment_recommendation_variants_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 500 | <code>[ErrorResponse1](walmart_apis/models/error_response1.py)</code> |
| 403 | <code>[V3Token500Error1](walmart_apis/models/v3_token500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_assortment_recommendations(wm_global_version: WmGlobalVersionOrStr, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, body: V3GrowthAssortmentRecommendationsRequest | V3GrowthAssortmentRecommendationsRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3GrowthAssortmentRecommendationsResponse, GetAssortmentRecommendationsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

You can fetch the list of recommendations that are recommended for you. 

Using ITEM as a recommendationType,
*   You can get the list of ITEM recommendations. You can apply filters to fetch selective item recommendations. <br><b style='color:green;'>Market availability: US | CA | MX</span></b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.assortment_recommendations.with_raw_response.get_assortment_recommendations(
    WmGlobalVersion._3_1,
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    V3GrowthAssortmentRecommendationsRequest(meta=Meta6(limit=2)),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3GrowthAssortmentRecommendationsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAssortmentRecommendationsErrorBody
```

**Async**

```python
result = await async_client.assortment_recommendations.with_raw_response.get_assortment_recommendations(
    WmGlobalVersion._3_1,
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    V3GrowthAssortmentRecommendationsRequest(meta=Meta6(limit=2)),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3GrowthAssortmentRecommendationsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAssortmentRecommendationsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. Required for authenticating requests to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>body</code> | <code>[V3GrowthAssortmentRecommendationsRequest](walmart_apis/models/v3_growth_assortment_recommendations_request.py) \| [V3GrowthAssortmentRecommendationsRequestDict](walmart_apis/models/v3_growth_assortment_recommendations_request.py)</code> | Request payload |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3GrowthAssortmentRecommendationsResponse](walmart_apis/models/v3_growth_assortment_recommendations_response.py), [GetAssortmentRecommendationsErrorBody](walmart_apis/errors/get_assortment_recommendations_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3GrowthAssortmentRecommendationsResponse](walmart_apis/models/v3_growth_assortment_recommendations_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetAssortmentRecommendationsErrorBody](walmart_apis/errors/get_assortment_recommendations_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 500 | <code>[ErrorResponse1](walmart_apis/models/error_response1.py)</code> |
| 403 | <code>[V3Token500Error1](walmart_apis/models/v3_token500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_categorization_details_of_assortment_recommendations(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3GrowthAssortmentRecommendationsCategorizationCountsRequest | V3GrowthAssortmentRecommendationsCategorizationCountsRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3GrowthAssortmentRecommendationsCategorizationCountsResponse, GetCategorizationDetailsOfAssortmentRecommendationsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

You can get the list of brands or categories associated with the items recommendations that are recommended for you.

Using BRAND as a categorizationType
*   You can get the list of brands sorted by the number of item recommendations associated with it. This is then sorted in lexicographic order of brand name. 

Using CATEGORY as a categorizationType
*   You can get the list of categories sorted by the number of item recommendations associated with it. This is then sorted in lexicographic order of category name. 
<br><b style='color:green;'>Market availability: US | CA | MX</span></b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.assortment_recommendations.with_raw_response.get_categorization_details_of_assortment_recommendations(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3GrowthAssortmentRecommendationsCategorizationCountsRequest(
        categorization_type=CategorizationType3.BRAND, meta=Meta10(limit=2)
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3GrowthAssortmentRecommendationsCategorizationCountsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCategorizationDetailsOfAssortmentRecommendationsErrorBody
```

**Async**

```python
result = await async_client.assortment_recommendations.with_raw_response.get_categorization_details_of_assortment_recommendations(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3GrowthAssortmentRecommendationsCategorizationCountsRequest(
        categorization_type=CategorizationType3.BRAND, meta=Meta10(limit=2)
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3GrowthAssortmentRecommendationsCategorizationCountsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCategorizationDetailsOfAssortmentRecommendationsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. Required for authenticating requests to Walmart Marketplace APIs <br><b style='color:green;'>Market availability: US \| CA \| MX</span></b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID <br><b style='color:green;'>Market availability: US \| CA \| MX</span></b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called <br><b style='color:green;'>Market availability: US \| CA \| MX</span></b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The default is set to 3.1<br><b style='color:green;'>Market availability: US \| CA \| MX</span></b> |
| <code>body</code> | <code>[V3GrowthAssortmentRecommendationsCategorizationCountsRequest](walmart_apis/models/v3_growth_assortment_recommendations_categorization_counts_request.py) \| [V3GrowthAssortmentRecommendationsCategorizationCountsRequestDict](walmart_apis/models/v3_growth_assortment_recommendations_categorization_counts_request.py)</code> | Request payload |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel <br><b style='color:green;'>Market availability: US \| CA \| MX</span></b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3GrowthAssortmentRecommendationsCategorizationCountsResponse](walmart_apis/models/v3_growth_assortment_recommendations_categorization_counts_response.py), [GetCategorizationDetailsOfAssortmentRecommendationsErrorBody](walmart_apis/errors/get_categorization_details_of_assortment_recommendations_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3GrowthAssortmentRecommendationsCategorizationCountsResponse](walmart_apis/models/v3_growth_assortment_recommendations_categorization_counts_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetCategorizationDetailsOfAssortmentRecommendationsErrorBody](walmart_apis/errors/get_categorization_details_of_assortment_recommendations_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 500 | <code>[ErrorResponse1](walmart_apis/models/error_response1.py)</code> |
| 403 | <code>[V3Token500Error1](walmart_apis/models/v3_token500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def reject_assortment_recommendations(wm_global_version: WmGlobalVersionOrStr, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, body: V3GrowthAssortmentRecommendationsRejectionsRequest | V3GrowthAssortmentRecommendationsRejectionsRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3GrowthAssortmentRecommendationsRejectionsResponse, RejectAssortmentRecommendationsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

You can reject a list of recommendations that are recommended for you. 

Using ITEM as a recommendationType,
*   You can reject specific item recommendations using the filterCriteria or by providing the list of itemRecommendationUniqueIds. 
*   You will need to provide valid rejection code(s) while submitting the reject request. You are required to send the custom rejection message if the rejection code is OTHER_REASON
<br><b style='color:green;'>Market availability: US | CA | MX</span></b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.assortment_recommendations.with_raw_response.reject_assortment_recommendations(
    WmGlobalVersion._3_1,
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    V3GrowthAssortmentRecommendationsRejectionsRequest(rejection_codes=RejectionCodes1.NOT_SELLING_THESE_ITEMS),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3GrowthAssortmentRecommendationsRejectionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RejectAssortmentRecommendationsErrorBody
```

**Async**

```python
result = await async_client.assortment_recommendations.with_raw_response.reject_assortment_recommendations(
    WmGlobalVersion._3_1,
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    V3GrowthAssortmentRecommendationsRejectionsRequest(rejection_codes=RejectionCodes1.NOT_SELLING_THESE_ITEMS),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3GrowthAssortmentRecommendationsRejectionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RejectAssortmentRecommendationsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. Required for authenticating requests to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>body</code> | <code>[V3GrowthAssortmentRecommendationsRejectionsRequest](walmart_apis/models/v3_growth_assortment_recommendations_rejections_request.py) \| [V3GrowthAssortmentRecommendationsRejectionsRequestDict](walmart_apis/models/v3_growth_assortment_recommendations_rejections_request.py)</code> | Request payload |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3GrowthAssortmentRecommendationsRejectionsResponse](walmart_apis/models/v3_growth_assortment_recommendations_rejections_response.py), [RejectAssortmentRecommendationsErrorBody](walmart_apis/errors/reject_assortment_recommendations_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3GrowthAssortmentRecommendationsRejectionsResponse](walmart_apis/models/v3_growth_assortment_recommendations_rejections_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RejectAssortmentRecommendationsErrorBody](walmart_apis/errors/reject_assortment_recommendations_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 500 | <code>[ErrorResponse1](walmart_apis/models/error_response1.py)</code> |
| 403 | <code>[V3Token500Error1](walmart_apis/models/v3_token500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Authorization

> Source: [Authorization](walmart_apis/apis/authorization.py)

<details>
<summary><code>def get_token_detail(wm_sec_access_token: str, wm_market: str, content_type: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TokenDetailResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This process retrieves the access permissions granted by sellers to applications in the context of OAuth 2.0. The scope encompasses various API categories, each with its respective access levels, for example Reports: View Only, Item: Full Access, etc.
<br><b style='color:green;'>Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.authorization.with_raw_response.get_token_detail(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "us, mx, ca or cl",
    "application/x-www-form-urlencoded",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TokenDetailResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.authorization.with_raw_response.get_token_detail(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "us, mx, ca or cl",
    "application/x-www-form-urlencoded",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TokenDetailResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_sec_access_token</code> | <code>str</code> | The access token retrieved in the Token API call <br><br><strong style="color: green;">**Market availability: Global**</strong> |
| <code>wm_market</code> | <code>str</code> | Available marketplace location: us (USA), mx (Mexico), ca (Canada) or cl (Chile)<br><br><strong style="color: green;">**Market availability: Global**</strong> |
| <code>content_type</code> | <code>str</code> | Content type of the request body. <br><br><strong style="color: green;">**Market availability: Global**</strong> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID <br><br><strong style="color: green;">**Market availability: Global**</strong> |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name <br><br><strong style="color: green;">**Market availability: Global**</strong> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding. <br><br><strong style="color: green;">**Market availability: Global**</strong><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[TokenDetailResponse](walmart_apis/models/token_detail_response.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TokenDetailResponse](walmart_apis/models/token_detail_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def token_api(wm_market: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_partner_id: str | None = None, wm_consumer_channel_type: str | None = None, grant_type: GrantType1OrStr = GrantType1.CLIENT_CREDENTIALS, code: str | None = None, redirect_uri: str | None = None, refresh_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[OauthTokenModel, TokenApiErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>This endpoint issues access tokens required for authenticating API requests. It supports multiple OAuth 2.0 grant types to accommodate various integration scenarios.</p> <b style='color:green;'>Market availability: Global</b><br/><h3>Supported Grant Types</h3><table><tr><th>Grant Type</th><th>Description</th><th>How to get the credentials</th></tr><tr><td>authorization_code</td><td>Exchanges an authorization code for an access token.</td><td>Used in app integration only via the OAuth consent screen. This is applicable to the <strong>US market only</strong>. Refer to <a href=/global-marketplace/docs/oauth-20-authorization>OAuth 2.0 authorization</a> for more details.</td></tr><tr><td>client_credentials</td><td>Issues a token using client ID and secret.</td><td>For <strong>sellers</strong>: Obtain client_id and client_secret from the <strong>Developer Portal</strong>.<br/>For <strong>solution providers</strong>: Obtain credentials from sellers via <a href=/global-marketplace/docs/delegated-access-auth>Delegated Access authorization</a>.</td></tr><tr><td>refresh_token</td><td>Issues a new access token using a refresh token.</td><td>Provided during the authorization_code flow. This is applicable to the <strong>US market only</strong>. Refer to <a href=/global-marketplace/docs/oauth-20-authorization>OAuth 2.0 authorization</a> for more details.</td></tr></table><br/><b>Note:<br/></b> Use authorization_code and refresh_token <b>only for app-based integrations.</b> These grant types are currently <b>supported only in the US market</b>.<br/><br/><h3>Token Lifetimes</h3><table><tr><th>Token Type</th><th>Duration</th></tr><tr><td>Access Token</td><td>15 minutes <i>(900 seconds)</i></td></tr><tr><td>Refresh Token</td><td>1 year <i>(365 days)</i></td></tr></table>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.authorization.with_raw_response.token_api(
    "us, mx, ca or cl",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    wm_partner_id="43423324",
    grant_type=GrantType1.CLIENT_CREDENTIALS,
    code="65CA5DA313A549D49D15D3119D9AD85D",
    redirect_uri="https://example-client-app.com",
    refresh_token="APXcIoTpKMH9OQN.....",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type OauthTokenModel
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TokenApiErrorBody
```

**Async**

```python
result = await async_client.authorization.with_raw_response.token_api(
    "us, mx, ca or cl",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    wm_partner_id="43423324",
    grant_type=GrantType1.CLIENT_CREDENTIALS,
    code="65CA5DA313A549D49D15D3119D9AD85D",
    redirect_uri="https://example-client-app.com",
    refresh_token="APXcIoTpKMH9OQN.....",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type OauthTokenModel
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TokenApiErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_market</code> | <code>str</code> | Available marketplace location: us (USA), mx (Mexico), ca (Canada) or cl (Chile)<br><br><strong style="color: green;">**Market availability: Global**</strong> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID <br><br><strong style="color: green;">**Market availability: Global**</strong> |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name <br><br><strong style="color: green;">**Market availability: Global**</strong> |
| <code>wm_partner_id</code> | <code>str \| None</code> | Partner Id registered in Walmart marketplace to identify a seller. <br /> This field is required when **grant_type: authorization_code** and **grant_type: refresh_token** <br><br><strong style="color: green;">**Market availability: Global**</strong><br>**Default**: <code>None</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding. <br><br><strong style="color: green;">**Market availability: Global**</strong><br>**Default**: <code>None</code> |
| <code>grant_type</code> | <code>[GrantType1OrStr](walmart_apis/models/enums/grant_type1.py)</code> | Type of grant requested. <br /> **Available grant types:** authorization_code, refresh_token and client_credentials <br><br><strong style="color: green;">**Market availability: Global**</strong><br>**Default**: <code>GrantType1.CLIENT_CREDENTIALS</code> |
| <code>code</code> | <code>str \| None</code> | Authorization code obtained by your client app when the seller authorizes your app to access the seller resource. <br /> This field is required when **grant_type: authorization_code** <br><br><strong style="color: green;">**Market availability: Global**</strong><br>**Default**: <code>None</code> |
| <code>redirect_uri</code> | <code>str \| None</code> | This should be same as one of your client app URIs provided while registering the app. <br /> This field is required when **grant_type: authorization_code** <br><br><strong style="color: green;">**Market availability: Global**</strong><br>**Default**: <code>None</code> |
| <code>refresh_token</code> | <code>str \| None</code> | Refresh token received as response of Authentication API with authorization_code grant type, to be used to refresh the access token. The token lifetime is 1 year. <br><br><strong style="color: green;">**Market availability: Global**</strong><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[OauthTokenModel](walmart_apis/models/oauth_token_model.py), [TokenApiErrorBody](walmart_apis/errors/token_api_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[OauthTokenModel](walmart_apis/models/oauth_token_model.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[TokenApiErrorBody](walmart_apis/errors/token_api_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V3Token400Error1](walmart_apis/models/v3_token400_error1.py)</code> |
| 401 | <code>[V3Token401Error1](walmart_apis/models/v3_token401_error1.py)</code> |
| 500 | <code>[V3Token500Error1](walmart_apis/models/v3_token500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Disputes

> Source: [Disputes](walmart_apis/apis/disputes.py)

<details>
<summary><code>def post_contest(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3ItemsDisputeDuplicatesContestRequest | V3ItemsDisputeDuplicatesContestRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DisputeContestResponses, PostContestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use this API to submit dispute for up to 100 items at a time.

We need to pass `productId`, and `productIdType` in the body for creating a dispute. 

*   POST {{url}}/v3/items/dispute/duplicates/contest 
<br><b style='color:green;'>Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.disputes.with_raw_response.post_contest(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3ItemsDisputeDuplicatesContestRequest(issues=[Issues1()]),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DisputeContestResponses
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostContestErrorBody
```

**Async**

```python
result = await async_client.disputes.with_raw_response.post_contest(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3ItemsDisputeDuplicatesContestRequest(issues=[Issues1()]),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DisputeContestResponses
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostContestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. Required for authenticating requests to Walmart Marketplace APIs.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>body</code> | <code>[V3ItemsDisputeDuplicatesContestRequest](walmart_apis/models/v3_items_dispute_duplicates_contest_request.py) \| [V3ItemsDisputeDuplicatesContestRequestDict](walmart_apis/models/v3_items_dispute_duplicates_contest_request.py)</code> | Required fields for the dispute. |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[DisputeContestResponses](walmart_apis/models/dispute_contest_responses.py), [PostContestErrorBody](walmart_apis/errors/post_contest_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DisputeContestResponses](walmart_apis/models/dispute_contest_responses.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[PostContestErrorBody](walmart_apis/errors/post_contest_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[V3ItemsDisputeDuplicatesContest403Error1](walmart_apis/models/v3_items_dispute_duplicates_contest403_error1.py)</code> |
| 404 | <code>[V3ItemsDisputeDuplicatesContest404Error1](walmart_apis/models/v3_items_dispute_duplicates_contest404_error1.py)</code> |
| 500 | <code>[V3ItemsDisputeDuplicatesContest500Error1](walmart_apis/models/v3_items_dispute_duplicates_contest500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def post_status(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3ItemsDisputeDuplicatesStatusRequest | V3ItemsDisputeDuplicatesStatusRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3ItemsDisputeDuplicatesStatusResponse, PostStatusErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use this API to retrieve the status of up to 100 disputed items at a time.

We need to pass `productId`, and `productIdType` in the body for creating a dispute. 

*   POST {{url}}/v3/items/dispute/duplicates/status 

Responses will be based on the item status: 

* 404: No item Response 

* 200: Response received for all items 

* 206: Partial response received 

An Item can be in 4 different stages: 
* `IN_REVIEW`, `IS_DUPLICATE`, `ERROR`, `NOT_DUPLICATE` 
<br><b style='color:green;'>Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.disputes.with_raw_response.post_status(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3ItemsDisputeDuplicatesStatusRequest(issues=[Issues1()]),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ItemsDisputeDuplicatesStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostStatusErrorBody
```

**Async**

```python
result = await async_client.disputes.with_raw_response.post_status(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3ItemsDisputeDuplicatesStatusRequest(issues=[Issues1()]),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ItemsDisputeDuplicatesStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. Required for authenticating requests to Walmart Marketplace APIs.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>body</code> | <code>[V3ItemsDisputeDuplicatesStatusRequest](walmart_apis/models/v3_items_dispute_duplicates_status_request.py) \| [V3ItemsDisputeDuplicatesStatusRequestDict](walmart_apis/models/v3_items_dispute_duplicates_status_request.py)</code> | Required fields for the dispute. |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3ItemsDisputeDuplicatesStatusResponse](walmart_apis/models/v3_items_dispute_duplicates_status_response.py), [PostStatusErrorBody](walmart_apis/errors/post_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3ItemsDisputeDuplicatesStatusResponse](walmart_apis/models/v3_items_dispute_duplicates_status_response.py)</code> -- Response received for all the items.

**On `Failure`**: `error` is <code>[PostStatusErrorBody](walmart_apis/errors/post_status_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[V3ItemsDisputeDuplicatesStatus403Error1](walmart_apis/models/v3_items_dispute_duplicates_status403_error1.py)</code> |
| 404 | <code>[V3ItemsDisputeDuplicatesStatus404Error1](walmart_apis/models/v3_items_dispute_duplicates_status404_error1.py)</code> |
| 500 | <code>[V3ItemsDisputeDuplicatesStatus500Error1](walmart_apis/models/v3_items_dispute_duplicates_status500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## FeedsApi

> Source: [FeedsApi](walmart_apis/apis/feeds_api.py)

<details>
<summary><code>def get_all_feed_statuses(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, feed_id: str | None = None, feed_type: str | None = None, feed_status: FeedStatus1OrStr | None = None, offset: str | None = "0", limit: str | None = "50", wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FeedRecordResponse, GetAllFeedStatusesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API returns the feed statuses for all the specified feed IDs. Use the specified feedTypes to query the status of each feed and identify whether it was processed successfully, failed, or is still in progress. 

| FeedTypes | Availability |
|--------|----------|
| MP_MAINTENANCE, MP_ITEM_MATCH, LAGTIME | Global |
| MP_INVENTORY, SKU_TEMPLATE_MAP | US, CA, MX |
| MP_ITEM_INTL | CA, MX, CL |
| MP_ITEM, MP_WFS_ITEM, WALMART_FUNDED_INCENTIVES_ENROLLMENT, INCENTIVE_ENROLLMENT,PRICE_AND_PROMOTION | US Only |
| OMNI_WFS, RETIRE_ITEM, SHIPPING_OVERRIDES, FITMENT_ACES, FITMENT_PIES, SPLIT_AND_MERGE | US Only |
| OMNI_WFSSETUP, OMNI_WFSCONVERT | CA, MX | 

<br><b style='color:green;'>Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.feeds_api.with_raw_response.get_all_feed_statuses(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket1.US, WmGlobalVersion._3_1
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FeedRecordResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAllFeedStatusesErrorBody
```

**Async**

```python
result = await async_client.feeds_api.with_raw_response.get_all_feed_statuses(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket1.US, WmGlobalVersion._3_1
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FeedRecordResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAllFeedStatusesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | The target market of the API call.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>feed_id</code> | <code>str \| None</code> | A unique ID returned from the Bulk Upload API, used for tracking the Feed File. Special characters must be escaped. (e.g., feedId: '...3456@789...' must be entered in the URL as '...3456%40789).<br><br><strong style="color: green;">**Market availability: Global**</strong><br>**Default**: <code>None</code> |
| <code>feed_type</code> | <code>str \| None</code> | The feedType parameter defines the type of feed whose status you are querying. Feed types are specific to each market, so be sure to provide a value that is supported for your target market. <br><br><strong style="color: green;">**Market availability: Global**</strong><br>**Default**: <code>None</code> |
| <code>feed_status</code> | <code>[FeedStatus1OrStr](walmart_apis/models/enums/feed_status1.py) \| None</code> | Status of the feed.<br><br><strong style="color: green;">**Market availability: Global**</strong><br>**Default**: <code>None</code> |
| <code>offset</code> | <code>str \| None</code> | The object response to start with, where 0 is the first entity that can be requested. <br><br><strong style="color: green;">**Market availability: Global**</strong><br>**Default**: <code>"0"</code> |
| <code>limit</code> | <code>str \| None</code> | The number of entities to be returned. It cannot be more than 50 entities.<br><strong style="color: green;">**Market availability: Global**</strong><br>**Default**: <code>"50"</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[FeedRecordResponse](walmart_apis/models/feed_record_response.py), [GetAllFeedStatusesErrorBody](walmart_apis/errors/get_all_feed_statuses_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FeedRecordResponse](walmart_apis/models/feed_record_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetAllFeedStatusesErrorBody](walmart_apis/errors/get_all_feed_statuses_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404, 500 | <code>[FeedRecordResponse](walmart_apis/models/feed_record_response.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_feed_error_report(feed_id: str, feed_type: FeedTypeOrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FileResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Feed Error Report API allows you to download a detailed error report for a submitted feed. 

Currently the API supports error report download for the following feeds: 
*   FITMENT_ACES 
*   FITMENT_PIES 

 This API returns a zipped .csv file, which contains line item level detailed error messages. For details and a sample, please refer to the guide section link below. 
<br><b style='color:green;'>Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.feeds_api.with_raw_response.get_feed_error_report(
    "some example string",
    FeedType.FITMENT_ACES,
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.feeds_api.with_raw_response.get_feed_error_report(
    "some example string",
    FeedType.FITMENT_ACES,
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AsyncFileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>feed_id</code> | <code>str</code> | Feed Id of the feed.<br><br><strong style="color: green;">**Market availability: US only**</strong> |
| <code>feed_type</code> | <code>[FeedTypeOrStr](walmart_apis/models/enums/feed_type.py)</code> | Feed type for which Error Report needs to be downloaded.<br><br><strong style="color: green;">**Market availability: US only**</strong> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | The target market of the API call.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;FileResponse, [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>FileResponse</code>, its body not yet read -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_feed_item_status(feed_id: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, include_details: str | None = "false", offset: str | None = "0", limit: str | None = "50", wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3FeedsResponse1, GetFeedItemStatusErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the feed and item status for a specified Feed ID.
<br><b style='color:green;'>Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.feeds_api.with_raw_response.get_feed_item_status(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3FeedsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetFeedItemStatusErrorBody
```

**Async**

```python
result = await async_client.feeds_api.with_raw_response.get_feed_item_status(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3FeedsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetFeedItemStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>feed_id</code> | <code>str</code> | A unique ID returned from the Bulk Upload API, used for tracking the Feed File. Special characters must be escaped. (e.g., feedId: '...3456@789...' must be entered in the URL as '...3456%40789).<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | The target market of the API call.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>include_details</code> | <code>str \| None</code> | Includes details for each entity in the feed. When set to true, returns detailed information about each item in the feed, including individual success or failure statuses and any specific error messages. Defaults to false, which returns only high-level feed status. <br><br><strong style="color: green;">**Market availability: Global**</strong><br>**Default**: <code>"false"</code> |
| <code>offset</code> | <code>str \| None</code> | The object response to start with, where 0 is the first entity that can be requested. Use only when `includeDetails` is set to true.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>"0"</code> |
| <code>limit</code> | <code>str \| None</code> | The number of entities to be returned. It cannot be more than 50 entities. Use only when `includeDetails` is set to true.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>"50"</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3FeedsResponse1](walmart_apis/models/v3_feeds_response1.py), [GetFeedItemStatusErrorBody](walmart_apis/errors/get_feed_item_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3FeedsResponse1](walmart_apis/models/v3_feeds_response1.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetFeedItemStatusErrorBody](walmart_apis/errors/get_feed_item_status_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[V3Feeds404Error21](walmart_apis/models/v3_feeds404_error21.py)</code> |
| 500 | <code>[V3Feeds500Error21](walmart_apis/models/v3_feeds500_error21.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## InsightApi

> Source: [InsightApi](walmart_apis/apis/insight_api.py)

<details>
<summary><code>def get_categories_list(wm_global_version: WmGlobalVersionOrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, *, view_trending_items: bool | None = True, wfs_flag: bool | None = None, has_issue: int | None = 0, type_: Type3OrStr | None = None, in_demand_indicator: bool | None = None, limit: int | None = None, offset: int | None = 0, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3InsightsItemsListingQualityCountResponse, GetCategoriesListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of all item categories that have items with listing quality issues or brands for a seller.<br><b style='color:green;'>Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.insight_api.with_raw_response.get_categories_list(
    WmGlobalVersion._3_1, "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket1.US
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3InsightsItemsListingQualityCountResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCategoriesListErrorBody
```

**Async**

```python
result = await async_client.insight_api.with_raw_response.get_categories_list(
    WmGlobalVersion._3_1, "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket1.US
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3InsightsItemsListingQualityCountResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCategoriesListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>view_trending_items</code> | <code>bool \| None</code> | Specify whether or not to include seller's items that are trending in the Listing Quality Score.<br><b style='color:green;'>Market availability: US only</b><br>**Default**: <code>True</code> |
| <code>wfs_flag</code> | <code>bool \| None</code> | Specify whether or not to include WFS-eligible items in the overall Listing Quality Score.<br><b style='color:green;'>Market availability: US only</b><br>**Default**: <code>None</code> |
| <code>has_issue</code> | <code>int \| None</code> | Specify whether or not to include items that have issues in the Listing Quality Score.<br><b style='color:green;'>Market availability: US only</b><br>**Default**: <code>0</code> |
| <code>type_</code> | <code>[Type3OrStr](walmart_apis/models/enums/type3.py) \| None</code> | Specify whether to get item count by brand or category.If not specified, category is the default value.<br><b style='color:green;'>Market availability: US only</b><br>**Default**: <code>None</code> |
| <code>in_demand_indicator</code> | <code>bool \| None</code> | Specify whether to get item count by customer favorite.<br><b style='color:green;'>Market availability: US only</b><br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Specify the number of items to return. The default is 100, with a maximum value of 1000..<br><b style='color:green;'>Market availability: US only</b><br>**Default**: <code>None</code> |
| <code>offset</code> | <code>int \| None</code> | Specify the offset of item list to be returned.<br><b style='color:green;'>Market availability: US only</b><br>**Default**: <code>0</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3InsightsItemsListingQualityCountResponse](walmart_apis/models/v3_insights_items_listing_quality_count_response.py), [GetCategoriesListErrorBody](walmart_apis/errors/get_categories_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3InsightsItemsListingQualityCountResponse](walmart_apis/models/v3_insights_items_listing_quality_count_response.py)</code> -- Successful Operation<br><b style='color:green;'>Market availability: US only</b>

**On `Failure`**: `error` is <code>[GetCategoriesListErrorBody](walmart_apis/errors/get_categories_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V3InsightsItemsListingQualityCount400Error1](walmart_apis/models/v3_insights_items_listing_quality_count400_error1.py)</code> |
| 401, 403 | <code>[V3Token400Error1](walmart_apis/models/v3_token400_error1.py)</code> |
| 500 | <code>[V3InsightsItemsListingQualityCount500Error1](walmart_apis/models/v3_insights_items_listing_quality_count500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_listing_quality_score(wm_global_version: WmGlobalVersionOrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, *, view_trending_items: bool | None = None, wfs_flag: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3InsightsItemsListingQualityScoreResponse, GetListingQualityScoreErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the total Listing Quality Score for a seller's entire item catalog.<br><b style='color:green;'>Market availability: US | CA | MX</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.insight_api.with_raw_response.get_listing_quality_score(
    WmGlobalVersion._3_1, "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket1.US
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3InsightsItemsListingQualityScoreResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetListingQualityScoreErrorBody
```

**Async**

```python
result = await async_client.insight_api.with_raw_response.get_listing_quality_score(
    WmGlobalVersion._3_1, "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket1.US
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3InsightsItemsListingQualityScoreResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetListingQualityScoreErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The value must be set to 3.1.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>view_trending_items</code> | <code>bool \| None</code> | Specify whether or not to include seller's items that are trending in the Listing Quality Score.<br><b style='color:green;'>Market availability: US \| CA \| MX</b><br>**Default**: <code>None</code> |
| <code>wfs_flag</code> | <code>str \| None</code> | Specify whether or not to include WFS-eligible items in the overall Listing Quality Score.<br><b style='color:green;'>Market availability: US \| CA \| MX</b><br>**Default**: <code>None</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3InsightsItemsListingQualityScoreResponse](walmart_apis/models/v3_insights_items_listing_quality_score_response.py), [GetListingQualityScoreErrorBody](walmart_apis/errors/get_listing_quality_score_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3InsightsItemsListingQualityScoreResponse](walmart_apis/models/v3_insights_items_listing_quality_score_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetListingQualityScoreErrorBody](walmart_apis/errors/get_listing_quality_score_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V3InsightsItemsListingQualityScore400Error1](walmart_apis/models/v3_insights_items_listing_quality_score400_error1.py)</code> |
| 401, 403 | <code>[V3Token400Error1](walmart_apis/models/v3_token400_error1.py)</code> |
| 500 | <code>[V3InsightsItemsListingQualityScore500Error1](walmart_apis/models/v3_insights_items_listing_quality_score500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_pro_seller_badge_info(wm_global_version: WmGlobalVersionOrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3InsightsProsellerbadgeResponse, GetProSellerBadgeInfoErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The Pro Seller badge status will provide you with information regarding your current badge status as well as the progress you've made in meeting the criteria.<br><b style='color:green;'>Market availability: MX only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.insight_api.with_raw_response.get_pro_seller_badge_info(
    WmGlobalVersion._3_1, "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket1.US
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3InsightsProsellerbadgeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetProSellerBadgeInfoErrorBody
```

**Async**

```python
result = await async_client.insight_api.with_raw_response.get_pro_seller_badge_info(
    WmGlobalVersion._3_1, "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket1.US
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3InsightsProsellerbadgeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetProSellerBadgeInfoErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3InsightsProsellerbadgeResponse](walmart_apis/models/v3_insights_prosellerbadge_response.py), [GetProSellerBadgeInfoErrorBody](walmart_apis/errors/get_pro_seller_badge_info_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3InsightsProsellerbadgeResponse](walmart_apis/models/v3_insights_prosellerbadge_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetProSellerBadgeInfoErrorBody](walmart_apis/errors/get_pro_seller_badge_info_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V3InsightsProsellerbadge400Error1](walmart_apis/models/v3_insights_prosellerbadge400_error1.py)</code> |
| 401, 403 | <code>[V3Token400Error1](walmart_apis/models/v3_token400_error1.py)</code> |
| 500 | <code>[V3InsightsProsellerbadge500Error1](walmart_apis/models/v3_insights_prosellerbadge500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_seller_incentives_info(wm_global_version: WmGlobalVersionOrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3InsightsSellerIncentivesResponse, GetSellerIncentivesInfoErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The Pro Seller Tier and Rewards Status API allows you to check your seller’s current tier status within the Pro Seller program, a three-tier incentive structure consisting of Rising, Advanced, and Pro Seller levels in US and a single-tier i.e Pro Seller in CA.<br><b style='color:green;'>Market availability: US | CA</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.insight_api.with_raw_response.get_seller_incentives_info(
    WmGlobalVersion._3_1, "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket1.US
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3InsightsSellerIncentivesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSellerIncentivesInfoErrorBody
```

**Async**

```python
result = await async_client.insight_api.with_raw_response.get_seller_incentives_info(
    WmGlobalVersion._3_1, "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket1.US
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3InsightsSellerIncentivesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSellerIncentivesInfoErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3InsightsSellerIncentivesResponse](walmart_apis/models/v3_insights_seller_incentives_response.py), [GetSellerIncentivesInfoErrorBody](walmart_apis/errors/get_seller_incentives_info_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3InsightsSellerIncentivesResponse](walmart_apis/models/v3_insights_seller_incentives_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetSellerIncentivesInfoErrorBody](walmart_apis/errors/get_seller_incentives_info_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 403 | <code>[V3Token400Error1](walmart_apis/models/v3_token400_error1.py)</code> |
| 500 | <code>[V3InsightsSellerIncentives500Error1](walmart_apis/models/v3_insights_seller_incentives500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_unpublished_item_count(from_date: str, wm_global_version: WmGlobalVersionOrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3InsightsItemsUnpublishedCountsResponse, GetUnpublishedItemCountErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API allows you to get the count of unpublished items.<br><b style='color:green;'>Market availability: US | CA | MX</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.insight_api.with_raw_response.get_unpublished_item_count(
    "2020-09-23", WmGlobalVersion._3_1, "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket1.US
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3InsightsItemsUnpublishedCountsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetUnpublishedItemCountErrorBody
```

**Async**

```python
result = await async_client.insight_api.with_raw_response.get_unpublished_item_count(
    "2020-09-23", WmGlobalVersion._3_1, "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket1.US
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3InsightsItemsUnpublishedCountsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetUnpublishedItemCountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>from_date</code> | <code>str</code> | Returns all unpublished items count with reason codes since the given date period<br><b style='color:green;'>Market availability: US \| CA \| MX</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3InsightsItemsUnpublishedCountsResponse](walmart_apis/models/v3_insights_items_unpublished_counts_response.py), [GetUnpublishedItemCountErrorBody](walmart_apis/errors/get_unpublished_item_count_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3InsightsItemsUnpublishedCountsResponse](walmart_apis/models/v3_insights_items_unpublished_counts_response.py)</code> -- Successful Operation<br><b style='color:green;'>Market availability: US | CA | MX</b>

**On `Failure`**: `error` is <code>[GetUnpublishedItemCountErrorBody](walmart_apis/errors/get_unpublished_item_count_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 403 | <code>[V3Token400Error1](walmart_apis/models/v3_token400_error1.py)</code> |
| 500 | <code>[V3InsightsItemsUnpublishedCounts500Error1](walmart_apis/models/v3_insights_items_unpublished_counts500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_unpublished_items(from_date: str, wm_global_version: WmGlobalVersionOrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, *, unpublished_reason_code: str | None = "all", limit: str | None = "20", offer_lifecycle_status: str | None = "all", market_trending: str | None = "true", items_with_inventory: str | None = "true", is_customer_favorite: bool | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3InsightsItemsUnpublishedItemsResponse, GetUnpublishedItemsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Unpublished Items<br><b style='color:green;'>Market availability: US | CA | MX</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.insight_api.with_raw_response.get_unpublished_items(
    "2020-09-23", WmGlobalVersion._3_1, "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket1.US
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3InsightsItemsUnpublishedItemsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetUnpublishedItemsErrorBody
```

**Async**

```python
result = await async_client.insight_api.with_raw_response.get_unpublished_items(
    "2020-09-23", WmGlobalVersion._3_1, "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket1.US
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3InsightsItemsUnpublishedItemsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetUnpublishedItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>from_date</code> | <code>str</code> | Returns all unpublished items since the given date<br><b style='color:green;'>Market availability: US \| CA \| MX</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>unpublished_reason_code</code> | <code>str \| None</code> | Unpublished reason code<br><b style='color:green;'>Market availability: US \| CA \| MX</b><br>**Default**: <code>"all"</code> |
| <code>limit</code> | <code>str \| None</code> | The number of items to be returned.<br><b style='color:green;'>Market availability: US \| CA \| MX</b><br>**Default**: <code>"20"</code> |
| <code>offer_lifecycle_status</code> | <code>str \| None</code> | The lifecycle status of an item describes where the item listing is in the overall lifecycle. Examples of allowed values are ACTIVE , ARCHIVED, RETIRED.<br><b style='color:green;'>Market availability: US \| CA \| MX</b><br>**Default**: <code>"all"</code> |
| <code>market_trending</code> | <code>str \| None</code> | Filter the item list to return only items that are trending on Walmart.com<br><b style='color:green;'>Market availability: US \| CA \| MX</b><br>**Default**: <code>"true"</code> |
| <code>items_with_inventory</code> | <code>str \| None</code> | Filter the item list to return only items that have inventory<br><b style='color:green;'>Market availability: US \| CA \| MX</b><br>**Default**: <code>"true"</code> |
| <code>is_customer_favorite</code> | <code>bool \| None</code> | Filters items by customer favorite status. When set to `true`, only customer favorites are returned. When set to `false`, only non-favorites are returned. If omitted, all items are returned.<br><b style='color:green;'>Market availability: US only</b><br>**Default**: <code>None</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3InsightsItemsUnpublishedItemsResponse](walmart_apis/models/v3_insights_items_unpublished_items_response.py), [GetUnpublishedItemsErrorBody](walmart_apis/errors/get_unpublished_items_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3InsightsItemsUnpublishedItemsResponse](walmart_apis/models/v3_insights_items_unpublished_items_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetUnpublishedItemsErrorBody](walmart_apis/errors/get_unpublished_items_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403 | <code>[V3Token400Error1](walmart_apis/models/v3_token400_error1.py)</code> |
| 500 | <code>[V3InsightsItemsUnpublishedItems500Error1](walmart_apis/models/v3_insights_items_unpublished_items500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def items_details_for_listing(wm_global_version: WmGlobalVersionOrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, body: V3InsightsItemsListingQualityItemsRequest | V3InsightsItemsListingQualityItemsRequestDict, *, limit: str | None = "200", next_cursor: str | None = None, offset: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3InsightsItemsListingQualityItemsResponse, ItemsDetailsForListingErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get each item's listing quality details including: item quality score, offer score, content score and issues, and item performance.<br><b style='color:green;'>Market availability: US | CA | MX</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.insight_api.with_raw_response.items_details_for_listing(
    WmGlobalVersion._3_1,
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    V3InsightsItemsListingQualityItemsRequest(query=Query1(field=Field41.SKU, value="WB 433KP412-12")),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3InsightsItemsListingQualityItemsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ItemsDetailsForListingErrorBody
```

**Async**

```python
result = await async_client.insight_api.with_raw_response.items_details_for_listing(
    WmGlobalVersion._3_1,
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    V3InsightsItemsListingQualityItemsRequest(query=Query1(field=Field41.SKU, value="WB 433KP412-12")),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3InsightsItemsListingQualityItemsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ItemsDetailsForListingErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>body</code> | <code>[V3InsightsItemsListingQualityItemsRequest](walmart_apis/models/v3_insights_items_listing_quality_items_request.py) \| [V3InsightsItemsListingQualityItemsRequestDict](walmart_apis/models/v3_insights_items_listing_quality_items_request.py)</code> | Request payload |
| <code>limit</code> | <code>str \| None</code> | Specify number of items to return. If no limit is specified, API returns 200 items by default.<br><b style='color:green;'>Market availability: US \| CA \| MX</b><br>**Default**: <code>"200"</code> |
| <code>next_cursor</code> | <code>str \| None</code> | Specify pagination for long list of items.<br><b style='color:green;'>Market availability: US only</b><br>**Default**: <code>None</code> |
| <code>offset</code> | <code>str \| None</code> | Specify pagination for long list of items.<br><b style='color:green;'>Market availability: CA \| MX</b><br>**Default**: <code>None</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3InsightsItemsListingQualityItemsResponse](walmart_apis/models/v3_insights_items_listing_quality_items_response.py), [ItemsDetailsForListingErrorBody](walmart_apis/errors/items_details_for_listing_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3InsightsItemsListingQualityItemsResponse](walmart_apis/models/v3_insights_items_listing_quality_items_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[ItemsDetailsForListingErrorBody](walmart_apis/errors/items_details_for_listing_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 403 | <code>[V3Token400Error1](walmart_apis/models/v3_token400_error1.py)</code> |
| 500 | <code>[V3InsightsItemsListingQualityItems500Error1](walmart_apis/models/v3_insights_items_listing_quality_items500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## InventoryApi

> Source: [InventoryApi](walmart_apis/apis/inventory_api.py)

<details>
<summary><code>def get_inventory(sku: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, ship_node: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Inventory1, GetInventoryErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

You can use this API to get the inventory for a given item.
<br><b style='color:green;'>Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory_api.with_raw_response.get_inventory(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Inventory1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetInventoryErrorBody
```

**Async**

```python
result = await async_client.inventory_api.with_raw_response.get_inventory(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Inventory1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetInventoryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sku</code> | <code>str</code> | An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’, '{', '}' as well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't need to be encoded.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | The target market of the API call.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>ship_node</code> | <code>str \| None</code> | The shipNode for which the inventory is requested. <br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[Inventory1](walmart_apis/models/inventory1.py), [GetInventoryErrorBody](walmart_apis/errors/get_inventory_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Inventory1](walmart_apis/models/inventory1.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetInventoryErrorBody](walmart_apis/errors/get_inventory_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 404 | <code>[Inventory1](walmart_apis/models/inventory1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_multi_node_inventory_for_all_sku_and_all_ship_nodes(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, limit: str | None = "10", next_cursor: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[MultiNodeInventoryFetchResponseDto, GetMultiNodeInventoryForAllSkuAndAllShipNodesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API will retrieve the inventory count for all of a seller's items across all ship nodes by item to ship node mapping. Inventory can be zero or non-zero. Please note that NextCursor value changes and it needs to be passed on from the previous call to next call.
<br><b style='color:green;'>Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory_api.with_raw_response.get_multi_node_inventory_for_all_sku_and_all_ship_nodes(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket1.US, WmGlobalVersion._3_1
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MultiNodeInventoryFetchResponseDto
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMultiNodeInventoryForAllSkuAndAllShipNodesErrorBody
```

**Async**

```python
result = await async_client.inventory_api.with_raw_response.get_multi_node_inventory_for_all_sku_and_all_ship_nodes(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket1.US, WmGlobalVersion._3_1
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MultiNodeInventoryFetchResponseDto
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMultiNodeInventoryForAllSkuAndAllShipNodesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | The target market of the API call.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>limit</code> | <code>str \| None</code> | The number of items returned. Cannot be more than 50.<br><br><strong style="color: green;">Market availability: US only</strong><br>**Default**: <code>"10"</code> |
| <code>next_cursor</code> | <code>str \| None</code> | String returned from initial API call to indicate pagination. Specify nextCursor value to retrieve the next 50 items.<br><br><strong style="color: green;">Market availability: US only</strong><br>**Default**: <code>None</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[MultiNodeInventoryFetchResponseDto](walmart_apis/models/multi_node_inventory_fetch_response_dto.py), [GetMultiNodeInventoryForAllSkuAndAllShipNodesErrorBody](walmart_apis/errors/get_multi_node_inventory_for_all_sku_and_all_ship_nodes_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[MultiNodeInventoryFetchResponseDto](walmart_apis/models/multi_node_inventory_fetch_response_dto.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetMultiNodeInventoryForAllSkuAndAllShipNodesErrorBody](walmart_apis/errors/get_multi_node_inventory_for_all_sku_and_all_ship_nodes_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[V3Inventories403Error1](walmart_apis/models/v3_inventories403_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_multi_node_inventory_for_sku_and_all_shipnodes(sku: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, ship_node: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[InventoriesDto, GetMultiNodeInventoryForSkuAndAllShipnodesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API will retrieve the inventory count for an item across all ship nodes or one specific ship node. You can specify the ship node for which you want to fetch the inventory
<br><b style='color:green;'>Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory_api.with_raw_response.get_multi_node_inventory_for_sku_and_all_shipnodes(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InventoriesDto
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMultiNodeInventoryForSkuAndAllShipnodesErrorBody
```

**Async**

```python
result = await async_client.inventory_api.with_raw_response.get_multi_node_inventory_for_sku_and_all_shipnodes(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InventoriesDto
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMultiNodeInventoryForSkuAndAllShipnodesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sku</code> | <code>str</code> | An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’ as well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't need to be encoded.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | The target market of the API call.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>ship_node</code> | <code>str \| None</code> | ShipNode Id of the ship node for which the inventory is requested<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[InventoriesDto](walmart_apis/models/inventories_dto.py), [GetMultiNodeInventoryForSkuAndAllShipnodesErrorBody](walmart_apis/errors/get_multi_node_inventory_for_sku_and_all_shipnodes_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[InventoriesDto](walmart_apis/models/inventories_dto.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetMultiNodeInventoryForSkuAndAllShipnodesErrorBody](walmart_apis/errors/get_multi_node_inventory_for_sku_and_all_shipnodes_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 404 | <code>[InventoriesDto](walmart_apis/models/inventories_dto.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_wfs_inventory(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, sku: str | None = None, from_modified_date: str | None = None, to_modified_date: str | None = None, limit: str | None = "10", offset: str | None = "0", ship_node_type: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3FulfillmentInventoryResponse, GetWfsinventoryErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

You can use this API to get the current Available to Sell inventory quantities for all WFS items in your catalog. You can also query specific SKUs or filter to only items updated after a specific date in order to reduce the response size.
<br><b style='color:green;'>Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory_api.with_raw_response.get_wfs_inventory(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket1.US, WmGlobalVersion._3_1
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3FulfillmentInventoryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetWfsinventoryErrorBody
```

**Async**

```python
result = await async_client.inventory_api.with_raw_response.get_wfs_inventory(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket1.US, WmGlobalVersion._3_1
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3FulfillmentInventoryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetWfsinventoryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | The target market of the API call.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>sku</code> | <code>str \| None</code> | An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’ as well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't need to be encoded.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>from_modified_date</code> | <code>str \| None</code> | last inventory modified date - starting range.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>to_modified_date</code> | <code>str \| None</code> | last inventory modified date - starting range.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>limit</code> | <code>str \| None</code> | Number of Sku to be returned. Cannot be larger than 300.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>"10"</code> |
| <code>offset</code> | <code>str \| None</code> | Offset is the number of records you wish to skip before selecting records.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>"0"</code> |
| <code>ship_node_type</code> | <code>str \| None</code> | Currently supported: multichannel. This param is enabled only for multi channel sellers. sku becomes mandatory and other params are ineffective while using this param. sku can either contain one item or list of sku's separated by comma (example: sku1,sku2)<br><br><strong style="color: green;">Market availability: US only</strong><br>**Default**: <code>None</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3FulfillmentInventoryResponse](walmart_apis/models/v3_fulfillment_inventory_response.py), [GetWfsinventoryErrorBody](walmart_apis/errors/get_wfsinventory_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3FulfillmentInventoryResponse](walmart_apis/models/v3_fulfillment_inventory_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetWfsinventoryErrorBody](walmart_apis/errors/get_wfsinventory_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[V3FulfillmentInventory403Error1](walmart_apis/models/v3_fulfillment_inventory403_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_bulk_inventory(feed_type: FeedType1OrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, file: FileInput, *, ship_node: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FeedId, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates inventory for items in bulk. 
Seller Can either use feed type "inventory" or "MP_INVENTORY" 
* Inventory spec 1.4 feed type: inventory 
* Inventory spec 1.5 feed type: MP_INVENTORY 

Note: Multi Node Inventory Update Feed (feedType=MP_INVENTORY) only supports JSON Request and Responses.

 Refer to the throttling limits before uploading the Feed Files.

<b>Download the request body sample from </b>

 <a href="/file/mp/us/inventory-samples.zip">US Samples JSON</a>
<a href="/file/mp/ca/inventory-samples.zip">CA Samples JSON</a>
<a href="/file/mp/mx/inventory-samples.zip">MX Samples JSON</a>
<a href="/file/mp/cl/inventory-samples.zip">CL Samples JSON</a>
<br><b style='color:green;'>Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory_api.with_raw_response.update_bulk_inventory(
    FeedType1.INVENTORY,
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    Path("path/to/file.bin"),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FeedId
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.inventory_api.with_raw_response.update_bulk_inventory(
    FeedType1.INVENTORY,
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    Path("path/to/file.bin"),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FeedId
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>feed_type</code> | <code>[FeedType1OrStr](walmart_apis/models/enums/feed_type1.py)</code> | The feed Type<br>Inventory: Global<br>MP_Inventory: US \| MX \| CA<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | The target market of the API call.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>file</code> | <code>FileInput</code> | Feed file to upload<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>ship_node</code> | <code>str \| None</code> | The shipNode for which the inventory is to be updated. Not required in case of Multi Node Inventory Update Feed (feedType=MP_INVENTORY)<br><br><strong style="color: green;">Market availability: US only</strong><br>**Default**: <code>None</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[FeedId](walmart_apis/models/feed_id.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[FeedId](walmart_apis/models/feed_id.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_inventory_for_an_item(sku: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3InventoryRequest | V3InventoryRequestDict, *, ship_node: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Inventory1, UpdateInventoryForAnItemErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the inventory for a given item.
<br><b style='color:green;'>Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory_api.with_raw_response.update_inventory_for_an_item(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3InventoryRequest(sku="97964_KFTest", quantity=Quantity5(amount=10), inventory_available_date="2024-09-20"),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Inventory1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateInventoryForAnItemErrorBody
```

**Async**

```python
result = await async_client.inventory_api.with_raw_response.update_inventory_for_an_item(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3InventoryRequest(sku="97964_KFTest", quantity=Quantity5(amount=10), inventory_available_date="2024-09-20"),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Inventory1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateInventoryForAnItemErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sku</code> | <code>str</code> | An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’, '{', '}' as well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't need to be encoded.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | The target market of the API call.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>body</code> | <code>[V3InventoryRequest](walmart_apis/models/v3_inventory_request.py) \| [V3InventoryRequestDict](walmart_apis/models/v3_inventory_request.py)</code> | File fields |
| <code>ship_node</code> | <code>str \| None</code> | The shipNode for which the inventory is to be updated.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[Inventory1](walmart_apis/models/inventory1.py), [UpdateInventoryForAnItemErrorBody](walmart_apis/errors/update_inventory_for_an_item_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Inventory1](walmart_apis/models/inventory1.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[UpdateInventoryForAnItemErrorBody](walmart_apis/errors/update_inventory_for_an_item_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 404 | <code>[Inventory1](walmart_apis/models/inventory1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_multi_node_inventory(sku: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3InventoriesRequest | V3InventoriesRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[MultiNodeInventoryUpdateResponseDto, UpdateMultiNodeInventoryErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API will update the inventory for an item across one or more fulfillment centers, known as ship nodes.
<br><b style='color:green;'>Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory_api.with_raw_response.update_multi_node_inventory(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3InventoriesRequest(
        inventories=Inventories3(
            nodes=[
                Node10(ship_node="1000005050", input_qty=InputQty13(), inventory_available_date="2024-09-20"),
                Node10(ship_node="79897837271126017", input_qty=InputQty13(), inventory_available_date="2024-09-20"),
            ],
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MultiNodeInventoryUpdateResponseDto
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateMultiNodeInventoryErrorBody
```

**Async**

```python
result = await async_client.inventory_api.with_raw_response.update_multi_node_inventory(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3InventoriesRequest(
        inventories=Inventories3(
            nodes=[
                Node10(ship_node="1000005050", input_qty=InputQty13(), inventory_available_date="2024-09-20"),
                Node10(ship_node="79897837271126017", input_qty=InputQty13(), inventory_available_date="2024-09-20"),
            ],
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MultiNodeInventoryUpdateResponseDto
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateMultiNodeInventoryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sku</code> | <code>str</code> | An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’ as well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't need to be encoded.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | The target market of the API call.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>body</code> | <code>[V3InventoriesRequest](walmart_apis/models/v3_inventories_request.py) \| [V3InventoriesRequestDict](walmart_apis/models/v3_inventories_request.py)</code> | Request fields |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[MultiNodeInventoryUpdateResponseDto](walmart_apis/models/multi_node_inventory_update_response_dto.py), [UpdateMultiNodeInventoryErrorBody](walmart_apis/errors/update_multi_node_inventory_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[MultiNodeInventoryUpdateResponseDto](walmart_apis/models/multi_node_inventory_update_response_dto.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[UpdateMultiNodeInventoryErrorBody](walmart_apis/errors/update_multi_node_inventory_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 404 | <code>[MultiNodeInventoryUpdateResponseDto](walmart_apis/models/multi_node_inventory_update_response_dto.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## LagTimeApi

> Source: [LagTimeApi](walmart_apis/apis/lag_time_api.py)

<details>
<summary><code>def get_lag_time(sku: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LagTimeResponse, GetLagTimeErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use this API to retrieve the lag time for a specific item using its SKU.

Lag Time represents the number of days between when an item is ordered and when it is shipped. Approval thresholds and exemption processes for higher lag times vary by market. For more details, refer to the relevant market-specific knowledge article.
<br><b style='color:green;'>Market availability: Global</strong>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.lag_time_api.with_raw_response.get_lag_time(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LagTimeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetLagTimeErrorBody
```

**Async**

```python
result = await async_client.lag_time_api.with_raw_response.get_lag_time(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LagTimeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetLagTimeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sku</code> | <code>str</code> | A unique alphanumeric ID assigned by the seller to identify each item. The seller uses this ID in the XSD file to reference specific items. If the SKU contains any of the following special characters — :, /, ?, #, [, ], @, !, $, &, ', (, ), *, +, ,, ;, =, space, {, }, or % — they must be URL-encoded. For example, encode spaces as %20. No encoding is required for other characters.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | The target market of the API call.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[LagTimeResponse](walmart_apis/models/lag_time_response.py), [GetLagTimeErrorBody](walmart_apis/errors/get_lag_time_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[LagTimeResponse](walmart_apis/models/lag_time_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetLagTimeErrorBody](walmart_apis/errors/get_lag_time_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V3Lagtime400Error1](walmart_apis/models/v3_lagtime400_error1.py)</code> |
| 404 | <code>[V3Lagtime404Error1](walmart_apis/models/v3_lagtime404_error1.py)</code> |
| 500 | <code>[V3Lagtime500Error1](walmart_apis/models/v3_lagtime500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_lag_time_bulk(feed_type: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3FeedsRequest | V3FeedsRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FeedId1, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use this API to update lag time for multiple items at once.

Lag Time represents the number of days between when an item is ordered and when it is shipped. Approval thresholds and exemption processes for higher lag times vary by market. For more details, refer to the relevant market-specific knowledge article.
<br><b style='color:green;'>Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.lag_time_api.with_raw_response.update_lag_time_bulk(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3FeedsRequest(lag_time_header=LagTimeHeader1()),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FeedId1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.lag_time_api.with_raw_response.update_lag_time_bulk(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3FeedsRequest(lag_time_header=LagTimeHeader1()),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FeedId1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>feed_type</code> | <code>str</code> | Indicates the feed type. Use 'lagtime'.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | The target market of the API call.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>body</code> | <code>[V3FeedsRequest](walmart_apis/models/v3_feeds_request.py) \| [V3FeedsRequestDict](walmart_apis/models/v3_feeds_request.py)</code> | File fields |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[FeedId1](walmart_apis/models/feed_id1.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[FeedId1](walmart_apis/models/feed_id1.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Notifications

> Source: [Notifications](walmart_apis/apis/notifications.py)

<details>
<summary><code>def create_subscription(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket2OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3WebhooksSubscriptionsRequest | V3WebhooksSubscriptionsRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3WebhooksSubscriptionsResponse1, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create one or more webhook subscriptions for event notifications by selecting an event type, event version, resource name, and providing a destination event URL.

Use the Get Event Types API to retrieve available event types, versions, and resource names. Configure the eventUrl to receive notifications.

URL authentication options
- If authMethod is BASIC_AUTH, Walmart passes an authentication header to the eventUrl using authHeaderName as the header key and the Base64-encoded userName:password as the value.
- If authMethod is HMAC, Walmart passes an authentication header to the eventUrl using authHeaderName as the header key and HMACSHA256 of the complete response as the value, with clientSecret as the key.
- If authMethod is OAUTH, Walmart makes a POST call to authUrl to generate a token with request body "grant_type=client_credentials" and headers:
(1) Authorization header using authHeaderName as the key and Base64-encoded clientId:clientSecret as the value, (2) Accept: "application/json; charset=UTF-8", (3) Content-Type: "application/x-www-form-urlencoded; charset=ISO-8859-1", and (4) any custom headers provided in headers. The authUrl must return HTTP 200 with access_token and expires_in fields. When sending notifications to eventUrl, Walmart includes the access_token in headers using authHeaderName as the key and value "Bearer <access_token>", along with any custom headers provided in headers.

<b style='color:green;'>Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.notifications.with_raw_response.create_subscription(
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    WmMarket2.US,
    WmGlobalVersion._3_1,
    V3WebhooksSubscriptionsRequest(
        events=[
            Events3(
                event_type="OFFER_UNPUBLISHED",
                event_version="V1",
                resource_name="ITEM",
                event_url="https://example.com/events",
                status="ACTIVE",
            ),
            Events3(
                event_type="PO_CREATED",
                event_version="V1",
                resource_name="ORDER",
                event_url="https://example.com/orders",
                status="ACTIVE",
            ),
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3WebhooksSubscriptionsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.notifications.with_raw_response.create_subscription(
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    WmMarket2.US,
    WmGlobalVersion._3_1,
    V3WebhooksSubscriptionsRequest(
        events=[
            Events3(
                event_type="OFFER_UNPUBLISHED",
                event_version="V1",
                resource_name="ITEM",
                event_url="https://example.com/events",
                status="ACTIVE",
            ),
            Events3(
                event_type="PO_CREATED",
                event_version="V1",
                resource_name="ORDER",
                event_url="https://example.com/orders",
                status="ACTIVE",
            ),
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3WebhooksSubscriptionsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Name of the Walmart service being called.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket2OrStr](walmart_apis/models/enums/wm_market2.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>body</code> | <code>[V3WebhooksSubscriptionsRequest](walmart_apis/models/v3_webhooks_subscriptions_request.py) \| [V3WebhooksSubscriptionsRequestDict](walmart_apis/models/v3_webhooks_subscriptions_request.py)</code> | Request body parameters for creating one or more subscriptions. |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3WebhooksSubscriptionsResponse1](walmart_apis/models/v3_webhooks_subscriptions_response1.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3WebhooksSubscriptionsResponse1](walmart_apis/models/v3_webhooks_subscriptions_response1.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_subscription(subscription_id: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket2OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3WebhooksSubscriptionsResponse2, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Delete an existing webhook subscription by ID. After deletion, the subscription cannot be retrieved.

<b style='color:green;'>Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.notifications.with_raw_response.delete_subscription(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    WmMarket2.US,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3WebhooksSubscriptionsResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.notifications.with_raw_response.delete_subscription(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    WmMarket2.US,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3WebhooksSubscriptionsResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>str</code> | Unique identifier of the subscription to delete.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Name of the Walmart service being called.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket2OrStr](walmart_apis/models/enums/wm_market2.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3WebhooksSubscriptionsResponse2](walmart_apis/models/v3_webhooks_subscriptions_response2.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3WebhooksSubscriptionsResponse2](walmart_apis/models/v3_webhooks_subscriptions_response2.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_all_subscriptions(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket2OrStr, wm_global_version: WmGlobalVersionOrStr, *, subscription_id: str | None = None, event_type: str | None = None, resource_name: str | None = None, status: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3WebhooksSubscriptionsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve details of all webhook subscriptions created using the Create Subscription API. Use query parameters to filter by subscription ID, event type, resource, or status.

<b style='color:green;'>Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.notifications.with_raw_response.get_all_subscriptions(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Marketplace", WmMarket2.US, WmGlobalVersion._3_1
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3WebhooksSubscriptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.notifications.with_raw_response.get_all_subscriptions(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Marketplace", WmMarket2.US, WmGlobalVersion._3_1
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3WebhooksSubscriptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Name of the Walmart service being called.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket2OrStr](walmart_apis/models/enums/wm_market2.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>subscription_id</code> | <code>str \| None</code> | Filter results to a specific subscription by its unique identifier.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>event_type</code> | <code>str \| None</code> | Filter results to a specific event type. Refer to the Event Payload section for the list of available event types.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>resource_name</code> | <code>str \| None</code> | Filter results to a specific resource (functional category). Refer to the Event Payload section for the list of available resource names.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>status</code> | <code>str \| None</code> | Filter results by subscription status. Allowed values: ACTIVE, INACTIVE.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3WebhooksSubscriptionsResponse](walmart_apis/models/v3_webhooks_subscriptions_response.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3WebhooksSubscriptionsResponse](walmart_apis/models/v3_webhooks_subscriptions_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_event_types(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket2OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3WebhooksEventTypesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve the list of event types and resource names available for subscription. Notifications are triggered only for event types that you subscribe to using the Create Subscription API.

Event types are workflow events fired when statuses or conditions change (for example, an offer moving from published to unpublished, an order auto-cancellation, or a buy box change).

Resource names are functional API categories (for example, ITEM, PRICE, ORDER, INVENTORY). Permissions to subscribe to an event type are governed by the resource's delegated access permissions.

<b style='color:green;'>Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.notifications.with_raw_response.get_event_types(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Marketplace", WmMarket2.US, WmGlobalVersion._3_1
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3WebhooksEventTypesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.notifications.with_raw_response.get_event_types(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Marketplace", WmMarket2.US, WmGlobalVersion._3_1
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3WebhooksEventTypesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Name of the Walmart service being called.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket2OrStr](walmart_apis/models/enums/wm_market2.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3WebhooksEventTypesResponse](walmart_apis/models/v3_webhooks_event_types_response.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3WebhooksEventTypesResponse](walmart_apis/models/v3_webhooks_event_types_response.py)</code> -- Successful operation. Returns the list of event types and resource names available for subscription.

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def test_notification(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket2OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3WebhooksTestRequest | V3WebhooksTestRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RejectRecommendationsResponsePayload, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a test notification to a destination URL using a sample payload.

<b style='color:green;'>Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.notifications.with_raw_response.test_notification(
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    WmMarket2.US,
    WmGlobalVersion._3_1,
    V3WebhooksTestRequest(
        event_type="OFFER_UNPUBLISHED",
        event_version="V1",
        resource_name="ITEM",
        event_url="https://example.com/events",
        auth_details=AuthDetails8(
            auth_method="BASIC_AUTH", user_name="abc", password="test", auth_header_name="Authorization"
        ),
        headers={"X-Custom-Header": "my-value"},
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RejectRecommendationsResponsePayload
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.notifications.with_raw_response.test_notification(
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    WmMarket2.US,
    WmGlobalVersion._3_1,
    V3WebhooksTestRequest(
        event_type="OFFER_UNPUBLISHED",
        event_version="V1",
        resource_name="ITEM",
        event_url="https://example.com/events",
        auth_details=AuthDetails8(
            auth_method="BASIC_AUTH", user_name="abc", password="test", auth_header_name="Authorization"
        ),
        headers={"X-Custom-Header": "my-value"},
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RejectRecommendationsResponsePayload
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Name of the Walmart service being called.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket2OrStr](walmart_apis/models/enums/wm_market2.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>body</code> | <code>[V3WebhooksTestRequest](walmart_apis/models/v3_webhooks_test_request.py) \| [V3WebhooksTestRequestDict](walmart_apis/models/v3_webhooks_test_request.py)</code> | Request fields |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[RejectRecommendationsResponsePayload](walmart_apis/models/reject_recommendations_response_payload.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RejectRecommendationsResponsePayload](walmart_apis/models/reject_recommendations_response_payload.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_subscription(subscription_id: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket2OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3WebhooksSubscriptionsRequest1 | V3WebhooksSubscriptionsRequest1Dict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3WebhooksSubscriptionsResponse3, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Update the details of a subscription. You can update the event version, destination URL, headers, and authentication details. You can also enable or disable the subscription by changing the status to ACTIVE or INACTIVE.

<b style='color:green;'>Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.notifications.with_raw_response.update_subscription(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    WmMarket2.US,
    WmGlobalVersion._3_1,
    V3WebhooksSubscriptionsRequest1(
        event_url="https://example.com/events",
        auth_details=AuthDetails8(
            auth_method="BASIC_AUTH", user_name="abc", password="test", auth_header_name="Authorization"
        ),
        status="ACTIVE",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3WebhooksSubscriptionsResponse3
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.notifications.with_raw_response.update_subscription(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    WmMarket2.US,
    WmGlobalVersion._3_1,
    V3WebhooksSubscriptionsRequest1(
        event_url="https://example.com/events",
        auth_details=AuthDetails8(
            auth_method="BASIC_AUTH", user_name="abc", password="test", auth_header_name="Authorization"
        ),
        status="ACTIVE",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3WebhooksSubscriptionsResponse3
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>str</code> | Unique identifier of the subscription to update.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Name of the Walmart service being called.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket2OrStr](walmart_apis/models/enums/wm_market2.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>body</code> | <code>[V3WebhooksSubscriptionsRequest1](walmart_apis/models/v3_webhooks_subscriptions_request1.py) \| [V3WebhooksSubscriptionsRequest1Dict](walmart_apis/models/v3_webhooks_subscriptions_request1.py)</code> | Request body parameters for updating a subscription. |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3WebhooksSubscriptionsResponse3](walmart_apis/models/v3_webhooks_subscriptions_response3.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3WebhooksSubscriptionsResponse3](walmart_apis/models/v3_webhooks_subscriptions_response3.py)</code> -- Successful Operation. Returns the updated subscription(s).

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## OnRequestReport

> Source: [OnRequestReport](walmart_apis/apis/on_request_report.py)

<details>
<summary><code>def generate_report(report_type: ReportType4OrStr, report_version: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, accept: str, *, wm_consumer_channel_type: str | None = None, body: V3ReportsReportRequestsRequest | V3ReportsReportRequestsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3ReportsReportRequestsResponse1, GenerateReportErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new request for report by specifying the `reportType` and `reportVersion`.
<br><b style='color:green;'>Market availability: Global</b>

**Max reporting window:** For `ITEM_PERFORMANCE` v3, the date range between `dataStartTime` and `dataEndTime` must not exceed 2 years (730 days). Exceeding this limit will return a `400` error.

**Row limit:** There is no limit on the number of rows returned in the report.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.on_request_report.with_raw_response.generate_report(
    ReportType4.ITEM,
    "v1",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    "application/json",
    body=V3ReportsReportRequestsRequest(
        row_filters=[
            EnumFilter2(column_name="Offer Start Date", type_=Type4.RANGE_FILTER),
            EnumFilter2(column_name="Offer End Date", type_=Type4.RANGE_FILTER),
            EnumFilter2(column_name="Price", type_=Type4.RANGE_FILTER),
            EnumFilter2(values=["PUBLISHED"], column_name="Publish Status", type_=Type4.ENUM_FILTER),
            EnumFilter2(values=["FELIX LECHEF", "ANEZUS"], column_name="brand", type_=Type4.MULTI_VALUE_FILTER),
            EnumFilter2(values=["JEWELRY MAKING AND STORAGE"], column_name="category", type_=Type4.MULTI_VALUE_FILTER),
        ],
        exclude_columns=["Average Rating", "Shelf Name"],
        data_start_time="2024-08-10T20:11:24.000Z",
        data_end_time="2024-09-10T20:11:24.000Z",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ReportsReportRequestsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GenerateReportErrorBody
```

**Async**

```python
result = await async_client.on_request_report.with_raw_response.generate_report(
    ReportType4.ITEM,
    "v1",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    "application/json",
    body=V3ReportsReportRequestsRequest(
        row_filters=[
            EnumFilter2(column_name="Offer Start Date", type_=Type4.RANGE_FILTER),
            EnumFilter2(column_name="Offer End Date", type_=Type4.RANGE_FILTER),
            EnumFilter2(column_name="Price", type_=Type4.RANGE_FILTER),
            EnumFilter2(values=["PUBLISHED"], column_name="Publish Status", type_=Type4.ENUM_FILTER),
            EnumFilter2(values=["FELIX LECHEF", "ANEZUS"], column_name="brand", type_=Type4.MULTI_VALUE_FILTER),
            EnumFilter2(values=["JEWELRY MAKING AND STORAGE"], column_name="category", type_=Type4.MULTI_VALUE_FILTER),
        ],
        exclude_columns=["Average Rating", "Shelf Name"],
        data_start_time="2024-08-10T20:11:24.000Z",
        data_end_time="2024-09-10T20:11:24.000Z",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ReportsReportRequestsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GenerateReportErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>report_type</code> | <code>[ReportType4OrStr](walmart_apis/models/enums/report_type4.py)</code> | Type of report for which the request is created. Example, ITEM for Item Report.<br><br><strong style="color: green;">Market availability: <br><br> ITEM: Global <br>INVENTORY: Global <br>LAGTIME: US\|CA\|MX <br>Other Reports: US only</strong> |
| <code>report_version</code> | <code>str</code> | Version of report for which the request is created.<br><br><strong style="color: green;">Market availability: Global</strong><br><br> \|ReportType \|Market Availabilty \|Version Supported <br>\|--------\|----------\|----------<br>\| ITEM   \|Global\|  v1  (**v3 to v6 : US only**)<br>\|INVENTORY\|Global\| v1 <br>\|LAGTIME\|US,CA,MX\| v1 <br>\|DELIVERY_DEFECT\|US only\| v1 <br>\|ITEM_PERFORMANCE\|US only\| v1 to v3 <br>\|PROMO\|US only\| v1 <br>\|RETURN_OVERRIDES\|US only\| v1 <br>\|CPA\|US only\| v1 <br>\|SHIPPING_CONFIGURATION\|US only\| v1 <br>\|SHIPPING_PROGRAM\|US only\| v1 <br>\|FITMENT_MISSING_ATTR\|US only\| v1 <br>\|FITMENT_ACES_COVERAGE\|US only\| v1 <br>\|BUYBOX\|US only\| v1 <br>\|ASSORTMENT_RECOMMENDATIONS\|US only\| v1 <br>\|CANCELLATION\|US only\| v1 <br>\|INVENTORY_RECOMMENDATIONS\|US only\| v1 \| |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | The target market of the API call. <br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>accept</code> | <code>str</code> | Only supported Media Type : application/json<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>body</code> | <code>[V3ReportsReportRequestsRequest](walmart_apis/models/v3_reports_report_requests_request.py) \| [V3ReportsReportRequestsRequestDict](walmart_apis/models/v3_reports_report_requests_request.py) \| None</code> | Request body<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3ReportsReportRequestsResponse1](walmart_apis/models/v3_reports_report_requests_response1.py), [GenerateReportErrorBody](walmart_apis/errors/generate_report_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3ReportsReportRequestsResponse1](walmart_apis/models/v3_reports_report_requests_response1.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GenerateReportErrorBody](walmart_apis/errors/generate_report_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RawError](walmart_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## OnRequestReportApi

> Source: [OnRequestReportApi](walmart_apis/apis/on_request_report_api.py)

<details>
<summary><code>def download_report(request_id: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, accept: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DownloadReportResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetches URL to download a generated report.
<br><b style='color:green;'>Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.on_request_report_api.with_raw_response.download_report(
    "28fae71e-7f34-4493-ad5b-1edca6afebf7",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    "application/json",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DownloadReportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.on_request_report_api.with_raw_response.download_report(
    "28fae71e-7f34-4493-ad5b-1edca6afebf7",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    "application/json",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DownloadReportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_id</code> | <code>str</code> | Automated ID generated by system that uniquely identifies the report request.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | The target market of the API call. <br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>accept</code> | <code>str</code> | Only supported Media Type : application/json<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[DownloadReportResponse](walmart_apis/models/download_report_response.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DownloadReportResponse](walmart_apis/models/download_report_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_requests_status(report_type: ReportType4OrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, accept: str, *, report_version: str | None = None, request_status: RequestStatus4OrStr | None = None, request_submission_start_date: str | None = None, request_submission_end_date: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RequestsStatusResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetches a list of all report requests for specified search criteria by using query parameters.

You can fetch details of report requests created in the last 30 days only.
<br><b style='color:green;'>Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.on_request_report_api.with_raw_response.get_requests_status(
    ReportType4.ITEM,
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    "application/json",
    report_version="v1",
    request_status=RequestStatus4.READY,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestsStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.on_request_report_api.with_raw_response.get_requests_status(
    ReportType4.ITEM,
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    "application/json",
    report_version="v1",
    request_status=RequestStatus4.READY,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestsStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>report_type</code> | <code>[ReportType4OrStr](walmart_apis/models/enums/report_type4.py)</code> | Type of report for which the request is created. Example, ITEM for Item Report.<br><br><strong style="color: green;">Market availability: <br><br> ITEM: Global <br>INVENTORY: Global <br>LAGTIME: US\|CA\|MX <br>Other Reports: US only</strong> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | The target market of the API call. <br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>accept</code> | <code>str</code> | Only supported Media Type : application/json<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>report_version</code> | <code>str \| None</code> | Version of report for which the request is created. Example, v1.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>request_status</code> | <code>[RequestStatus4OrStr](walmart_apis/models/enums/request_status4.py) \| None</code> | Status of report request. Possible values are RECEIVED, INPROGRESS, READY, ERROR.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>request_submission_start_date</code> | <code>str \| None</code> | Report request submittal start date for range of reports requested, in format: YYYY-MM-DDTHH:mm:ssZ<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>request_submission_end_date</code> | <code>str \| None</code> | Report request submittal end date for range of reports requested, in format YYYY-MM-DDTHH:mm:ssZ<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[RequestsStatusResponse](walmart_apis/models/requests_status_response.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RequestsStatusResponse](walmart_apis/models/requests_status_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_single_request_status(request_id: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, accept: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RequestStatusResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetches status and other details of a report request by providing a requestID.

You can fetch details of report request created in the last 30 days only.
<br><b style='color:green;'>Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.on_request_report_api.with_raw_response.get_single_request_status(
    "28fae71e-7f34-4493-ad5b-1edca6afebf7",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    "application/json",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.on_request_report_api.with_raw_response.get_single_request_status(
    "28fae71e-7f34-4493-ad5b-1edca6afebf7",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    "application/json",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_id</code> | <code>str</code> | Automated ID generated by system that uniquely identifies the report request.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | The target market of the API call. <br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>accept</code> | <code>str</code> | Only supported Media Type : application/json<br><br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><strong style="color: green;">Market availability: Global</strong><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[RequestStatusResponse](walmart_apis/models/request_status_response.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RequestStatusResponse](walmart_apis/models/request_status_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Prices

> Source: [Prices](walmart_apis/apis/prices.py)

<details>
<summary><code>def create_strategy(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3RepricerStrategyRequest1 | V3RepricerStrategyRequest1Dict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3RepricerStrategyResponse2, CreateStrategyErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new strategy for the seller.<br><b style='color:green;'>Market availability: US | CA | MX</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.prices.with_raw_response.create_strategy(
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3RepricerStrategyRequest1(),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3RepricerStrategyResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateStrategyErrorBody
```

**Async**

```python
result = await async_client.prices.with_raw_response.create_strategy(
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3RepricerStrategyRequest1(),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3RepricerStrategyResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateStrategyErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The default is set to 3.1.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>body</code> | <code>[V3RepricerStrategyRequest1](walmart_apis/models/v3_repricer_strategy_request1.py) \| [V3RepricerStrategyRequest1Dict](walmart_apis/models/v3_repricer_strategy_request1.py)</code> | The request body will have the strategy related information.<br><b style='color:green;'>Market availability: US \| CA \| MX</b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3RepricerStrategyResponse2](walmart_apis/models/v3_repricer_strategy_response2.py), [CreateStrategyErrorBody](walmart_apis/errors/create_strategy_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3RepricerStrategyResponse2](walmart_apis/models/v3_repricer_strategy_response2.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[CreateStrategyErrorBody](walmart_apis/errors/create_strategy_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V3RepricerStrategy400Error1](walmart_apis/models/v3_repricer_strategy400_error1.py)</code> |
| 403, 500 | <code>[V3Token400Error1](walmart_apis/models/v3_token400_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_strategy(strategy_collection_id: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RejectRecommendationsResponsePayload, DeleteStrategyErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes the strategy.<br><b style='color:green;'>Market availability: US | CA | MX</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.prices.with_raw_response.delete_strategy(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RejectRecommendationsResponsePayload
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteStrategyErrorBody
```

**Async**

```python
result = await async_client.prices.with_raw_response.delete_strategy(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RejectRecommendationsResponsePayload
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteStrategyErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>strategy_collection_id</code> | <code>str</code> | Unique identifier used to group and manage repricing strategies across different resources.<br><b style='color:green;'>Market availability: US \| CA \| MX</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The default is set to 3.1.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[RejectRecommendationsResponsePayload](walmart_apis/models/reject_recommendations_response_payload.py), [DeleteStrategyErrorBody](walmart_apis/errors/delete_strategy_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[RejectRecommendationsResponsePayload](walmart_apis/models/reject_recommendations_response_payload.py)</code> -- Successful Operation.<br><b style='color:green;'>Market availability: US | CA | MX</b>

**On `Failure`**: `error` is <code>[DeleteStrategyErrorBody](walmart_apis/errors/delete_strategy_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V3RepricerStrategy400Error1](walmart_apis/models/v3_repricer_strategy400_error1.py)</code> |
| 403, 500 | <code>[V3Token400Error1](walmart_apis/models/v3_token400_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_all_incentives(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, incentive_status: IncentiveStatusOrStr = IncentiveStatus.ELIGIBLE, limit: int | None = 25, offset: int | None = 0, sort_by: SortBy1OrStr | None = SortBy1.EXPIRATION_DATE, sort_order: OrderOrStr | None = Order.DESC, incentive_type: IncentiveTypeOrStr | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3PriceIncentivesResponse, GetAllIncentivesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Incentives API endpoint gives you the list of all price incentives for items in your catalog. 

The details include Item Id, Product Name, Product Url, SKU Id, Target Price, current Price, Incentive Type, Incentive Status, Base referral fee, Reduced Referral Fee, Enrollment Type, Inventory count, Enrollment Date (epoch Timestamp), Start date (epoch Timestamp), Expiration date (epoch Timestamp), and Incentive Id. 

Target Price, Expiration date, Start date, Incentive Id, and Reduced Ref fee and Enrollment Type for WF items would not be shown (null values). 

Enrollment Type and Date for Eligible Reduced Referral Fee incentives will not show up.<br><b style='color:green;'>Market availability: US</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.prices.with_raw_response.get_all_incentives(
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    incentive_status=IncentiveStatus.ELIGIBLE,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3PriceIncentivesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAllIncentivesErrorBody
```

**Async**

```python
result = await async_client.prices.with_raw_response.get_all_incentives(
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    incentive_status=IncentiveStatus.ELIGIBLE,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3PriceIncentivesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAllIncentivesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The default is set to 3.1.<br><b style='color:green;'>Market availability: Global</b> |
| <code>incentive_status</code> | <code>[IncentiveStatusOrStr](walmart_apis/models/enums/incentive_status.py)</code> | Specify the incentive status to retrieve items with ELIGIBLE or ENROLLED incentives. Allowed values include ENROLLED and ELIGIBLE.<br><b style='color:green;'>Market availability: US</b><br>**Default**: <code>IncentiveStatus.ELIGIBLE</code> |
| <code>limit</code> | <code>int \| None</code> | Specify number of items to return. Max limit value is 200 and min is 1.<br><b style='color:green;'>Market availability: US</b><br>**Default**: <code>25</code> |
| <code>offset</code> | <code>int \| None</code> | Specify the offset of item list to be returned. Min offset value is 0.<br><b style='color:green;'>Market availability: US</b><br>**Default**: <code>0</code> |
| <code>sort_by</code> | <code>[SortBy1OrStr](walmart_apis/models/enums/sort_by1.py) \| None</code> | Specify the sort criteria for items. Examples of the allowed values are ITEM_ID, PRODUCT_NAME, CURRENT_PRICE, EXPIRATION_DATE, ENROLLMENT_DATE.<br><b style='color:green;'>Market availability: US</b><br>**Default**: <code>SortBy1.EXPIRATION_DATE</code> |
| <code>sort_order</code> | <code>[OrderOrStr](walmart_apis/models/enums/order.py) \| None</code> | Specify the sort order for given sort criteria. Examples of the allowed values are ASC or DESC.<br><b style='color:green;'>Market availability: US</b><br>**Default**: <code>Order.DESC</code> |
| <code>incentive_type</code> | <code>[IncentiveTypeOrStr](walmart_apis/models/enums/incentive_type.py) \| None</code> | Specify the incentive type to filter the incentive items. Allowed values include REDUCED_REFERRAL, WALMART_FUNDED.<br><b style='color:green;'>Market availability: US</b><br>**Default**: <code>None</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3PriceIncentivesResponse](walmart_apis/models/v3_price_incentives_response.py), [GetAllIncentivesErrorBody](walmart_apis/errors/get_all_incentives_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3PriceIncentivesResponse](walmart_apis/models/v3_price_incentives_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetAllIncentivesErrorBody](walmart_apis/errors/get_all_incentives_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V3PriceIncentives400Error1](walmart_apis/models/v3_price_incentives400_error1.py)</code> |
| 403, 500 | <code>[V3Token400Error1](walmart_apis/models/v3_token400_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_repricer_feed(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3RepricerFeedsRequest | V3RepricerFeedsRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FeedId1, GetRepricerFeedErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Add/Remove one or more items from a strategy.<br><b style='color:green;'>Market availability: US | CA | MX</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.prices.with_raw_response.get_repricer_feed(
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3RepricerFeedsRequest(),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FeedId1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetRepricerFeedErrorBody
```

**Async**

```python
result = await async_client.prices.with_raw_response.get_repricer_feed(
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3RepricerFeedsRequest(),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FeedId1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetRepricerFeedErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The default is set to 3.1.<br><b style='color:green;'>Market availability: Global</b> |
| <code>body</code> | <code>[V3RepricerFeedsRequest](walmart_apis/models/v3_repricer_feeds_request.py) \| [V3RepricerFeedsRequestDict](walmart_apis/models/v3_repricer_feeds_request.py)</code> | The request body. |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[FeedId1](walmart_apis/models/feed_id1.py), [GetRepricerFeedErrorBody](walmart_apis/errors/get_repricer_feed_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FeedId1](walmart_apis/models/feed_id1.py)</code> -- <br><b style='color:green;'>Market availability: US | CA | MX</b>

**On `Failure`**: `error` is <code>[GetRepricerFeedErrorBody](walmart_apis/errors/get_repricer_feed_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403, 500 | <code>[V3Token400Error1](walmart_apis/models/v3_token400_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_strategies(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, offset: str | None = "0", limit: str | None = "10", wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3RepricerStrategiesResponse, GetStrategiesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the list of strategies.<br><b style='color:green;'>Market availability: US | CA | MX</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.prices.with_raw_response.get_strategies(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket1.US, WmGlobalVersion._3_1
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3RepricerStrategiesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetStrategiesErrorBody
```

**Async**

```python
result = await async_client.prices.with_raw_response.get_strategies(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket1.US, WmGlobalVersion._3_1
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3RepricerStrategiesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetStrategiesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The default is set to 3.1.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>offset</code> | <code>str \| None</code> | The response object starts at 0, representing the first entity that can be retrieved.<br><b style='color:green;'>Market availability: CA \| MX</b><br>**Default**: <code>"0"</code> |
| <code>limit</code> | <code>str \| None</code> | The number of entities to return, with a maximum limit of 25.<br><b style='color:green;'>Market availability: CA \| MX</b><br>**Default**: <code>"10"</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3RepricerStrategiesResponse](walmart_apis/models/v3_repricer_strategies_response.py), [GetStrategiesErrorBody](walmart_apis/errors/get_strategies_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3RepricerStrategiesResponse](walmart_apis/models/v3_repricer_strategies_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetStrategiesErrorBody](walmart_apis/errors/get_strategies_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403, 500 | <code>[V3Token400Error1](walmart_apis/models/v3_token400_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def price_and_promotion_bulk_uploads(feed_type: FeedType21OrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3FeedsFeedTypePriceAndPromotionRequest | V3FeedsFeedTypePriceAndPromotionRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FeedId, PriceAndPromotionBulkUploadsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates prices and promotions in bulk for multiple items. You can modify the prices of multiple items in bulk using a price feed. This is useful for implementing pricing strategies across your catalog, such as seasonal discounts, competitive pricing adjustments, or clearance sales.

Each price feed can contain up to 10,000 items. To ensure optimal performance (feed processing time), we recommend limiting feeds to 1,000 items and keeping the payload under 10 MB.

Use this API instead of the single price update API when updating prices for multiple items. For newly created items, ensure that the Walmart Part ID (WPID) has been assigned and that at least 24 hours have passed since item creation before submitting a bulk price update feed. The bulk price update Service Level Agreement (SLA) is 15 minutes.

The price sequence guarantee is observed by the bulk price update functionality, subject to the following rules:

<ul><li>You may include the same Stock Keeping Unit (SKU) multiple times in a single feed. However, if a SKU is repeated in a feed, only one price will be applied.</li><li>The price sequence guarantee ensures that the latest price update, based on its creation timestamp, is the one that changes the item's price, overwriting the previous version.</li><li>Price updates received with an earlier timestamp are ignored. We recommend using UTC timestamps for the value of <code>feedDate</code> in all feed-based bulk updates.</li></ul>

After submitting the price feed, wait at least 5 minutes before checking whether the bulk price update was successful. If a price update fails, for example, due to duplicate SKU entries, an error response will be returned.

For more information and usage examples, refer to the <a href="https://developer.walmart.com/global-marketplace/docs/update-pricing-for-multiple-items-bulk">Pricing API Guide</a>.

<strong style="color: green;">Market availability: Global</strong>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.prices.with_raw_response.price_and_promotion_bulk_uploads(
    FeedType21.PRICE_AND_PROMOTION,
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3FeedsFeedTypePriceAndPromotionRequest(),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FeedId
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PriceAndPromotionBulkUploadsErrorBody
```

**Async**

```python
result = await async_client.prices.with_raw_response.price_and_promotion_bulk_uploads(
    FeedType21.PRICE_AND_PROMOTION,
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3FeedsFeedTypePriceAndPromotionRequest(),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FeedId
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PriceAndPromotionBulkUploadsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>feed_type</code> | <code>[FeedType21OrStr](walmart_apis/models/enums/feed_type21.py)</code> | The feed Type.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The default is set to 3.1.<br><b style='color:green;'>Market availability: Global</b> |
| <code>body</code> | <code>[V3FeedsFeedTypePriceAndPromotionRequest](walmart_apis/models/v3_feeds_feed_type_price_and_promotion_request.py) \| [V3FeedsFeedTypePriceAndPromotionRequestDict](walmart_apis/models/v3_feeds_feed_type_price_and_promotion_request.py)</code> | The request body consists of a Feed file attached to the request based on the feedType selected .<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[FeedId](walmart_apis/models/feed_id.py), [PriceAndPromotionBulkUploadsErrorBody](walmart_apis/errors/price_and_promotion_bulk_uploads_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FeedId](walmart_apis/models/feed_id.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[PriceAndPromotionBulkUploadsErrorBody](walmart_apis/errors/price_and_promotion_bulk_uploads_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403, 500 | <code>[V3Token400Error1](walmart_apis/models/v3_token400_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def reduced_referral_fee_incentives_enrollment(feed_type: FeedType11OrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3FeedsFeedTypeIncentiveEnrollmentRequest | V3FeedsFeedTypeIncentiveEnrollmentRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3FeedsFeedTypeIncentiveEnrollmentResponse, ReducedReferralFeeIncentivesEnrollmentErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

You can use this API endpoint to enroll any eligible reduced referral fee incentive and unenroll any active reduced referral fee incentives.<br><b style='color:green;'>Market availability: US</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.prices.with_raw_response.reduced_referral_fee_incentives_enrollment(
    FeedType11.INCENTIVE_ENROLLMENT,
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3FeedsFeedTypeIncentiveEnrollmentRequest(),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3FeedsFeedTypeIncentiveEnrollmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ReducedReferralFeeIncentivesEnrollmentErrorBody
```

**Async**

```python
result = await async_client.prices.with_raw_response.reduced_referral_fee_incentives_enrollment(
    FeedType11.INCENTIVE_ENROLLMENT,
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3FeedsFeedTypeIncentiveEnrollmentRequest(),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3FeedsFeedTypeIncentiveEnrollmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ReducedReferralFeeIncentivesEnrollmentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>feed_type</code> | <code>[FeedType11OrStr](walmart_apis/models/enums/feed_type11.py)</code> | The feed Type.<br><b style='color:green;'>Market availability: US</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The default is set to 3.1.<br><b style='color:green;'>Market availability: Global</b> |
| <code>body</code> | <code>[V3FeedsFeedTypeIncentiveEnrollmentRequest](walmart_apis/models/v3_feeds_feed_type_incentive_enrollment_request.py) \| [V3FeedsFeedTypeIncentiveEnrollmentRequestDict](walmart_apis/models/v3_feeds_feed_type_incentive_enrollment_request.py)</code> | The request body consists referralFeeIncentiveEnrollment through which sku opt-in using Y and opt-out using N.<br><b style='color:green;'>Market availability: US</b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3FeedsFeedTypeIncentiveEnrollmentResponse](walmart_apis/models/v3_feeds_feed_type_incentive_enrollment_response.py), [ReducedReferralFeeIncentivesEnrollmentErrorBody](walmart_apis/errors/reduced_referral_fee_incentives_enrollment_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3FeedsFeedTypeIncentiveEnrollmentResponse](walmart_apis/models/v3_feeds_feed_type_incentive_enrollment_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[ReducedReferralFeeIncentivesEnrollmentErrorBody](walmart_apis/errors/reduced_referral_fee_incentives_enrollment_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403, 500 | <code>[V3Token400Error1](walmart_apis/models/v3_token400_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_price(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3PriceRequest | V3PriceRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3PriceResponse, UpdatePriceErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the price of an item listed on Walmart Marketplace. Use this API to change the price of a single item. If you want to update pricing for multiple items, we recommend using the <a href="https://developer.walmart.com/global-marketplace/reference/priceandpromotionbulkuploads">Update pricing for multiple items in bulk</a> API. 

For more information and usage examples, refer to the <a href="https://developer.walmart.com/us-marketplace/docs/update-pricing-for-a-single-item">Pricing API Guide</a>.<br><b style='color:green;'>Market availability: CA | MX | CL</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.prices.with_raw_response.update_price(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket1.US, WmGlobalVersion._3_1, V3PriceRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3PriceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdatePriceErrorBody
```

**Async**

```python
result = await async_client.prices.with_raw_response.update_price(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket1.US, WmGlobalVersion._3_1, V3PriceRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3PriceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdatePriceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The default is set to 3.1.<br><b style='color:green;'>Market availability: Global</b> |
| <code>body</code> | <code>[V3PriceRequest](walmart_apis/models/v3_price_request.py) \| [V3PriceRequestDict](walmart_apis/models/v3_price_request.py)</code> | The request body consists of a Feed file attached to the request based on the feedType selected .<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3PriceResponse](walmart_apis/models/v3_price_response.py), [UpdatePriceErrorBody](walmart_apis/errors/update_price_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3PriceResponse](walmart_apis/models/v3_price_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[UpdatePriceErrorBody](walmart_apis/errors/update_price_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403, 500 | <code>[V3Token400Error1](walmart_apis/models/v3_token400_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_strategy(strategy_collection_id: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3RepricerStrategyRequest | V3RepricerStrategyRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3RepricerStrategyResponse, UpdateStrategyErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the existing strategy.<br><b style='color:green;'>Market availability: US | CA | MX</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.prices.with_raw_response.update_strategy(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3RepricerStrategyRequest(enabled=True),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3RepricerStrategyResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateStrategyErrorBody
```

**Async**

```python
result = await async_client.prices.with_raw_response.update_strategy(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3RepricerStrategyRequest(enabled=True),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3RepricerStrategyResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateStrategyErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>strategy_collection_id</code> | <code>str</code> | Unique identifier used to group and manage repricing strategies across different resources.<br><b style='color:green;'>Market availability: US \| CA \| MX</span></b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The default is set to 3.1.<br><b style='color:green;'>Market availability: Global</span></b> |
| <code>body</code> | <code>[V3RepricerStrategyRequest](walmart_apis/models/v3_repricer_strategy_request.py) \| [V3RepricerStrategyRequestDict](walmart_apis/models/v3_repricer_strategy_request.py)</code> | The request body will have the strategy related information |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel.<br><b style='color:green;'>Market availability: Global</span></b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3RepricerStrategyResponse](walmart_apis/models/v3_repricer_strategy_response.py), [UpdateStrategyErrorBody](walmart_apis/errors/update_strategy_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3RepricerStrategyResponse](walmart_apis/models/v3_repricer_strategy_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[UpdateStrategyErrorBody](walmart_apis/errors/update_strategy_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V3RepricerStrategy400Error1](walmart_apis/models/v3_repricer_strategy400_error1.py)</code> |
| 403, 500 | <code>[V3Token400Error1](walmart_apis/models/v3_token400_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_walmart_funded_incentives_enrollment_status(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, auto_enroll_enabled: bool = True, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3PriceIncentivesWfpreferenceResponse, UpdateWalmartFundedIncentivesEnrollmentStatusErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

If you wish to permanently disable Walmart-funded incentives for all items of your catalog, you can use this API to set the Walmart-funded incentives program as OFF. 

The default value of this variable is ON. 

Any changes to preferences will lock in (disable) the preference option for a period of 4 hours as indicated by isDisabled response field of the API.<br><b style='color:green;'>Market availability: US</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.prices.with_raw_response.update_walmart_funded_incentives_enrollment_status(
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    auto_enroll_enabled=True,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3PriceIncentivesWfpreferenceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateWalmartFundedIncentivesEnrollmentStatusErrorBody
```

**Async**

```python
result = await async_client.prices.with_raw_response.update_walmart_funded_incentives_enrollment_status(
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    auto_enroll_enabled=True,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3PriceIncentivesWfpreferenceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateWalmartFundedIncentivesEnrollmentStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The default is set to 3.1.<br><b style='color:green;'>Market availability: Global</b> |
| <code>auto_enroll_enabled</code> | <code>bool</code> | Specify the boolean for enabling auto enrollment. Examples of the allowed values are true or false.<br><b style='color:green;'>Market availability: US</b><br>**Default**: <code>True</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3PriceIncentivesWfpreferenceResponse](walmart_apis/models/v3_price_incentives_wfpreference_response.py), [UpdateWalmartFundedIncentivesEnrollmentStatusErrorBody](walmart_apis/errors/update_walmart_funded_incentives_enrollment_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3PriceIncentivesWfpreferenceResponse](walmart_apis/models/v3_price_incentives_wfpreference_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[UpdateWalmartFundedIncentivesEnrollmentStatusErrorBody](walmart_apis/errors/update_walmart_funded_incentives_enrollment_status_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403, 500 | <code>[V3Token400Error1](walmart_apis/models/v3_token400_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def walmart_funded_incentives_enrollment(feed_type: FeedType2OrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequest | V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FeedId, WalmartFundedIncentivesEnrollmentErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

While all Walmart-funded incentives are auto-enrolled by default, you can use this API endpoint to 'Opt-out' specific Walmart-funded items whose price you don't wish to lower. 

You can also 'Opt-in' items which were previously Opted-out by you at any time using this API.<br><b style='color:green;'>Market availability: US</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.prices.with_raw_response.walmart_funded_incentives_enrollment(
    FeedType2.WALMART_FUNDED_INCENTIVES_ENROLLMENT,
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequest(),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FeedId
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type WalmartFundedIncentivesEnrollmentErrorBody
```

**Async**

```python
result = await async_client.prices.with_raw_response.walmart_funded_incentives_enrollment(
    FeedType2.WALMART_FUNDED_INCENTIVES_ENROLLMENT,
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequest(),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FeedId
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type WalmartFundedIncentivesEnrollmentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>feed_type</code> | <code>[FeedType2OrStr](walmart_apis/models/enums/feed_type2.py)</code> | The feed Type.<br><b style='color:green;'>Market availability: US</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The default is set to 3.1.<br><b style='color:green;'>Market availability: Global</b> |
| <code>body</code> | <code>[V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequest](walmart_apis/models/v3_feeds_feed_type_walmart_funded_incentives_enrollment_request.py) \| [V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequestDict](walmart_apis/models/v3_feeds_feed_type_walmart_funded_incentives_enrollment_request.py)</code> | The request body consists walmartFundedIncentivesEnrollment through which Opt-in / Opt-out has to be updated |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[FeedId](walmart_apis/models/feed_id.py), [WalmartFundedIncentivesEnrollmentErrorBody](walmart_apis/errors/walmart_funded_incentives_enrollment_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FeedId](walmart_apis/models/feed_id.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[WalmartFundedIncentivesEnrollmentErrorBody](walmart_apis/errors/walmart_funded_incentives_enrollment_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403, 500 | <code>[V3Token400Error1](walmart_apis/models/v3_token400_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Promotions

> Source: [Promotions](walmart_apis/apis/promotions.py)

<details>
<summary><code>def get_promotional_prices(sku: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3PromoSkuResponse, GetPromotionalPricesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a list of promotional prices for a single SKU.<br><b style='color:green;'>Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.promotions.with_raw_response.get_promotional_prices(
    "some example string",
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3PromoSkuResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetPromotionalPricesErrorBody
```

**Async**

```python
result = await async_client.promotions.with_raw_response.get_promotional_prices(
    "some example string",
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3PromoSkuResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetPromotionalPricesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sku</code> | <code>str</code> | An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: ':', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', as well as '%' itself. Other characters don't need to be encoded.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_sec_access_token</code> | <code>str</code> | The access token retrieved in the Token API call. <br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name. <br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Global Version is set to 3.1 by default. <br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding. <br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3PromoSkuResponse](walmart_apis/models/v3_promo_sku_response.py), [GetPromotionalPricesErrorBody](walmart_apis/errors/get_promotional_prices_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3PromoSkuResponse](walmart_apis/models/v3_promo_sku_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetPromotionalPricesErrorBody](walmart_apis/errors/get_promotional_prices_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[V3Token500Error1](walmart_apis/models/v3_token500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def price_bulk_uploads(feed_type: FeedType21OrStr, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, body: V3FeedsFeedTypePriceAndPromotionRequest1 | V3FeedsFeedTypePriceAndPromotionRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FeedId1, PriceBulkUploadsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The price and promotional price API allows you to creates, updates, or deletes promotional prices for multiple SKUs 

To set a new promotional price, set the "promotionSettingAction" attribute to "Create". To update an existing one, set the "promotionSettingAction" attribute to "Create" with promoId. To delete a promotional price, set the "promotionSettingAction" attribute to "Delete". To delete all promotions for a SKU, set the "promotionSettingAction" attribute to "Replace All" 

 Please Note: 
- The effective start date for a given promotion should be within 365 days from the current date and time. 
- The end date of a given promotion should be within 180 days from the start date and time. Any promotions beyond 180 days will result in an error <br><b style='color:green;'>Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.promotions.with_raw_response.price_bulk_uploads(
    FeedType21.PRICE_AND_PROMOTION,
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FeedId1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PriceBulkUploadsErrorBody
```

**Async**

```python
result = await async_client.promotions.with_raw_response.price_bulk_uploads(
    FeedType21.PRICE_AND_PROMOTION,
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FeedId1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PriceBulkUploadsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>feed_type</code> | <code>[FeedType21OrStr](walmart_apis/models/enums/feed_type21.py)</code> | The feed Type. <br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_sec_access_token</code> | <code>str</code> | The access token retrieved in the Token API call. <br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name. <br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Global Version is set to 3.1 by default. <br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding. <br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>body</code> | <code>[V3FeedsFeedTypePriceAndPromotionRequest1](walmart_apis/models/v3_feeds_feed_type_price_and_promotion_request1.py) \| [V3FeedsFeedTypePriceAndPromotionRequest1Dict](walmart_apis/models/v3_feeds_feed_type_price_and_promotion_request1.py) \| None</code> | The request body consists of a Feed file attached to the request based on the feedType selected<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[FeedId1](walmart_apis/models/feed_id1.py), [PriceBulkUploadsErrorBody](walmart_apis/errors/price_bulk_uploads_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FeedId1](walmart_apis/models/feed_id1.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[PriceBulkUploadsErrorBody](walmart_apis/errors/price_bulk_uploads_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 500 | <code>[V3Token500Error1](walmart_apis/models/v3_token500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_promotional_prices(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3PriceRequest | V3PriceRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3PriceResponse, UpdatePromotionalPricesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The update a promotional price API allows you to creates, updates, or deletes promotional prices for single SKUs 

To set a new promotional price, set the "promotionSettingAction" attribute to "Create". To update an existing one, set the "promotionSettingAction" attribute to "Create" with promoId. To delete a promotional price, set the "promotionSettingAction" attribute to "Delete". To delete all promotions for a SKU, set the "promotionSettingAction" attribute to "Replace All" 

 Please Note: 
- The effective start date for a given promotion should be within 365 days from the current date and time. 
- The end date of a given promotion should be within 180 days from the start date and time. Any promotions beyond 180 days will result in an error <br><b style='color:green;'>Market availability: CA | MX | CL</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.promotions.with_raw_response.update_promotional_prices(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3PriceRequest(),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3PriceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdatePromotionalPricesErrorBody
```

**Async**

```python
result = await async_client.promotions.with_raw_response.update_promotional_prices(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3PriceRequest(),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3PriceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdatePromotionalPricesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. Required for authenticating requests to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Global Version is set to 3.1 by default. <br><b style='color:green;'>Market availability: Global</b> |
| <code>body</code> | <code>[V3PriceRequest](walmart_apis/models/v3_price_request.py) \| [V3PriceRequestDict](walmart_apis/models/v3_price_request.py)</code> | The request body consists of a Feed file attached to the request.<br><b style='color:green;'>Market availability: CA \| MX \| CL</b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3PriceResponse](walmart_apis/models/v3_price_response.py), [UpdatePromotionalPricesErrorBody](walmart_apis/errors/update_promotional_prices_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3PriceResponse](walmart_apis/models/v3_price_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[UpdatePromotionalPricesErrorBody](walmart_apis/errors/update_promotional_prices_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403, 500 | <code>[V3Token500Error1](walmart_apis/models/v3_token500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## RecommendationsApi

> Source: [RecommendationsApi](walmart_apis/apis/recommendations_api.py)

<details>
<summary><code>def get_fulfill_with_wfs_recommendations(content_type: str, accept: str, wm_global_version: str, wm_market: str, wm_audit_origin_source: str, *, customer_favorite: bool | None = None, show_insights: bool | None = False, limit: int | None = 30, offset: int | None = 0, sort_by: str | None = "estimatedSalesLift", sort_order: SortOrderOrStr | None = SortOrder.DESC, show_hidden_records_only: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3WfsRecommendationFulfilWithWfsResponse, GetFulfillWithWfsrecommendationsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use **Fulfill With WFS Recommendations** to identify which seller-fulfilled items in your catalog Walmart suggests could potentially perform best when fulfilled by WFS. These suggestions are available on demand, and suggestions are refreshed the 1st and 15th of each month.

Key attributes include:

- **estimatedSalesLift**: The estimated increase in sales you could see if you converted the suggested items from seller-fulfilled to WFS.

- **sellerFulfilledPast30DaysSales**: A historical view of your seller-fulfilled sales for the past 30 days.
- **walmartFulfilledEstimatedSales**: An estimated view of your potential sales if the suggested items were fulfilled by WFS.

You can use these suggestions to determine which items to convert to WFS.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.recommendations_api.with_raw_response.get_fulfill_with_wfs_recommendations(
    "application/json",
    "application/json",
    "3.1",
    "US",
    "SELLER_API",
    customer_favorite=True,
    limit=10,
    offset=1,
    sort_by="estimatedSalesLift",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3WfsRecommendationFulfilWithWfsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetFulfillWithWfsrecommendationsErrorBody
```

**Async**

```python
result = await async_client.recommendations_api.with_raw_response.get_fulfill_with_wfs_recommendations(
    "application/json",
    "application/json",
    "3.1",
    "US",
    "SELLER_API",
    customer_favorite=True,
    limit=10,
    offset=1,
    sort_by="estimatedSalesLift",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3WfsRecommendationFulfilWithWfsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetFulfillWithWfsrecommendationsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>str</code> | Specifies the literal **application/json**. This value identifies the content type of the request body.<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>accept</code> | <code>str</code> | Only supported Media Type : application/json.<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>wm_global_version</code> | <code>str</code> | Global version for API compatibility.<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>wm_market</code> | <code>str</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>wm_audit_origin_source</code> | <code>str</code> | Seller identifier.<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>customer_favorite</code> | <code>bool \| None</code> | Filters items by customer favorite status. When set to `true`, only customer favorites are returned. When set to `false`, only non-favorites are returned. If omitted, all items are returned.<br>**Default**: <code>None</code> |
| <code>show_insights</code> | <code>bool \| None</code> | Shows aggregate recommendation values for all items.<br><br><b style='color: green;'>Market availability: US only</b><br>**Default**: <code>False</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of SKUs to include in the response (1–300). If you omit this parameter, Walmart returns up to 30 SKUs.<br><br><b style='color: green;'>Market availability: US only</b><br>**Default**: <code>30</code> |
| <code>offset</code> | <code>int \| None</code> | The number of SKUs to skip before Walmart starts listing results. Set to 0 to start at the first SKU.<br><br><b style='color: green;'>Market availability: US only</b><br>**Default**: <code>0</code> |
| <code>sort_by</code> | <code>str \| None</code> | The attribute to be used in sorting the response.<br><br><b style='color: green;'>Market availability: US only</b><br>**Default**: <code>"estimatedSalesLift"</code> |
| <code>sort_order</code> | <code>[SortOrderOrStr](walmart_apis/models/enums/sort_order.py) \| None</code> | The order in which the response should be sorted. This can be in set to "ASC" or "DESC" order of value. Default is "DESC.<br><br><b style='color: green;'>Market availability: US only</b><br>**Default**: <code>SortOrder.DESC</code> |
| <code>show_hidden_records_only</code> | <code>bool \| None</code> | Shows insights you have hidden.<br><br><b style='color: green;'>Market availability: US only</b><br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3WfsRecommendationFulfilWithWfsResponse](walmart_apis/models/v3_wfs_recommendation_fulfil_with_wfs_response.py), [GetFulfillWithWfsrecommendationsErrorBody](walmart_apis/errors/get_fulfill_with_wfsrecommendations_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3WfsRecommendationFulfilWithWfsResponse](walmart_apis/models/v3_wfs_recommendation_fulfil_with_wfs_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetFulfillWithWfsrecommendationsErrorBody](walmart_apis/errors/get_fulfill_with_wfsrecommendations_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 500 | <code>[ErrorResponse2](walmart_apis/models/error_response2.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_restock_recommendations(authorization: str, content_type: str, accept: str, wm_global_version: str, wm_market: str, wm_audit_origin_source: str, *, customer_favorite: bool | None = None, show_insights: bool | None = True, limit: int | None = 30, offset: int | None = 0, sort_by: str | None = "forecastedSalesLift", sort_order: SortOrderOrStr | None = SortOrder.DESC, show_hidden_records_only: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3WfsRecommendationRestockResponse, GetRestockRecommendationsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use **Restock Recommendations** to get Walmart-generated suggestions for the items you should restock with WFS based on your current inventory and forecasted sales demand. These suggestions are available on demand. Key attributes include:

- **suggestedUnits**: The number of units we suggest you send of this item to WFS
- **forecastedSalesLift**: The estimated increase in sales you may see if your items are restocked according to our suggestions
- **totalForecastedSalesLost**: How much money you're estimated to lose out on if you don't restock your inventory

Once you determine which suggested items to restock, you can use the Create inbound shipment API to create a shipping plan to send inventory to WFS.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.recommendations_api.with_raw_response.get_restock_recommendations(
    "Basic YzcyOTFjNmItNzI5MC00....",
    "application/json",
    "application/json",
    "3.1",
    "US",
    "SELLER_API",
    customer_favorite=True,
    limit=10,
    offset=1,
    sort_by="forecastedSalesLift",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3WfsRecommendationRestockResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetRestockRecommendationsErrorBody
```

**Async**

```python
result = await async_client.recommendations_api.with_raw_response.get_restock_recommendations(
    "Basic YzcyOTFjNmItNzI5MC00....",
    "application/json",
    "application/json",
    "3.1",
    "US",
    "SELLER_API",
    customer_favorite=True,
    limit=10,
    offset=1,
    sort_by="forecastedSalesLift",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3WfsRecommendationRestockResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetRestockRecommendationsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>authorization</code> | <code>str</code> | Basic authorization header. Base 64 encodes the Client ID and Client Secret retrieved in step two of the integration steps.<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>content_type</code> | <code>str</code> | Specifies the literal **application/json**. This value identifies the content type of the request body.<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>accept</code> | <code>str</code> | Only supported Media Type : application/json.<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>wm_global_version</code> | <code>str</code> | Global version for API compatibility.<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>wm_market</code> | <code>str</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>wm_audit_origin_source</code> | <code>str</code> | Seller identifier.<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>customer_favorite</code> | <code>bool \| None</code> | Filters items by customer favorite status. When set to `true`, only customer favorites are returned. When set to `false`, only non-favorites are returned. If omitted, all items are returned.<br>**Default**: <code>None</code> |
| <code>show_insights</code> | <code>bool \| None</code> | Shows aggregate recommendation values for all items.<br><br><b style='color: green;'>Market availability: US only</b><br>**Default**: <code>True</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of SKUs to include in the response (1–300). If you omit this parameter, Walmart returns up to 30 SKUs.<br><br><b style='color: green;'>Market availability: US only</b><br>**Default**: <code>30</code> |
| <code>offset</code> | <code>int \| None</code> | The number of SKUs to skip before Walmart starts listing results. Set to 0 to start at the first SKU.<br><br><b style='color: green;'>Market availability: US only</b><br>**Default**: <code>0</code> |
| <code>sort_by</code> | <code>str \| None</code> | The attribute to be used in sorting the response.<br><br><b style='color: green;'>Market availability: US only</b><br>**Default**: <code>"forecastedSalesLift"</code> |
| <code>sort_order</code> | <code>[SortOrderOrStr](walmart_apis/models/enums/sort_order.py) \| None</code> | The order in which the response should be sorted. This can be in set to "ASC" or "DESC" order of value. Default is "DESC.<br><br><b style='color: green;'>Market availability: US only</b><br>**Default**: <code>SortOrder.DESC</code> |
| <code>show_hidden_records_only</code> | <code>bool \| None</code> | Shows insights you have hidden.<br><br><b style='color: green;'>Market availability: US only</b><br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3WfsRecommendationRestockResponse](walmart_apis/models/v3_wfs_recommendation_restock_response.py), [GetRestockRecommendationsErrorBody](walmart_apis/errors/get_restock_recommendations_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3WfsRecommendationRestockResponse](walmart_apis/models/v3_wfs_recommendation_restock_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetRestockRecommendationsErrorBody](walmart_apis/errors/get_restock_recommendations_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 500 | <code>[ErrorResponse2](walmart_apis/models/error_response2.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_shipment_quantity_recommendations(authorization: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, accept: str, wm_global_version: str, wm_market: str, body: V3WfsRecommendationShipmentQuantityRequest | V3WfsRecommendationShipmentQuantityRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3WfsRecommendationShipmentQuantityResponse, GetShipmentQuantityRecommendationsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use this API to get recommended shipment quantities for the items that you plan to send to Walmart Fulfillment Services (WFS) in order to achieve optimal inventory levels.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.recommendations_api.with_raw_response.get_shipment_quantity_recommendations(
    "Basic YzcyOTFjNmItNzI5MC00....",
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    "application/json",
    "3.1",
    "US",
    V3WfsRecommendationShipmentQuantityRequest(
        list_of_gtins=["00723508807642", "00643131798370", "00643131799155"], list_of_skus=[]
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3WfsRecommendationShipmentQuantityResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetShipmentQuantityRecommendationsErrorBody
```

**Async**

```python
result = await async_client.recommendations_api.with_raw_response.get_shipment_quantity_recommendations(
    "Basic YzcyOTFjNmItNzI5MC00....",
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    "application/json",
    "3.1",
    "US",
    V3WfsRecommendationShipmentQuantityRequest(
        list_of_gtins=["00723508807642", "00643131798370", "00643131799155"], list_of_skus=[]
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3WfsRecommendationShipmentQuantityResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetShipmentQuantityRecommendationsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>authorization</code> | <code>str</code> | Basic authorization header. Base 64 encodes the Client ID and Client Secret retrieved in step two of the integration steps.<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>wm_sec_access_token</code> | <code>str</code> | The access token retrieved in the Token API call<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID.<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name.<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>accept</code> | <code>str</code> | Only supported Media Type : application/json.<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>wm_global_version</code> | <code>str</code> | Global version for API compatibility.<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>wm_market</code> | <code>str</code> | Market identifier.<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>body</code> | <code>[V3WfsRecommendationShipmentQuantityRequest](walmart_apis/models/v3_wfs_recommendation_shipment_quantity_request.py) \| [V3WfsRecommendationShipmentQuantityRequestDict](walmart_apis/models/v3_wfs_recommendation_shipment_quantity_request.py)</code> | Request body containing GTINs or SKUs to retrieve the quantity limit.<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><b style='color: green;'>Market availability: US only</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3WfsRecommendationShipmentQuantityResponse](walmart_apis/models/v3_wfs_recommendation_shipment_quantity_response.py), [GetShipmentQuantityRecommendationsErrorBody](walmart_apis/errors/get_shipment_quantity_recommendations_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3WfsRecommendationShipmentQuantityResponse](walmart_apis/models/v3_wfs_recommendation_shipment_quantity_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetShipmentQuantityRecommendationsErrorBody](walmart_apis/errors/get_shipment_quantity_recommendations_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 500 | <code>[ErrorResponse2](walmart_apis/models/error_response2.py)</code> |
| 404 | <code>[NotFoundResponse](walmart_apis/models/not_found_response.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_unpublished_recommendations(content_type: str, accept: str, wm_global_version: str, wm_market: str, wm_audit_origin_source: str, *, customer_favorite: bool | None = None, show_insights: bool | None = False, limit: int | None = 30, offset: int | None = 0, sort_by: str | None = "estimatedSalesLift", sort_order: SortOrderOrStr | None = SortOrder.DESC, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3WfsRecommendationUnpublishedResponse, GetUnpublishedRecommendationsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This call helps you identify the estimated storage fees with Walmart for your unpublished WFS items.

Use **Unpublish Recommendations** to fetch a current list of your unpublished WFS items. This is available on demand. 

Key data attributes include:

- **unpublishedIssue**: The reason your item is currently unpublished with Walmart.
- **estimatedStorageFee**: The estimated storage costs associated with your unpublished WFS inventory.
- **totalunpublishedunitsstored**: The total quantity of units in WFS fulfillment centers for unpublished items.

Use this data to identify the reason these items are unpublished and the estimated costs associated with these unpublished items. By default, these suggestions will only include items that are active with an Available to Sell (ATS) quantity of 0.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.recommendations_api.with_raw_response.get_unpublished_recommendations(
    "application/json",
    "application/json",
    "3.1",
    "US",
    "SELLER_API",
    customer_favorite=True,
    limit=10,
    offset=1,
    sort_by="forecastedSalesLift",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3WfsRecommendationUnpublishedResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetUnpublishedRecommendationsErrorBody
```

**Async**

```python
result = await async_client.recommendations_api.with_raw_response.get_unpublished_recommendations(
    "application/json",
    "application/json",
    "3.1",
    "US",
    "SELLER_API",
    customer_favorite=True,
    limit=10,
    offset=1,
    sort_by="forecastedSalesLift",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3WfsRecommendationUnpublishedResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetUnpublishedRecommendationsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>str</code> | Specifies the literal **application/json**. This value identifies the content type of the request body.<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>accept</code> | <code>str</code> | Only supported Media Type : application/json.<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>wm_global_version</code> | <code>str</code> | Global version for API compatibility.<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>wm_market</code> | <code>str</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>wm_audit_origin_source</code> | <code>str</code> | Seller identifier.<br><br><b style='color: green;'>Market availability: US only</b> |
| <code>customer_favorite</code> | <code>bool \| None</code> | Filters items by customer favorite status. When set to `true`, only customer favorites are returned. When set to `false`, only non-favorites are returned. If omitted, all items are returned.<br>**Default**: <code>None</code> |
| <code>show_insights</code> | <code>bool \| None</code> | Shows aggregate recommendation values for all items.<br><br><b style='color: green;'>Market availability: US only</b><br>**Default**: <code>False</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of SKUs to include in the response (1–300). If you omit this parameter, Walmart returns up to 30 SKUs.<br><br><b style='color: green;'>Market availability: US only</b><br>**Default**: <code>30</code> |
| <code>offset</code> | <code>int \| None</code> | The number of SKUs to skip before Walmart starts listing results. Set to 0 to start at the first SKU.<br><br><b style='color: green;'>Market availability: US only</b><br>**Default**: <code>0</code> |
| <code>sort_by</code> | <code>str \| None</code> | The attribute to be used in sorting the response.<br><br><b style='color: green;'>Market availability: US only</b><br>**Default**: <code>"estimatedSalesLift"</code> |
| <code>sort_order</code> | <code>[SortOrderOrStr](walmart_apis/models/enums/sort_order.py) \| None</code> | The order in which the response should be sorted. This can be in set to "ASC" or "DESC" order of value. Default is "DESC.<br><br><b style='color: green;'>Market availability: US only</b><br>**Default**: <code>SortOrder.DESC</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3WfsRecommendationUnpublishedResponse](walmart_apis/models/v3_wfs_recommendation_unpublished_response.py), [GetUnpublishedRecommendationsErrorBody](walmart_apis/errors/get_unpublished_recommendations_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3WfsRecommendationUnpublishedResponse](walmart_apis/models/v3_wfs_recommendation_unpublished_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetUnpublishedRecommendationsErrorBody](walmart_apis/errors/get_unpublished_recommendations_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 500 | <code>[ErrorResponse2](walmart_apis/models/error_response2.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ReportScheduler

> Source: [ReportScheduler](walmart_apis/apis/report_scheduler.py)

<details>
<summary><code>def delete_report_schedule(schedule_id: str, wm_svc_name: str, wm_qos_correlation_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RejectRecommendationsResponsePayload, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API allows you to remove an existing report schedule. 

<strong style="color: green;">Market availability: US only</strong>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.report_scheduler.with_raw_response.delete_report_schedule(
    "some example string", "Walmart Marketplace", "b3261d2d-028a-4ef7-8602-633c23200af6"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RejectRecommendationsResponsePayload
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.report_scheduler.with_raw_response.delete_report_schedule(
    "some example string", "Walmart Marketplace", "b3261d2d-028a-4ef7-8602-633c23200af6"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RejectRecommendationsResponsePayload
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>schedule_id</code> | <code>str</code> | A unique identifier assigned to the report schedule. |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[RejectRecommendationsResponsePayload](walmart_apis/models/reject_recommendations_response_payload.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RejectRecommendationsResponsePayload](walmart_apis/models/reject_recommendations_response_payload.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_all_report_schedules(report_type: ReportType10OrStr, wm_svc_name: str, wm_qos_correlation_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3ReportsSchedulesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The Get All Report Schedules API retrieves a list of all existing report schedules. This helps you to easily view and manage all scheduled reports in one place. 

<strong style="color: green;">Market availability: US only</strong>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.report_scheduler.with_raw_response.get_all_report_schedules(
    ReportType10.ITEM, "Walmart Marketplace", "b3261d2d-028a-4ef7-8602-633c23200af6"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ReportsSchedulesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.report_scheduler.with_raw_response.get_all_report_schedules(
    ReportType10.ITEM, "Walmart Marketplace", "b3261d2d-028a-4ef7-8602-633c23200af6"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ReportsSchedulesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>report_type</code> | <code>[ReportType10OrStr](walmart_apis/models/enums/report_type10.py)</code> | Specifies the type of report to be generated. Example: ITEM for Item Report. |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3ReportsSchedulesResponse](walmart_apis/models/v3_reports_schedules_response.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3ReportsSchedulesResponse](walmart_apis/models/v3_reports_schedules_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_report_schedule(schedule_id: str, wm_svc_name: str, wm_qos_correlation_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3ReportsSchedulesResponse1, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API retrieves the details of a single report schedule based on the specified scheduleId.

<strong style="color: green;">Market availability: US only</strong>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.report_scheduler.with_raw_response.get_report_schedule(
    "some example string", "Walmart Marketplace", "b3261d2d-028a-4ef7-8602-633c23200af6"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ReportsSchedulesResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.report_scheduler.with_raw_response.get_report_schedule(
    "some example string", "Walmart Marketplace", "b3261d2d-028a-4ef7-8602-633c23200af6"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ReportsSchedulesResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>schedule_id</code> | <code>str</code> | Value sent with the request. |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3ReportsSchedulesResponse1](walmart_apis/models/v3_reports_schedules_response1.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3ReportsSchedulesResponse1](walmart_apis/models/v3_reports_schedules_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_report_schedule(schedule_id: str, wm_svc_name: str, wm_qos_correlation_id: str, *, body: V3ReportsSchedulesRequest | V3ReportsSchedulesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3ReportsSchedulesResponse1, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API allows you to modify an existing report schedule. You can change the parameters to better suit your needs, ensuring that reports are generated and delivered according to the most current requirements. 

<strong style="color: green;">Market availability: US only</strong>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.report_scheduler.with_raw_response.update_report_schedule(
    "some example string", "Walmart Marketplace", "b3261d2d-028a-4ef7-8602-633c23200af6"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ReportsSchedulesResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.report_scheduler.with_raw_response.update_report_schedule(
    "some example string", "Walmart Marketplace", "b3261d2d-028a-4ef7-8602-633c23200af6"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ReportsSchedulesResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>schedule_id</code> | <code>str</code> | A unique identifier assigned to the report schedule. |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID |
| <code>body</code> | <code>[V3ReportsSchedulesRequest](walmart_apis/models/v3_reports_schedules_request.py) \| [V3ReportsSchedulesRequestDict](walmart_apis/models/v3_reports_schedules_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3ReportsSchedulesResponse1](walmart_apis/models/v3_reports_schedules_response1.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3ReportsSchedulesResponse1](walmart_apis/models/v3_reports_schedules_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## ReportsApi

> Source: [ReportsApi](walmart_apis/apis/reports_api.py)

<details>
<summary><code>def get_available_recon_report_dates(wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ReconReportDateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API will list all the available Marketplace reconciliation report dates for the Seller.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.reports_api.with_raw_response.get_available_recon_report_dates(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReconReportDateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.reports_api.with_raw_response.get_available_recon_report_dates(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReconReportDateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ReconReportDateResponse](walmart_apis/models/recon_report_date_response.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ReconReportDateResponse](walmart_apis/models/recon_report_date_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_available_v1_recon_report_as_json(report_date: str, offset: int, no_of_records: int, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ReconReportV1AsJsonResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API will get a partner’s transaction details in JSON format for a specific date range (available only for v1 reports). Dates for accessing the report can be found by using the ‘GET Available recon report dates’ API.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.reports_api.with_raw_response.get_available_v1_recon_report_as_json(
    "some example string", 1, 1, "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReconReportV1AsJsonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.reports_api.with_raw_response.get_available_v1_recon_report_as_json(
    "some example string", 1, 1, "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReconReportV1AsJsonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>report_date</code> | <code>str</code> | Date of the settlement report |
| <code>offset</code> | <code>int</code> | starting number of the bytes, initial value for the offset is zero |
| <code>no_of_records</code> | <code>int</code> | number of records in the report (max limit 1000) |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ReconReportV1AsJsonResponse](walmart_apis/models/recon_report_v1_as_json_response.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ReconReportV1AsJsonResponse](walmart_apis/models/recon_report_v1_as_json_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_available_v1_recon_report_dates(wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ReconReportDateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API will list all the available Marketplace reconciliation report dates for the Seller.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.reports_api.with_raw_response.get_available_v1_recon_report_dates(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReconReportDateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.reports_api.with_raw_response.get_available_v1_recon_report_dates(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReconReportDateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ReconReportDateResponse](walmart_apis/models/recon_report_date_response.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ReconReportDateResponse](walmart_apis/models/recon_report_date_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_partner_performance(wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PartnerProgramPerformanceRes, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API will get a partner's current cycle performance

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.reports_api.with_raw_response.get_partner_performance(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PartnerProgramPerformanceRes
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.reports_api.with_raw_response.get_partner_performance(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PartnerProgramPerformanceRes
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[PartnerProgramPerformanceRes](walmart_apis/models/partner_program_performance_res.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PartnerProgramPerformanceRes](walmart_apis/models/partner_program_performance_res.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_partner_statement(wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PartnerProgramStatementRes, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API will get a partner's current cycle statement

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.reports_api.with_raw_response.get_partner_statement(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PartnerProgramStatementRes
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.reports_api.with_raw_response.get_partner_statement(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PartnerProgramStatementRes
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[PartnerProgramStatementRes](walmart_apis/models/partner_program_statement_res.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PartnerProgramStatementRes](walmart_apis/models/partner_program_statement_res.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_recon_report(report_date: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FileResponse, GetReconReportErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Seller can download the reconciliation report for a specific date using this API. Dates available to be downloaded can be found by using the Get available reconciliation report dates API.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.reports_api.with_raw_response.get_recon_report(
    "some example string", "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetReconReportErrorBody
```

**Async**

```python
result = await async_client.reports_api.with_raw_response.get_recon_report(
    "some example string", "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AsyncFileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetReconReportErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>report_date</code> | <code>str</code> | The date for which the reconcilation file is available |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;FileResponse, [GetReconReportErrorBody](walmart_apis/errors/get_recon_report_error.py)&#93;</code>

**On `Success`**: `payload` is <code>FileResponse</code>, its body not yet read -- Successful Operation

**On `Failure`**: `error` is <code>[GetReconReportErrorBody](walmart_apis/errors/get_recon_report_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RawError](walmart_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_recon_report_v1(report_date: str, report_version: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FileResponse, GetReconReportV1ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Seller can download the reconciliation report for a specific date using this API. Dates available to be downloaded can be found by using the Get available reconciliation report dates API.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.reports_api.with_raw_response.get_recon_report_v1(
    "some example string", "some example string", "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetReconReportV1ErrorBody
```

**Async**

```python
result = await async_client.reports_api.with_raw_response.get_recon_report_v1(
    "some example string", "some example string", "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AsyncFileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetReconReportV1ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>report_date</code> | <code>str</code> | The date for which the reconcilation file is available |
| <code>report_version</code> | <code>str</code> | Report Version |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;FileResponse, [GetReconReportV1ErrorBody](walmart_apis/errors/get_recon_report_v1_error.py)&#93;</code>

**On `Success`**: `payload` is <code>FileResponse</code>, its body not yet read -- Successful Operation

**On `Failure`**: `error` is <code>[GetReconReportV1ErrorBody](walmart_apis/errors/get_recon_report_v1_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RawError](walmart_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ReturnsRefund

> Source: [ReturnsRefund](walmart_apis/apis/returns_refund.py)

<details>
<summary><code>def get_returns(query_params: QueryParams | QueryParamsDict, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ReturnOrderResponse, GetReturnsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the details of all return orders for the specified filter criteria.

<br><b style='color:green;'>Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.returns_refund.with_raw_response.get_returns(
    QueryParams(), "some example string", "some example string", WmMarket1.US, WmGlobalVersion._3_1
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReturnOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetReturnsErrorBody
```

**Async**

```python
result = await async_client.returns_refund.with_raw_response.get_returns(
    QueryParams(), "some example string", "some example string", WmMarket1.US, WmGlobalVersion._3_1
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReturnOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetReturnsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>query_params</code> | <code>[QueryParams](walmart_apis/models/query_params.py) \| [QueryParamsDict](walmart_apis/models/query_params.py)</code> | Value sent with the request. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br>Example: b3261d2d-028a-4ef7-8602-633c23200af6<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br>Example: Walmart Marketplace<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The value must be set to 3.1.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ReturnOrderResponse](walmart_apis/models/return_order_response.py), [GetReturnsErrorBody](walmart_apis/errors/get_returns_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ReturnOrderResponse](walmart_apis/models/return_order_response.py)</code> -- success

**On `Failure`**: `error` is <code>[GetReturnsErrorBody](walmart_apis/errors/get_returns_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse3](walmart_apis/models/error_response3.py)</code> |
| 401 | <code>[Unauthorized1](walmart_apis/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](walmart_apis/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](walmart_apis/models/too_many_requests1.py)</code> |
| 500 | <code>[ErrorResponses](walmart_apis/models/error_responses.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def refund_request(return_order_id: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket3OrStr, wm_global_version: WmGlobalVersionOrStr, body: RefundRequest | RefundRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Request, RefundRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Refunds one or more order lines that have been shipped. The response to a successful call contains the order with the refunded line item. 

<br><b style='color:green;'>Market availability: US | MX</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.returns_refund.with_raw_response.refund_request(
    "some example string",
    "some example string",
    "some example string",
    WmMarket3.US,
    WmGlobalVersion._3_1,
    RefundRequest(
        customer_order_id="some example string",
        refund_lines=[
            RefundLine(
                return_order_line_number=1,
                quantity=Quantity(unit_of_measure="some example string", measurement_value=1),
            ),
        ],
        order_refund=OrderRefund(),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Request
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RefundRequestErrorBody
```

**Async**

```python
result = await async_client.returns_refund.with_raw_response.refund_request(
    "some example string",
    "some example string",
    "some example string",
    WmMarket3.US,
    WmGlobalVersion._3_1,
    RefundRequest(
        customer_order_id="some example string",
        refund_lines=[
            RefundLine(
                return_order_line_number=1,
                quantity=Quantity(unit_of_measure="some example string", measurement_value=1),
            ),
        ],
        order_refund=OrderRefund(),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Request
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RefundRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>return_order_id</code> | <code>str</code> | Return order identifier of the return order object as part of array. This is the same as RMA number.<br><b style='color:green;'>Market availability: US \| MX</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br>Example: b3261d2d-028a-4ef7-8602-633c23200af6<br><b style='color:green;'>Market availability: US \| MX</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br>Example: Walmart Marketplace<br><b style='color:green;'>Market availability: US \| MX</b> |
| <code>wm_market</code> | <code>[WmMarket3OrStr](walmart_apis/models/enums/wm_market3.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: US \| MX</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The value must be set to 3.1.<br><b style='color:green;'>Market availability: US \| MX</b> |
| <code>body</code> | <code>[RefundRequest](walmart_apis/models/refund_request.py) \| [RefundRequestDict](walmart_apis/models/refund_request.py)</code> | The request body. |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><b style='color:green;'>Market availability: US \| MX</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[Request](walmart_apis/models/request.py), [RefundRequestErrorBody](walmart_apis/errors/refund_request_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Request](walmart_apis/models/request.py)</code> -- success

**On `Failure`**: `error` is <code>[RefundRequestErrorBody](walmart_apis/errors/refund_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse3](walmart_apis/models/error_response3.py)</code> |
| 401 | <code>[Unauthorized1](walmart_apis/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](walmart_apis/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](walmart_apis/models/too_many_requests1.py)</code> |
| 500 | <code>[ErrorResponses](walmart_apis/models/error_responses.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def return_order_cursor(query_params: QueryParamsMx | QueryParamsMxDict, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket21OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ReturnOrdersResponses, ReturnOrderCursorErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API retrieves the details of all return orders based on the specified filter criteria and returns all orders in the response. It returns a nextCursorMark for the next 100 orders, and continues in this manner until the last order. The same API can also be used to search for a single order based on returnOrderId or customerOrderId.<br><b style='color:green;'>Market availability: MX</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.returns_refund.with_raw_response.return_order_cursor(
    QueryParamsMx(), "some example string", "some example string", WmMarket21.MX, WmGlobalVersion._3_1
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReturnOrdersResponses
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ReturnOrderCursorErrorBody
```

**Async**

```python
result = await async_client.returns_refund.with_raw_response.return_order_cursor(
    QueryParamsMx(), "some example string", "some example string", WmMarket21.MX, WmGlobalVersion._3_1
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReturnOrdersResponses
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ReturnOrderCursorErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>query_params</code> | <code>[QueryParamsMx](walmart_apis/models/query_params_mx.py) \| [QueryParamsMxDict](walmart_apis/models/query_params_mx.py)</code> | Value sent with the request. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br>Example: b3261d2d-028a-4ef7-8602-633c23200af6<br><b style='color:green;'>Market availability: MX</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br>Example: Walmart Marketplace<br><b style='color:green;'>Market availability: MX</b> |
| <code>wm_market</code> | <code>[WmMarket21OrStr](walmart_apis/models/enums/wm_market21.py)</code> | Identifies the Walmart Marketplace region for the request.<br><b style='color:green;'>Market availability: MX</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The value must be set to 3.1.<br><b style='color:green;'>Market availability: MX</b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><b style='color:green;'>Market availability: MX</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ReturnOrdersResponses](walmart_apis/models/return_orders_responses.py), [ReturnOrderCursorErrorBody](walmart_apis/errors/return_order_cursor_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ReturnOrdersResponses](walmart_apis/models/return_orders_responses.py)</code> -- success

**On `Failure`**: `error` is <code>[ReturnOrderCursorErrorBody](walmart_apis/errors/return_order_cursor_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse3](walmart_apis/models/error_response3.py)</code> |
| 401 | <code>[Unauthorized1](walmart_apis/models/unauthorized1.py)</code> |
| 403 | <code>[Forbidden1](walmart_apis/models/forbidden1.py)</code> |
| 429 | <code>[TooManyRequests1](walmart_apis/models/too_many_requests1.py)</code> |
| 500 | <code>[ErrorResponses](walmart_apis/models/error_responses.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Reviews

> Source: [Reviews](walmart_apis/apis/reviews.py)

<details>
<summary><code>def bulk_update_item_status(wm_global_version: WmGlobalVersionOrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, body: V3GrowthReviewsAcceleratorItemsStatusRequest | V3GrowthReviewsAcceleratorItemsStatusRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3GrowthReviewsAcceleratorItemsStatusResponse, BulkUpdateItemStatusErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use this API to enroll or disenroll items in the Review Accelerator Program (RAP).<br><b style='color:green;'>Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.reviews.with_raw_response.bulk_update_item_status(
    WmGlobalVersion._3_1,
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    WmMarket1.US,
    V3GrowthReviewsAcceleratorItemsStatusRequest(
        status=Status11.ENROLL, items=[Item9(item_id="2719243"), Item9(item_id="2719255")]
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3GrowthReviewsAcceleratorItemsStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BulkUpdateItemStatusErrorBody
```

**Async**

```python
result = await async_client.reviews.with_raw_response.bulk_update_item_status(
    WmGlobalVersion._3_1,
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    WmMarket1.US,
    V3GrowthReviewsAcceleratorItemsStatusRequest(
        status=Status11.ENROLL, items=[Item9(item_id="2719243"), Item9(item_id="2719255")]
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3GrowthReviewsAcceleratorItemsStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BulkUpdateItemStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The default is set to 3.1.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>body</code> | <code>[V3GrowthReviewsAcceleratorItemsStatusRequest](walmart_apis/models/v3_growth_reviews_accelerator_items_status_request.py) \| [V3GrowthReviewsAcceleratorItemsStatusRequestDict](walmart_apis/models/v3_growth_reviews_accelerator_items_status_request.py)</code> | Request fields |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3GrowthReviewsAcceleratorItemsStatusResponse](walmart_apis/models/v3_growth_reviews_accelerator_items_status_response.py), [BulkUpdateItemStatusErrorBody](walmart_apis/errors/bulk_update_item_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3GrowthReviewsAcceleratorItemsStatusResponse](walmart_apis/models/v3_growth_reviews_accelerator_items_status_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[BulkUpdateItemStatusErrorBody](walmart_apis/errors/bulk_update_item_status_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V3GrowthReviewsAcceleratorItemsStatus400Error1](walmart_apis/models/v3_growth_reviews_accelerator_items_status400_error1.py)</code> |
| 401 | <code>[V3GrowthReviewsAcceleratorItemsStatus401Error1](walmart_apis/models/v3_growth_reviews_accelerator_items_status401_error1.py)</code> |
| 403 | <code>[V3GrowthReviewsAcceleratorItemsStatus403Error1](walmart_apis/models/v3_growth_reviews_accelerator_items_status403_error1.py)</code> |
| 500 | <code>[V3GrowthReviewsAcceleratorItemsStatus500Error1](walmart_apis/models/v3_growth_reviews_accelerator_items_status500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_irp_categories(wm_global_version: WmGlobalVersionOrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, body: V3GrowthReviewsAcceleratorCategoriesRequest | V3GrowthReviewsAcceleratorCategoriesRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3GrowthReviewsAcceleratorCategoriesResponse, GetIrpCategoriesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use this API to get the set of categories the RAP post-purchase items belong to.<br><b style='color:green;'>Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.reviews.with_raw_response.get_irp_categories(
    WmGlobalVersion._3_1,
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    WmMarket1.US,
    V3GrowthReviewsAcceleratorCategoriesRequest(),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3GrowthReviewsAcceleratorCategoriesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetIrpCategoriesErrorBody
```

**Async**

```python
result = await async_client.reviews.with_raw_response.get_irp_categories(
    WmGlobalVersion._3_1,
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    WmMarket1.US,
    V3GrowthReviewsAcceleratorCategoriesRequest(),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3GrowthReviewsAcceleratorCategoriesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetIrpCategoriesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The default is set to 3.1.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>body</code> | <code>[V3GrowthReviewsAcceleratorCategoriesRequest](walmart_apis/models/v3_growth_reviews_accelerator_categories_request.py) \| [V3GrowthReviewsAcceleratorCategoriesRequestDict](walmart_apis/models/v3_growth_reviews_accelerator_categories_request.py)</code> | Request payload |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3GrowthReviewsAcceleratorCategoriesResponse](walmart_apis/models/v3_growth_reviews_accelerator_categories_response.py), [GetIrpCategoriesErrorBody](walmart_apis/errors/get_irp_categories_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3GrowthReviewsAcceleratorCategoriesResponse](walmart_apis/models/v3_growth_reviews_accelerator_categories_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetIrpCategoriesErrorBody](walmart_apis/errors/get_irp_categories_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V3GrowthReviewsAcceleratorCategories400Error1](walmart_apis/models/v3_growth_reviews_accelerator_categories400_error1.py)</code> |
| 401 | <code>[V3GrowthReviewsAcceleratorCategories401Error1](walmart_apis/models/v3_growth_reviews_accelerator_categories401_error1.py)</code> |
| 403 | <code>[V3GrowthReviewsAcceleratorCategories403Error1](walmart_apis/models/v3_growth_reviews_accelerator_categories403_error1.py)</code> |
| 500 | <code>[V3InsightsItemsListingQualityItems500Error1](walmart_apis/models/v3_insights_items_listing_quality_items500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_irp_items(wm_global_version: WmGlobalVersionOrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, body: V3GrowthReviewsAcceleratorItemsRequest | V3GrowthReviewsAcceleratorItemsRequestDict, *, scroll_id: str = "*", wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3GrowthReviewsAcceleratorItemsResponse, GetIrpItemsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To get all eligible products that can be enrolled in the Reviews Accelerator post-purchase program, as well as to retrieve all products currently enrolled in the program, and all products that have attained target reviews after enrollment, you can use the following criteria:
<li>Filter products by category and price.
<li>Sort products by Walmart-recommended item priorities.
<li>Search using wildcards to match the product name and SKU.<br><b style='color:green;'>Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.reviews.with_raw_response.get_irp_items(
    WmGlobalVersion._3_1,
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    WmMarket1.US,
    V3GrowthReviewsAcceleratorItemsRequest(filter=Filter1(item_status=ItemStatus8.ELIGIBLE)),
    scroll_id="some example string",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3GrowthReviewsAcceleratorItemsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetIrpItemsErrorBody
```

**Async**

```python
result = await async_client.reviews.with_raw_response.get_irp_items(
    WmGlobalVersion._3_1,
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    WmMarket1.US,
    V3GrowthReviewsAcceleratorItemsRequest(filter=Filter1(item_status=ItemStatus8.ELIGIBLE)),
    scroll_id="some example string",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3GrowthReviewsAcceleratorItemsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetIrpItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The default is set to 3.1.1<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>body</code> | <code>[V3GrowthReviewsAcceleratorItemsRequest](walmart_apis/models/v3_growth_reviews_accelerator_items_request.py) \| [V3GrowthReviewsAcceleratorItemsRequestDict](walmart_apis/models/v3_growth_reviews_accelerator_items_request.py)</code> | Request payload |
| <code>scroll_id</code> | <code>str</code> | Optional parameter specifying the scrollId to return the next set of results.<br><b style='color:green;'>Market availability: US only</b><br>**Default**: <code>"*"</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3GrowthReviewsAcceleratorItemsResponse](walmart_apis/models/v3_growth_reviews_accelerator_items_response.py), [GetIrpItemsErrorBody](walmart_apis/errors/get_irp_items_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3GrowthReviewsAcceleratorItemsResponse](walmart_apis/models/v3_growth_reviews_accelerator_items_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetIrpItemsErrorBody](walmart_apis/errors/get_irp_items_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V3GrowthReviewsAcceleratorItems400Error1](walmart_apis/models/v3_growth_reviews_accelerator_items400_error1.py)</code> |
| 401 | <code>[V3GrowthReviewsAcceleratorItems401Error1](walmart_apis/models/v3_growth_reviews_accelerator_items401_error1.py)</code> |
| 403 | <code>[V3GrowthReviewsAcceleratorItems403Error1](walmart_apis/models/v3_growth_reviews_accelerator_items403_error1.py)</code> |
| 500 | <code>[V3InsightsItemsListingQualityItems500Error1](walmart_apis/models/v3_insights_items_listing_quality_items500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## RichMedia

> Source: [RichMedia](walmart_apis/apis/rich_media.py)

<details>
<summary><code>def get_all_assets(wm_qos_correlation_id: str, wm_svc_name: str, *, page: int | None = 1, limit: int | None = 25, linked_gtins: list[str] | None = None, rich_media_title: str | None = None, rich_media_type: RichMediaTypeOrStr | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AssetsResponse, GetAllAssetsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use this API to retrieve rich media assets, including 360-spin images and videos, from the seller catalog. Assets can be created in seller center media library or programmatically through the API. Use this endpoint to retrieve the asset hash, which uniquely identifies each media asset for future management.

<b style="color: green;">Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.rich_media.with_raw_response.get_all_assets(
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    page=1,
    limit=25,
    linked_gtins=["00716999676446", "07815386164856"],
    rich_media_title="title",
    rich_media_type=RichMediaType.VIDEO,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssetsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAllAssetsErrorBody
```

**Async**

```python
result = await async_client.rich_media.with_raw_response.get_all_assets(
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    page=1,
    limit=25,
    linked_gtins=["00716999676446", "07815386164856"],
    rich_media_title="title",
    rich_media_type=RichMediaType.VIDEO,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssetsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAllAssetsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>page</code> | <code>int \| None</code> | Indicates the page number to return in the paginated result set. Use this parameter to navigate through multiple pages of results. The value should be a positive integer. For example, 1 for the first page, 2 for the second, and so on.<br><br><b style="color: green;">Market availability: US only</b><br>**Default**: <code>1</code> |
| <code>limit</code> | <code>int \| None</code> | Defines the maximum number of items to return per page when retrieving paginated data. Use this parameter to control the number of results included in a single page. The value should be a positive integer.<br><br><b style="color: green;">Market availability: US only</b><br>**Default**: <code>25</code> |
| <code>linked_gtins</code> | <code>list&#91;str&#93; \| None</code> | Filters assets by linked GTIN. Provide multiple GTINs as a list. If omitted, all assets are returned.<br><br><b style="color: green;">Market availability: US only</b><br>**Default**: <code>None</code> |
| <code>rich_media_title</code> | <code>str \| None</code> | Filters assets by rich media title or asset title. If omitted, all assets are returned.<br><br><b style="color: green;">Market availability: US only</b><br>**Default**: <code>None</code> |
| <code>rich_media_type</code> | <code>[RichMediaTypeOrStr](walmart_apis/models/enums/rich_media_type.py) \| None</code> | Filters assets by rich media type. Allowed values: `IMAGES360`, `VIDEO`.<br><br><b style="color: green;">Market availability: US only</b><br>**Default**: <code>None</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the consumer channel type received during onboarding.<br><br><b style="color: green;">Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[AssetsResponse](walmart_apis/models/assets_response.py), [GetAllAssetsErrorBody](walmart_apis/errors/get_all_assets_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AssetsResponse](walmart_apis/models/assets_response.py)</code> -- Successful operation. Returns matching rich media assets. When no items match the query, the response contains an empty payload and total records as 0.

**On `Failure`**: `error` is <code>[GetAllAssetsErrorBody](walmart_apis/errors/get_all_assets_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 429, 500 | <code>[RawError](walmart_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def rich_media_operation(wm_qos_correlation_id: str, wm_svc_name: str, body: RichMediaFeedRequest | RichMediaFeedRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FeedId1, RichMediaOperationErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use this API to create, update, or delink rich media assets for items in the seller catalog. Supported asset types are `IMAGES360` and `VIDEO`. Use this API to 1) add new rich media, 2) update associations for existing rich media, or 3) delink item association on existing rich media. Provide accessible media URLs and related metadata in the request body. Video assets require one video URL. 360-spin image assets require 24 image URLs.

<b style="color: green;">Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.rich_media.with_raw_response.rich_media_operation(
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    RichMediaFeedRequest(
        supplier_item_feed_header=SupplierItemFeedHeader(
            locale="some example string", version="some example string", sub_category=SubCategory.VIDEO
        ),
        supplier_item=[
            SupplierItemPayload(
                orderable=SupplierItemOrderable(product_id="some example string"), visible=VisibleVideoPayload()
            ),
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FeedId1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RichMediaOperationErrorBody
```

**Async**

```python
result = await async_client.rich_media.with_raw_response.rich_media_operation(
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    RichMediaFeedRequest(
        supplier_item_feed_header=SupplierItemFeedHeader(
            locale="some example string", version="some example string", sub_category=SubCategory.VIDEO
        ),
        supplier_item=[
            SupplierItemPayload(
                orderable=SupplierItemOrderable(product_id="some example string"), visible=VisibleVideoPayload()
            ),
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FeedId1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RichMediaOperationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>body</code> | <code>[RichMediaFeedRequest](walmart_apis/models/rich_media_feed_request.py) \| [RichMediaFeedRequestDict](walmart_apis/models/rich_media_feed_request.py)</code> | Rich media feed payload containing asset metadata, item associations, and media URLs. |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the consumer channel type received during onboarding.<br><br><b style="color: green;">Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[FeedId1](walmart_apis/models/feed_id1.py), [RichMediaOperationErrorBody](walmart_apis/errors/rich_media_operation_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FeedId1](walmart_apis/models/feed_id1.py)</code> -- Successful — The feed accepted and queued for processing

**On `Failure`**: `error` is <code>[RichMediaOperationErrorBody](walmart_apis/errors/rich_media_operation_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 429, 500 | <code>[RawError](walmart_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SemCampaignManagement

> Source: [SemCampaignManagement](walmart_apis/apis/sem_campaign_management.py)

<details>
<summary><code>def create_campaign(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, body: SemCampaignCreateRequest | SemCampaignCreateRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SemCampaignResponse, CreateCampaignErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API allows you to create a new campaign by providing the required details in the request. Upon successful creation, a unique campaign ID will be assigned to the newly created campaign for identification and management purposes.<br><b style='color:green;'>Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sem_campaign_management.with_raw_response.create_campaign(
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    SemCampaignCreateRequest(
        metadata=SemCampaignCreateMetadata(
            name="some example string", start_date="some example string", daily_budget=1.5
        ),
        items_operations=[SemCampaignItemsOperation(operation_type=OperationType.ADD, skus=["some example string"])],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SemCampaignResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateCampaignErrorBody
```

**Async**

```python
result = await async_client.sem_campaign_management.with_raw_response.create_campaign(
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    SemCampaignCreateRequest(
        metadata=SemCampaignCreateMetadata(
            name="some example string", start_date="some example string", daily_budget=1.5
        ),
        items_operations=[SemCampaignItemsOperation(operation_type=OperationType.ADD, skus=["some example string"])],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SemCampaignResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateCampaignErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. This is required for authenticating requests to Walmart Marketplace APIs. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID. |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. |
| <code>body</code> | <code>[SemCampaignCreateRequest](walmart_apis/models/sem_campaign_create_request.py) \| [SemCampaignCreateRequestDict](walmart_apis/models/sem_campaign_create_request.py)</code> | Request Payload |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[SemCampaignResponse](walmart_apis/models/sem_campaign_response.py), [CreateCampaignErrorBody](walmart_apis/errors/create_campaign_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SemCampaignResponse](walmart_apis/models/sem_campaign_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[CreateCampaignErrorBody](walmart_apis/errors/create_campaign_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 500 | <code>[SemErrorResponse400](walmart_apis/models/sem_error_response400.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_campaign(campaign_id: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SemCampaignResponse, DeleteCampaignErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API allows you to permanently remove an existing campaign from the system. Once deleted, the campaign and its unique ID will no longer be retrievable. The campaign's unique ID must be included in the request.<br><b style='color:green;'>Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sem_campaign_management.with_raw_response.delete_campaign(
    "some example string",
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SemCampaignResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteCampaignErrorBody
```

**Async**

```python
result = await async_client.sem_campaign_management.with_raw_response.delete_campaign(
    "some example string",
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SemCampaignResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteCampaignErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>campaign_id</code> | <code>str</code> | Campaign ID of the campaign to be deleted. |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. This is required for authenticating requests to Walmart Marketplace APIs. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID. |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[SemCampaignResponse](walmart_apis/models/sem_campaign_response.py), [DeleteCampaignErrorBody](walmart_apis/errors/delete_campaign_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SemCampaignResponse](walmart_apis/models/sem_campaign_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[DeleteCampaignErrorBody](walmart_apis/errors/delete_campaign_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 404, 500 | <code>[SemErrorResponse400](walmart_apis/models/sem_error_response400.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_campaign_details(campaign_id: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SemCampaign, GetCampaignDetailsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API allows you to retrieve detailed information about a specific campaign. Provide the campaign's unique ID in the request to fetch its attributes.<br><b style='color:green;'>Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sem_campaign_management.with_raw_response.get_campaign_details(
    "some example string",
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SemCampaign
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCampaignDetailsErrorBody
```

**Async**

```python
result = await async_client.sem_campaign_management.with_raw_response.get_campaign_details(
    "some example string",
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SemCampaign
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCampaignDetailsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>campaign_id</code> | <code>str</code> | Campaign ID of the campaign whose details are to be retrieved. |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. This is required for authenticating requests to Walmart Marketplace APIs. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID. |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[SemCampaign](walmart_apis/models/sem_campaign.py), [GetCampaignDetailsErrorBody](walmart_apis/errors/get_campaign_details_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SemCampaign](walmart_apis/models/sem_campaign.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetCampaignDetailsErrorBody](walmart_apis/errors/get_campaign_details_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 404, 500 | <code>[SemErrorResponse400](walmart_apis/models/sem_error_response400.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_campaign_recommendations(wm_svc_name: str, wm_qos_correlation_id: str, *, wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1, wm_market: WmMarketOrStr = WmMarket.US, accept: AcceptOrStr = Accept.APPLICATION_JSON, wm_consumer_channel_type: str | None = None, body: CampaignRecommendationsSearchRequest | CampaignRecommendationsSearchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CampaignRecommendationsSearchResponse, SearchCampaignRecommendationsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Search for campaign-level recommendations to improve SEM campaign performance. Returns a paginated list of active campaigns for the authenticated seller, each enriched with actionable recommendations — including budget adjustments and bidding strategy optimizations — along with projected performance impact metrics (clicks, impressions, ad spend).<br><b style='color:green;'>Market availability: US only</b>

### Why this API matters
SEM campaigns require continuous optimization to stay competitive. Budget constraints and suboptimal bidding strategies are the two most common reasons campaigns underperform. Without data-driven guidance, sellers either overspend without results or miss revenue opportunities by underspending.

This API bridges that gap by surfacing **machine-generated recommendations** for each active campaign, complete with projected impact on clicks, impressions, and ad spend. Partners can integrate these recommendations into their dashboards and automation pipelines to:
- **Increase ROAS**: Apply budget and bidding strategy recommendations to maximize return on ad spend
- **Reduce wasted spend**: Identify campaigns where budget is being underutilized or misallocated
- **Automate campaign tuning**: Build automated workflows that periodically fetch recommendations and apply them programmatically, reducing manual effort and reaction time
- **Enable data-driven decisions**: Each recommendation includes three impact scenarios (recommended, conservative, aggressive) so sellers can choose the option that fits their risk tolerance

### Key use cases
1. **Campaign Health Dashboard**: Display campaigns with pending recommendations, color-coded by type (`BUDGET` vs `BIDDING_STRATEGY`), with projected impact metrics
2. **Automated Budget Optimizer**: Periodically poll this API and auto-apply budget recommendations that meet a minimum projected ROAS threshold
3. **Bidding Strategy Advisor**: Surface bidding strategy change suggestions to sellers with before/after performance projections
4. **Bulk Campaign Management**: Retrieve all recommendations across campaigns in a single paginated call, enabling batch review and bulk application of changes

### How it works
The API returns only active campaigns that are eligible for recommendations. You can filter results using `campaignIds` or `recommendationType` (`BUDGET` or `BIDDING_STRATEGY`).

### Default behavior
- When no request body is provided, the API defaults to `offset=0`, `limit=10`.
- By default, the API returns recommendations for both `BUDGET` and `BIDDING_STRATEGY`.
- Results are not sorted by default; use the sort object to order by adspend.
- Returns only **active campaigns** that have at least one pending recommendation
- Results are not sorted by default; use the `sort` object to order by `adspend`

### Supported filters
Filters are combined with AND logic. Multiple values within a single filter act as OR.

| Filter Field              | Supported Values              | Description                                              |
|---------------------------|-------------------------------|----------------------------------------------------------|
| `campaignIds`             | Numeric string campaign IDs   | Filter by specific campaign identifiers                  |
| `recommendationType`  | `BUDGET`, `BIDDING_STRATEGY`  | Filter by recommendation type                            |

### Sorting
Results can be sorted using the `sort` object:

| Sort Field | Supported Orders | Description                              |
|------------|------------------|------------------------------------------|
| `adspend`  | `ASC`, `DESC`    | Sort campaigns by ad spend               |

### Recommendation types
| Type               | Description                                                              |
|--------------------|--------------------------------------------------------------------------|
| `BUDGET`           | Recommended total or daily budget adjustment to improve campaign reach    |
| `BIDDING_STRATEGY` | Recommended change to bidding strategy for better performance            |

### Response structure
Each response contains two top-level fields:
- `pagination`: Standard pagination metadata (`pageNo`, `pageSize`, `totalCount`, `totalPages`, `hasNextPage`, `hasPreviousPage`)
- `data`: Array of campaign-level suggestions. Each campaign includes current settings (bidding strategy, target ROAS, daily budget) and an array of `campaignRecommendations` with projected performance impact at three levels: recommended, minimum, and maximum.

### Performance impact projections
Each recommendation includes a `recommendedValueImpact` object with up to three scenarios:
- **recommended**: The optimal suggested value (marked `isRecommended: true`)
- **minRecommendation**: A conservative lower-bound option (may be `null` if not applicable)
- **maxRecommendation**: An aggressive upper-bound option

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sem_campaign_management.with_raw_response.search_campaign_recommendations(
    "Walmart Marketplace",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    wm_global_version=WmGlobalVersion._3_1,
    wm_market=WmMarket.US,
    accept=Accept.APPLICATION_JSON,
    body=CampaignRecommendationsSearchRequest(page=CampaignRecommendationsPage(offset=0, limit=10)),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CampaignRecommendationsSearchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchCampaignRecommendationsErrorBody
```

**Async**

```python
result = await async_client.sem_campaign_management.with_raw_response.search_campaign_recommendations(
    "Walmart Marketplace",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    wm_global_version=WmGlobalVersion._3_1,
    wm_market=WmMarket.US,
    accept=Accept.APPLICATION_JSON,
    body=CampaignRecommendationsSearchRequest(page=CampaignRecommendationsPage(offset=0, limit=10)),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CampaignRecommendationsSearchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchCampaignRecommendationsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID. |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br>**Default**: <code>WmGlobalVersion._3_1</code> |
| <code>wm_market</code> | <code>[WmMarketOrStr](walmart_apis/models/enums/wm_market.py)</code> | Identifies the Walmart Marketplace region for the request.<br>**Default**: <code>WmMarket.US</code> |
| <code>accept</code> | <code>[AcceptOrStr](walmart_apis/models/enums/accept.py)</code> | The expected response content type.<br>**Default**: <code>Accept.APPLICATION_JSON</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[CampaignRecommendationsSearchRequest](walmart_apis/models/campaign_recommendations_search_request.py) \| [CampaignRecommendationsSearchRequestDict](walmart_apis/models/campaign_recommendations_search_request.py) \| None</code> | Optional search request with pagination, sorting, and filters. Defaults to `offset=0`, `limit=10` with no filters and no sorting if body is absent.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CampaignRecommendationsSearchResponse](walmart_apis/models/campaign_recommendations_search_response.py), [SearchCampaignRecommendationsErrorBody](walmart_apis/errors/search_campaign_recommendations_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CampaignRecommendationsSearchResponse](walmart_apis/models/campaign_recommendations_search_response.py)</code> -- Campaign recommendations retrieved successfully

**On `Failure`**: `error` is <code>[SearchCampaignRecommendationsErrorBody](walmart_apis/errors/search_campaign_recommendations_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 422, 500, 503 | <code>[ErrorResponse](walmart_apis/models/error_response.py)</code> |
| 429 | <code>[ErrorResponse429](walmart_apis/models/error_response429.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stop_campaign(campaign_id: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SemCampaignResponse, StopCampaignErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API allows you to stop an active campaign. Stopping a campaign does not delete it but prevents further actions. The campaign's unique ID must be included in the request.<br><b style='color:green;'>Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sem_campaign_management.with_raw_response.stop_campaign(
    "some example string",
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SemCampaignResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type StopCampaignErrorBody
```

**Async**

```python
result = await async_client.sem_campaign_management.with_raw_response.stop_campaign(
    "some example string",
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SemCampaignResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type StopCampaignErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>campaign_id</code> | <code>str</code> | Campaign ID of the campaign to be stopped. |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. This is required for authenticating requests to Walmart Marketplace APIs. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID. |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[SemCampaignResponse](walmart_apis/models/sem_campaign_response.py), [StopCampaignErrorBody](walmart_apis/errors/stop_campaign_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SemCampaignResponse](walmart_apis/models/sem_campaign_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[StopCampaignErrorBody](walmart_apis/errors/stop_campaign_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 404, 500 | <code>[SemErrorResponse400](walmart_apis/models/sem_error_response400.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_campaign(campaign_id: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, body: SemCampaignUpdateRequest | SemCampaignUpdateRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SemCampaignResponse, UpdateCampaignErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API allows you to modify an existing campaign's details and manage its associated items. You must provide the campaign's unique ID along with the necessary changes in the request. The specified updates will be applied while preserving the campaign's unique identifier.<br><b style='color:green;'>Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sem_campaign_management.with_raw_response.update_campaign(
    "some example string",
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    SemCampaignUpdateRequest(),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SemCampaignResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateCampaignErrorBody
```

**Async**

```python
result = await async_client.sem_campaign_management.with_raw_response.update_campaign(
    "some example string",
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    SemCampaignUpdateRequest(),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SemCampaignResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateCampaignErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>campaign_id</code> | <code>str</code> | Campaign ID of the campaign to be updated. |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. This is required for authenticating requests to Walmart Marketplace APIs. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID. |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. |
| <code>body</code> | <code>[SemCampaignUpdateRequest](walmart_apis/models/sem_campaign_update_request.py) \| [SemCampaignUpdateRequestDict](walmart_apis/models/sem_campaign_update_request.py)</code> | Request Payload |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[SemCampaignResponse](walmart_apis/models/sem_campaign_response.py), [UpdateCampaignErrorBody](walmart_apis/errors/update_campaign_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SemCampaignResponse](walmart_apis/models/sem_campaign_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[UpdateCampaignErrorBody](walmart_apis/errors/update_campaign_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 404, 500 | <code>[SemErrorResponse400](walmart_apis/models/sem_error_response400.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SemCatalog

> Source: [SemCatalog](walmart_apis/apis/sem_catalog.py)

<details>
<summary><code>def get_eligible_items(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, body: SemItemEligibilityRequest | SemItemEligibilityRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SemCatalogueResponse, GetEligibleItemsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API allows you to check whether an item from your catalog meets the required conditions for Search Engine Marketing ads.<br><b style='color:green;'>Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sem_catalog.with_raw_response.get_eligible_items(
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    SemItemEligibilityRequest(filters=[SemFilter(field="some example string", values=["some example string"])]),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SemCatalogueResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEligibleItemsErrorBody
```

**Async**

```python
result = await async_client.sem_catalog.with_raw_response.get_eligible_items(
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    SemItemEligibilityRequest(filters=[SemFilter(field="some example string", values=["some example string"])]),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SemCatalogueResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEligibleItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. This is required for authenticating requests to Walmart Marketplace APIs. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID. |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. |
| <code>body</code> | <code>[SemItemEligibilityRequest](walmart_apis/models/sem_item_eligibility_request.py) \| [SemItemEligibilityRequestDict](walmart_apis/models/sem_item_eligibility_request.py)</code> | Request Payload |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[SemCatalogueResponse](walmart_apis/models/sem_catalogue_response.py), [GetEligibleItemsErrorBody](walmart_apis/errors/get_eligible_items_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SemCatalogueResponse](walmart_apis/models/sem_catalogue_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetEligibleItemsErrorBody](walmart_apis/errors/get_eligible_items_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 500 | <code>[SemErrorResponse400](walmart_apis/models/sem_error_response400.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_item_recommendations(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, *, limit: int | None = 100, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SemCatalogueResponse, GetItemRecommendationsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API allows you to fetch a list of top recommended items from your catalog. You can customize the number of recommendations to be returned by adjusting the request parameter.<br><b style='color:green;'>Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sem_catalog.with_raw_response.get_item_recommendations(
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SemCatalogueResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetItemRecommendationsErrorBody
```

**Async**

```python
result = await async_client.sem_catalog.with_raw_response.get_item_recommendations(
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SemCatalogueResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetItemRecommendationsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. This is required for authenticating requests to Walmart Marketplace APIs. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID. |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. |
| <code>limit</code> | <code>int \| None</code> | Specifies the maximum number of recommended items to be returned. This value cannot exceed 200.<br>**Default**: <code>100</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[SemCatalogueResponse](walmart_apis/models/sem_catalogue_response.py), [GetItemRecommendationsErrorBody](walmart_apis/errors/get_item_recommendations_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SemCatalogueResponse](walmart_apis/models/sem_catalogue_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetItemRecommendationsErrorBody](walmart_apis/errors/get_item_recommendations_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 500 | <code>[SemErrorResponse400](walmart_apis/models/sem_error_response400.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SemItemDiagnostics

> Source: [SemItemDiagnostics](walmart_apis/apis/sem_item_diagnostics.py)

<details>
<summary><code>def get_issue_types(wm_svc_name: str, wm_qos_correlation_id: str, *, wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1, wm_market: WmMarketOrStr = WmMarket.US, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[dict[str, IssueMetadata], GetIssueTypesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the complete, authoritative metadata for all SEM eligibility issue types (~61 issue types, ~5KB).<br><b style='color:green;'>Market availability: US only</b>

Items used in Search Engine Marketing (SEM) campaigns such as Google Shopping Ads must meet specific content, quality, and policy requirements before they can be advertised on search engines. When items fail to meet these requirements, they are flagged with specific issue types that either **block** the item from being advertised entirely or **limit** its visibility and performance in SEM.

This endpoint returns the complete catalog of all issue types that can affect an item's SEM eligibility, along with human-readable names, descriptions, remediation guidance, severity categories, and help links. It serves as the **single source of truth** for issue metadata.

### Current scope
The issue types returned by this endpoint apply to items that are currently part of active SEM campaigns. The `POST /item-issues/search` endpoint uses these issue types to report diagnostics on campaign items.

### Future extensibility
In a future release, the `POST /item-issues/search` endpoint will support querying diagnostic issues for any item in the seller's catalog — even items not yet added to a campaign — using the `itemId` filter. The same issue types returned by this endpoint will apply to those items as well, enabling sellers to proactively diagnose and fix issues before campaign onboarding.

### SEM eligibility issue categories
Each issue type belongs to one of three categories that indicate its impact on an item's ability to be advertised on search engines:

| Category     | Count | SEM Impact                                                                     |
|--------------|-------|--------------------------------------------------------------------------------|
| `BLOCKED`    | ~49   | Item **cannot be advertised** on search engines. Must be resolved before the item can appear in SEM ads. Examples: `ITEM_OUT_OF_STOCK`, `POLICY_VIOLATION`, `MISSING_INVALID_TITLE`, `INVALID_IMAGE`, `BUYBOX_NOT_WINNER` |
| `LIMITED`    | ~11   | Item **can be advertised but with reduced visibility** or performance on search engines. Resolving these issues improves ad reach and effectiveness. Examples: `TITLE_TOO_LONG`, `LOW_IMAGE_QUALITY`, `DESCRIPTION_TOO_SHORT`, `LOW_OFFER_LISTING_QUALITY` |
| `NO_ISSUES`  | ~1    | Informational statuses such as `DUPLICATE_OFFER` — item has no SEM eligibility issues |

### Actionable vs non-actionable issues
Each issue type includes an `isFixable` flag that indicates whether the seller can resolve the issue:
- `isFixable=true`: Seller can take action to restore or improve SEM eligibility (For example, restock inventory, update title, improve image quality). Partners should surface these with a "Fix Now" UI affordance.
- `isFixable=false`: Requires Walmart or system intervention (For example, Google policy violations, BuyBox eligibility). Partners should display these as informational — the seller cannot directly resolve them.

### Response structure
The response is a map keyed by `issueType` (string), where each value is an `IssueMetadata` object containing:
- `issueName`: Human-readable short headline for UI display (For example, "Item Out of Stock")
- `issueCategory`: SEM eligibility impact — `BLOCKED` (cannot advertise on search engines) or `LIMITED` (reduced SEM visibility)
- `isFixable`: Whether the partner can remediate this issue to restore SEM eligibility
- `issueDescription`: Human-readable description with specific remediation guidance (For example, "Item is out of stock. Add inventory to make the item available.")
- `learnMoreUrl`: Help link to Walmart-hosted or Google support documentation for step-by-step remediation. May be null for some issue types.

### Recommended usage pattern
1. Call this endpoint **once** on application initialization
2. Cache the result locally (recommended **TTL: 24 hours**)
3. Use cached metadata to enrich items returned by the `POST /item-issues/search` endpoint — match each item's `issueType` to the cached metadata for display name, description, and help links
4. Use `isFixable` to drive UI affordances: show "Fix Now" buttons for fixable SEM issues, informational badges for non-fixable ones
5. Use `learnMoreUrl` to deep-link to help documentation for step-by-step remediation guidance
6. Use `issueCategory` to color-code or badge issues in your UI: red for `BLOCKED` (cannot advertise), yellow for `LIMITED` (reduced SEM performance)

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sem_item_diagnostics.with_raw_response.get_issue_types(
    "Walmart Marketplace",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    wm_global_version=WmGlobalVersion._3_1,
    wm_market=WmMarket.US,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type dict[str, IssueMetadata]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetIssueTypesErrorBody
```

**Async**

```python
result = await async_client.sem_item_diagnostics.with_raw_response.get_issue_types(
    "Walmart Marketplace",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    wm_global_version=WmGlobalVersion._3_1,
    wm_market=WmMarket.US,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type dict[str, IssueMetadata]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetIssueTypesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID. |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br>**Default**: <code>WmGlobalVersion._3_1</code> |
| <code>wm_market</code> | <code>[WmMarketOrStr](walmart_apis/models/enums/wm_market.py)</code> | Identifies the Walmart Marketplace region for the request.<br>**Default**: <code>WmMarket.US</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;dict&#91;str, [IssueMetadata](walmart_apis/models/issue_metadata.py)&#93;, [GetIssueTypesErrorBody](walmart_apis/errors/get_issue_types_error.py)&#93;</code>

**On `Success`**: `payload` is <code>dict&#91;str, [IssueMetadata](walmart_apis/models/issue_metadata.py)&#93;</code> -- Issue types metadata retrieved successfully

**On `Failure`**: `error` is <code>[GetIssueTypesErrorBody](walmart_apis/errors/get_issue_types_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 403, 500, 503 | <code>[ErrorResponse](walmart_apis/models/error_response.py)</code> |
| 429 | <code>[ErrorResponse429](walmart_apis/models/error_response429.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_item_issues(wm_svc_name: str, wm_qos_correlation_id: str, *, wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1, wm_market: WmMarketOrStr = WmMarket.US, accept: AcceptOrStr = Accept.APPLICATION_JSON, wm_consumer_channel_type: str | None = None, body: ItemDiagnosticSearchRequest | ItemDiagnosticSearchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ItemDiagnosticSearchResponse, SearchItemIssuesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Search for item-level diagnostic issues that block or limit items from being used in Search Engine Marketing (SEM). Returns paginated, item-level diagnostic details including campaign associations, issue types, severity, remediation guidance, and overall item status.<br><b style='color:green;'>Market availability: US only</b>

Items in SEM campaigns must meet content, quality, and policy requirements before they can be advertised on search engines (For example, Google Shopping Ads). This endpoint surfaces the specific issues preventing or limiting an item's SEM eligibility, along with actionable remediation guidance so sellers can resolve problems and restore advertising reach.

### Current scope
This endpoint currently returns diagnostics for **items that are part of active SEM campaigns** for the authenticated seller. Each item in the response includes its `campaignAssociations` — the list of campaigns the item belongs to. Items not associated with any campaign are not included in the results.

### Default behavior
- When no request body is provided, defaults to `offset=0`, `limit=100` with no filters
- When no `issueCategory` filter is provided, returns **only items with issues** (`BLOCKED` or `LIMITED`)
- To include healthy items, explicitly pass `issueCategory` filter with `NO_ISSUES` or all three values
- By default, the API prioritizes returning actionable diagnostic issues rather than healthy items. This reduces payload size and improves relevance

### Supported filters
Filters are combined with AND logic. Multiple values within a single filter act as OR.

| Filter Field    | Supported Values                          | Max Values | Description                                              |
|-----------------|-------------------------------------------|------------|----------------------------------------------------------|
| `issues`        | Any valid `issueType` enum value          | 100        | Filter by specific SEM issue types (For example, `ITEM_OUT_OF_STOCK`, `TITLE_TOO_LONG`, `POLICY_VIOLATION`) |
| `issueCategory` | `LIMITED`, `BLOCKED`, `NO_ISSUES`         | 100        | Filter by SEM issue severity — `BLOCKED` items cannot be advertised at all, `LIMITED` items have reduced SEM performance |
| `itemId`        | Numeric string item IDs                   | 100        | Filter by Walmart catalog item identifiers within the seller's active campaigns. *In a future release, this filter will also support items outside of campaigns.* |

### Response structure
Each response contains two top-level fields:
- `pagination`: Standard pagination metadata including `hasNextPage`/`hasPreviousPage` for convenient UI navigation
- `data`: Array of item-level diagnostics. Each item appears **once** per unique `offerId` with all campaign associations listed. Each item includes an `issueCategory` field representing the overall SEM eligibility status of the item, and an `issues` array containing issue type identifiers. Issues are item-level, not campaign-specific — a blocked item is blocked in all SEM campaigns it belongs to.

Issue metadata (name, description, fixability, help links) is not included in this response. Partners should use the dedicated `GET /item-issues/issue-types` endpoint to retrieve complete issue metadata and cache it locally (TTL: 24 hours).

### Issue categories
| Category     | SEM Impact                                                                     |
|--------------|--------------------------------------------------------------------------------|
| `BLOCKED`    | Item **cannot be advertised** on search engines. Must be resolved before the item can appear in SEM ads. Examples: out of stock, missing title, policy violation, invalid image. |
| `LIMITED`    | Item **can be advertised but with reduced visibility** or performance on search engines. Resolving these issues improves ad reach and effectiveness. Examples: title too long, low image quality, description too short. |
| `NO_ISSUES`  | Item has no SEM issues and can be advertised normally with full visibility.      |

### Actionable vs non-actionable issues
Each issue type has an `isFixable` flag available via the `GET /item-issues/issue-types` reference endpoint:
- `isFixable=true`: Seller can fix the issue to restore SEM eligibility (For example, restock inventory, update title, fix image). Partners should surface these with a "Fix Now" UI affordance.
- `isFixable=false`: Requires Walmart or system intervention (For example, Google policy violations). Partners should display these as informational — the seller cannot directly resolve them.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sem_item_diagnostics.with_raw_response.search_item_issues(
    "Walmart Marketplace",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    wm_global_version=WmGlobalVersion._3_1,
    wm_market=WmMarket.US,
    accept=Accept.APPLICATION_JSON,
    body=ItemDiagnosticSearchRequest(page=DiagnosticPage(offset=0, limit=20)),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemDiagnosticSearchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchItemIssuesErrorBody
```

**Async**

```python
result = await async_client.sem_item_diagnostics.with_raw_response.search_item_issues(
    "Walmart Marketplace",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    wm_global_version=WmGlobalVersion._3_1,
    wm_market=WmMarket.US,
    accept=Accept.APPLICATION_JSON,
    body=ItemDiagnosticSearchRequest(page=DiagnosticPage(offset=0, limit=20)),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemDiagnosticSearchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchItemIssuesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID. |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br>**Default**: <code>WmGlobalVersion._3_1</code> |
| <code>wm_market</code> | <code>[WmMarketOrStr](walmart_apis/models/enums/wm_market.py)</code> | Identifies the Walmart Marketplace region for the request.<br>**Default**: <code>WmMarket.US</code> |
| <code>accept</code> | <code>[AcceptOrStr](walmart_apis/models/enums/accept.py)</code> | The expected response content type.<br>**Default**: <code>Accept.APPLICATION_JSON</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[ItemDiagnosticSearchRequest](walmart_apis/models/item_diagnostic_search_request.py) \| [ItemDiagnosticSearchRequestDict](walmart_apis/models/item_diagnostic_search_request.py) \| None</code> | Optional search request with pagination and filters.<br>Defaults to `offset=0`, `limit=100` with no filters if body is absent.<br>When no `issueCategory` filter is provided, only items with issues (`BLOCKED` or `LIMITED`) are returned.<br>This reduces payload size and improves relevance — diagnostics API consumers typically want problems, not healthy-item confirmation.<br>To include all items, explicitly pass `issueCategory` filter with all three values: `LIMITED`, `BLOCKED`, `NO_ISSUES`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ItemDiagnosticSearchResponse](walmart_apis/models/item_diagnostic_search_response.py), [SearchItemIssuesErrorBody](walmart_apis/errors/search_item_issues_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ItemDiagnosticSearchResponse](walmart_apis/models/item_diagnostic_search_response.py)</code> -- Search results retrieved successfully

**On `Failure`**: `error` is <code>[SearchItemIssuesErrorBody](walmart_apis/errors/search_item_issues_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 422, 500, 503 | <code>[ErrorResponse](walmart_apis/models/error_response.py)</code> |
| 429 | <code>[ErrorResponse429](walmart_apis/models/error_response429.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SemReporting

> Source: [SemReporting](walmart_apis/apis/sem_reporting.py)

<details>
<summary><code>def get_billing_history(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, body: SemBillingHistoryRequest | SemBillingHistoryRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SemBillingHistoryResponse, GetBillingHistoryErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API allows you to fetch your billing history.<br><b style='color:green;'>Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sem_reporting.with_raw_response.get_billing_history(
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SemBillingHistoryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetBillingHistoryErrorBody
```

**Async**

```python
result = await async_client.sem_reporting.with_raw_response.get_billing_history(
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SemBillingHistoryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetBillingHistoryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. This is required for authenticating requests to Walmart Marketplace APIs. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID. |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[SemBillingHistoryRequest](walmart_apis/models/sem_billing_history_request.py) \| [SemBillingHistoryRequestDict](walmart_apis/models/sem_billing_history_request.py) \| None</code> | Request Payload<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[SemBillingHistoryResponse](walmart_apis/models/sem_billing_history_response.py), [GetBillingHistoryErrorBody](walmart_apis/errors/get_billing_history_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SemBillingHistoryResponse](walmart_apis/models/sem_billing_history_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetBillingHistoryErrorBody](walmart_apis/errors/get_billing_history_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 500 | <code>[SemErrorResponse400](walmart_apis/models/sem_error_response400.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_campaign_level_summary(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, body: SemReportRequest | SemReportRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SemCampaignLevelReportResponse, GetCampaignLevelSummaryErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API allows you to fetch comprehensive performance metrics for all campaigns, allowing you to analyze key performance indicators based on specified filtering and sorting criteria.<br><b style='color:green;'>Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sem_reporting.with_raw_response.get_campaign_level_summary(
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SemCampaignLevelReportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCampaignLevelSummaryErrorBody
```

**Async**

```python
result = await async_client.sem_reporting.with_raw_response.get_campaign_level_summary(
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SemCampaignLevelReportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCampaignLevelSummaryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. This is required for authenticating requests to Walmart Marketplace APIs. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID. |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[SemReportRequest](walmart_apis/models/sem_report_request.py) \| [SemReportRequestDict](walmart_apis/models/sem_report_request.py) \| None</code> | Request Payload<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[SemCampaignLevelReportResponse](walmart_apis/models/sem_campaign_level_report_response.py), [GetCampaignLevelSummaryErrorBody](walmart_apis/errors/get_campaign_level_summary_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SemCampaignLevelReportResponse](walmart_apis/models/sem_campaign_level_report_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetCampaignLevelSummaryErrorBody](walmart_apis/errors/get_campaign_level_summary_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 500 | <code>[SemErrorResponse400](walmart_apis/models/sem_error_response400.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_item_level_summary(campaign_id: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, body: SemReportRequest | SemReportRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SemItemLevelReportResponse, GetItemLevelSummaryErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API allows you to fetch comprehensive performance metrics for all the items in a specific campaign, allowing you to analyze key performance indicators based on specified filtering and sorting criteria.<br><b style='color:green;'>Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sem_reporting.with_raw_response.get_item_level_summary(
    "some example string",
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SemItemLevelReportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetItemLevelSummaryErrorBody
```

**Async**

```python
result = await async_client.sem_reporting.with_raw_response.get_item_level_summary(
    "some example string",
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SemItemLevelReportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetItemLevelSummaryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>campaign_id</code> | <code>str</code> | Campaign ID of the campaign whose item-level performance report is to be retrieved. |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. This is required for authenticating requests to Walmart Marketplace APIs. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID. |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[SemReportRequest](walmart_apis/models/sem_report_request.py) \| [SemReportRequestDict](walmart_apis/models/sem_report_request.py) \| None</code> | Request Payload<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[SemItemLevelReportResponse](walmart_apis/models/sem_item_level_report_response.py), [GetItemLevelSummaryErrorBody](walmart_apis/errors/get_item_level_summary_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SemItemLevelReportResponse](walmart_apis/models/sem_item_level_report_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetItemLevelSummaryErrorBody](walmart_apis/errors/get_item_level_summary_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 404, 500 | <code>[SemErrorResponse400](walmart_apis/models/sem_error_response400.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SeoRecommendations

> Source: [SeoRecommendations](walmart_apis/apis/seo_recommendations.py)

<details>
<summary><code>def get_seo_recommendations(wm_qos_correlation_id: str, wm_svc_name: str, accept: str, *, status: Status2OrStr | None = None, limit: str | None = None, next_cursor: str | None = None, previous_cursor: str | None = None, wm_consumer_channel_type: str | None = None, body: V3SeoRecommendationGetItemsRequest | V3SeoRecommendationGetItemsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3SeoRecommendationGetItemsResponse, GetSeoRecommendationsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get list of items with SEO recommendations. Sellers can filter items by status (all, new, accepted, rejected), search for specific items using identifiers like (itemId, sku, or name) and paginate results for large datasets..

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.seo_recommendations.with_raw_response.get_seo_recommendations(
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    "application/json",
    limit="200",
    next_cursor="*",
    previous_cursor="1374004777531007833",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3SeoRecommendationGetItemsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSeoRecommendationsErrorBody
```

**Async**

```python
result = await async_client.seo_recommendations.with_raw_response.get_seo_recommendations(
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    "application/json",
    limit="200",
    next_cursor="*",
    previous_cursor="1374004777531007833",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3SeoRecommendationGetItemsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSeoRecommendationsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name |
| <code>accept</code> | <code>str</code> | Only supported Media Type : application/json |
| <code>status</code> | <code>[Status2OrStr](walmart_apis/models/enums/status2.py) \| None</code> | Specifies the type of items to retrieve. Default when type not provided it will return new items.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>str \| None</code> | Specify number of items to return. If no limit is specified, API returns 200 items by default.<br>**Default**: <code>None</code> |
| <code>next_cursor</code> | <code>str \| None</code> | Link to go to the next page<br>**Default**: <code>None</code> |
| <code>previous_cursor</code> | <code>str \| None</code> | Link to go to the previous page<br>**Default**: <code>None</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[V3SeoRecommendationGetItemsRequest](walmart_apis/models/v3_seo_recommendation_get_items_request.py) \| [V3SeoRecommendationGetItemsRequestDict](walmart_apis/models/v3_seo_recommendation_get_items_request.py) \| None</code> | This will contain the wild card search related details<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3SeoRecommendationGetItemsResponse](walmart_apis/models/v3_seo_recommendation_get_items_response.py), [GetSeoRecommendationsErrorBody](walmart_apis/errors/get_seo_recommendations_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3SeoRecommendationGetItemsResponse](walmart_apis/models/v3_seo_recommendation_get_items_response.py)</code> -- OK. The request was successful. The server returned the requested data.

**On `Failure`**: `error` is <code>[GetSeoRecommendationsErrorBody](walmart_apis/errors/get_seo_recommendations_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V3SeoRecommendationGetItems400Error1](walmart_apis/models/v3_seo_recommendation_get_items400_error1.py)</code> |
| 500 | <code>[V3SeoRecommendationGetItems500Error1](walmart_apis/models/v3_seo_recommendation_get_items500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_seo_recommendations(item_id: str, decision: DecisionOrStr, wm_qos_correlation_id: str, wm_svc_name: str, accept: str, *, wm_consumer_channel_type: str | None = None, body: V3SeoRecommendationUpdateItemsRequest | V3SeoRecommendationUpdateItemsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3SeoRecommendationUpdateItemsResponse, UpdateSeoRecommendationsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Sellers can accept or reject SEO recommendations with optimal feedback for rejected recommendations

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.seo_recommendations.with_raw_response.update_seo_recommendations(
    "some example string",
    Decision.APPROVED,
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    "application/json",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3SeoRecommendationUpdateItemsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateSeoRecommendationsErrorBody
```

**Async**

```python
result = await async_client.seo_recommendations.with_raw_response.update_seo_recommendations(
    "some example string",
    Decision.APPROVED,
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    "application/json",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3SeoRecommendationUpdateItemsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateSeoRecommendationsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>item_id</code> | <code>str</code> | Unique Item Identifier |
| <code>decision</code> | <code>[DecisionOrStr](walmart_apis/models/enums/decision.py)</code> | approve/reject a recommendation |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name |
| <code>accept</code> | <code>str</code> | Only supported Media Type : application/json |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[V3SeoRecommendationUpdateItemsRequest](walmart_apis/models/v3_seo_recommendation_update_items_request.py) \| [V3SeoRecommendationUpdateItemsRequestDict](walmart_apis/models/v3_seo_recommendation_update_items_request.py) \| None</code> | Additional details required for submission<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3SeoRecommendationUpdateItemsResponse](walmart_apis/models/v3_seo_recommendation_update_items_response.py), [UpdateSeoRecommendationsErrorBody](walmart_apis/errors/update_seo_recommendations_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3SeoRecommendationUpdateItemsResponse](walmart_apis/models/v3_seo_recommendation_update_items_response.py)</code> -- OK. The SEO recommendation update was successful

**On `Failure`**: `error` is <code>[UpdateSeoRecommendationsErrorBody](walmart_apis/errors/update_seo_recommendations_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V3SeoRecommendationUpdateItems400Error1](walmart_apis/models/v3_seo_recommendation_update_items400_error1.py)</code> |
| 404 | <code>[V3SeoRecommendationUpdateItems404Error1](walmart_apis/models/v3_seo_recommendation_update_items404_error1.py)</code> |
| 500 | <code>[V3SeoRecommendationUpdateItems500Error1](walmart_apis/models/v3_seo_recommendation_update_items500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ShipWithWalmart

> Source: [ShipWithWalmart](walmart_apis/apis/ship_with_walmart.py)

<details>
<summary><code>def create_label(accept: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3ShippingLabelsRequest | V3ShippingLabelsRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3ShippingLabelsResponse, CreateLabelErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Generates a shipping label using the provided shipment information. A successful response includes a tracking number and a label file in the media type specified in the Accept header.<br><br>This API is supported for <b>all shipping programs</b>, including <b>Walmart Provided Shipping (WPS)</b> and <b>Ship with Walmart (SWW)</b>.<br><br><b>Media Type Options (via Accept header):</b><br>• application/json, application/pdf → Returns label in PDF format.
• application/json, image/png → Returns label in PNG format.
• application/json → Returns tracking info only in JSON. <br><br> <b>Note:</b> The <b>Ship with Walmart service from China to the U.S.</b> is <b>paused until further notice</b>.

<b style="color: green;">Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.ship_with_walmart.with_raw_response.create_label(
    "application/json",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3ShippingLabelsRequest(
        package_type="CUSTOM_PACKAGE",
        box_dimensions=BoxDimensions3(
            box_length=13,
            box_width=9,
            box_height=0,
            box_weight=13,
            box_dimension_unit=BoxDimensionUnit3.IN,
            box_weight_unit=BoxWeightUnit3.LB,
        ),
        box_items=[BoxItem6(sku="PRECISE3PGLASS9", quantity=1, line_number="1")],
        from_address=FromAddress2(
            contact_name="Test Seller",
            company_name="Test Company",
            address_line1="Add1",
            address_line2="Add2",
            city="Anchorage",
            state="AK",
            postal_code="99501",
            country="US",
            phone="12253",
            email="test@walmart.com",
        ),
        purchase_order_id="97108719025934786",
        carrier_name="FedEx",
        carrier_service_type="FEDEX_2_DAY",
        hazmat=True,
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ShippingLabelsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateLabelErrorBody
```

**Async**

```python
result = await async_client.ship_with_walmart.with_raw_response.create_label(
    "application/json",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3ShippingLabelsRequest(
        package_type="CUSTOM_PACKAGE",
        box_dimensions=BoxDimensions3(
            box_length=13,
            box_width=9,
            box_height=0,
            box_weight=13,
            box_dimension_unit=BoxDimensionUnit3.IN,
            box_weight_unit=BoxWeightUnit3.LB,
        ),
        box_items=[BoxItem6(sku="PRECISE3PGLASS9", quantity=1, line_number="1")],
        from_address=FromAddress2(
            contact_name="Test Seller",
            company_name="Test Company",
            address_line1="Add1",
            address_line2="Add2",
            city="Anchorage",
            state="AK",
            postal_code="99501",
            country="US",
            phone="12253",
            email="test@walmart.com",
        ),
        purchase_order_id="97108719025934786",
        carrier_name="FedEx",
        carrier_service_type="FEDEX_2_DAY",
        hazmat=True,
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ShippingLabelsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateLabelErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>accept</code> | <code>str</code> | Specifies the desired response format. The order of media types determines the priority for format selection.<br><br>**Supported values:**<br>- `application/json` : Returns tracking information only (no label file).<br>- `application/json, application/pdf` : Returns the label in PDF format.<br>- `application/json, image/png` : Returns the label in PNG format.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br>Example: Walmart Marketplace<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Case-sensitive market identifier. Valid values: MX, CA, CL, US <br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The value must be set to 3.1.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>body</code> | <code>[V3ShippingLabelsRequest](walmart_apis/models/v3_shipping_labels_request.py) \| [V3ShippingLabelsRequestDict](walmart_apis/models/v3_shipping_labels_request.py)</code> | Label fields |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding<br><br><b style="color: green;">Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3ShippingLabelsResponse](walmart_apis/models/v3_shipping_labels_response.py), [CreateLabelErrorBody](walmart_apis/errors/create_label_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3ShippingLabelsResponse](walmart_apis/models/v3_shipping_labels_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[CreateLabelErrorBody](walmart_apis/errors/create_label_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 500 | <code>[V3ShippingLabels500Error1](walmart_apis/models/v3_shipping_labels500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_label_mps(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket11OrStr, wm_global_version: WmGlobalVersionOrStr, accept: str, body: V3ShippingMultiPackageLabelsRequest | V3ShippingMultiPackageLabelsRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3ShippingMultiPackageLabelsResponse, CreateLabelMpsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a shipping label for items, supporting multiple packages per request. A successful response includes a tracking number and a label file in the media type specified by the Accept header. This API supports <b>all shipping programs</b>, including <b>Walmart Provided Shipping (WPS)</b> and <b>Ship with Walmart (SWW)</b>.<br><br><b>Media Type Options (via Accept header):</b><br>•application/json, application/pdf → Returns the label in PDF format.<br>•application/json → Returns tracking info only, in JSON format.

<b style="color: green;">Market availability: CA | MX</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.ship_with_walmart.with_raw_response.create_label_mps(
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket11.MX,
    WmGlobalVersion._3_1,
    "application/json",
    V3ShippingMultiPackageLabelsRequest(
        package_dimensions=[
            PackageDimension(
                package_type="CUSTOM_PACKAGE",
                box_dimensions=BoxDimensions4(
                    box_dimension_unit=BoxDimensionUnit4.IN,
                    box_weight_unit=BoxWeightUnit4.LB,
                    box_weight=3,
                    box_length=9,
                    box_width=12,
                    box_height=1,
                ),
            ),
            PackageDimension(
                package_type="CUSTOM_PACKAGE",
                box_dimensions=BoxDimensions4(
                    box_dimension_unit=BoxDimensionUnit4.IN,
                    box_weight_unit=BoxWeightUnit4.LB,
                    box_weight=3,
                    box_length=9,
                    box_width=12,
                    box_height=1,
                ),
            ),
            PackageDimension(
                package_type="CUSTOM_PACKAGE",
                box_dimensions=BoxDimensions4(
                    box_dimension_unit=BoxDimensionUnit4.IN,
                    box_weight_unit=BoxWeightUnit4.LB,
                    box_weight=3,
                    box_length=9,
                    box_width=12,
                    box_height=1,
                ),
            ),
        ],
        box_items=[BoxItem8(sku="EDF07661449630550", quantity=1, country_of_origin="MX", line_number="1")],
        from_address=FromAddress3(
            contact_name="Test",
            company_name="Walmart",
            address_line1="Add1",
            address_line2="Add2",
            city="Anchorage",
            state="AK",
            postal_code="99501",
            country="US",
            phone="12253",
            email="test@walmart.com",
        ),
        purchase_order_id="309006496534952",
        carrier_name="FedEx",
        carrier_service_type="FEDEX_INTERNATIONAL_ECONOMY",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ShippingMultiPackageLabelsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateLabelMpsErrorBody
```

**Async**

```python
result = await async_client.ship_with_walmart.with_raw_response.create_label_mps(
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket11.MX,
    WmGlobalVersion._3_1,
    "application/json",
    V3ShippingMultiPackageLabelsRequest(
        package_dimensions=[
            PackageDimension(
                package_type="CUSTOM_PACKAGE",
                box_dimensions=BoxDimensions4(
                    box_dimension_unit=BoxDimensionUnit4.IN,
                    box_weight_unit=BoxWeightUnit4.LB,
                    box_weight=3,
                    box_length=9,
                    box_width=12,
                    box_height=1,
                ),
            ),
            PackageDimension(
                package_type="CUSTOM_PACKAGE",
                box_dimensions=BoxDimensions4(
                    box_dimension_unit=BoxDimensionUnit4.IN,
                    box_weight_unit=BoxWeightUnit4.LB,
                    box_weight=3,
                    box_length=9,
                    box_width=12,
                    box_height=1,
                ),
            ),
            PackageDimension(
                package_type="CUSTOM_PACKAGE",
                box_dimensions=BoxDimensions4(
                    box_dimension_unit=BoxDimensionUnit4.IN,
                    box_weight_unit=BoxWeightUnit4.LB,
                    box_weight=3,
                    box_length=9,
                    box_width=12,
                    box_height=1,
                ),
            ),
        ],
        box_items=[BoxItem8(sku="EDF07661449630550", quantity=1, country_of_origin="MX", line_number="1")],
        from_address=FromAddress3(
            contact_name="Test",
            company_name="Walmart",
            address_line1="Add1",
            address_line2="Add2",
            city="Anchorage",
            state="AK",
            postal_code="99501",
            country="US",
            phone="12253",
            email="test@walmart.com",
        ),
        purchase_order_id="309006496534952",
        carrier_name="FedEx",
        carrier_service_type="FEDEX_INTERNATIONAL_ECONOMY",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ShippingMultiPackageLabelsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateLabelMpsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket11OrStr](walmart_apis/models/enums/wm_market11.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default. Valid values: MX, CA, CL.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The value must be set to 3.1.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>accept</code> | <code>str</code> | Response type. The order of media types in the Accept header determines the priority for response format selection.<br><br><b style="color: green;">Market availability: CA</b> |
| <code>body</code> | <code>[V3ShippingMultiPackageLabelsRequest](walmart_apis/models/v3_shipping_multi_package_labels_request.py) \| [V3ShippingMultiPackageLabelsRequestDict](walmart_apis/models/v3_shipping_multi_package_labels_request.py)</code> | Label fields |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding<br><br><b style="color: green;">Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3ShippingMultiPackageLabelsResponse](walmart_apis/models/v3_shipping_multi_package_labels_response.py), [CreateLabelMpsErrorBody](walmart_apis/errors/create_label_mps_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3ShippingMultiPackageLabelsResponse](walmart_apis/models/v3_shipping_multi_package_labels_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[CreateLabelMpsErrorBody](walmart_apis/errors/create_label_mps_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>list&#91;[Error5](walmart_apis/models/error5.py)&#93;</code> |
| 500 | <code>[V3ShippingMultiPackageLabels500Error1](walmart_apis/models/v3_shipping_multi_package_labels500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def discard_label(carrier_short_name: str, tracking_no: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket6OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3ShippingLabelsCarriersTrackingsResponse, DiscardLabelErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Marks a previously generated shipping label as discarded.
This API is used when the label should no longer be used for shipment processing. <br><br> <b>Applicable Shipping Programs:</b><br>This API is supported for the following <b>shipping programs:  Walmart Provided Shipping (WPS) and Ship with Walmart (SWW).</b>

<b style="color: green;">Market availability: US | CA | MX</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.ship_with_walmart.with_raw_response.discard_label(
    "some example string",
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket6.MX,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ShippingLabelsCarriersTrackingsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DiscardLabelErrorBody
```

**Async**

```python
result = await async_client.ship_with_walmart.with_raw_response.discard_label(
    "some example string",
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket6.MX,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ShippingLabelsCarriersTrackingsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DiscardLabelErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>carrier_short_name</code> | <code>str</code> | The short name of the shipping carrier.<br>Use the carrierShortName value returned from the Supported Carriers API to ensure compatibility.<br><br><b style="color: green;">Market availability: US \| CA \| MX</b> |
| <code>tracking_no</code> | <code>str</code> | The shipment tracking number.<br><br><br><br><b style="color: green;">Market availability: US \| CA \| MX</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID. <br> Example: b3261d2d-028a-4ef7-8602-633c23200af6 <br> <b style="color: green;">Market availability: Global </b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. <br> Example: Walmart Marketplace.<br><br><b style="color: green;">Market availability: Global </b> |
| <code>wm_market</code> | <code>[WmMarket6OrStr](walmart_apis/models/enums/wm_market6.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default. Valid values: MX, US<br><br><b style="color: green;">Market availability: Global </b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The value must be set to 3.1.<br><br><b style="color: green;">Market availability: Global </b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><b style="color: green;">Market availability: Global </b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3ShippingLabelsCarriersTrackingsResponse](walmart_apis/models/v3_shipping_labels_carriers_trackings_response.py), [DiscardLabelErrorBody](walmart_apis/errors/discard_label_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3ShippingLabelsCarriersTrackingsResponse](walmart_apis/models/v3_shipping_labels_carriers_trackings_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[DiscardLabelErrorBody](walmart_apis/errors/discard_label_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>list&#91;[V3ShippingLabelsCarriersTrackings400Error1](walmart_apis/models/v3_shipping_labels_carriers_trackings400_error1.py)&#93;</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_carrier_package_types(carrier_short_name: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket11OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3ShippingLabelsCarriersPackageTypesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API retrieves all supported package types for the selected carrier.

<b style="color: green;">Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.ship_with_walmart.with_raw_response.get_carrier_package_types(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket11.MX,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ShippingLabelsCarriersPackageTypesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.ship_with_walmart.with_raw_response.get_carrier_package_types(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket11.MX,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ShippingLabelsCarriersPackageTypesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>carrier_short_name</code> | <code>str</code> | carrierShortName fetched from carrier API response or pass 'ALL' to fetch all package types of supported carriers<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and is used to track and debug issues. Use a random generated GUID for this ID.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket11OrStr](walmart_apis/models/enums/wm_market11.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default. Valid values: MX, CA, CL.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The value must be set to 3.1.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding<br><br><b style="color: green;">Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3ShippingLabelsCarriersPackageTypesResponse](walmart_apis/models/v3_shipping_labels_carriers_package_types_response.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3ShippingLabelsCarriersPackageTypesResponse](walmart_apis/models/v3_shipping_labels_carriers_package_types_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_carriers(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket11OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3ShippingLabelsCarriersResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API retrieves all carriers supported by Ship With Walmart.

<b style="color: green;">Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.ship_with_walmart.with_raw_response.get_carriers(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket11.MX, WmGlobalVersion._3_1
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ShippingLabelsCarriersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.ship_with_walmart.with_raw_response.get_carriers(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmMarket11.MX, WmGlobalVersion._3_1
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ShippingLabelsCarriersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket11OrStr](walmart_apis/models/enums/wm_market11.py)</code> | Case-sensitive market identifier. Valid values: MX, CA, CL<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The value must be set to 3.1.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding<br><br><b style="color: green;">Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3ShippingLabelsCarriersResponse](walmart_apis/models/v3_shipping_labels_carriers_response.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3ShippingLabelsCarriersResponse](walmart_apis/models/v3_shipping_labels_carriers_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_label(purchase_order_id: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket11OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3ShippingLabelsPurchaseOrdersResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API retrieves all label details generated for a purchase order id.

<b style="color: green;">Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.ship_with_walmart.with_raw_response.get_label(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket11.MX,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ShippingLabelsPurchaseOrdersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.ship_with_walmart.with_raw_response.get_label(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket11.MX,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ShippingLabelsPurchaseOrdersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>purchase_order_id</code> | <code>str</code> | purchaseOrderId<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket11OrStr](walmart_apis/models/enums/wm_market11.py)</code> | Case-sensitive market identifier. Valid values: MX, CA, CL<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding<br><br><b style="color: green;">Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3ShippingLabelsPurchaseOrdersResponse](walmart_apis/models/v3_shipping_labels_purchase_orders_response.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3ShippingLabelsPurchaseOrdersResponse](walmart_apis/models/v3_shipping_labels_purchase_orders_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_label_by_tracking_and_carrier(carrier_short_name: str, tracking_no: str, accept: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket11OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the shipping label for a specific carrier and tracking number combination.
The response includes the tracking number and the label in the requested media type (PDF or PNG), based on the Accept header provided. <br><br> <b>Media Type Options:</b><br>•Accept: application/json,application/pdf → Returns label in PDF format.<br>•Accept: application/json,image/png → Returns label in PNG format. <br><br><b>Market and Shipment Program Applicability:</b><br>•<b>CL</b> : Applicable for <b>International</b> shipments only.<br>•<b>US, MX, CA</b>: Applicable for <b>Domestic and International</b> shipments across <b>all shipping programs</b> (including <b>Walmart Provided Shipping (WPS)</b> and <b>Ship with Walmart (SWW)</b>).

<b style="color: green;">Market availability: Global</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.ship_with_walmart.with_raw_response.get_label_by_tracking_and_carrier(
    "some example string",
    "some example string",
    "application/pdf",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket11.MX,
    WmGlobalVersion._3_1,
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.ship_with_walmart.with_raw_response.get_label_by_tracking_and_carrier(
    "some example string",
    "some example string",
    "application/pdf",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket11.MX,
    WmGlobalVersion._3_1,
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>carrier_short_name</code> | <code>str</code> | carrierShortName<br><br><b style="color: green;">Market availability: Global</b> |
| <code>tracking_no</code> | <code>str</code> | trackingNo<br><br><b style="color: green;">Market availability: Global</b> |
| <code>accept</code> | <code>str</code> | Supported media types for US, CA, MX are:\napplication/pdf, image/png. For CL, the supported media type is\napplication/pdf, image/png, application/zpl.\n\n<b style=\"color: green;\">Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Walmart Service Name<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket11OrStr](walmart_apis/models/enums/wm_market11.py)</code> | Case-sensitive market identifier. Valid values: MX, CA, CL<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The value must be set to 3.1.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding<br><br><b style="color: green;">Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;None, [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_scan_form_by_manifest_id(manifest_id: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarketOrStr, wm_global_version: WmGlobalVersionOrStr, accept: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FileResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API retrieves a scan form for a given manifest ID.

**Rate Limits:** This endpoint allows 100 requests per minute. Exceeding this limit returns a `429 Too Many Requests` response. See the [Rate Limiting guide](https://developer.walmart.com/us-marketplace/docs/rate-limiting) for full details. The response includes `x-current-token-count` (remaining requests in the current window) and `X-Next-Replenishment-Time` (when the token count next increases).

**Sandbox:** Use base URL `https://sandbox.walmartapis.com`. The sandbox returns a stub binary document for any valid sandbox `manifestId`. The `documentFormat` selection (PDF/ZPL/PNG) is honored in production; in sandbox, a PDF stub is always returned regardless of the format requested during scan form creation.

**Note:** This endpoint returns a binary document stream (application/octet-stream). Treat the response body as bytes and save it to a file. The underlying document format aligns with the scan form documentFormat selected during creation (for example, PDF, ZPL, PNG).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.ship_with_walmart.with_raw_response.get_scan_form_by_manifest_id(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    WmMarket.US,
    WmGlobalVersion._3_1,
    "application/octet-stream",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.ship_with_walmart.with_raw_response.get_scan_form_by_manifest_id(
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    WmMarket.US,
    WmGlobalVersion._3_1,
    "application/octet-stream",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AsyncFileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>manifest_id</code> | <code>str</code> | Manifest ID returned by the create scan form API. Use this value to download the scan form document. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarketOrStr](walmart_apis/models/enums/wm_market.py)</code> | Case-sensitive market identifier. Valid values: US<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The value must be set to 3.1.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>accept</code> | <code>str</code> | Requested response media type. This endpoint returns a binary document stream (application/octet-stream). Treat the response body as bytes.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><b style="color: green;">Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;FileResponse, [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>FileResponse</code>, its body not yet read -- Successful operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_shipping_estimate(accept: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket11OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3ShippingLabelsShippingEstimatesRequest | V3ShippingLabelsShippingEstimatesRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3ShippingLabelsShippingEstimatesResponse, GetShippingEstimateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API retrieves shipping cost estimates for available shipping services based on address and package (example, customer address, packaged weight.)

<b style="color: green;">Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.ship_with_walmart.with_raw_response.get_shipping_estimate(
    "application/json",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket11.MX,
    WmGlobalVersion._3_1,
    V3ShippingLabelsShippingEstimatesRequest(
        box_dimensions=BoxDimensions5(
            box_length=6,
            box_width=6,
            box_height=6,
            box_weight=0.8,
            box_dimension_unit=BoxDimensionUnit.IN,
            box_weight_unit=BoxWeightUnit.LB,
        ),
        deliver_by_date="2023-06-07T23:00:00.611Z",
        ship_by_date="2023-06-05T08:00:00.611Z",
        from_address=FromAddress4(
            postal_code="91776",
            country_code="US",
            address_lines=["311 E VALLEY BLVD STE 112 PMB 271as"],
            city="SAN GABRIEL1as",
            state="CA",
        ),
        to_address=ToAddress1(
            postal_code="94085",
            country_code="US",
            address_lines=["748 N Mathilda Ave", "Room # 224"],
            city="SUNNYVALE",
            state="CA",
        ),
        carriers=["FEDEX"],
        package_type="CUSTOM_PACKAGE",
        include_services_not_meeting_delivery_promise=True,
        purchase_order_id="91088062299813853",
        box_items=[BoxItem10(sku="sku-1NMeZnK1B1MNJdXde5771022", quantity=1, line_number="1")],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ShippingLabelsShippingEstimatesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetShippingEstimateErrorBody
```

**Async**

```python
result = await async_client.ship_with_walmart.with_raw_response.get_shipping_estimate(
    "application/json",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket11.MX,
    WmGlobalVersion._3_1,
    V3ShippingLabelsShippingEstimatesRequest(
        box_dimensions=BoxDimensions5(
            box_length=6,
            box_width=6,
            box_height=6,
            box_weight=0.8,
            box_dimension_unit=BoxDimensionUnit.IN,
            box_weight_unit=BoxWeightUnit.LB,
        ),
        deliver_by_date="2023-06-07T23:00:00.611Z",
        ship_by_date="2023-06-05T08:00:00.611Z",
        from_address=FromAddress4(
            postal_code="91776",
            country_code="US",
            address_lines=["311 E VALLEY BLVD STE 112 PMB 271as"],
            city="SAN GABRIEL1as",
            state="CA",
        ),
        to_address=ToAddress1(
            postal_code="94085",
            country_code="US",
            address_lines=["748 N Mathilda Ave", "Room # 224"],
            city="SUNNYVALE",
            state="CA",
        ),
        carriers=["FEDEX"],
        package_type="CUSTOM_PACKAGE",
        include_services_not_meeting_delivery_promise=True,
        purchase_order_id="91088062299813853",
        box_items=[BoxItem10(sku="sku-1NMeZnK1B1MNJdXde5771022", quantity=1, line_number="1")],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ShippingLabelsShippingEstimatesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetShippingEstimateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>accept</code> | <code>str</code> | Response type. The order of media types in the Accept header determines the priority for response format selection.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. <br> Example: Walmart Marketplace<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarket11OrStr](walmart_apis/models/enums/wm_market11.py)</code> | Case-sensitive market identifier. Valid values: MX, CA, CL<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The value must be set to 3.1.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>body</code> | <code>[V3ShippingLabelsShippingEstimatesRequest](walmart_apis/models/v3_shipping_labels_shipping_estimates_request.py) \| [V3ShippingLabelsShippingEstimatesRequestDict](walmart_apis/models/v3_shipping_labels_shipping_estimates_request.py)</code> | Shipping fields |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><b style="color: green;">Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3ShippingLabelsShippingEstimatesResponse](walmart_apis/models/v3_shipping_labels_shipping_estimates_response.py), [GetShippingEstimateErrorBody](walmart_apis/errors/get_shipping_estimate_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3ShippingLabelsShippingEstimatesResponse](walmart_apis/models/v3_shipping_labels_shipping_estimates_response.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[GetShippingEstimateErrorBody](walmart_apis/errors/get_shipping_estimate_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>list&#91;[V3ShippingLabelsShippingEstimates400Error1](walmart_apis/models/v3_shipping_labels_shipping_estimates400_error1.py)&#93;</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def scan_form(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarketOrStr, wm_global_version: WmGlobalVersionOrStr, accept: str, body: V3ShippingScanFormRequest | V3ShippingScanFormRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3ShippingScanFormResponse, ScanFormErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API generates a scan form using the provided tracking numbers. The scan form is a consolidated document that contains all the tracking numbers and shipping details for the packages being shipped out on a particular day. It is used by carriers to verify and process the shipments during pickup and delivery. Currently, only USPS supports scan forms.

**Idempotency:** `scanFormId` acts as a natural idempotency key — the client supplies it in the request body before the call. Submitting a second POST with a `scanFormId` that was already successfully processed returns `409 Conflict`; no duplicate scan form is created. On network failure or timeout, clients may safely retry using the same `scanFormId`. This guarantee is critical for EOD automation — a duplicate manifest can cause carrier processing errors and shipment delays.

**Rate Limits:** This endpoint allows 100 requests per minute. Exceeding this limit returns a `429 Too Many Requests` response. See the [Rate Limiting guide](https://developer.walmart.com/us-marketplace/docs/rate-limiting) for full details. The response includes `x-current-token-count` (remaining requests in the current window) and `X-Next-Replenishment-Time` (when the token count next increases).

**Sandbox:** Use base URL `https://sandbox.walmartapis.com`. The sandbox accepts test tracking numbers and returns a synthetic `manifestId` (e.g. `SANDBOX-12345`). Use that `manifestId` with the GET endpoint to retrieve the stub scan form document.

<b style="color: green;">Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.ship_with_walmart.with_raw_response.scan_form(
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    WmMarket.US,
    WmGlobalVersion._3_1,
    "application/json",
    V3ShippingScanFormRequest(
        scan_form_id="string",
        carrier_name="USPS",
        ship_on_date="2025-08-23",
        from_address=FromAddress5(
            contact_name="John Doe",
            company_name="Walmart",
            address_line1="1375 Crossman Ave",
            address_line2="string",
            city="Sunnyvale",
            state="CA",
            postal_code="63116",
            country="US",
            phone="6172012456",
            email="",
        ),
        tracking_numbers=["100044481029", "100044481030"],
        document_format="PDF",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ShippingScanFormResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ScanFormErrorBody
```

**Async**

```python
result = await async_client.ship_with_walmart.with_raw_response.scan_form(
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    WmMarket.US,
    WmGlobalVersion._3_1,
    "application/json",
    V3ShippingScanFormRequest(
        scan_form_id="string",
        carrier_name="USPS",
        ship_on_date="2025-08-23",
        from_address=FromAddress5(
            contact_name="John Doe",
            company_name="Walmart",
            address_line1="1375 Crossman Ave",
            address_line2="string",
            city="Sunnyvale",
            state="CA",
            postal_code="63116",
            country="US",
            phone="6172012456",
            email="",
        ),
        tracking_numbers=["100044481029", "100044481030"],
        document_format="PDF",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ShippingScanFormResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ScanFormErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarketOrStr](walmart_apis/models/enums/wm_market.py)</code> | Case-sensitive market identifier. Valid values: US<br><br><b style="color: green;">Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The value must be set to 3.1.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>accept</code> | <code>str</code> | Response media type. Only supported media type: application/json.<br><br><b style="color: green;">Market availability: Global</b> |
| <code>body</code> | <code>[V3ShippingScanFormRequest](walmart_apis/models/v3_shipping_scan_form_request.py) \| [V3ShippingScanFormRequestDict](walmart_apis/models/v3_shipping_scan_form_request.py)</code> | Scan form request payload, including carrier, ship date, origin address, and tracking numbers to include in the manifest. |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><b style="color: green;">Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3ShippingScanFormResponse](walmart_apis/models/v3_shipping_scan_form_response.py), [ScanFormErrorBody](walmart_apis/errors/scan_form_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3ShippingScanFormResponse](walmart_apis/models/v3_shipping_scan_form_response.py)</code> -- Successful operation

**On `Failure`**: `error` is <code>[ScanFormErrorBody](walmart_apis/errors/scan_form_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 409 | <code>[RawError](walmart_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ShipmentProtection

> Source: [ShipmentProtection](walmart_apis/apis/shipment_protection.py)

<details>
<summary><code>def download_claim_documents(claim_number: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, body: V3ClaimsShipmentProtectionClaimDocumentsRequest | V3ClaimsShipmentProtectionClaimDocumentsRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FileResponse, DownloadClaimDocumentsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a ZIP file containing one or more uploaded claim documents.<br><b style='color:green;'>Market availability: US Only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.shipment_protection.with_raw_response.download_claim_documents(
    "some example string",
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    V3ClaimsShipmentProtectionClaimDocumentsRequest(document_ids=["some example string"]),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadClaimDocumentsErrorBody
```

**Async**

```python
result = await async_client.shipment_protection.with_raw_response.download_claim_documents(
    "some example string",
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    V3ClaimsShipmentProtectionClaimDocumentsRequest(document_ids=["some example string"]),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AsyncFileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadClaimDocumentsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>claim_number</code> | <code>str</code> | Exact claim number for filtering (query) or identifying a specific claim (path). |
| <code>wm_sec_access_token</code> | <code>str</code> | The access token retrieved in the Token API call. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and is used to track and debug issues; use a randomly generated GUID for this ID. |
| <code>wm_svc_name</code> | <code>str</code> | Walmart service name—for Marketplace APIs simply use `Walmart Service Name` or the service identifier provided by Walmart. |
| <code>body</code> | <code>[V3ClaimsShipmentProtectionClaimDocumentsRequest](walmart_apis/models/v3_claims_shipment_protection_claim_documents_request.py) \| [V3ClaimsShipmentProtectionClaimDocumentsRequestDict](walmart_apis/models/v3_claims_shipment_protection_claim_documents_request.py)</code> | The request body. |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;FileResponse, [DownloadClaimDocumentsErrorBody](walmart_apis/errors/download_claim_documents_error.py)&#93;</code>

**On `Success`**: `payload` is <code>FileResponse</code>, its body not yet read -- ZIP file of documents

**On `Failure`**: `error` is <code>[DownloadClaimDocumentsErrorBody](walmart_apis/errors/download_claim_documents_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V3ClaimsShipmentProtectionClaimDocuments400Error1](walmart_apis/models/v3_claims_shipment_protection_claim_documents400_error1.py)</code> |
| 404 | <code>[V3ClaimsShipmentProtectionClaimDocuments404Error1](walmart_apis/models/v3_claims_shipment_protection_claim_documents404_error1.py)</code> |
| 500 | <code>[V3ClaimsShipmentProtectionClaimDocuments500Error1](walmart_apis/models/v3_claims_shipment_protection_claim_documents500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_claim_details(claim_number: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, GetClaimDetailsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves detailed information for a single claim.<br><b style='color:green;'>Market availability: US Only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.shipment_protection.with_raw_response.get_claim_details(
    "some example string",
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetClaimDetailsErrorBody
```

**Async**

```python
result = await async_client.shipment_protection.with_raw_response.get_claim_details(
    "some example string",
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetClaimDetailsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>claim_number</code> | <code>str</code> | Exact claim number for filtering (query) or identifying a specific claim (path). |
| <code>wm_sec_access_token</code> | <code>str</code> | The access token retrieved in the Token API call. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and is used to track and debug issues; use a randomly generated GUID for this ID. |
| <code>wm_svc_name</code> | <code>str</code> | Walmart service name—for Marketplace APIs simply use `Walmart Service Name` or the service identifier provided by Walmart. |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [GetClaimDetailsErrorBody](walmart_apis/errors/get_claim_details_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Details retrieved successfully.

**On `Failure`**: `error` is <code>[GetClaimDetailsErrorBody](walmart_apis/errors/get_claim_details_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V3ClaimsShipmentProtectionClaim400Error1](walmart_apis/models/v3_claims_shipment_protection_claim400_error1.py)</code> |
| 404 | <code>[V3ClaimsShipmentProtectionClaim404Error1](walmart_apis/models/v3_claims_shipment_protection_claim404_error1.py)</code> |
| 500 | <code>[V3ClaimsShipmentProtectionClaim500Error1](walmart_apis/models/v3_claims_shipment_protection_claim500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_claim_history(claim_number: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3ClaimsShipmentProtectionClaimHistoryResponse, GetClaimHistoryErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a chronological log of status changes, notes, and uploaded documents.<br><b style='color:green;'>Market availability: US Only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.shipment_protection.with_raw_response.get_claim_history(
    "some example string",
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ClaimsShipmentProtectionClaimHistoryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetClaimHistoryErrorBody
```

**Async**

```python
result = await async_client.shipment_protection.with_raw_response.get_claim_history(
    "some example string",
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3ClaimsShipmentProtectionClaimHistoryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetClaimHistoryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>claim_number</code> | <code>str</code> | Exact claim number for filtering (query) or identifying a specific claim (path). |
| <code>wm_sec_access_token</code> | <code>str</code> | The access token retrieved in the Token API call. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and is used to track and debug issues; use a randomly generated GUID for this ID. |
| <code>wm_svc_name</code> | <code>str</code> | Walmart service name—for Marketplace APIs simply use `Walmart Service Name` or the service identifier provided by Walmart. |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3ClaimsShipmentProtectionClaimHistoryResponse](walmart_apis/models/v3_claims_shipment_protection_claim_history_response.py), [GetClaimHistoryErrorBody](walmart_apis/errors/get_claim_history_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3ClaimsShipmentProtectionClaimHistoryResponse](walmart_apis/models/v3_claims_shipment_protection_claim_history_response.py)</code> -- History retrieved successfully.

**On `Failure`**: `error` is <code>[GetClaimHistoryErrorBody](walmart_apis/errors/get_claim_history_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V3ClaimsShipmentProtectionClaimHistory400Error1](walmart_apis/models/v3_claims_shipment_protection_claim_history400_error1.py)</code> |
| 404 | <code>[V3ClaimsShipmentProtectionClaimHistory404Error1](walmart_apis/models/v3_claims_shipment_protection_claim_history404_error1.py)</code> |
| 500 | <code>[V3ClaimsShipmentProtectionClaimHistory500Error1](walmart_apis/models/v3_claims_shipment_protection_claim_history500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_claims(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, *, limit: int | None = 25, offset: int | None = 0, claims_group: ClaimsGroupOrStr | None = None, claim_number: str | None = None, purchase_order_id: str | None = None, tracking_no: str | None = None, claim_types: str | None = None, claim_statuses: str | None = None, sort_by: SortByOrStr | None = None, sort_order: OrderOrStr | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, ListClaimsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a paginated list of claims, with optional filters.<br><b style='color:green;'>Market availability: US Only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.shipment_protection.with_raw_response.list_claims(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....", "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListClaimsErrorBody
```

**Async**

```python
result = await async_client.shipment_protection.with_raw_response.list_claims(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....", "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListClaimsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_sec_access_token</code> | <code>str</code> | The access token retrieved in the Token API call. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and is used to track and debug issues; use a randomly generated GUID for this ID. |
| <code>wm_svc_name</code> | <code>str</code> | Walmart service name—for Marketplace APIs simply use `Walmart Service Name` or the service identifier provided by Walmart. |
| <code>limit</code> | <code>int \| None</code> | Maximum number of results to return in the response page (default 25, maximum 300).<br>**Default**: <code>25</code> |
| <code>offset</code> | <code>int \| None</code> | Zero‑based index of the first result to return (default 0). Use together with `limit` for pagination.<br>**Default**: <code>0</code> |
| <code>claims_group</code> | <code>[ClaimsGroupOrStr](walmart_apis/models/enums/claims_group.py) \| None</code> | Filter claims by broad status group: OPEN, ACTION_NEEDED, or CLOSED.<br>**Default**: <code>None</code> |
| <code>claim_number</code> | <code>str \| None</code> | Exact claim number for filtering (query) or identifying a specific claim (path).<br>**Default**: <code>None</code> |
| <code>purchase_order_id</code> | <code>str \| None</code> | Filter by the Walmart purchase order ID associated with the claim.<br>**Default**: <code>None</code> |
| <code>tracking_no</code> | <code>str \| None</code> | Filter by the package tracking number associated with the claim.<br>**Default**: <code>None</code> |
| <code>claim_types</code> | <code>str \| None</code> | Comma‑separated list of claim types to include (LIT, LAD, DAMAGED).<br>**Default**: <code>None</code> |
| <code>claim_statuses</code> | <code>str \| None</code> | Comma‑separated list of claim status codes to include (INITIATED, IN_REVIEW, NEED_INFO, etc.).<br>**Default**: <code>None</code> |
| <code>sort_by</code> | <code>[SortByOrStr](walmart_apis/models/enums/sort_by.py) \| None</code> | Field to sort by; currently supports `claimDate`.<br>**Default**: <code>None</code> |
| <code>sort_order</code> | <code>[OrderOrStr](walmart_apis/models/enums/order.py) \| None</code> | Sort direction: `ASC` for ascending or `DESC` for descending (default DESC).<br>**Default**: <code>None</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [ListClaimsErrorBody](walmart_apis/errors/list_claims_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Claims retrieved successfully.

**On `Failure`**: `error` is <code>[ListClaimsErrorBody](walmart_apis/errors/list_claims_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V3ClaimsShipmentProtection400Error1](walmart_apis/models/v3_claims_shipment_protection400_error1.py)</code> |
| 401 | <code>[V3ClaimsShipmentProtection401Error1](walmart_apis/models/v3_claims_shipment_protection401_error1.py)</code> |
| 500 | <code>[V3ClaimsShipmentProtection500Error1](walmart_apis/models/v3_claims_shipment_protection500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def submit_additional_info(claim_number: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, files: FileInput, document_types: list[DocumentType1 | DocumentType1Dict], *, wm_consumer_channel_type: str | None = None, notes: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, SubmitAdditionalInfoErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Adds documents or notes to an existing claim when Walmart requests more details.<br><b style='color:green;'>Market availability: US Only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.shipment_protection.with_raw_response.submit_additional_info(
    "some example string",
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    Path("path/to/file.bin"),
    [DocumentType1(file_name="item_damage.jpg", type_=Type11.PROOF_OF_DAMAGED_ITEM)],
    notes="Here is the picture you requested.",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SubmitAdditionalInfoErrorBody
```

**Async**

```python
result = await async_client.shipment_protection.with_raw_response.submit_additional_info(
    "some example string",
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    Path("path/to/file.bin"),
    [DocumentType1(file_name="item_damage.jpg", type_=Type11.PROOF_OF_DAMAGED_ITEM)],
    notes="Here is the picture you requested.",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SubmitAdditionalInfoErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>claim_number</code> | <code>str</code> | Exact claim number for filtering (query) or identifying a specific claim (path). |
| <code>wm_sec_access_token</code> | <code>str</code> | The access token retrieved in the Token API call. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and is used to track and debug issues; use a randomly generated GUID for this ID. |
| <code>wm_svc_name</code> | <code>str</code> | Walmart service name—for Marketplace APIs simply use `Walmart Service Name` or the service identifier provided by Walmart. |
| <code>files</code> | <code>FileInput</code> | Additional supporting file. |
| <code>document_types</code> | <code>list&#91;[DocumentType1](walmart_apis/models/document_type1.py) \| [DocumentType1Dict](walmart_apis/models/document_type1.py)&#93;</code> | Mapping for each uploaded file. |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br>**Default**: <code>None</code> |
| <code>notes</code> | <code>str \| None</code> | Additional information requested by Walmart<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [SubmitAdditionalInfoErrorBody](walmart_apis/errors/submit_additional_info_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Additional information submitted successfully.

**On `Failure`**: `error` is <code>[SubmitAdditionalInfoErrorBody](walmart_apis/errors/submit_additional_info_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V3ClaimsShipmentProtectionClaim400Error1](walmart_apis/models/v3_claims_shipment_protection_claim400_error1.py)</code> |
| 404 | <code>[V3ClaimsShipmentProtectionClaim404Error1](walmart_apis/models/v3_claims_shipment_protection_claim404_error1.py)</code> |
| 500 | <code>[V3ClaimsShipmentProtectionClaim500Error1](walmart_apis/models/v3_claims_shipment_protection_claim500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def submit_claim(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, files: FileInput, document_types: list[DocumentType | DocumentTypeDict], payload: Payload | PayloadDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, SubmitClaimErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a shipment-protection claim. Send multipart/form-data with files, documentTypes, and payload.<br><b style='color:green;'>Market availability: US Only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.shipment_protection.with_raw_response.submit_claim(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    Path("path/to/file.bin"),
    [
        DocumentType(file_name="file1.jpg", type_=Type1.PROOF_OF_DAMAGED_ITEM),
        DocumentType(file_name="invoice.pdf", type_=Type1.INVOICE),
    ],
    Payload(
        purchase_order_no="RAPMOCK1729803026938",
        purchase_order_line_no="1",
        sales_order_no="RAPMOCK1729803026883",
        sales_order_line_no="1",
        fulfiller_line_id="1",
        quantity=3,
        return_order_id="136900073772361154",
        claim_type=ClaimType.DAMAGED,
        notes="Claim submission notes.",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SubmitClaimErrorBody
```

**Async**

```python
result = await async_client.shipment_protection.with_raw_response.submit_claim(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    Path("path/to/file.bin"),
    [
        DocumentType(file_name="file1.jpg", type_=Type1.PROOF_OF_DAMAGED_ITEM),
        DocumentType(file_name="invoice.pdf", type_=Type1.INVOICE),
    ],
    Payload(
        purchase_order_no="RAPMOCK1729803026938",
        purchase_order_line_no="1",
        sales_order_no="RAPMOCK1729803026883",
        sales_order_line_no="1",
        fulfiller_line_id="1",
        quantity=3,
        return_order_id="136900073772361154",
        claim_type=ClaimType.DAMAGED,
        notes="Claim submission notes.",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SubmitClaimErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_sec_access_token</code> | <code>str</code> | The access token retrieved in the Token API call. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID which identifies each API call and is used to track and debug issues; use a randomly generated GUID for this ID. |
| <code>wm_svc_name</code> | <code>str</code> | Walmart service name—for Marketplace APIs simply use `Walmart Service Name` or the service identifier provided by Walmart. |
| <code>files</code> | <code>FileInput</code> | Supporting file (image, PDF, etc.). |
| <code>document_types</code> | <code>list&#91;[DocumentType](walmart_apis/models/document_type.py) \| [DocumentTypeDict](walmart_apis/models/document_type.py)&#93;</code> | Maps each uploaded file to its document category. |
| <code>payload</code> | <code>[Payload](walmart_apis/models/payload.py) \| [PayloadDict](walmart_apis/models/payload.py)</code> | Claim details. |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [SubmitClaimErrorBody](walmart_apis/errors/submit_claim_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Claim submitted successfully

**On `Failure`**: `error` is <code>[SubmitClaimErrorBody](walmart_apis/errors/submit_claim_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V3ClaimsShipmentProtectionClaim400Error1](walmart_apis/models/v3_claims_shipment_protection_claim400_error1.py)</code> |
| 401 | <code>[V3ClaimsShipmentProtectionClaim401Error1](walmart_apis/models/v3_claims_shipment_protection_claim401_error1.py)</code> |
| 500 | <code>[V3ClaimsShipmentProtectionClaim500Error1](walmart_apis/models/v3_claims_shipment_protection_claim500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SimplifiedShippingSettings

> Source: [SimplifiedShippingSettings](walmart_apis/apis/simplified_shipping_settings.py)

<details>
<summary><code>def bulk_migrate_offers_for_simplified_shipping_settings(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3FeedsRequest1 | V3FeedsRequest1Dict, *, feed_type: str = "PROGRAM_ACTIONS", request_type: str = "SHIPPING_CONFIG", wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FeedId1, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API is used to bulk migrate offers from manual templates to Simplified Shipping Settings and vice-versa. Make sure to create account level settings before proceeding with item migration to Simplified Shipping Settings.
<br><b style='color:green;'>Market availability: US</span></b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.simplified_shipping_settings.with_raw_response.bulk_migrate_offers_for_simplified_shipping_settings(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3FeedsRequest1(
        program_action_feed_header=ProgramActionFeedHeader11(
            version="5.0.20241002-17_27_17-api", locale="en", business_unit="WALMART_US"
        ),
        program_action=[ProgramAction11(programs=Programs21(), item_identifiers=ItemIdentifiers(sku="8922gfgf"))],
    ),
    feed_type="some example string",
    request_type="some example string",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FeedId1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.simplified_shipping_settings.with_raw_response.bulk_migrate_offers_for_simplified_shipping_settings(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3FeedsRequest1(
        program_action_feed_header=ProgramActionFeedHeader11(
            version="5.0.20241002-17_27_17-api", locale="en", business_unit="WALMART_US"
        ),
        program_action=[ProgramAction11(programs=Programs21(), item_identifiers=ItemIdentifiers(sku="8922gfgf"))],
    ),
    feed_type="some example string",
    request_type="some example string",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FeedId1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. This is required for authenticating requests to Walmart Marketplace APIs.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The value must be set to 3.1.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>body</code> | <code>[V3FeedsRequest1](walmart_apis/models/v3_feeds_request1.py) \| [V3FeedsRequest1Dict](walmart_apis/models/v3_feeds_request1.py)</code> | Request fields |
| <code>feed_type</code> | <code>str</code> | The type of feed, which specifies the nature of the update.<br><br><b style='color:green;'>Market availability: US</span></b><br>**Default**: <code>"PROGRAM_ACTIONS"</code> |
| <code>request_type</code> | <code>str</code> | Specifies the type of request being made. <br><br><b style='color:green;'>Market availability: US</span></b><br>**Default**: <code>"SHIPPING_CONFIG"</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><b style='color:green;'>Market availability: Global</span></b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[FeedId1](walmart_apis/models/feed_id1.py), [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[FeedId1](walmart_apis/models/feed_id1.py)</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_simplified_shipping_settings(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3SettingsShippingSimplifiedshippingsettingsAccountRequest1 | V3SettingsShippingSimplifiedshippingsettingsAccountRequest1Dict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[V3SettingsShippingSimplifiedshippingsettingsAccountResponse1], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API is used to update the account-level configuration. The carrier configurations created using this API will be applied across all Fulfillment Centers (FCs) unless they are overridden using the FC Configuration API..
<br><b style='color:green;'>Market availability: US</span></b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.simplified_shipping_settings.with_raw_response.create_simplified_shipping_settings(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3SettingsShippingSimplifiedshippingsettingsAccountRequest1(
        simplified_shipping_settings=SimplifiedShippingSettings10(
            account_configs=AccountConfigs9(
                shipping_priority=ShippingPriority7.FASTEST,
                migrate_eligible_offers=False,
                carrier_configs=[CarrierConfig20(), CarrierConfig20()],
            ),
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[V3SettingsShippingSimplifiedshippingsettingsAccountResponse1]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.simplified_shipping_settings.with_raw_response.create_simplified_shipping_settings(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3SettingsShippingSimplifiedshippingsettingsAccountRequest1(
        simplified_shipping_settings=SimplifiedShippingSettings10(
            account_configs=AccountConfigs9(
                shipping_priority=ShippingPriority7.FASTEST,
                migrate_eligible_offers=False,
                carrier_configs=[CarrierConfig20(), CarrierConfig20()],
            ),
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[V3SettingsShippingSimplifiedshippingsettingsAccountResponse1]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. This is required for authenticating requests to Walmart Marketplace APIs.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The value must be set to 3.1.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>body</code> | <code>[V3SettingsShippingSimplifiedshippingsettingsAccountRequest1](walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_account_request1.py) \| [V3SettingsShippingSimplifiedshippingsettingsAccountRequest1Dict](walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_account_request1.py)</code> | Request fields |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><br><b style='color:green;'>Market availability: Global</span></b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;list&#91;[V3SettingsShippingSimplifiedshippingsettingsAccountResponse1](walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_account_response1.py)&#93;, [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[V3SettingsShippingSimplifiedshippingsettingsAccountResponse1](walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_account_response1.py)&#93;</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_simplified_shipping_settings(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[V3SettingsShippingSimplifiedshippingsettingsResponse], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API helps seller to fetch the Simplified Shipping Settings for a seller account and FC-level configurations.
<br><b style='color:green;'>Market availability: Global</span></b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.simplified_shipping_settings.with_raw_response.get_simplified_shipping_settings(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[V3SettingsShippingSimplifiedshippingsettingsResponse]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.simplified_shipping_settings.with_raw_response.get_simplified_shipping_settings(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[V3SettingsShippingSimplifiedshippingsettingsResponse]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. This is required for authenticating requests to Walmart Marketplace APIs.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The value must be set to 3.1.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding..<br><br><b style='color:green;'>Market availability: Global</span></b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;list&#91;[V3SettingsShippingSimplifiedshippingsettingsResponse](walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_response.py)&#93;, [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[V3SettingsShippingSimplifiedshippingsettingsResponse](walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_response.py)&#93;</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_fc_level_simplified_shipping_settings(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequest | V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterResponse], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API can be used for overriding the configurations at one or more Fulfillment Centers.
<br><b style='color:green;'>Market availability: US</span></b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.simplified_shipping_settings.with_raw_response.update_fc_level_simplified_shipping_settings(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequest(
        simplified_shipping_settings=SimplifiedShippingSettings6(
            ship_node_configs=[
                ShipNodeConfig5(ship_nodes=["1234567616356"], is_overridden=False),
                ShipNodeConfig5(ship_nodes=["1234567616357"], is_overridden=True, carrier_configs=[CarrierConfig16()]),
            ],
        ),
    ),
)
match result:
    case Success(payload=payload):
        # TODO: Handle 'payload' of type list[V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterResponse]
        ...
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.simplified_shipping_settings.with_raw_response.update_fc_level_simplified_shipping_settings(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequest(
        simplified_shipping_settings=SimplifiedShippingSettings6(
            ship_node_configs=[
                ShipNodeConfig5(ship_nodes=["1234567616356"], is_overridden=False),
                ShipNodeConfig5(ship_nodes=["1234567616357"], is_overridden=True, carrier_configs=[CarrierConfig16()]),
            ],
        ),
    ),
)
match result:
    case Success(payload=payload):
        # TODO: Handle 'payload' of type list[V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterResponse]
        ...
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. This is required for authenticating requests to Walmart Marketplace APIs.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The value must be set to 3.1.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>body</code> | <code>[V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequest](walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_fulfillmentcenter_request.py) \| [V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequestDict](walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_fulfillmentcenter_request.py)</code> | Request fields |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding..<br><br><b style='color:green;'>Market availability: Global</span></b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;list&#91;[V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterResponse](walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_fulfillmentcenter_response.py)&#93;, [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterResponse](walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_fulfillmentcenter_response.py)&#93;</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_simplified_shipping_settings(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3SettingsShippingSimplifiedshippingsettingsAccountRequest | V3SettingsShippingSimplifiedshippingsettingsAccountRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[V3SettingsShippingSimplifiedshippingsettingsAccountResponse], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API is used to update the account-level configuration. The carrier configurations updated using this API will be applied across all Fulfillment Centers (FCs) unless they are overridden using the FC Configuration API.

<br><b style='color:green;'>Market availability: US</span></b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.simplified_shipping_settings.with_raw_response.update_simplified_shipping_settings(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3SettingsShippingSimplifiedshippingsettingsAccountRequest(
        simplified_shipping_settings=SimplifiedShippingSettings8(
            account_configs=AccountConfigs7(carrier_configs=[CarrierConfig18(), CarrierConfig18()])
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[V3SettingsShippingSimplifiedshippingsettingsAccountResponse]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.simplified_shipping_settings.with_raw_response.update_simplified_shipping_settings(
    "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmMarket1.US,
    WmGlobalVersion._3_1,
    V3SettingsShippingSimplifiedshippingsettingsAccountRequest(
        simplified_shipping_settings=SimplifiedShippingSettings8(
            account_configs=AccountConfigs7(carrier_configs=[CarrierConfig18(), CarrierConfig18()])
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[V3SettingsShippingSimplifiedshippingsettingsAccountResponse]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. This is required for authenticating requests to Walmart Marketplace APIs.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. <br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_market</code> | <code>[WmMarket1OrStr](walmart_apis/models/enums/wm_market1.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | Indicates the global version of the API. The value must be set to 3.1.<br><br><b style='color:green;'>Market availability: Global</span></b> |
| <code>body</code> | <code>[V3SettingsShippingSimplifiedshippingsettingsAccountRequest](walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_account_request.py) \| [V3SettingsShippingSimplifiedshippingsettingsAccountRequestDict](walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_account_request.py)</code> | Request fields |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding..<br><br><b style='color:green;'>Market availability: Global</span></b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;list&#91;[V3SettingsShippingSimplifiedshippingsettingsAccountResponse](walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_account_response.py)&#93;, [RawError](walmart_apis/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[V3SettingsShippingSimplifiedshippingsettingsAccountResponse](walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_account_response.py)&#93;</code> -- Successful Operation

**On `Failure`**: `error` is <code>[RawError](walmart_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## TaxFormApis

> Source: [TaxFormApis](walmart_apis/apis/tax_form_apis.py)

<details>
<summary><code>def download_tax_form(payout_year: str, tax_form_type: str, form_id: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_global_version: WmGlobalVersionOrStr, wm_market: str, wm_partner_id: str, wm_tenant_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, DownloadTaxFormErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The Download Tax Form API downloads the selected tax form document as a byte stream.

<b style='color:green;'>Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.tax_form_apis.with_raw_response.download_tax_form(
    "some example string",
    "some example string",
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmGlobalVersion._3_1,
    "US",
    "123456789",
    "0",
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadTaxFormErrorBody
```

**Async**

```python
result = await async_client.tax_form_apis.with_raw_response.download_tax_form(
    "some example string",
    "some example string",
    "some example string",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Service Name",
    WmGlobalVersion._3_1,
    "US",
    "123456789",
    "0",
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadTaxFormErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>payout_year</code> | <code>str</code> | The tax year associated with the payout (for example, 2024). <br><b style='color:green;'>Market availability: US only</b> |
| <code>tax_form_type</code> | <code>str</code> | The tax form type to download (for example, 1099-K).<br><b style='color:green;'>Market availability: US only</b> |
| <code>form_id</code> | <code>str</code> | The unique form ID returned by the list tax forms endpoint.<br><b style='color:green;'>Market availability: US only</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_market</code> | <code>str</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default. <br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_partner_id</code> | <code>str</code> | The partner (seller) identifier registered in Walmart Marketplace. <br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_tenant_id</code> | <code>str</code> | Specifies the tenant identifier. <br><b style='color:green;'>Market availability: Global</b> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;None, [DownloadTaxFormErrorBody](walmart_apis/errors/download_tax_form_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[DownloadTaxFormErrorBody](walmart_apis/errors/download_tax_form_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1SettingsDownloadtaxformprofile400Error1](walmart_apis/models/v1_settings_downloadtaxformprofile400_error1.py)</code> |
| 404 | <code>[V1SettingsDownloadtaxformprofile404Error1](walmart_apis/models/v1_settings_downloadtaxformprofile404_error1.py)</code> |
| 500 | <code>[V1SettingsDownloadtaxformprofile500Error1](walmart_apis/models/v1_settings_downloadtaxformprofile500_error1.py)</code> |
| 502 | <code>[V1SettingsDownloadtaxformprofile502Error1](walmart_apis/models/v1_settings_downloadtaxformprofile502_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_tax_forms(wm_qos_correlation_id: str, wm_svc_name: str, wm_global_version: WmGlobalVersionOrStr, wm_market: str, wm_partner_id: str, wm_tenant_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1SettingsGettaxformprofileResponse, GetTaxFormsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The Get Tax Forms API returns available tax forms for the authenticated seller, including form type and form ID. The response is a JSON object containing tax form metadata.

<b style='color:green;'>Market availability: US only</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.tax_form_apis.with_raw_response.get_tax_forms(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmGlobalVersion._3_1, "US", "123456789", "0"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1SettingsGettaxformprofileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetTaxFormsErrorBody
```

**Async**

```python
result = await async_client.tax_form_apis.with_raw_response.get_tax_forms(
    "b3261d2d-028a-4ef7-8602-633c23200af6", "Walmart Service Name", WmGlobalVersion._3_1, "US", "123456789", "0"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1SettingsGettaxformprofileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetTaxFormsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br><strong style="color: green;">Market availability: Global</strong> |
| <code>wm_market</code> | <code>str</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default. <br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_partner_id</code> | <code>str</code> | The partner (seller) identifier registered in Walmart Marketplace. <br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_tenant_id</code> | <code>str</code> | Specifies the tenant identifier for multi-tenant contexts. <br><b style='color:green;'>Market availability: Global</b> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V1SettingsGettaxformprofileResponse](walmart_apis/models/v1_settings_gettaxformprofile_response.py), [GetTaxFormsErrorBody](walmart_apis/errors/get_tax_forms_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1SettingsGettaxformprofileResponse](walmart_apis/models/v1_settings_gettaxformprofile_response.py)</code> -- Tax forms retrieved successfully.

**On `Failure`**: `error` is <code>[GetTaxFormsErrorBody](walmart_apis/errors/get_tax_forms_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1SettingsGettaxformprofile400Error1](walmart_apis/models/v1_settings_gettaxformprofile400_error1.py)</code> |
| 404 | <code>[V1SettingsGettaxformprofile404Error1](walmart_apis/models/v1_settings_gettaxformprofile404_error1.py)</code> |
| 500 | <code>[V1SettingsGettaxformprofile500Error1](walmart_apis/models/v1_settings_gettaxformprofile500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## WsrAttributionReports

> Source: [WsrAttributionReports](walmart_apis/apis/wsr_attribution_reports.py)

<details>
<summary><code>def get_tag_templates(wm_sec_access_token: str, wm_svc_name: str, wm_qos_correlation_id: str, *, template_type: TemplateTypeOrStr = TemplateType.NON_MACRO, wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1, wm_market: WmMarketOrStr = WmMarket.US, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WsrTagTemplatesResponse, GetTagTemplatesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetch referral link tag templates for different page types (ITEM, BRANDSHOP). Tag templates contain URL patterns with placeholders that can be used to construct final referral URLs/tags for affiliate tracking.

<span style="color:green">**Market availability: US**</span>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.wsr_attribution_reports.with_raw_response.get_tag_templates(
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "Walmart Marketplace",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    template_type=TemplateType.NON_MACRO,
    wm_global_version=WmGlobalVersion._3_1,
    wm_market=WmMarket.US,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WsrTagTemplatesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetTagTemplatesErrorBody
```

**Async**

```python
result = await async_client.wsr_attribution_reports.with_raw_response.get_tag_templates(
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "Walmart Marketplace",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    template_type=TemplateType.NON_MACRO,
    wm_global_version=WmGlobalVersion._3_1,
    wm_market=WmMarket.US,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WsrTagTemplatesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetTagTemplatesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. This is required for authenticating requests to Walmart Marketplace APIs. |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID. |
| <code>template_type</code> | <code>[TemplateTypeOrStr](walmart_apis/models/enums/template_type.py)</code> | The type of tag template to fetch. Currently supports NON_MACRO.<br><br><span style="color:green">**Market availability: Global**</span><br>**Default**: <code>TemplateType.NON_MACRO</code> |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br>**Default**: <code>WmGlobalVersion._3_1</code> |
| <code>wm_market</code> | <code>[WmMarketOrStr](walmart_apis/models/enums/wm_market.py)</code> | The target market of the API call.<br>**Default**: <code>WmMarket.US</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[WsrTagTemplatesResponse](walmart_apis/models/wsr_tag_templates_response.py), [GetTagTemplatesErrorBody](walmart_apis/errors/get_tag_templates_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[WsrTagTemplatesResponse](walmart_apis/models/wsr_tag_templates_response.py)</code> -- Tag templates retrieved successfully

**On `Failure`**: `error` is <code>[GetTagTemplatesErrorBody](walmart_apis/errors/get_tag_templates_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 500 | <code>[WsrErrorResponse](walmart_apis/models/wsr_error_response.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_wsr_item_report(wm_sec_access_token: str, wm_svc_name: str, wm_qos_correlation_id: str, body: WsrReportRequest | WsrReportRequestDict, *, wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1, wm_market: WmMarketOrStr = WmMarket.US, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WsrItemReportResponse, GetWsrItemReportErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve detailed item-level performance reports for affiliate campaigns.

<span style="color:green">**Market availability: US only**</span>

This endpoint returns performance data at the individual item/product level,
including product details such as item name, category, and product type along
with performance metrics. This is useful for understanding which products are
driving the most revenue through affiliate channels.

### Aggregation Levels and Field Availability
The `performanceBy` parameter determines which identifier fields are populated in the response:

| performanceBy | campaignId | adGroupId | creativeId |
|---------------|------------|-----------|------------|
| CAMPAIGN      | ✓          | null      | null       |
| ADGROUP       | ✓          | ✓         | null       |
| CREATIVE      | ✓          | ✓         | ✓          |

### Supported filters
- `startDate`: Report start date (required)
- `endDate`: Report end date (required)
- `campaignId`: Filter by specific campaign IDs
- `adGroupId`: Filter by specific ad group IDs
- `creativeId`: Filter by specific creative IDs

### Date Validation Rules
- End date must be strictly after start date
- Maximum date range: less than 1 year
- Dates must be in ISO format (YYYY-MM-DD)

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.wsr_attribution_reports.with_raw_response.get_wsr_item_report(
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "Walmart Marketplace",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    WsrReportRequest(
        performance_by=PerformanceBy.CAMPAIGN,
        start_date=date(2026, 1, 1),
        end_date=date(2026, 1, 31),
        page=WsrPage(limit=10, offset=0),
        sort=WsrSort(field=FieldModel.GMV, order=Order.DESC),
    ),
    wm_global_version=WmGlobalVersion._3_1,
    wm_market=WmMarket.US,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WsrItemReportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetWsrItemReportErrorBody
```

**Async**

```python
result = await async_client.wsr_attribution_reports.with_raw_response.get_wsr_item_report(
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "Walmart Marketplace",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    WsrReportRequest(
        performance_by=PerformanceBy.CAMPAIGN,
        start_date=date(2026, 1, 1),
        end_date=date(2026, 1, 31),
        page=WsrPage(limit=10, offset=0),
        sort=WsrSort(field=FieldModel.GMV, order=Order.DESC),
    ),
    wm_global_version=WmGlobalVersion._3_1,
    wm_market=WmMarket.US,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WsrItemReportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetWsrItemReportErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. This is required for authenticating requests to Walmart Marketplace APIs. |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID. |
| <code>body</code> | <code>[WsrReportRequest](walmart_apis/models/wsr_report_request.py) \| [WsrReportRequestDict](walmart_apis/models/wsr_report_request.py)</code> | Item report request with filters and parameters |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br>**Default**: <code>WmGlobalVersion._3_1</code> |
| <code>wm_market</code> | <code>[WmMarketOrStr](walmart_apis/models/enums/wm_market.py)</code> | Identifies the Walmart Marketplace region for the request.<br>**Default**: <code>WmMarket.US</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[WsrItemReportResponse](walmart_apis/models/wsr_item_report_response.py), [GetWsrItemReportErrorBody](walmart_apis/errors/get_wsr_item_report_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[WsrItemReportResponse](walmart_apis/models/wsr_item_report_response.py)</code> -- Item report retrieved successfully

**On `Failure`**: `error` is <code>[GetWsrItemReportErrorBody](walmart_apis/errors/get_wsr_item_report_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 500 | <code>[WsrErrorResponse](walmart_apis/models/wsr_error_response.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_wsr_performance_report(wm_sec_access_token: str, wm_svc_name: str, wm_qos_correlation_id: str, body: WsrReportRequest | WsrReportRequestDict, *, wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1, wm_market: WmMarketOrStr = WmMarket.US, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WsrPerformanceReportResponse, GetWsrPerformanceReportErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve performance analytics and metrics for affiliate campaigns.

<span style="color:green">**Market availability: US only**</span>

This endpoint returns aggregated performance data including clicks, orders,
GMV, and commission metrics within a specified date range. Data can be
aggregated at different levels based on the `performanceBy` parameter.

### Aggregation Levels and Field Availability
The `performanceBy` parameter determines which identifier fields are populated in the response:

| performanceBy | campaignId | adGroupId | creativeId |
|---------------|------------|-----------|------------|
| CAMPAIGN      | ✓          | null      | null       |
| ADGROUP       | ✓          | ✓         | null       |
| CREATIVE      | ✓          | ✓         | ✓          |

### Supported filters
- `startDate`: Report start date (required)
- `endDate`: Report end date (required)
- `campaignId`: Filter by specific campaign IDs
- `adGroupId`: Filter by specific ad group IDs
- `creativeId`: Filter by specific creative IDs

### Date Validation Rules
- End date must be strictly after start date
- Maximum date range: less than 1 year
- Dates must be in ISO format (YYYY-MM-DD)

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.wsr_attribution_reports.with_raw_response.get_wsr_performance_report(
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "Walmart Marketplace",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    WsrReportRequest(
        performance_by=PerformanceBy.CAMPAIGN,
        start_date=date(2026, 1, 1),
        end_date=date(2026, 1, 31),
        page=WsrPage(limit=10, offset=0),
        sort=WsrSort(field=FieldModel.GMV, order=Order.DESC),
    ),
    wm_global_version=WmGlobalVersion._3_1,
    wm_market=WmMarket.US,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WsrPerformanceReportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetWsrPerformanceReportErrorBody
```

**Async**

```python
result = await async_client.wsr_attribution_reports.with_raw_response.get_wsr_performance_report(
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "Walmart Marketplace",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    WsrReportRequest(
        performance_by=PerformanceBy.CAMPAIGN,
        start_date=date(2026, 1, 1),
        end_date=date(2026, 1, 31),
        page=WsrPage(limit=10, offset=0),
        sort=WsrSort(field=FieldModel.GMV, order=Order.DESC),
    ),
    wm_global_version=WmGlobalVersion._3_1,
    wm_market=WmMarket.US,
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WsrPerformanceReportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetWsrPerformanceReportErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. This is required for authenticating requests to Walmart Marketplace APIs. |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called. |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID. |
| <code>body</code> | <code>[WsrReportRequest](walmart_apis/models/wsr_report_request.py) \| [WsrReportRequestDict](walmart_apis/models/wsr_report_request.py)</code> | Performance report request with date range and optional filters |
| <code>wm_global_version</code> | <code>[WmGlobalVersionOrStr](walmart_apis/models/enums/wm_global_version.py)</code> | The version of the global API used.<br>**Default**: <code>WmGlobalVersion._3_1</code> |
| <code>wm_market</code> | <code>[WmMarketOrStr](walmart_apis/models/enums/wm_market.py)</code> | Identifies the Walmart Marketplace region for the request.<br>**Default**: <code>WmMarket.US</code> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[WsrPerformanceReportResponse](walmart_apis/models/wsr_performance_report_response.py), [GetWsrPerformanceReportErrorBody](walmart_apis/errors/get_wsr_performance_report_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[WsrPerformanceReportResponse](walmart_apis/models/wsr_performance_report_response.py)</code> -- Performance report retrieved successfully

**On `Failure`**: `error` is <code>[GetWsrPerformanceReportErrorBody](walmart_apis/errors/get_wsr_performance_report_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 500 | <code>[WsrErrorResponse](walmart_apis/models/wsr_error_response.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## WalmartSellerFulfilled

> Source: [WalmartSellerFulfilled](walmart_apis/apis/walmart_seller_fulfilled.py)

<details>
<summary><code>def walmart_plus_enrollment(feed_type: FeedType3OrStr, request_type: RequestTypeOrStr, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarketOrStr, file_name: FileInput, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSffResponse, WalmartPlusEnrollmentErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API endpoint allows you to efficiently manage item participation in the Walmart+ program. Use it to enroll eligible items in Walmart+ or to unenroll items that are currently part of the program.<br><b style='color:green;'>Market availability: US</b> 

<b>Download and review the <a href="/file/mp/us/PROGRAM_ACTIONS_5.0.20250617-00_03_34_US_WalmartPlusEnrollment.xlsx">Excel template sample </a> and the <a href="/file/mp/us/bulk-enroll-requestBody-template.json">JSON body sample</a> to ensure proper formatting of the updated file before uploading it for processing.</b>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.walmart_seller_fulfilled.with_raw_response.walmart_plus_enrollment(
    FeedType3.PROGRAM_ACTIONS,
    RequestType.WALMART_PLUS_SFF,
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    WmMarket.US,
    Path("path/to/file.bin"),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSffResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type WalmartPlusEnrollmentErrorBody
```

**Async**

```python
result = await async_client.walmart_seller_fulfilled.with_raw_response.walmart_plus_enrollment(
    FeedType3.PROGRAM_ACTIONS,
    RequestType.WALMART_PLUS_SFF,
    "eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....",
    "b3261d2d-028a-4ef7-8602-633c23200af6",
    "Walmart Marketplace",
    WmMarket.US,
    Path("path/to/file.bin"),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSffResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type WalmartPlusEnrollmentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>feed_type</code> | <code>[FeedType3OrStr](walmart_apis/models/enums/feed_type3.py)</code> | The type of feed, which specifies the nature of the update.<br><b style='color:green;'>Market availability: US</b> |
| <code>request_type</code> | <code>[RequestTypeOrStr](walmart_apis/models/enums/request_type.py)</code> | Specifies the type of request for the Walmart+ SFF (Seller-Fulfilled) program.<br><b style='color:green;'>Market availability: US</b> |
| <code>wm_sec_access_token</code> | <code>str</code> | Access token obtained from the Token API. This is required for authenticating requests to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_qos_correlation_id</code> | <code>str</code> | A unique ID that identifies each API call and is used to track and debug issues. Use a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_svc_name</code> | <code>str</code> | Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market availability: Global</b> |
| <code>wm_market</code> | <code>[WmMarketOrStr](walmart_apis/models/enums/wm_market.py)</code> | Identifies the Walmart Marketplace region for the request. If not specified, US is used by default.<br><b style='color:green;'>Market availability: Global</b> |
| <code>file_name</code> | <code>FileInput</code> | Upload an Excel file or a JSON file containing the data for Walmart+ enrollment or unenrollment.<br><b style='color:green;'>Market availability: US</b> |
| <code>wm_consumer_channel_type</code> | <code>str \| None</code> | A unique ID to identify the consumer request by channel. Use the Consumer Channel Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSffResponse](walmart_apis/models/v3_feeds_feed_type_program_actions_request_type_walmart_plus_sff_response.py), [WalmartPlusEnrollmentErrorBody](walmart_apis/errors/walmart_plus_enrollment_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSffResponse](walmart_apis/models/v3_feeds_feed_type_program_actions_request_type_walmart_plus_sff_response.py)</code> -- Indicates successful operation. The response provides details on both successful and failed item enrollments or unenrollments, allowing you to review which items were updated and which encountered issues.

**On `Failure`**: `error` is <code>[WalmartPlusEnrollmentErrorBody](walmart_apis/errors/walmart_plus_enrollment_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSff400Error1](walmart_apis/models/v3_feeds_feed_type_program_actions_request_type_walmart_plus_sff400_error1.py)</code> |
| 500 | <code>[V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSff500Error1](walmart_apis/models/v3_feeds_feed_type_program_actions_request_type_walmart_plus_sff500_error1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

