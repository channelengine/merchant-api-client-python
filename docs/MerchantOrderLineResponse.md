# MerchantOrderLineResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**is_fulfillment_by_marketplace** | **bool** |  | [optional] 
**merchant_product_no** | **str** |  | [optional] 
**channel_product_no** | **str** |  | 
**quantity** | **int** |  | 
**unit_price_incl_vat** | **float** | The value of a single unit of the ordered product including VAT  (in the tenant&#39;s base currency calculated using the exchange rate at the time of ordering). | 
**fee_fixed** | **float** | A fixed fee that is charged by the Channel for this orderline.  This field is optional, send 0 if not applicable. | [optional] 
**fee_rate** | **float** | A percentage fee that is charged by the Channel for this orderline.  This field is optional, send 0 if not applicable. | [optional] 
**condition** | **str** | The condition of the product, this can be used to indicate that a product is a second-hand product | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


