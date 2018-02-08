# ChannelEngine
Please visit https://www.channelengine.com/developers/ for more information.
The API reference can be found at https://demo.channelengine.net/api/swagger/ui/index

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import channelengine_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import channelengine_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import channelengine_api_client
from channelengine_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
channelengine_api_client.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# channelengine_api_client.configuration.api_key_prefix['apikey'] = 'Bearer'
# create an instance of the API class
api_instance = channelengine_api_client.CancellationApi()
cancellation = channelengine_api_client.MerchantCancellationRequest() # MerchantCancellationRequest | 

try:
    # Merchant: Create Cancellation
    api_response = api_instance.cancellation_create(cancellation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CancellationApi->cancellation_create: %s\n" % e)

```
