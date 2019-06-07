# JobStatusResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statuses** | [**list[JobRunStatus]**](JobRunStatus.md) | The list of statuses tracked by the given runId. | [optional] 
**start_index** | **int** | The index of the first item in the list. | [optional] 
**items_per_page** | **int** | The maximum number of items returned by each status request. | [optional] 
**returned** | **int** | The number of the return items by the search. | [optional] 
**total** | **int** | The total number of items. | [optional] 
**sort** | **str** | The field the list is sorted by. | [optional] 
**next_uri** | **str** | URI to get the next items in the list, if any. | [optional] 
**prev_uri** | **str** | URI to get the previous items in the list, if any. | [optional] 
**monitor_page_uri** | **str** | A URI to a page displaying the workflow run live. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


