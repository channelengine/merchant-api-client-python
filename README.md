# channelengine-api-client
## Requirements.

Python 2.7 and 3.4+

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
    config.api_key['apiKey'] = 'xxxxxxxxxx'
    config.host = 'https://demo.channelengine.net/api'

    client = ApiClient(config)

    # create an instance of the API class
    order_api = OrderApi(client)
    product_api = ProductApi(client)
    offer_api = OfferApi(client)
    return_api = ReturnApi(client)

    try:
        # Merchant: Update offer
        # returns a 200 with "product not found" warning in content
        offer = [{'MerchantProductNo': 'ABC123', 'Stock': '98'}]
        pprint(offer_api.offer_stock_price_update(merchant_stock_price_update_request=offer))
        
        # Merchant: Get returns
        two_years_ago = datetime.now() - relativedelta(years=2)
        returns = return_api.return_get_declared_by_channel(from_date=two_years_ago)
        pprint(returns)

        # Merchant: Get new orders
        new_orders = order_api.order_get_new()
        pprint(new_orders)

        # Merchant: Get product by MPN
        # raises a 404 on product not found
        product = product_api.product_get_by_merchant_product_no('ABC123')
        pprint(product)

    except ApiException as e:
        print("Exception when calling API: %s\n" % e)

if __name__ == '__main__':
    main()
```
