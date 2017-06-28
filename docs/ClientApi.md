# swagger_client.ClientApi

All URIs are relative to *http://dev.channelengine.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client_get**](ClientApi.md#client_get) | **GET** /v2/clients/{language} | Get API Client


# **client_get**
> file client_get(language)

Get API Client

This call generates a Swagger API client and returns it as a ZIP

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
api_instance = swagger_client.ClientApi()
language = 'language_example' # str | The programming language

try: 
    # Get API Client
    api_response = api_instance.client_get(language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->client_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| The programming language | 

### Return type

[**file**](file.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

