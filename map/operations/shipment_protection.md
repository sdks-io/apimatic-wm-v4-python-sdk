<!-- Generated file — do not edit; regenerated with the SDK. -->

# ShipmentProtection — operations

Accessor: `client.shipment_protection` · Source: `walmart_apis/apis/shipment_protection.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.shipment_protection.download_claim_documents

- **Route**: `POST /v3/claims/shipment-protection/claim/{claimNumber}/documents`
- **Signature**: `def download_claim_documents(claim_number: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, body: V3ClaimsShipmentProtectionClaimDocumentsRequest | V3ClaimsShipmentProtectionClaimDocumentsRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `claim_number`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `body`
- **Params**: `claim_number` — path `claimNumber` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `FileResponse`
- **Returns (raw)**: `ApiResult[FileResponse, DownloadClaimDocumentsErrorBody]`
- **Error**: `DownloadClaimDocumentsErrorBody` — **Case A (typed)**
- **Error arms**: `V3ClaimsShipmentProtectionClaimDocuments400Error1` [400] · `V3ClaimsShipmentProtectionClaimDocuments404Error1` [404] · `V3ClaimsShipmentProtectionClaimDocuments500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V3ClaimsShipmentProtectionClaimDocumentsRequest` | `walmart_apis/models/v3_claims_shipment_protection_claim_documents_request.py` |
| `V3ClaimsShipmentProtectionClaimDocumentsRequestDict` | `walmart_apis/models/v3_claims_shipment_protection_claim_documents_request.py` |
| `DownloadClaimDocumentsErrorBody` | `walmart_apis/errors/download_claim_documents_error.py` |
| `V3ClaimsShipmentProtectionClaimDocuments400Error1` | `walmart_apis/models/v3_claims_shipment_protection_claim_documents400_error1.py` |
| `V3ClaimsShipmentProtectionClaimDocuments404Error1` | `walmart_apis/models/v3_claims_shipment_protection_claim_documents404_error1.py` |
| `V3ClaimsShipmentProtectionClaimDocuments500Error1` | `walmart_apis/models/v3_claims_shipment_protection_claim_documents500_error1.py` |

### client.shipment_protection.get_claim_details

- **Route**: `GET /v3/claims/shipment-protection/claim/{claimNumber}`
- **Signature**: `def get_claim_details(claim_number: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `claim_number`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`
- **Params**: `claim_number` — path `claimNumber` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, GetClaimDetailsErrorBody]`
- **Error**: `GetClaimDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `V3ClaimsShipmentProtectionClaim400Error1` [400] · `V3ClaimsShipmentProtectionClaim404Error1` [404] · `V3ClaimsShipmentProtectionClaim500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetClaimDetailsErrorBody` | `walmart_apis/errors/get_claim_details_error.py` |
| `V3ClaimsShipmentProtectionClaim400Error1` | `walmart_apis/models/v3_claims_shipment_protection_claim400_error1.py` |
| `V3ClaimsShipmentProtectionClaim404Error1` | `walmart_apis/models/v3_claims_shipment_protection_claim404_error1.py` |
| `V3ClaimsShipmentProtectionClaim500Error1` | `walmart_apis/models/v3_claims_shipment_protection_claim500_error1.py` |

### client.shipment_protection.get_claim_history

- **Route**: `GET /v3/claims/shipment-protection/claim/{claimNumber}/history`
- **Signature**: `def get_claim_history(claim_number: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `claim_number`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`
- **Params**: `claim_number` — path `claimNumber` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `V3ClaimsShipmentProtectionClaimHistoryResponse`
- **Returns (raw)**: `ApiResult[V3ClaimsShipmentProtectionClaimHistoryResponse, GetClaimHistoryErrorBody]`
- **Error**: `GetClaimHistoryErrorBody` — **Case A (typed)**
- **Error arms**: `V3ClaimsShipmentProtectionClaimHistory400Error1` [400] · `V3ClaimsShipmentProtectionClaimHistory404Error1` [404] · `V3ClaimsShipmentProtectionClaimHistory500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V3ClaimsShipmentProtectionClaimHistoryResponse` | `walmart_apis/models/v3_claims_shipment_protection_claim_history_response.py` |
| `GetClaimHistoryErrorBody` | `walmart_apis/errors/get_claim_history_error.py` |
| `V3ClaimsShipmentProtectionClaimHistory400Error1` | `walmart_apis/models/v3_claims_shipment_protection_claim_history400_error1.py` |
| `V3ClaimsShipmentProtectionClaimHistory404Error1` | `walmart_apis/models/v3_claims_shipment_protection_claim_history404_error1.py` |
| `V3ClaimsShipmentProtectionClaimHistory500Error1` | `walmart_apis/models/v3_claims_shipment_protection_claim_history500_error1.py` |

### client.shipment_protection.list_claims

