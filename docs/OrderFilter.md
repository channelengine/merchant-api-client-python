# OrderFilter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statuses** | **list[str]** |  | [optional] 
**merchant_order_nos** | **list[str]** |  | [optional] 
**exclude_marketplace_fulfilled_orders_and_lines** | **bool** |  | [optional] 
**fulfillment_type** | **str** | Filter orders on fulfillment type. This will include all orders lines, even if they are partially fulfilled by the marketplace.  To exclude orders and lines that are fulfilled by the marketplace from the response, set ExcludeMarketplaceFulfilledOrdersAndLines to true. | [optional] 
**page** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


