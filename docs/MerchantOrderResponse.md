# MerchantOrderResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier used by ChannelEngine. This identifier does  not have to be saved. It should only be used in a call to acknowledge the order. | [optional] 
**channel_name** | **str** |  | [optional] 
**channel_order_support** | **str** |  | [optional] 
**channel_order_no** | **str** |  | [optional] 
**lines** | [**list[MerchantOrderLineResponse]**](MerchantOrderLineResponse.md) |  | [optional] 
**phone** | **str** |  | [optional] 
**email** | **str** |  | 
**company_registration_no** | **str** |  | [optional] 
**vat_no** | **str** |  | [optional] 
**payment_method** | **str** |  | 
**shipping_costs_incl_vat** | **float** | The shipping fee including VAT  (in the tenant&#39;s base currency calculated using the exchange rate at the time of ordering). | 
**currency_code** | **str** |  | 
**order_date** | **datetime** |  | 
**channel_customer_no** | **str** |  | [optional] 
**billing_address** | [**EntitiesAddressModels**](EntitiesAddressModels.md) |  | 
**shipping_address** | [**EntitiesAddressModels**](EntitiesAddressModels.md) |  | 
**extra_data** | **dict(str, str)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


