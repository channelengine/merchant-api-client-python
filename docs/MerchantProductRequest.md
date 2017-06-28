# MerchantProductRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_product_no** | **str** | A unique identifier of the product. | [optional] 
**parent_merchant_product_no** | **str** | If this product is a different version of another  product (for example, all fields are the same except  size and/or color), then this field should contain  the &#39;MerchantProductNo&#39; of the parent. The parent  should already exist (or be present between the products  in the content of the API call, it does not matter whether   the parent is behind the child in the list). | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**brand** | **str** |  | [optional] 
**size** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**ean** | **str** |  | [optional] 
**manufacturer_product_number** | **str** |  | [optional] 
**stock** | **int** |  | [optional] 
**price** | **float** | Price, including VAT. | [optional] 
**msrp** | **float** | Manufacturer&#39;s suggested retail price | [optional] 
**purchase_price** | **float** |  | [optional] 
**vat_rate_type** | **str** | The type of VAT which applies to this product.  See: http://ec.europa.eu/taxation_customs/taxation/vat/topics/rates_en.htm | [optional] 
**shipping_cost** | **float** |  | [optional] 
**shipping_time** | **str** | A textual representation of the shippingtime.  For example, in Dutch: &#39;Op werkdagen voor 22:00 uur besteld, morgen in huis&#39; | [optional] 
**url** | **str** | A URL pointing to the merchant&#39;s webpage  which displays this product. | [optional] 
**image_url** | **str** | A URL at which an image of this product  can be found. | [optional] 
**category_trail** | **str** | The category to which this product belongs.  Please supply this field in the following format:  &#39;maincategory &amp;gt; category &amp;gt; subcategory&#39;  For example:  &#39;vehicles &amp;gt; bikes &amp;gt; mountainbike&#39; | [optional] 
**extra_data** | [**list[ExtraDataItem]**](ExtraDataItem.md) | An optional list of key-value pairs containing  extra data about this product. This data can be  sent to channels or used for filtering products. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


