# controlm_client.ReportingApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_report_by_name**](ReportingApi.md#get_report_by_name) | **GET** /reporting/report/{name} | Retrives a report by name.
[**get_report_status**](ReportingApi.md#get_report_status) | **GET** /reporting/status/{reportId} | Retrieves status information for a report generation request based on the report ID
[**run_report**](ReportingApi.md#run_report) | **POST** /reporting/report | Run a report


# **get_report_by_name**
> ReportResult get_report_by_name(name, format=format)

Retrives a report by name.

Retrieves a report by name in the desired format (CSV or PDF). If the report is shared, add [shared:] before the name. This REST API command will be deprecated soon.

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
api_instance = controlm_client.ReportingApi(controlm_client.ApiClient(configuration))
name = 'name_example' # str | The report name.
format = 'format_example' # str |  (optional)

try:
    # Retrives a report by name.
    api_response = api_instance.get_report_by_name(name, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingApi->get_report_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The report name. | 
 **format** | **str**|  | [optional] 

### Return type

[**ReportResult**](ReportResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_status**
> RunReportInfo get_report_status(report_id)

Retrieves status information for a report generation request based on the report ID

Retrieves status information for a report generation request based on the report ID

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
api_instance = controlm_client.ReportingApi(controlm_client.ApiClient(configuration))
report_id = 'report_id_example' # str | The ID of the report

try:
    # Retrieves status information for a report generation request based on the report ID
    api_response = api_instance.get_report_status(report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingApi->get_report_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| The ID of the report | 

### Return type

[**RunReportInfo**](RunReportInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_report**
> RunReportInfo run_report(report_run)

Run a report

Sends a request to generate a report asynchronously and returns the request status. If the report is shared, add [shared:] before the name.

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
api_instance = controlm_client.ReportingApi(controlm_client.ApiClient(configuration))
report_run = controlm_client.RunReport() # RunReport | The report generation parameters

try:
    # Run a report
    api_response = api_instance.run_report(report_run)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingApi->run_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_run** | [**RunReport**](RunReport.md)| The report generation parameters | 

### Return type

[**RunReportInfo**](RunReportInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

