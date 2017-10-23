# channelengine_api_client.OfferApi

All URIs are relative to *http://dev.channelengine.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offer_stock_price_update**](OfferApi.md#offer_stock_price_update) | **PUT** /v2/offer | Update stock or price.


# **offer_stock_price_update**
> SingleOfCollectionsDictionary2Generic offer_stock_price_update(updates)

Update stock or price.

### Example 
```python
from __future__ import print_function
import time
import channelengine_api_client
from channelengine_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = channelengine_api_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = channelengine_api_client.OfferApi(channelengine_api_client.ApiClient(configuration))
updates = [channelengine_api_client.MerchantStockPriceUpdateRequest()] # list[MerchantStockPriceUpdateRequest] | References to the products that should be updated, and the new values  for the stock or price fields. It is possible to supply only one of the two fields  or both.

try: 
    # Update stock or price.
    api_response = api_instance.offer_stock_price_update(updates)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfferApi->offer_stock_price_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updates** | [**list[MerchantStockPriceUpdateRequest]**](MerchantStockPriceUpdateRequest.md)| References to the products that should be updated, and the new values  for the stock or price fields. It is possible to supply only one of the two fields  or both. | 

### Return type

[**SingleOfCollectionsDictionary2Generic**](SingleOfCollectionsDictionary2Generic.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

