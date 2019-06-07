# controlm_client.SamplesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_many_samples**](SamplesApi.md#add_many_samples) | **POST** /samples/load | Upload samples file
[**add_sample**](SamplesApi.md#add_sample) | **POST** /samples | Create sample
[**delete_sample**](SamplesApi.md#delete_sample) | **DELETE** /samples/{sampleId} | Delete sample
[**find_sample_by_id**](SamplesApi.md#find_sample_by_id) | **GET** /samples/{sampleId} | Get sample
[**get_samples**](SamplesApi.md#get_samples) | **GET** /samples | Get all samples


# **add_many_samples**
> SamplesLoadData add_many_samples(samples_file)

Upload samples file

Bulk create many samples by uploading a file.

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
api_instance = controlm_client.SamplesApi(controlm_client.ApiClient(configuration))
samples_file = '/path/to/file.txt' # file | Samples file to upload.

try:
    # Upload samples file
    api_response = api_instance.add_many_samples(samples_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SamplesApi->add_many_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **samples_file** | **file**| Samples file to upload. | 

### Return type

[**SamplesLoadData**](SamplesLoadData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_sample**
> AddRemoveSuccessData add_sample(new_sample)

Create sample

Create a new sample in the system.

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
api_instance = controlm_client.SamplesApi(controlm_client.ApiClient(configuration))
new_sample = controlm_client.NewSample() # NewSample | Sample to add

try:
    # Create sample
    api_response = api_instance.add_sample(new_sample)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SamplesApi->add_sample: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_sample** | [**NewSample**](NewSample.md)| Sample to add | 

### Return type

[**AddRemoveSuccessData**](AddRemoveSuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sample**
> SuccessData delete_sample(sample_id)

Delete sample

Deletes a single sample based on the ID supplied.

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
api_instance = controlm_client.SamplesApi(controlm_client.ApiClient(configuration))
sample_id = 789 # int | ID of sample to delete

try:
    # Delete sample
    api_response = api_instance.delete_sample(sample_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SamplesApi->delete_sample: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**| ID of sample to delete | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_sample_by_id**
> Sample find_sample_by_id(sample_id)

Get sample

Get a specific sample.

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
api_instance = controlm_client.SamplesApi(controlm_client.ApiClient(configuration))
sample_id = 789 # int | ID of the sample to return.

try:
    # Get sample
    api_response = api_instance.find_sample_by_id(sample_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SamplesApi->find_sample_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**| ID of the sample to return. | 

### Return type

[**Sample**](Sample.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_samples**
> list[Sample] get_samples()

Get all samples

List all samples defined in the system.

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
api_instance = controlm_client.SamplesApi(controlm_client.ApiClient(configuration))

try:
    # Get all samples
    api_response = api_instance.get_samples()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SamplesApi->get_samples: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Sample]**](Sample.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

