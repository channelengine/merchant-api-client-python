# swagger_client.ShipmentApi

All URIs are relative to *http://dev.channelengine.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shipment_create**](ShipmentApi.md#shipment_create) | **POST** /v2/shipments | Merchant: Create Shipment
[**shipment_index**](ShipmentApi.md#shipment_index) | **GET** /v2/shipments | Channel: Get Shipments
[**shipment_update**](ShipmentApi.md#shipment_update) | **PUT** /v2/shipments/{merchantShipmentNo} | Merchant: Update Shipment


# **shipment_create**
> ApiResponse shipment_create(model)

Merchant: Create Shipment

For merchants.    Mark (part of) an order as shipped.

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
api_instance = swagger_client.ShipmentApi(swagger_client.ApiClient(configuration))
model = swagger_client.MerchantShipmentRequest() # MerchantShipmentRequest | 

try: 
    # Merchant: Create Shipment
    api_response = api_instance.shipment_create(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentApi->shipment_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**MerchantShipmentRequest**](MerchantShipmentRequest.md)|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_index**
> CollectionOfChannelShipmentResponse shipment_index(created_since)

Channel: Get Shipments

For channels.    Gets all shipments created since the supplied date.

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
api_instance = swagger_client.ShipmentApi(swagger_client.ApiClient(configuration))
created_since = '2013-10-20T19:20:30+01:00' # datetime | 

try: 
    # Channel: Get Shipments
    api_response = api_instance.shipment_index(created_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentApi->shipment_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_since** | **datetime**|  | 

### Return type

[**CollectionOfChannelShipmentResponse**](CollectionOfChannelShipmentResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_update**
> ApiResponse shipment_update(merchant_shipment_no, model)

Merchant: Update Shipment

For merchants.    Update an existing shipment with tracking information

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
api_instance = swagger_client.ShipmentApi(swagger_client.ApiClient(configuration))
merchant_shipment_no = 'merchant_shipment_no_example' # str | The merchant's shipment reference
model = swagger_client.MerchantShipmentTrackingRequest() # MerchantShipmentTrackingRequest | The updated tracking information

try: 
    # Merchant: Update Shipment
    api_response = api_instance.shipment_update(merchant_shipment_no, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentApi->shipment_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_shipment_no** | **str**| The merchant&#39;s shipment reference | 
 **model** | [**MerchantShipmentTrackingRequest**](MerchantShipmentTrackingRequest.md)| The updated tracking information | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

