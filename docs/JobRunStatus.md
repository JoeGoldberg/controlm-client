# JobRunStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Order ID of the job. | 
**folder_id** | **str** | Order ID of the folder containing this job. | [optional] 
**number_of_runs** | **int** | The run number (in case of cyclic jobs or reruns) | [optional] 
**name** | **str** | The name of the run job. | [optional] 
**folder** | **str** | The name of the run job. | [optional] 
**type** | **str** | The type of the run job. | [optional] 
**status** | **str** | The status of the run job. | [optional] 
**held** | **bool** | Is job held. | [optional] 
**deleted** | **bool** | Is job held. | [optional] 
**start_time** | **str** | The start time of the job run. | [optional] 
**end_time** | **str** | The end time of the job run. | [optional] 
**estimated_start_time** | **list[str]** | The estimated start time of the jobs. | [optional] 
**estimated_end_time** | **list[str]** | The estimated end time of the jobs. | [optional] 
**order_date** | **str** | The order date. | [optional] 
**ctm** | **str** | The controlm server. | [optional] 
**description** | **str** | The job description. | [optional] 
**host** | **str** | host machine where the job runs. | [optional] 
**application** | **str** | job application. | [optional] 
**sub_application** | **str** | job subApplication. | [optional] 
**job_json** | **str** | The JSON string that describes the job. | [optional] 
**output_uri** | **str** | A URI that can be used to get the output of the run job | [optional] 
**log_uri** | **str** | A URI that can be used to get the log of the run job | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


