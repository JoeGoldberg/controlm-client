# controlm_client.BuildApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_file**](BuildApi.md#build_file) | **POST** /build | Compile definitions file to check its validity


# **build_file**
> list[DeploymentFileResults] build_file(definitions_file, deploy_descriptor_file=deploy_descriptor_file)

Compile definitions file to check its validity

Compile the provided definition file (JSON or zip) to verify it is valid for Control-M.

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
api_instance = controlm_client.BuildApi(controlm_client.ApiClient(configuration))
definitions_file = '/path/to/file.txt' # file | A file that contains definitions to be compiled. Can be either a JSON definition file, or a zip file that contains multiple JSON definition files.
deploy_descriptor_file = '/path/to/file.txt' # file | Deploy Descriptor JSON file. (optional)

try:
    # Compile definitions file to check its validity
    api_response = api_instance.build_file(definitions_file, deploy_descriptor_file=deploy_descriptor_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->build_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definitions_file** | **file**| A file that contains definitions to be compiled. Can be either a JSON definition file, or a zip file that contains multiple JSON definition files. | 
 **deploy_descriptor_file** | **file**| Deploy Descriptor JSON file. | [optional] 

### Return type

[**list[DeploymentFileResults]**](DeploymentFileResults.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

