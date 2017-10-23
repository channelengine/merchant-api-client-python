# swagger_client.ReturnApi

All URIs are relative to *http://dev.channelengine.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**return_declare_for_channel**](ReturnApi.md#return_declare_for_channel) | **POST** /v2/returns/channel | Channel: Create Return
[**return_declare_for_merchant**](ReturnApi.md#return_declare_for_merchant) | **POST** /v2/returns/merchant | Merchant: Create Return
[**return_get_declared_by_channel**](ReturnApi.md#return_get_declared_by_channel) | **GET** /v2/returns/merchant | Merchant: Get Returns
[**return_get_declared_by_merchant**](ReturnApi.md#return_get_declared_by_merchant) | **GET** /v2/returns/channel | Channel: Get Returns


# **return_declare_for_channel**
> ApiResponse return_declare_for_channel(model)

Channel: Create Return

For channels.                Mark (part of) an order as returned by the customer.

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
api_instance = swagger_client.ReturnApi(swagger_client.ApiClient(configuration))
model = swagger_client.ChannelReturnRequest() # ChannelReturnRequest | 

try: 
    # Channel: Create Return
    api_response = api_instance.return_declare_for_channel(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnApi->return_declare_for_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**ChannelReturnRequest**](ChannelReturnRequest.md)|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_declare_for_merchant**
> ApiResponse return_declare_for_merchant(model)

Merchant: Create Return

For merchants.    Mark (part of) an order as returned by the customer.

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
api_instance = swagger_client.ReturnApi(swagger_client.ApiClient(configuration))
model = swagger_client.MerchantReturnRequest() # MerchantReturnRequest | 

try: 
    # Merchant: Create Return
    api_response = api_instance.return_declare_for_merchant(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnApi->return_declare_for_merchant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**MerchantReturnRequest**](MerchantReturnRequest.md)|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_get_declared_by_channel**
> CollectionOfMerchantReturnResponse return_get_declared_by_channel(created_since)

Merchant: Get Returns

For merchants.    Get all returns created by the channel. This call is supposed  to be used by merchants. Channels should use the 'GET /v2/returns/channel'  call.

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
api_instance = swagger_client.ReturnApi(swagger_client.ApiClient(configuration))
created_since = '2013-10-20T19:20:30+01:00' # datetime | 

try: 
    # Merchant: Get Returns
    api_response = api_instance.return_get_declared_by_channel(created_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnApi->return_get_declared_by_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_since** | **datetime**|  | 

### Return type

[**CollectionOfMerchantReturnResponse**](CollectionOfMerchantReturnResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_get_declared_by_merchant**
> CollectionOfChannelReturnResponse return_get_declared_by_merchant(created_since)

Channel: Get Returns

For channels.                Get all returns created by the merchant. This call is supposed  to be used by channels. Merchants should use the 'GET /v2/returns/merchant'  call.

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
api_instance = swagger_client.ReturnApi(swagger_client.ApiClient(configuration))
created_since = '2013-10-20T19:20:30+01:00' # datetime | 

try: 
    # Channel: Get Returns
    api_response = api_instance.return_get_declared_by_merchant(created_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnApi->return_get_declared_by_merchant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_since** | **datetime**|  | 

### Return type

[**CollectionOfChannelReturnResponse**](CollectionOfChannelReturnResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

