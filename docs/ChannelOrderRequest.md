# ChannelOrderRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_order_no** | **str** | The unique order reference used by the Channel | 
**lines** | [**list[ChannelOrderLineRequest]**](ChannelOrderLineRequest.md) | The order lines | 
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


