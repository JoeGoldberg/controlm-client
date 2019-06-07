# controlm_client.RunApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_workload_policy**](RunApi.md#activate_workload_policy) | **POST** /run/workloadpolicy/{policy}/activate | activate workload policy
[**add_event**](RunApi.md#add_event) | **POST** /run/event/{ctm} | Add a new  event.
[**add_resource**](RunApi.md#add_resource) | **POST** /run/resource/{ctm} | Add a new quantitative resource.
[**confirm_job**](RunApi.md#confirm_job) | **POST** /run/job/{jobId}/confirm | confirm a job
[**deactivate_workload_policy**](RunApi.md#deactivate_workload_policy) | **POST** /run/workloadpolicy/{policy}/deactivate | deactivate a workload policy
[**delete_event**](RunApi.md#delete_event) | **DELETE** /run/event/{ctm}/{name}/{date} | Delete a  event.
[**delete_job**](RunApi.md#delete_job) | **POST** /run/job/{jobId}/delete | mark job as deleted
[**delete_resource**](RunApi.md#delete_resource) | **DELETE** /run/resource/{ctm}/{name} | Delete a quantitative resource.
[**free_job**](RunApi.md#free_job) | **POST** /run/job/{jobId}/free | free an already held the job
[**get_events**](RunApi.md#get_events) | **GET** /run/events | Get all events records for specific search.
[**get_job_log**](RunApi.md#get_job_log) | **GET** /run/job/{jobId}/log | Get job&#39;s log
[**get_job_output**](RunApi.md#get_job_output) | **GET** /run/job/{jobId}/output | Get job output
[**get_job_status**](RunApi.md#get_job_status) | **GET** /run/job/{jobId}/status | Get status of a job
[**get_jobs_status**](RunApi.md#get_jobs_status) | **GET** /run/status/{runId} | Get status of running jobs
[**get_jobs_status_by_filter**](RunApi.md#get_jobs_status_by_filter) | **GET** /run/jobs/status | Get jobs that match the search criteria.
[**get_resources**](RunApi.md#get_resources) | **GET** /run/resources | Get all resources records matching search.
[**get_workload_policies**](RunApi.md#get_workload_policies) | **GET** /run/workloadpolicies | get workload policies
[**hold_job**](RunApi.md#hold_job) | **POST** /run/job/{jobId}/hold | hold the job so it will not start untill it is freed
[**kill_job**](RunApi.md#kill_job) | **POST** /run/job/{jobId}/kill | Cancel running job
[**order_jobs_in_folder**](RunApi.md#order_jobs_in_folder) | **POST** /run/order | Execute requested jobs in certain folder
[**rerun_job**](RunApi.md#rerun_job) | **POST** /run/job/{jobId}/rerun | Run job again
[**run_jobs**](RunApi.md#run_jobs) | **POST** /run | Run jobs
[**run_now**](RunApi.md#run_now) | **POST** /run/job/{jobId}/runNow | Bypass scheduling cretirias and start the job
[**set_to_ok**](RunApi.md#set_to_ok) | **POST** /run/job/{jobId}/setToOk | set job end status to OK
[**undelete_job**](RunApi.md#undelete_job) | **POST** /run/job/{jobId}/undelete | recover a mark for deletion job
[**update_resource**](RunApi.md#update_resource) | **POST** /run/resource/{ctm}/{name} | Update a quantitative resource.


# **activate_workload_policy**
> WorkloadPolicyStateList activate_workload_policy(policy, ctm=ctm)

activate workload policy

Activate a workload policy, supports wildcard in names

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
policy = 'policy_example' # str | The policy name to be activated. Case sensitive. Wildcards can be used.
ctm = 'ctm_example' # str | Optional Control-M Server filter. (optional)

try:
    # activate workload policy
    api_response = api_instance.activate_workload_policy(policy, ctm=ctm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->activate_workload_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | **str**| The policy name to be activated. Case sensitive. Wildcards can be used. | 
 **ctm** | **str**| Optional Control-M Server filter. | [optional] 

### Return type

[**WorkloadPolicyStateList**](WorkloadPolicyStateList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_event**
> SuccessData add_event(ctm, event)

Add a new  event.

Add a new  event. date may be of format MMDD, ODAT to set current controlm date, STAT to set no date. default value is ODAT.

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server hosting the event.
event = controlm_client.EventParam() # EventParam | The defined event name.

try:
    # Add a new  event.
    api_response = api_instance.add_event(ctm, event)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->add_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server hosting the event. | 
 **event** | [**EventParam**](EventParam.md)| The defined event name. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_resource**
> SuccessData add_resource(ctm, resource)

Add a new quantitative resource.

Add a new quantitative resource.

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server hosting the resource.
resource = controlm_client.ResourceParam() # ResourceParam | The defined resource name.

try:
    # Add a new quantitative resource.
    api_response = api_instance.add_resource(ctm, resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->add_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server hosting the resource. | 
 **resource** | [**ResourceParam**](ResourceParam.md)| The defined resource name. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_job**
> SuccessData confirm_job(job_id)

confirm a job

confirm a job that waits for confirmation

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID

try:
    # confirm a job
    api_response = api_instance.confirm_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->confirm_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_workload_policy**
> WorkloadPolicyStateList deactivate_workload_policy(policy, ctm=ctm)

deactivate a workload policy

Deactivate a workload policy, supports wildcard in names

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
policy = 'policy_example' # str | The policy name to be deactivated. Case sensitive. Wildcards can be used.
ctm = 'ctm_example' # str | Optional Control-M Server filter. (optional)

try:
    # deactivate a workload policy
    api_response = api_instance.deactivate_workload_policy(policy, ctm=ctm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->deactivate_workload_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | **str**| The policy name to be deactivated. Case sensitive. Wildcards can be used. | 
 **ctm** | **str**| Optional Control-M Server filter. | [optional] 

### Return type

[**WorkloadPolicyStateList**](WorkloadPolicyStateList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event**
> SuccessData delete_event(ctm, name, _date)

Delete a  event.

Delete a  event.

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server hosting the event.
name = 'name_example' # str | event name
_date = '_date_example' # str | event date

try:
    # Delete a  event.
    api_response = api_instance.delete_event(ctm, name, _date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->delete_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server hosting the event. | 
 **name** | **str**| event name | 
 **_date** | **str**| event date | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job**
> SuccessData delete_job(job_id)

mark job as deleted

mark delete as deleted

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID

try:
    # mark job as deleted
    api_response = api_instance.delete_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->delete_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource**
> SuccessData delete_resource(ctm, name)

Delete a quantitative resource.

Delete a quantitative resource.

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server hosting the resource.
name = 'name_example' # str | Resource name

try:
    # Delete a quantitative resource.
    api_response = api_instance.delete_resource(ctm, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->delete_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server hosting the resource. | 
 **name** | **str**| Resource name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **free_job**
> SuccessData free_job(job_id)

free an already held the job

free the job

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID

try:
    # free an already held the job
    api_response = api_instance.free_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->free_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events**
> EventSet get_events(ctm=ctm, name=name, _date=_date, limit=limit)

Get all events records for specific search.

Get all events records for specific search.

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | Control-M Server filter. (optional)
name = 'name_example' # str | The event name filter. (optional)
_date = '_date_example' # str | The event date filter. (optional)
limit = 1000 # int | maximum events to fetch (default 1000). (optional) (default to 1000)

try:
    # Get all events records for specific search.
    api_response = api_instance.get_events(ctm=ctm, name=name, _date=_date, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| Control-M Server filter. | [optional] 
 **name** | **str**| The event name filter. | [optional] 
 **_date** | **str**| The event date filter. | [optional] 
 **limit** | **int**| maximum events to fetch (default 1000). | [optional] [default to 1000]

### Return type

[**EventSet**](EventSet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_log**
> str get_job_log(job_id)

Get job's log

Get the job execution log.

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID

try:
    # Get job's log
    api_response = api_instance.get_job_log(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_job_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_output**
> str get_job_output(job_id, run_no=run_no)

Get job output

Get the output returned from a job.

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID
run_no = 0 # int | The execution number in case of multiple executions (0 will get the last execution's output) (optional) (default to 0)

try:
    # Get job output
    api_response = api_instance.get_job_output(job_id, run_no=run_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_job_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 
 **run_no** | **int**| The execution number in case of multiple executions (0 will get the last execution&#39;s output) | [optional] [default to 0]

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_status**
> JobRunStatus get_job_status(job_id)

Get status of a job

Get the job status.

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
job_id = 'job_id_example' # str | Job ID returned from the run status action.

try:
    # Get status of a job
    api_response = api_instance.get_job_status(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_job_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID returned from the run status action. | 

### Return type

[**JobRunStatus**](JobRunStatus.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs_status**
> JobStatusResult get_jobs_status(run_id, start_index=start_index)

Get status of running jobs

Run status of jobs started with the Run service.

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
run_id = 'run_id_example' # str | Run ID returned from the run action.
start_index = 0 # int | The index of the job status from which to start. returning results (optional) (default to 0)

try:
    # Get status of running jobs
    api_response = api_instance.get_jobs_status(run_id, start_index=start_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_jobs_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| Run ID returned from the run action. | 
 **start_index** | **int**| The index of the job status from which to start. returning results | [optional] [default to 0]

### Return type

[**JobStatusResult**](JobStatusResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs_status_by_filter**
> JobStatusResult get_jobs_status_by_filter(limit=limit, jobname=jobname, ctm=ctm, application=application, sub_application=sub_application, host=host, status=status, folder=folder, description=description, jobid=jobid, neighborhood=neighborhood, depth=depth, direction=direction, order_date_from=order_date_from, order_date_to=order_date_to, from_time=from_time, to_time=to_time, folder_library=folder_library, host_group=host_group, run_as=run_as, command=command, file_path=file_path, file_name=file_name, workload_policy=workload_policy, rule_based_calendar=rule_based_calendar, resource_mutex=resource_mutex, resource_semaphore=resource_semaphore)

Get jobs that match the search criteria.

Get status of jobs that match the requested search criteria.

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
limit = 1000 # int | maximum jobs status to fetch (default 1000). (optional) (default to 1000)
jobname = 'jobname_example' # str |  (optional)
ctm = 'ctm_example' # str |  (optional)
application = 'application_example' # str |  (optional)
sub_application = 'sub_application_example' # str |  (optional)
host = 'host_example' # str |  (optional)
status = 'status_example' # str |  (optional)
folder = 'folder_example' # str |  (optional)
description = 'description_example' # str |  (optional)
jobid = 'jobid_example' # str |  (optional)
neighborhood = 'neighborhood_example' # str |  (optional)
depth = 56 # int |  (optional)
direction = 'direction_example' # str |  (optional)
order_date_from = 'order_date_from_example' # str |  (optional)
order_date_to = 'order_date_to_example' # str |  (optional)
from_time = 'from_time_example' # str |  (optional)
to_time = 'to_time_example' # str |  (optional)
folder_library = 'folder_library_example' # str |  (optional)
host_group = 'host_group_example' # str |  (optional)
run_as = 'run_as_example' # str |  (optional)
command = 'command_example' # str |  (optional)
file_path = 'file_path_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)
workload_policy = 'workload_policy_example' # str |  (optional)
rule_based_calendar = 'rule_based_calendar_example' # str |  (optional)
resource_mutex = 'resource_mutex_example' # str |  (optional)
resource_semaphore = 'resource_semaphore_example' # str |  (optional)

try:
    # Get jobs that match the search criteria.
    api_response = api_instance.get_jobs_status_by_filter(limit=limit, jobname=jobname, ctm=ctm, application=application, sub_application=sub_application, host=host, status=status, folder=folder, description=description, jobid=jobid, neighborhood=neighborhood, depth=depth, direction=direction, order_date_from=order_date_from, order_date_to=order_date_to, from_time=from_time, to_time=to_time, folder_library=folder_library, host_group=host_group, run_as=run_as, command=command, file_path=file_path, file_name=file_name, workload_policy=workload_policy, rule_based_calendar=rule_based_calendar, resource_mutex=resource_mutex, resource_semaphore=resource_semaphore)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_jobs_status_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| maximum jobs status to fetch (default 1000). | [optional] [default to 1000]
 **jobname** | **str**|  | [optional] 
 **ctm** | **str**|  | [optional] 
 **application** | **str**|  | [optional] 
 **sub_application** | **str**|  | [optional] 
 **host** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **folder** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **jobid** | **str**|  | [optional] 
 **neighborhood** | **str**|  | [optional] 
 **depth** | **int**|  | [optional] 
 **direction** | **str**|  | [optional] 
 **order_date_from** | **str**|  | [optional] 
 **order_date_to** | **str**|  | [optional] 
 **from_time** | **str**|  | [optional] 
 **to_time** | **str**|  | [optional] 
 **folder_library** | **str**|  | [optional] 
 **host_group** | **str**|  | [optional] 
 **run_as** | **str**|  | [optional] 
 **command** | **str**|  | [optional] 
 **file_path** | **str**|  | [optional] 
 **file_name** | **str**|  | [optional] 
 **workload_policy** | **str**|  | [optional] 
 **rule_based_calendar** | **str**|  | [optional] 
 **resource_mutex** | **str**|  | [optional] 
 **resource_semaphore** | **str**|  | [optional] 

### Return type

[**JobStatusResult**](JobStatusResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resources**
> ResourceSet get_resources(ctm=ctm, name=name)

Get all resources records matching search.

Get all resources records matching search.

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | Control-M Server filter. (optional)
name = 'name_example' # str | The resource name filter. (optional)

try:
    # Get all resources records matching search.
    api_response = api_instance.get_resources(ctm=ctm, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| Control-M Server filter. | [optional] 
 **name** | **str**| The resource name filter. | [optional] 

### Return type

[**ResourceSet**](ResourceSet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workload_policies**
> WorkloadPolicyList get_workload_policies(state=state)

get workload policies

Get all the workload policies.

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
state = 'state_example' # str | Optionally state filter. Available values Active, Inactive (optional)

try:
    # get workload policies
    api_response = api_instance.get_workload_policies(state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_workload_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| Optionally state filter. Available values Active, Inactive | [optional] 

### Return type

[**WorkloadPolicyList**](WorkloadPolicyList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hold_job**
> SuccessData hold_job(job_id)

hold the job so it will not start untill it is freed

hold the job

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID

try:
    # hold the job so it will not start untill it is freed
    api_response = api_instance.hold_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->hold_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kill_job**
> SuccessData kill_job(job_id)

Cancel running job

Abort job execution.

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID

try:
    # Cancel running job
    api_response = api_instance.kill_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->kill_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_jobs_in_folder**
> RunResult order_jobs_in_folder(data=data)

Execute requested jobs in certain folder

Run jobs from selected folder according to given filter

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
data = controlm_client.OrderFolderParameters() # OrderFolderParameters | parameters to select the jobs to run (optional)

try:
    # Execute requested jobs in certain folder
    api_response = api_instance.order_jobs_in_folder(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->order_jobs_in_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**OrderFolderParameters**](OrderFolderParameters.md)| parameters to select the jobs to run | [optional] 

### Return type

[**RunResult**](RunResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rerun_job**
> JobRunStatus rerun_job(job_id)

Run job again

Run an already executed job (again).

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID

try:
    # Run job again
    api_response = api_instance.rerun_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->rerun_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 

### Return type

[**JobRunStatus**](JobRunStatus.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_jobs**
> RunResult run_jobs(job_definitions_file, deploy_descriptor_file=deploy_descriptor_file)

Run jobs

Run jobs according to given definitions file (JSON or zip).

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
job_definitions_file = '/path/to/file.txt' # file | File that contains the definitions of the jobs to run. It can be a JSON file, or a zip file that can contain one or more JSON files, as well as account(s) information.
deploy_descriptor_file = '/path/to/file.txt' # file | Deploy Descriptor JSON file. (optional)

try:
    # Run jobs
    api_response = api_instance.run_jobs(job_definitions_file, deploy_descriptor_file=deploy_descriptor_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->run_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_definitions_file** | **file**| File that contains the definitions of the jobs to run. It can be a JSON file, or a zip file that can contain one or more JSON files, as well as account(s) information. | 
 **deploy_descriptor_file** | **file**| Deploy Descriptor JSON file. | [optional] 

### Return type

[**RunResult**](RunResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_now**
> SuccessData run_now(job_id)

Bypass scheduling cretirias and start the job

start a job immediately

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID

try:
    # Bypass scheduling cretirias and start the job
    api_response = api_instance.run_now(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->run_now: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_to_ok**
> SuccessData set_to_ok(job_id)

set job end status to OK

set job status to OK, post processing action

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID

try:
    # set job end status to OK
    api_response = api_instance.set_to_ok(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->set_to_ok: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **undelete_job**
> SuccessData undelete_job(job_id)

recover a mark for deletion job

recover a mark for deletion job

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID

try:
    # recover a mark for deletion job
    api_response = api_instance.undelete_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->undelete_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resource**
> SuccessData update_resource(ctm, name, max)

Update a quantitative resource.

Update a quantitative resource.

### Example
```python
from __future__ import print_function
import time
import controlm_client
from controlm_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = controlm_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_client.RunApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server hosting the resource.
name = 'name_example' # str | Resource name
max = controlm_client.ResourceMax() # ResourceMax | The defined resource name.

try:
    # Update a quantitative resource.
    api_response = api_instance.update_resource(ctm, name, max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->update_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server hosting the resource. | 
 **name** | **str**| Resource name | 
 **max** | [**ResourceMax**](ResourceMax.md)| The defined resource name. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

