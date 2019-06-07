# controlm_client.ProvisionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_upgrade_activity**](ProvisionApi.md#cancel_upgrade_activity) | **POST** /provision/upgrade/{upgradeId}/cancel | Cancel upgrade activity
[**delete_upgrade_activity**](ProvisionApi.md#delete_upgrade_activity) | **DELETE** /provision/upgrade/{upgradeId} | Delete upgrade activity status for specific upgrade id.
[**get_all_upgrade_activities_status**](ProvisionApi.md#get_all_upgrade_activities_status) | **GET** /provision/upgrades | Get all upgrade activities status.
[**get_deploy_versions**](ProvisionApi.md#get_deploy_versions) | **GET** /provision/upgrades/versions | Get available versions for upgrade.
[**get_eligible_agents_for_upgrade**](ProvisionApi.md#get_eligible_agents_for_upgrade) | **GET** /provision/upgrades/agents | Get eligible agents for upgrade that match the requested search criteria.
[**get_images**](ProvisionApi.md#get_images) | **GET** /provision/images/{os} | get list of available images for the requested OS
[**get_upgrade_activity_log**](ProvisionApi.md#get_upgrade_activity_log) | **GET** /provision/upgrade/{upgradeId}/output | Returns log of upgrade activity.
[**get_upgrade_activity_status_per_upgrade_id**](ProvisionApi.md#get_upgrade_activity_status_per_upgrade_id) | **GET** /provision/upgrade/{upgradeId} | Get upgrade activity status for specific upgrade id.
[**retry_upgrade_activity**](ProvisionApi.md#retry_upgrade_activity) | **POST** /provision/upgrade/{upgradeId}/retry | Retry upgrade activity
[**transfer_and_install_product**](ProvisionApi.md#transfer_and_install_product) | **POST** /provision/upgrade/install | Transfer and install a product on an agent
[**uninstall_product**](ProvisionApi.md#uninstall_product) | **POST** /provision/upgrade/uninstall | Uninstall a product from an agent


# **cancel_upgrade_activity**
> SuccessData cancel_upgrade_activity(upgrade_id)

Cancel upgrade activity

Cancel upgrade activity

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
api_instance = controlm_client.ProvisionApi(controlm_client.ApiClient(configuration))
upgrade_id = 'upgrade_id_example' # str | Id of upgrade to cancel

try:
    # Cancel upgrade activity
    api_response = api_instance.cancel_upgrade_activity(upgrade_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->cancel_upgrade_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upgrade_id** | **str**| Id of upgrade to cancel | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_upgrade_activity**
> SuccessData delete_upgrade_activity(upgrade_id)

Delete upgrade activity status for specific upgrade id.

Delete upgrade activity status for specific upgrade id.

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
api_instance = controlm_client.ProvisionApi(controlm_client.ApiClient(configuration))
upgrade_id = 'upgrade_id_example' # str | The upgrade id.

try:
    # Delete upgrade activity status for specific upgrade id.
    api_response = api_instance.delete_upgrade_activity(upgrade_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->delete_upgrade_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upgrade_id** | **str**| The upgrade id. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_upgrade_activities_status**
> UpgradeRecordList get_all_upgrade_activities_status(ctm=ctm, agent=agent, from_version=from_version, to_version=to_version, activity=activity, status=status, activity_name=activity_name)

Get all upgrade activities status.

Get all upgrade activities status.

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
api_instance = controlm_client.ProvisionApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M server name (optional)
agent = 'agent_example' # str | The Control-M Agent name (optional)
from_version = 'from_version_example' # str | Current product version (optional)
to_version = 'to_version_example' # str | Upgrade to version (optional)
activity = 'activity_example' # str | Activity type (Install, Uninstall) (optional)
status = 'status_example' # str | Upgrade activity status (Cancel, Running, Completed, TransferCompleted, Failed, Unavailable) (optional)
activity_name = 'activity_name_example' # str | Name of the upgrade activity (optional)

try:
    # Get all upgrade activities status.
    api_response = api_instance.get_all_upgrade_activities_status(ctm=ctm, agent=agent, from_version=from_version, to_version=to_version, activity=activity, status=status, activity_name=activity_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->get_all_upgrade_activities_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M server name | [optional] 
 **agent** | **str**| The Control-M Agent name | [optional] 
 **from_version** | **str**| Current product version | [optional] 
 **to_version** | **str**| Upgrade to version | [optional] 
 **activity** | **str**| Activity type (Install, Uninstall) | [optional] 
 **status** | **str**| Upgrade activity status (Cancel, Running, Completed, TransferCompleted, Failed, Unavailable) | [optional] 
 **activity_name** | **str**| Name of the upgrade activity | [optional] 

### Return type

[**UpgradeRecordList**](UpgradeRecordList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deploy_versions**
> list[UpgradeInfo] get_deploy_versions()

Get available versions for upgrade.

Get available versions for upgrade

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
api_instance = controlm_client.ProvisionApi(controlm_client.ApiClient(configuration))

try:
    # Get available versions for upgrade.
    api_response = api_instance.get_deploy_versions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->get_deploy_versions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UpgradeInfo]**](UpgradeInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_eligible_agents_for_upgrade**
> UpgradeAgentInfoList get_eligible_agents_for_upgrade(type=type, version=version)

Get eligible agents for upgrade that match the requested search criteria.

Get eligible agents for upgrade that match the requested search criteria from Control-M server.

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
api_instance = controlm_client.ProvisionApi(controlm_client.ApiClient(configuration))
type = 'type_example' # str | The type (Agent, MFT, AppPack). (optional)
version = 'version_example' # str | The version. (optional)

try:
    # Get eligible agents for upgrade that match the requested search criteria.
    api_response = api_instance.get_eligible_agents_for_upgrade(type=type, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->get_eligible_agents_for_upgrade: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type (Agent, MFT, AppPack). | [optional] 
 **version** | **str**| The version. | [optional] 

### Return type

[**UpgradeAgentInfoList**](UpgradeAgentInfoList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images**
> StringListResult get_images(os)

get list of available images for the requested OS

Get a list of the images in the system for the requested OS.

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
api_instance = controlm_client.ProvisionApi(controlm_client.ApiClient(configuration))
os = 'os_example' # str | The OS name of the requested images.

try:
    # get list of available images for the requested OS
    api_response = api_instance.get_images(os)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->get_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os** | **str**| The OS name of the requested images. | 

### Return type

[**StringListResult**](StringListResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_activity_log**
> str get_upgrade_activity_log(upgrade_id)

Returns log of upgrade activity.

Returns log of upgrade activity

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
api_instance = controlm_client.ProvisionApi(controlm_client.ApiClient(configuration))
upgrade_id = 'upgrade_id_example' # str | The upgrade id.

try:
    # Returns log of upgrade activity.
    api_response = api_instance.get_upgrade_activity_log(upgrade_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->get_upgrade_activity_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upgrade_id** | **str**| The upgrade id. | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_activity_status_per_upgrade_id**
> UpgradeRecord get_upgrade_activity_status_per_upgrade_id(upgrade_id)

Get upgrade activity status for specific upgrade id.

Get upgrade activity status for specific upgrade id.

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
api_instance = controlm_client.ProvisionApi(controlm_client.ApiClient(configuration))
upgrade_id = 'upgrade_id_example' # str | The upgrade id.

try:
    # Get upgrade activity status for specific upgrade id.
    api_response = api_instance.get_upgrade_activity_status_per_upgrade_id(upgrade_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->get_upgrade_activity_status_per_upgrade_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upgrade_id** | **str**| The upgrade id. | 

### Return type

[**UpgradeRecord**](UpgradeRecord.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_upgrade_activity**
> SuccessData retry_upgrade_activity(upgrade_id)

Retry upgrade activity

Retry upgrade activity

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
api_instance = controlm_client.ProvisionApi(controlm_client.ApiClient(configuration))
upgrade_id = 'upgrade_id_example' # str | Id of upgrade to retry

try:
    # Retry upgrade activity
    api_response = api_instance.retry_upgrade_activity(upgrade_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->retry_upgrade_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upgrade_id** | **str**| Id of upgrade to retry | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_and_install_product**
> UpgradeResponse transfer_and_install_product(upgrade_request)

Transfer and install a product on an agent

Transfer and install a product on an agent

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
api_instance = controlm_client.ProvisionApi(controlm_client.ApiClient(configuration))
upgrade_request = controlm_client.UpgradeRequest() # UpgradeRequest | Upgrade request details

try:
    # Transfer and install a product on an agent
    api_response = api_instance.transfer_and_install_product(upgrade_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->transfer_and_install_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upgrade_request** | [**UpgradeRequest**](UpgradeRequest.md)| Upgrade request details | 

### Return type

[**UpgradeResponse**](UpgradeResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uninstall_product**
> UpgradeResponse uninstall_product(rollback_request)

Uninstall a product from an agent

Uninstall a product from an agent

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
api_instance = controlm_client.ProvisionApi(controlm_client.ApiClient(configuration))
rollback_request = controlm_client.UpgradeRequest() # UpgradeRequest | Rollback request details

try:
    # Uninstall a product from an agent
    api_response = api_instance.uninstall_product(rollback_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->uninstall_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rollback_request** | [**UpgradeRequest**](UpgradeRequest.md)| Rollback request details | 

### Return type

[**UpgradeResponse**](UpgradeResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

