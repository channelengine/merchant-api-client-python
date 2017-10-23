# swagger_client.OrderApi

All URIs are relative to *http://dev.channelengine.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**order_acknowledge**](OrderApi.md#order_acknowledge) | **POST** /v2/orders/acknowledge | Merchant: Acknowledge Order
[**order_create**](OrderApi.md#order_create) | **POST** /v2/orders | Channel: Create Order
[**order_get_by_filter**](OrderApi.md#order_get_by_filter) | **GET** /v2/orders | Merchant: Get Orders By Filter
[**order_get_new**](OrderApi.md#order_get_new) | **GET** /v2/orders/new | Merchant: Get New Orders
[**order_invoice**](OrderApi.md#order_invoice) | **GET** /v2/orders/{merchantOrderNo}/invoice | Merchant: Download Invoice
[**order_packing_slip**](OrderApi.md#order_packing_slip) | **GET** /v2/orders/{merchantOrderNo}/packingslip | Merchant: Download Packing Slip


# **order_acknowledge**
> ApiResponse order_acknowledge(model)

Merchant: Acknowledge Order

For merchants.    Acknowledge an order. By acknowledging the order the merchant can confirm that  the order has been imported. When acknowledging an order the merchant has to supply  references that uniquely identify the order and the order lines. These references  will be used in the other API calls.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
model = swagger_client.OrderAcknowledgement() # OrderAcknowledgement | Relations between the id's returned by ChannelEngine and the references which the merchant uses

try: 
    # Merchant: Acknowledge Order
    api_response = api_instance.order_acknowledge(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_acknowledge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**OrderAcknowledgement**](OrderAcknowledgement.md)| Relations between the id&#39;s returned by ChannelEngine and the references which the merchant uses | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_create**
> ApiResponse order_create(model)

Channel: Create Order

For channels.    Create a new order in ChannelEngine.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
model = swagger_client.ChannelOrderRequest() # ChannelOrderRequest | 

try: 
    # Channel: Create Order
    api_response = api_instance.order_create(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**ChannelOrderRequest**](ChannelOrderRequest.md)|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_get_by_filter**
> CollectionOfMerchantOrderResponse order_get_by_filter(filter_statuses=filter_statuses, filter_merchant_order_nos=filter_merchant_order_nos, filter_exclude_marketplace_fulfilled_orders_and_lines=filter_exclude_marketplace_fulfilled_orders_and_lines, filter_fulfillment_type=filter_fulfillment_type, filter_page=filter_page)

Merchant: Get Orders By Filter

For merchants.                Fetch orders based on the provided OrderFilter

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
filter_statuses = ['filter_statuses_example'] # list[str] |  (optional)
filter_merchant_order_nos = ['filter_merchant_order_nos_example'] # list[str] |  (optional)
filter_exclude_marketplace_fulfilled_orders_and_lines = true # bool |  (optional)
filter_fulfillment_type = 'filter_fulfillment_type_example' # str | Filter orders on fulfillment type. This will include all orders lines, even if they are partially fulfilled by the marketplace.  To exclude orders and lines that are fulfilled by the marketplace from the response, set ExcludeMarketplaceFulfilledOrdersAndLines to true. (optional)
filter_page = 56 # int |  (optional)

try: 
    # Merchant: Get Orders By Filter
    api_response = api_instance.order_get_by_filter(filter_statuses=filter_statuses, filter_merchant_order_nos=filter_merchant_order_nos, filter_exclude_marketplace_fulfilled_orders_and_lines=filter_exclude_marketplace_fulfilled_orders_and_lines, filter_fulfillment_type=filter_fulfillment_type, filter_page=filter_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_get_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_statuses** | [**list[str]**](str.md)|  | [optional] 
 **filter_merchant_order_nos** | [**list[str]**](str.md)|  | [optional] 
 **filter_exclude_marketplace_fulfilled_orders_and_lines** | **bool**|  | [optional] 
 **filter_fulfillment_type** | **str**| Filter orders on fulfillment type. This will include all orders lines, even if they are partially fulfilled by the marketplace.  To exclude orders and lines that are fulfilled by the marketplace from the response, set ExcludeMarketplaceFulfilledOrdersAndLines to true. | [optional] 
 **filter_page** | **int**|  | [optional] 

### Return type

[**CollectionOfMerchantOrderResponse**](CollectionOfMerchantOrderResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_get_new**
> CollectionOfMerchantOrderResponse order_get_new()

Merchant: Get New Orders

For merchants.                Fetch newly placed orders (order with status NEW).

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))

try: 
    # Merchant: Get New Orders
    api_response = api_instance.order_get_new()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_get_new: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CollectionOfMerchantOrderResponse**](CollectionOfMerchantOrderResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_invoice**
> file order_invoice(merchant_order_no, use_customer_culture=use_customer_culture)

Merchant: Download Invoice

For merchants.    Generates the ChannelEngine VAT invoice for this order in PDF

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
merchant_order_no = 'merchant_order_no_example' # str | The unique order reference as used by the merchant
use_customer_culture = true # bool | Generate the invoice in the billing address' country's language (optional)

try: 
    # Merchant: Download Invoice
    api_response = api_instance.order_invoice(merchant_order_no, use_customer_culture=use_customer_culture)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_order_no** | **str**| The unique order reference as used by the merchant | 
 **use_customer_culture** | **bool**| Generate the invoice in the billing address&#39; country&#39;s language | [optional] 

### Return type

[**file**](file.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_packing_slip**
> file order_packing_slip(merchant_order_no, use_customer_culture=use_customer_culture)

Merchant: Download Packing Slip

For merchants.    Generates the ChannelEngine packing slip for this order in PDF

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
merchant_order_no = 'merchant_order_no_example' # str | The unique order reference as used by the merchant
use_customer_culture = true # bool | Generate the invoice in the billing address' country's language (optional)

try: 
    # Merchant: Download Packing Slip
    api_response = api_instance.order_packing_slip(merchant_order_no, use_customer_culture=use_customer_culture)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_packing_slip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_order_no** | **str**| The unique order reference as used by the merchant | 
 **use_customer_culture** | **bool**| Generate the invoice in the billing address&#39; country&#39;s language | [optional] 

### Return type

[**file**](file.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

