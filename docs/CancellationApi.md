# swagger_client.CancellationApi

All URIs are relative to *http://dev.channelengine.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancellation_create**](CancellationApi.md#cancellation_create) | **POST** /v2/cancellations | Merchant: Create Cancellation
[**cancellation_index**](CancellationApi.md#cancellation_index) | **GET** /v2/cancellations | Channel: Get Cancellations


# **cancellation_create**
> ApiResponse cancellation_create(cancellation)

Merchant: Create Cancellation

For merchants.    Mark (part of) an order as cancelled.

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
api_instance = swagger_client.CancellationApi(swagger_client.ApiClient(configuration))
cancellation = swagger_client.MerchantCancellationRequest() # MerchantCancellationRequest | 

try: 
    # Merchant: Create Cancellation
    api_response = api_instance.cancellation_create(cancellation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CancellationApi->cancellation_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancellation** | [**MerchantCancellationRequest**](MerchantCancellationRequest.md)|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancellation_index**
> CollectionOfChannelCancellationResponse cancellation_index(created_since)

Channel: Get Cancellations

For channels.    Gets all cancellations created since the supplied date.

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
api_instance = swagger_client.CancellationApi(swagger_client.ApiClient(configuration))
created_since = '2013-10-20T19:20:30+01:00' # datetime | 

try: 
    # Channel: Get Cancellations
    api_response = api_instance.cancellation_index(created_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CancellationApi->cancellation_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_since** | **datetime**|  | 

### Return type

[**CollectionOfChannelCancellationResponse**](CollectionOfChannelCancellationResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