- **Route**: `GET /v3/claims/shipment-protection`
- **Signature**: `def list_claims(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, *, limit: int | None = 25, offset: int | None = 0, claims_group: ClaimsGroupOrStr | None = None, claim_number: str | None = None, purchase_order_id: str | None = None, tracking_no: str | None = None, claim_types: str | None = None, claim_statuses: str | None = None, sort_by: SortByOrStr | None = None, sort_order: OrderOrStr | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`
- **Params**: `limit` — query · `offset` — query · `claims_group` — query `claimsGroup` · `claim_number` — query `claimNumber` · `purchase_order_id` — query `purchaseOrderId` · `tracking_no` — query `trackingNo` · `claim_types` — query `claimTypes` · `claim_statuses` — query `claimStatuses` · `sort_by` — query `sortBy` · `sort_order` — query `sortOrder` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, ListClaimsErrorBody]`
- **Error**: `ListClaimsErrorBody` — **Case A (typed)**
- **Error arms**: `V3ClaimsShipmentProtection400Error1` [400] · `V3ClaimsShipmentProtection401Error1` [401] · `V3ClaimsShipmentProtection500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClaimsGroupOrStr` | `walmart_apis/models/enums/claims_group.py` |
| `SortByOrStr` | `walmart_apis/models/enums/sort_by.py` |
| `OrderOrStr` | `walmart_apis/models/enums/order.py` |
| `ListClaimsErrorBody` | `walmart_apis/errors/list_claims_error.py` |
| `V3ClaimsShipmentProtection400Error1` | `walmart_apis/models/v3_claims_shipment_protection400_error1.py` |
| `V3ClaimsShipmentProtection401Error1` | `walmart_apis/models/v3_claims_shipment_protection401_error1.py` |
| `V3ClaimsShipmentProtection500Error1` | `walmart_apis/models/v3_claims_shipment_protection500_error1.py` |

### client.shipment_protection.submit_additional_info

- **Route**: `PATCH /v3/claims/shipment-protection/claim/{claimNumber}`
- **Signature**: `def submit_additional_info(claim_number: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, files: FileInput, document_types: list[DocumentType1 | DocumentType1Dict], *, wm_consumer_channel_type: str | None = None, notes: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `claim_number`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `files`, `document_types`
- **Params**: `claim_number` — path `claimNumber` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `files` — multipart file · `document_types` — multipart field `documentTypes` · `notes` — multipart field
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, SubmitAdditionalInfoErrorBody]`
- **Error**: `SubmitAdditionalInfoErrorBody` — **Case A (typed)**
- **Error arms**: `V3ClaimsShipmentProtectionClaim400Error1` [400] · `V3ClaimsShipmentProtectionClaim404Error1` [404] · `V3ClaimsShipmentProtectionClaim500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DocumentType1` | `walmart_apis/models/document_type1.py` |
| `DocumentType1Dict` | `walmart_apis/models/document_type1.py` |
| `SubmitAdditionalInfoErrorBody` | `walmart_apis/errors/submit_additional_info_error.py` |
| `V3ClaimsShipmentProtectionClaim400Error1` | `walmart_apis/models/v3_claims_shipment_protection_claim400_error1.py` |
| `V3ClaimsShipmentProtectionClaim404Error1` | `walmart_apis/models/v3_claims_shipment_protection_claim404_error1.py` |
| `V3ClaimsShipmentProtectionClaim500Error1` | `walmart_apis/models/v3_claims_shipment_protection_claim500_error1.py` |

### client.shipment_protection.submit_claim

- **Route**: `POST /v3/claims/shipment-protection/claim`
- **Signature**: `def submit_claim(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, files: FileInput, document_types: list[DocumentType | DocumentTypeDict], payload: Payload | PayloadDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `files`, `document_types`, `payload`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `files` — multipart file · `document_types` — multipart field `documentTypes` · `payload` — multipart field
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, SubmitClaimErrorBody]`
- **Error**: `SubmitClaimErrorBody` — **Case A (typed)**
- **Error arms**: `V3ClaimsShipmentProtectionClaim400Error1` [400] · `V3ClaimsShipmentProtectionClaim401Error1` [401] · `V3ClaimsShipmentProtectionClaim500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DocumentType` | `walmart_apis/models/document_type.py` |
| `DocumentTypeDict` | `walmart_apis/models/document_type.py` |
| `Payload` | `walmart_apis/models/payload.py` |
| `PayloadDict` | `walmart_apis/models/payload.py` |
| `SubmitClaimErrorBody` | `walmart_apis/errors/submit_claim_error.py` |
| `V3ClaimsShipmentProtectionClaim400Error1` | `walmart_apis/models/v3_claims_shipment_protection_claim400_error1.py` |
| `V3ClaimsShipmentProtectionClaim401Error1` | `walmart_apis/models/v3_claims_shipment_protection_claim401_error1.py` |
| `V3ClaimsShipmentProtectionClaim500Error1` | `walmart_apis/models/v3_claims_shipment_protection_claim500_error1.py` |

