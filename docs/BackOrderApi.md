# swagger_client.BackOrderApi

All URIs are relative to *http://dev.channelengine.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**back_order_create**](BackOrderApi.md#back_order_create) | **POST** /v2/backorders | Merchant: Create Backorder
[**back_order_index**](BackOrderApi.md#back_order_index) | **GET** /v2/backorders | Channel: Get Backorders


# **back_order_create**
> ApiResponse back_order_create(back_order)

Merchant: Create Backorder

Mark (part of) an order as in backorder.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
swagger_client.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.BackOrderApi()
back_order = swagger_client.MerchantBackOrderRequest() # MerchantBackOrderRequest | The Backorder to create

try: 
    # Merchant: Create Backorder
    api_response = api_instance.back_order_create(back_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackOrderApi->back_order_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **back_order** | [**MerchantBackOrderRequest**](MerchantBackOrderRequest.md)| The Backorder to create | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **back_order_index**
> CollectionOfChannelBackOrderResponse back_order_index(created_since)

Channel: Get Backorders

Gets all backorders created since the supplied date.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
swagger_client.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.BackOrderApi()
created_since = '2013-10-20T19:20:30+01:00' # datetime | 

try: 
    # Channel: Get Backorders
    api_response = api_instance.back_order_index(created_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackOrderApi->back_order_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_since** | **datetime**|  | 

### Return type

[**CollectionOfChannelBackOrderResponse**](CollectionOfChannelBackOrderResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

