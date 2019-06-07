# controlm_client.DeployApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_connection_profile**](DeployApi.md#delete_connection_profile) | **DELETE** /deploy/connectionprofile/{ctm}/{agent}/{type}/{name} | Delete a Connection Profile
[**delete_folder**](DeployApi.md#delete_folder) | **DELETE** /deploy/folder/{controlM}/{folderName} | delete a folder
[**deploy_file**](DeployApi.md#deploy_file) | **POST** /deploy | Deploy definitions file
[**get_deployed_connection_profiles**](DeployApi.md#get_deployed_connection_profiles) | **GET** /deploy/connectionprofiles | Get deployed folder
[**get_deployed_folders_new**](DeployApi.md#get_deployed_folders_new) | **GET** /deploy/jobs | Get deployed jobs that match the search criteria.
[**transform_file**](DeployApi.md#transform_file) | **POST** /deploy/transform | Transform a definitions file


# **delete_connection_profile**
> SuccessData delete_connection_profile(ctm, agent, type, name)

Delete a Connection Profile

Delete a Connection Profile

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
api_instance = controlm_client.DeployApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The name of the Control-M in which the connection profile is deployed.
agent = 'agent_example' # str | The name of the agent the connection profile is deployed on.
type = 'type_example' # str | The name of the agent the connection profile is deployed on.
name = 'name_example' # str | Name of the Connection Profile

try:
    # Delete a Connection Profile
    api_response = api_instance.delete_connection_profile(ctm, agent, type, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->delete_connection_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The name of the Control-M in which the connection profile is deployed. | 
 **agent** | **str**| The name of the agent the connection profile is deployed on. | 
 **type** | **str**| The name of the agent the connection profile is deployed on. | 
 **name** | **str**| Name of the Connection Profile | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> SuccessData delete_folder(control_m, folder_name)

delete a folder

Delete a folder

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
api_instance = controlm_client.DeployApi(controlm_client.ApiClient(configuration))
control_m = 'control_m_example' # str | The name of the Control-M in which the folder(s) are deployed. Wildcards can be used.
folder_name = 'folder_name_example' # str | The name of the required folder(s). Wildcards can be used.

try:
    # delete a folder
    api_response = api_instance.delete_folder(control_m, folder_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->delete_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **control_m** | **str**| The name of the Control-M in which the folder(s) are deployed. Wildcards can be used. | 
 **folder_name** | **str**| The name of the required folder(s). Wildcards can be used. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_file**
> list[DeploymentFileResults] deploy_file(definitions_file, deploy_descriptor_file=deploy_descriptor_file)

Deploy definitions file

Deploy the provided definition file (JSON, XML or zip) to Control-M

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
api_instance = controlm_client.DeployApi(controlm_client.ApiClient(configuration))
definitions_file = '/path/to/file.txt' # file | A file that contains definitions to be deployed to the server. Can be either a JSON definition file, an XML definition file, or a zip file that contains multiple JSON or XML definition files.
deploy_descriptor_file = '/path/to/file.txt' # file | Deploy Descriptor JSON file. (optional)

try:
    # Deploy definitions file
    api_response = api_instance.deploy_file(definitions_file, deploy_descriptor_file=deploy_descriptor_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->deploy_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definitions_file** | **file**| A file that contains definitions to be deployed to the server. Can be either a JSON definition file, an XML definition file, or a zip file that contains multiple JSON or XML definition files. | 
 **deploy_descriptor_file** | **file**| Deploy Descriptor JSON file. | [optional] 

### Return type

[**list[DeploymentFileResults]**](DeploymentFileResults.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployed_connection_profiles**
> str get_deployed_connection_profiles(ctm, agent, type)

Get deployed folder

Export currently deployed folders to XML.

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
api_instance = controlm_client.DeployApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The name of the Control-M in which the connection profile is deployed on.
agent = 'agent_example' # str | The name of the agent the connection profile is deployed on.
type = 'type_example' # str | The type of connection profile such as Hadoop, Database, FileTransfer.

try:
    # Get deployed folder
    api_response = api_instance.get_deployed_connection_profiles(ctm, agent, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_deployed_connection_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The name of the Control-M in which the connection profile is deployed on. | 
 **agent** | **str**| The name of the agent the connection profile is deployed on. | 
 **type** | **str**| The type of connection profile such as Hadoop, Database, FileTransfer. | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployed_folders_new**
> str get_deployed_folders_new(format=format, folder=folder, ctm=ctm)

Get deployed jobs that match the search criteria.

Get definition of jobs and folders (in the desired format - JSON or XML) that match the requested search criteria.

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
api_instance = controlm_client.DeployApi(controlm_client.ApiClient(configuration))
format = 'json' # str | Output format (json or xml) (optional) (default to json)
folder = 'folder_example' # str |  (optional)
ctm = 'ctm_example' # str |  (optional)

try:
    # Get deployed jobs that match the search criteria.
    api_response = api_instance.get_deployed_folders_new(format=format, folder=folder, ctm=ctm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_deployed_folders_new: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Output format (json or xml) | [optional] [default to json]
 **folder** | **str**|  | [optional] 
 **ctm** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transform_file**
> str transform_file(definitions_file, deploy_descriptor_file)

Transform a definitions file

Transform the provided definitions file (JSON) according to the provided Deploy Descriptor file (JSON).

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
api_instance = controlm_client.DeployApi(controlm_client.ApiClient(configuration))
definitions_file = '/path/to/file.txt' # file | A file that contains definitions to be deployed to the server. Can be either a JSON definition file, an XML definition file, or a zip file that contains multiple JSON or XML definition files.
deploy_descriptor_file = '/path/to/file.txt' # file | Deploy Descriptor JSON file.

try:
    # Transform a definitions file
    api_response = api_instance.transform_file(definitions_file, deploy_descriptor_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->transform_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definitions_file** | **file**| A file that contains definitions to be deployed to the server. Can be either a JSON definition file, an XML definition file, or a zip file that contains multiple JSON or XML definition files. | 
 **deploy_descriptor_file** | **file**| Deploy Descriptor JSON file. | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

