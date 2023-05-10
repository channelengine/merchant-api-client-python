# ChannelEngine
[![No Maintenance Intended](https://img.shields.io/badge/STATUS-DEPRECATED-%23cf0000?style=for-the-badge)](https://support.channelengine.com/hc/en-us/articles/4409503691165-Merchant-API-API-clients)

### Deprecation of the Merchant API client libraries

This library is no longer supported by ChannelEngine. To build your own library via OpenAPI Generator, using your programming language of choice, check out the [Merchant API: API clients](https://support.channelengine.com/hc/en-us/articles/4409503691165-Merchant-API-API-clients) article in our Help Center.

ChannelEngine’s APIs follow the OpenAPI/Swagger specifications, which you can find in our [API reference](https://demo.channelengine.net/api/swagger/index.html). 

### Additional information for developers
For detailed information on ChannelEngine’s APIs, go to the [REST APIs category](https://support.channelengine.com/hc/en-us/categories/4419833201937-REST-APIs) in our Help Center.


## Requirements.

Python 3.6+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install channelengine-merchant-api-client
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import channelengine_merchant_api_client 
```

## Documentation for API Endpoints
Please refer to https://demo.channelengine.net/api/swagger

## Example usage

```python
from channelengine_merchant_api_client import ApiClient, OrderApi, ProductApi, OfferApi, ReturnApi, Configuration
from channelengine_merchant_api_client.rest import ApiException
from pprint import pprint
from datetime import datetime
from dateutil.relativedelta import relativedelta

def main():

    # Configure API key authorization: apikey
    config = Configuration()
    config.api_key['apikey'] = 'xxxxxxxxxx'
    config.host = 'https://demo.channelengine.net/api'

    client = ApiClient(config)

    # create an instance of the API class
    order_api = OrderApi(client)
    product_api = ProductApi(client)
    offer_api = OfferApi(client)
    return_api = ReturnApi(client)

    try:
        # Merchant: Update offer
        offer = [{'MerchantProductNo': 'ABC123', 'Stock': '98'}]
        pprint(offer_api.offer_stock_price_update(offer))
        
        # Merchant: Get returns
        two_years_ago = datetime.now() - relativedelta(years=2)
        returns = return_api.return_get_declared_by_channel(two_years_ago)
        pprint(returns)

        # Merchant: Get new orders
        new_orders = order_api.order_get_new()
        pprint(new_orders)

        # Merchant: Get product by MPN
        product = product_api.product_get_by_merchant_product_no('ABC123')
        pprint(product)

    except ApiException as e:
        print("Exception when calling API: %s\n" % e)

if __name__ == '__main__':
    main()
```
