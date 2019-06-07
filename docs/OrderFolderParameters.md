# OrderFolderParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ctm** | **str** | The Control-M Server to order from. REQUIRED. | [optional] 
**folder** | **str** | The folder to order. REQUIRED. | [optional] 
**jobs** | **str** | Filter the jobs to order. | [optional] 
**create_duplicate** | **bool** | Is it allowed to order the same jobs more than once to the same SMART folder. HIDDEN. | [optional] 
**hold** | **bool** | Are jobs ordered in a HOLD state. HIDDEN. | [optional] 
**ignore_criteria** | **bool** | Is scheduling criteria to be ignored. HIDDEN. | [optional] 
**independent_flow** | **bool** | Whether to generate new flow in this order. HIDDEN. | [optional] 
**order_date** | **str** | The order date that is attached to this order command. HIDDEN. | [optional] 
**order_into_folder** | **str** | Policy for placing the jobs in a SMART folder. HIDDEN. | [optional] 
**wait_for_order_date** | **bool** | Whether to wait for the order date when running the jobs. HIDDEN. | [optional] 
**variables** | **list[dict(str, str)]** | Job Variables for this run. HIDDEN. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


