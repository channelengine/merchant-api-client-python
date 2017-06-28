# ChannelProcessedChangesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | [**list[ChannelReferencesRequest]**](ChannelReferencesRequest.md) | A collection of pairs of merchant and channel references  of the products which are successfully created. The channel references  are saved such that in subsequent calls these can be used instead of the   merchant references. | [optional] 
**updated** | **list[str]** | The channel references of the products which are successfully updated. | [optional] 
**removed** | **list[str]** | The channel references of the products which are successfully removed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


