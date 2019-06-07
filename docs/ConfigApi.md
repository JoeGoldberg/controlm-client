# controlm_client.ConfigApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_agent**](ConfigApi.md#add_agent) | **POST** /config/server/{ctm}/agent | add agent to Control-M Server
[**add_host_to_hostgroup**](ConfigApi.md#add_host_to_hostgroup) | **POST** /config/server/{ctm}/hostgroup/{hostgroup}/agent | add agent to hostgroup
[**add_remote_host**](ConfigApi.md#add_remote_host) | **POST** /config/server/{ctm}/remotehost | add remote host to Control-M Server
[**add_role**](ConfigApi.md#add_role) | **POST** /config/authorization/role | Add Authorization Role
[**add_role_to_ldap_group**](ConfigApi.md#add_role_to_ldap_group) | **POST** /config/authorization/ldap/{ldapgroup}/role/{role} | Add a role to LDAP group
[**add_role_to_user**](ConfigApi.md#add_role_to_user) | **POST** /config/authorization/user/{user}/role/{role} | Add a role to user
[**add_secret**](ConfigApi.md#add_secret) | **POST** /config/secret | Add a new secret
[**add_server**](ConfigApi.md#add_server) | **POST** /config/server | add Control-M server to the system
[**add_user**](ConfigApi.md#add_user) | **POST** /config/authorization/user | Add user
[**authorize_ssh_known_remotehost**](ConfigApi.md#authorize_ssh_known_remotehost) | **POST** /config/server/{ctm}/remotehost/{remotehost}/authorize | Authorize
[**change_user_password**](ConfigApi.md#change_user_password) | **POST** /config/user/{user}/password/adminUpdate | Change user password
[**create_run_as_user**](ConfigApi.md#create_run_as_user) | **POST** /config/server/{ctm}/runasuser | Add a new Run-as user
[**delete_agent**](ConfigApi.md#delete_agent) | **DELETE** /config/server/{ctm}/agent/{agent} | delete an agent from Control-M Server
[**delete_authorization_role**](ConfigApi.md#delete_authorization_role) | **DELETE** /config/authorization/role/{role} | Delete Authorization Role
[**delete_host_from_group**](ConfigApi.md#delete_host_from_group) | **DELETE** /config/server/{ctm}/hostgroup/{hostgroup}/agent/{host} | delete an agent from a hostgroup
[**delete_remote_host**](ConfigApi.md#delete_remote_host) | **DELETE** /config/server/{ctm}/remotehost/{remotehost} | delete a remote host from Control-M Server
[**delete_role_from_ldap_group**](ConfigApi.md#delete_role_from_ldap_group) | **DELETE** /config/authorization/ldap/{ldapgroup}/role/{role} | Delete a role from LDAP group
[**delete_run_as_user**](ConfigApi.md#delete_run_as_user) | **DELETE** /config/server/{ctm}/runasuser/{agent}/{user} | delete Run-as user
[**delete_secret**](ConfigApi.md#delete_secret) | **DELETE** /config/secret/{name} | Delete an existing secret
[**delete_user**](ConfigApi.md#delete_user) | **DELETE** /config/authorization/user/{user} | Delete user
[**disable_agent**](ConfigApi.md#disable_agent) | **POST** /config/server/{ctm}/agent/{agent}/disable | disable agent from the Control-M Server
[**enable_agent**](ConfigApi.md#enable_agent) | **POST** /config/server/{ctm}/agent/{agent}/enable | enable agent from the Control-M Server
[**failover**](ConfigApi.md#failover) | **PUT** /config/server/{ctm}/failover | Perform Manual Failover on a specified Control-M Server
[**get_agent_parameters**](ConfigApi.md#get_agent_parameters) | **GET** /config/server/{ctm}/agent/{agent}/params | get agent parameters
[**get_agents**](ConfigApi.md#get_agents) | **GET** /config/server/{ctm}/agents | get Control-M Server agents
[**get_all_authorization_roles**](ConfigApi.md#get_all_authorization_roles) | **GET** /config/authorization/roles | Get Authorization Roles
[**get_all_roles_associated_with_ldap**](ConfigApi.md#get_all_roles_associated_with_ldap) | **GET** /config/authorization/ldap/{ldapgroup}/roles | Get Authorization Roles associated with an LDAP group
[**get_all_users**](ConfigApi.md#get_all_users) | **GET** /config/authorization/users | Get users
[**get_hostgroups**](ConfigApi.md#get_hostgroups) | **GET** /config/server/{ctm}/hostgroups | get Control-M Server hostgroups
[**get_hosts_in_group**](ConfigApi.md#get_hosts_in_group) | **GET** /config/server/{ctm}/hostgroup/{hostgroup}/agents | get hostgroup agents
[**get_remote_host_properties**](ConfigApi.md#get_remote_host_properties) | **GET** /config/server/{ctm}/remotehost/{remotehost} | get a remote host configuration from Control-M Server
[**get_remote_hosts**](ConfigApi.md#get_remote_hosts) | **GET** /config/server/{ctm}/remotehosts | get Control-M Server remote hosts
[**get_role**](ConfigApi.md#get_role) | **GET** /config/authorization/role/{role} | Get Authorization Role
[**get_role_associates**](ConfigApi.md#get_role_associates) | **GET** /config/authorization/role/{role}/associates | Get all authorization entities associated with role
[**get_run_as_user**](ConfigApi.md#get_run_as_user) | **GET** /config/server/{ctm}/runasuser/{agent}/{user} | Get Run-as user
[**get_run_as_users_list**](ConfigApi.md#get_run_as_users_list) | **GET** /config/server/{ctm}/runasusers | Get Run-as user list that match the requested search criteria.
[**get_server_parameters**](ConfigApi.md#get_server_parameters) | **GET** /config/server/{ctm}/params | get Control-M Server parameters
[**get_servers**](ConfigApi.md#get_servers) | **GET** /config/servers | get all the Control-M Servers name and hostname in the system
[**get_user**](ConfigApi.md#get_user) | **GET** /config/authorization/user/{user} | Get user
[**list_secrets**](ConfigApi.md#list_secrets) | **GET** /config/secrets | Get list of secret names
[**ping_agent**](ConfigApi.md#ping_agent) | **POST** /config/server/{ctm}/agent/{agent}/ping | ping to the agent in the Control-M Server
[**remove_controlm_server**](ConfigApi.md#remove_controlm_server) | **DELETE** /config/server/{ctm} | Delete Control-M server
[**remove_role_from_user**](ConfigApi.md#remove_role_from_user) | **DELETE** /config/authorization/user/{user}/role/{role} | Remove a role from a user
[**set_agent_parameter**](ConfigApi.md#set_agent_parameter) | **POST** /config/server/{ctm}/agent/{agent}/param/{name} | set agent parameter
[**set_system_param**](ConfigApi.md#set_system_param) | **POST** /config/em/param/{name} | set value of a an em system parameter
[**setasprimary**](ConfigApi.md#setasprimary) | **PUT** /config/server/{ctm}/setasprimary | Set secondary server as Primary on a specified Control-M Server
[**test_run_as_user**](ConfigApi.md#test_run_as_user) | **POST** /config/server/{ctm}/runasuser/{agent}/{user}/test | Test existed Run-as user
[**update_role**](ConfigApi.md#update_role) | **POST** /config/authorization/role/{role} | Update Authorization Role
[**update_run_as_user**](ConfigApi.md#update_run_as_user) | **POST** /config/server/{ctm}/runasuser/{agent}/{user} | Update Run-as user
[**update_secret**](ConfigApi.md#update_secret) | **POST** /config/secret/{name} | Update an existing secret
[**update_user**](ConfigApi.md#update_user) | **POST** /config/authorization/user/{user} | Update user


# **add_agent**
> SuccessData add_agent(ctm, body)

add agent to Control-M Server

Add an agent to Control-M Server. This command does not install or configure the agent. It only defines the agent in the system.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server the agent is going to be added to.
body = controlm_client.AddAgentParams() # AddAgentParams | 

try:
    # add agent to Control-M Server
    api_response = api_instance.add_agent(ctm, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server the agent is going to be added to. | 
 **body** | [**AddAgentParams**](AddAgentParams.md)|  | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_host_to_hostgroup**
> AgentsInGroupSuccessData add_host_to_hostgroup(ctm, hostgroup, agent)

add agent to hostgroup

Add an agent to hostgroup. Create the the hostgroup if it does not exist.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server the hostgroup belongs to.
hostgroup = 'hostgroup_example' # str | The hostgroup name
agent = controlm_client.AgentInGroupParams() # AgentInGroupParams | The hostname of the new agent

try:
    # add agent to hostgroup
    api_response = api_instance.add_host_to_hostgroup(ctm, hostgroup, agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_host_to_hostgroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server the hostgroup belongs to. | 
 **hostgroup** | **str**| The hostgroup name | 
 **agent** | [**AgentInGroupParams**](AgentInGroupParams.md)| The hostname of the new agent | 

### Return type

[**AgentsInGroupSuccessData**](AgentsInGroupSuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_remote_host**
> SuccessData add_remote_host(ctm, data=data)

add remote host to Control-M Server

Add a remote host to Control-M Server.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server the remote host is going to be added to.
data = controlm_client.AddRemoteHostParams() # AddRemoteHostParams | The non default, advanced configuration data (optional)

try:
    # add remote host to Control-M Server
    api_response = api_instance.add_remote_host(ctm, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_remote_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server the remote host is going to be added to. | 
 **data** | [**AddRemoteHostParams**](AddRemoteHostParams.md)| The non default, advanced configuration data | [optional] 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_role**
> SuccessData add_role(role_file)

Add Authorization Role

Add Authorization Role

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
role_file = '/path/to/file.txt' # file | File with contenet of Role Data.

try:
    # Add Authorization Role
    api_response = api_instance.add_role(role_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_file** | **file**| File with contenet of Role Data. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_role_to_ldap_group**
> SuccessData add_role_to_ldap_group(ldapgroup, role)

Add a role to LDAP group

Add a role to LDAP group so any user belong to the LDAP group will get all permissions defined in the role

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ldapgroup = 'ldapgroup_example' # str | Name of LDAP group
role = 'role_example' # str | Name of role

try:
    # Add a role to LDAP group
    api_response = api_instance.add_role_to_ldap_group(ldapgroup, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_role_to_ldap_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapgroup** | **str**| Name of LDAP group | 
 **role** | **str**| Name of role | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_role_to_user**
> SuccessData add_role_to_user(user, role)

Add a role to user

Add a role to user so that user will inherit role authorization

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
user = 'user_example' # str | Name of user
role = 'role_example' # str | Name of role

try:
    # Add a role to user
    api_response = api_instance.add_role_to_user(user, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_role_to_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Name of user | 
 **role** | **str**| Name of role | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_secret**
> SuccessData add_secret(name_value)

Add a new secret

Add a new secret to the secrets vault.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
name_value = controlm_client.SecretKeyValue() # SecretKeyValue | The new secret value

try:
    # Add a new secret
    api_response = api_instance.add_secret(name_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_value** | [**SecretKeyValue**](SecretKeyValue.md)| The new secret value | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_server**
> SuccessData add_server(body)

add Control-M server to the system

Add a Control-M Server. This command setting up new Control-M server in the system

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
body = controlm_client.AddServerParams() # AddServerParams | 

try:
    # add Control-M server to the system
    api_response = api_instance.add_server(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddServerParams**](AddServerParams.md)|  | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user**
> SuccessData add_user(user_file)

Add user

Add user

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
user_file = '/path/to/file.txt' # file | File with contenet of user data.

try:
    # Add user
    api_response = api_instance.add_user(user_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_file** | **file**| File with contenet of user data. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorize_ssh_known_remotehost**
> SuccessData authorize_ssh_known_remotehost(ctm, remotehost)

Authorize

Authorized known ssh remote host.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server the remote host is connected to.
remotehost = 'remotehost_example' # str | The name of the remote host.

try:
    # Authorize
    api_response = api_instance.authorize_ssh_known_remotehost(ctm, remotehost)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->authorize_ssh_known_remotehost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server the remote host is connected to. | 
 **remotehost** | **str**| The name of the remote host. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_password**
> SuccessData change_user_password(user, password=password)

Change user password

Change user password

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
user = 'user_example' # str | user name
password = controlm_client.UserPassword() # UserPassword | The new password. (optional)

try:
    # Change user password
    api_response = api_instance.change_user_password(user, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->change_user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| user name | 
 **password** | [**UserPassword**](UserPassword.md)| The new password. | [optional] 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_run_as_user**
> SuccessData create_run_as_user(ctm, run_as_user_data)

Add a new Run-as user

Add a new Run-as user to Control-M server.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server.
run_as_user_data = controlm_client.RunAsUserData() # RunAsUserData | Run as user data

try:
    # Add a new Run-as user
    api_response = api_instance.create_run_as_user(ctm, run_as_user_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->create_run_as_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server. | 
 **run_as_user_data** | [**RunAsUserData**](RunAsUserData.md)| Run as user data | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent**
> SuccessData delete_agent(ctm, agent)

delete an agent from Control-M Server

Delete an agent from a Control-M Server. This will not shut the agent down. It only disconnects and removes it from the list.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server the agent is connected to.
agent = 'agent_example' # str | The name of the agent to delete.

try:
    # delete an agent from Control-M Server
    api_response = api_instance.delete_agent(ctm, agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server the agent is connected to. | 
 **agent** | **str**| The name of the agent to delete. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_authorization_role**
> SuccessData delete_authorization_role(role)

Delete Authorization Role

Delete Authorization Role

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
role = 'role_example' # str | The Role name.

try:
    # Delete Authorization Role
    api_response = api_instance.delete_authorization_role(role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_authorization_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The Role name. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_host_from_group**
> AgentsInGroupSuccessData delete_host_from_group(ctm, hostgroup, host)

delete an agent from a hostgroup

Delete an agent from the specified hostgroup. If the group is empty it will also be deleted.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server the hostgroup belongs to.
hostgroup = 'hostgroup_example' # str | The hostgroup name
host = 'host_example' # str | The agent to be deleted

try:
    # delete an agent from a hostgroup
    api_response = api_instance.delete_host_from_group(ctm, hostgroup, host)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_host_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server the hostgroup belongs to. | 
 **hostgroup** | **str**| The hostgroup name | 
 **host** | **str**| The agent to be deleted | 

### Return type

[**AgentsInGroupSuccessData**](AgentsInGroupSuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_remote_host**
> SuccessData delete_remote_host(ctm, remotehost)

delete a remote host from Control-M Server

Delete a remote host from a Control-M Server.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server the remote host is connected to.
remotehost = 'remotehost_example' # str | The name of the remote host to delete.

try:
    # delete a remote host from Control-M Server
    api_response = api_instance.delete_remote_host(ctm, remotehost)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_remote_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server the remote host is connected to. | 
 **remotehost** | **str**| The name of the remote host to delete. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_from_ldap_group**
> SuccessData delete_role_from_ldap_group(ldapgroup, role)

Delete a role from LDAP group

Delete a role from LDAP group

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ldapgroup = 'ldapgroup_example' # str | Name of LDAP group
role = 'role_example' # str | Name of role

try:
    # Delete a role from LDAP group
    api_response = api_instance.delete_role_from_ldap_group(ldapgroup, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_role_from_ldap_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapgroup** | **str**| Name of LDAP group | 
 **role** | **str**| Name of role | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_run_as_user**
> SuccessData delete_run_as_user(ctm, agent, user)

delete Run-as user

Delete Run-as user from Control-M server

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server.
agent = 'agent_example' # str | The Control-M Agent
user = 'user_example' # str | The user name

try:
    # delete Run-as user
    api_response = api_instance.delete_run_as_user(ctm, agent, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_run_as_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server. | 
 **agent** | **str**| The Control-M Agent | 
 **user** | **str**| The user name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_secret**
> SuccessData delete_secret(name)

Delete an existing secret

Delete an existing secret from the secrets vault.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
name = 'name_example' # str | The name of the secret to update

try:
    # Delete an existing secret
    api_response = api_instance.delete_secret(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the secret to update | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> SuccessData delete_user(user)

Delete user

Delete user

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
user = 'user_example' # str | The user name.

try:
    # Delete user
    api_response = api_instance.delete_user(user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The user name. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_agent**
> SuccessData disable_agent(ctm, agent)

disable agent from the Control-M Server

Disable a Control-M agent.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server the agent is connected too.
agent = 'agent_example' # str | The Control-M agent to be disabled.

try:
    # disable agent from the Control-M Server
    api_response = api_instance.disable_agent(ctm, agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->disable_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server the agent is connected too. | 
 **agent** | **str**| The Control-M agent to be disabled. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_agent**
> SuccessData enable_agent(ctm, agent)

enable agent from the Control-M Server

Enable a Control-M agent. This command does not install or configure the agent. It only enable existing agent in the system.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server the agent is connected too.
agent = 'agent_example' # str | The Control-M agent to be enabled.

try:
    # enable agent from the Control-M Server
    api_response = api_instance.enable_agent(ctm, agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->enable_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server the agent is connected too. | 
 **agent** | **str**| The Control-M agent to be enabled. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **failover**
> SuccessData failover(ctm)

Perform Manual Failover on a specified Control-M Server

Perform Manual Failover on a specified Control-M Server

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | 

try:
    # Perform Manual Failover on a specified Control-M Server
    api_response = api_instance.failover(ctm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->failover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**|  | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_parameters**
> KeyValueListResult get_agent_parameters(ctm, agent)

get agent parameters

Get all the parameters of the specified Control-M Agent.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server the agent is connected to.
agent = 'agent_example' # str | The name of the agent to query.

try:
    # get agent parameters
    api_response = api_instance.get_agent_parameters(ctm, agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_agent_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server the agent is connected to. | 
 **agent** | **str**| The name of the agent to query. | 

### Return type

[**KeyValueListResult**](KeyValueListResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agents**
> AgentDetailsList get_agents(ctm, agent=agent)

get Control-M Server agents

Get all the agents of the specified Control-M Server.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server to query. Optionally you can filter agent name of host or alias of the Control-M Agent
agent = 'agent_example' # str | Optionally case insensitive agent name filter of host or alias of the Control-M Agent. `ctm server:agents::get ControlM AgentName` returns all agents which names start with `agentname` (optional)

try:
    # get Control-M Server agents
    api_response = api_instance.get_agents(ctm, agent=agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_agents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server to query. Optionally you can filter agent name of host or alias of the Control-M Agent | 
 **agent** | **str**| Optionally case insensitive agent name filter of host or alias of the Control-M Agent. &#x60;ctm server:agents::get ControlM AgentName&#x60; returns all agents which names start with &#x60;agentname&#x60; | [optional] 

### Return type

[**AgentDetailsList**](AgentDetailsList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_authorization_roles**
> RoleHeaderList get_all_authorization_roles(role=role, description=description)

Get Authorization Roles

Get Authorization Roles

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
role = 'role_example' # str | The Role name. (optional)
description = 'description_example' # str | The Role description. (optional)

try:
    # Get Authorization Roles
    api_response = api_instance.get_all_authorization_roles(role=role, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_all_authorization_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The Role name. | [optional] 
 **description** | **str**| The Role description. | [optional] 

### Return type

[**RoleHeaderList**](RoleHeaderList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_roles_associated_with_ldap**
> list[str] get_all_roles_associated_with_ldap(ldapgroup, role=role)

Get Authorization Roles associated with an LDAP group

Get Authorization Roles associated with an LDAP group

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ldapgroup = 'ldapgroup_example' # str | Name of Ldap group
role = 'role_example' # str | The Role name. (optional)

try:
    # Get Authorization Roles associated with an LDAP group
    api_response = api_instance.get_all_roles_associated_with_ldap(ldapgroup, role=role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_all_roles_associated_with_ldap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapgroup** | **str**| Name of Ldap group | 
 **role** | **str**| The Role name. | [optional] 

### Return type

**list[str]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_users**
> list[UserHeader] get_all_users(name=name, full_name=full_name, description=description)

Get users

Get users

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
name = 'name_example' # str | The user name. (optional)
full_name = 'full_name_example' # str | The user full name. (optional)
description = 'description_example' # str | The user description. (optional)

try:
    # Get users
    api_response = api_instance.get_all_users(name=name, full_name=full_name, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_all_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The user name. | [optional] 
 **full_name** | **str**| The user full name. | [optional] 
 **description** | **str**| The user description. | [optional] 

### Return type

[**list[UserHeader]**](UserHeader.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hostgroups**
> StringListResult get_hostgroups(ctm)

get Control-M Server hostgroups

Get all the hostgroups of the specified Control-M Server.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server the hostgroups belong to.

try:
    # get Control-M Server hostgroups
    api_response = api_instance.get_hostgroups(ctm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_hostgroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server the hostgroups belong to. | 

### Return type

[**StringListResult**](StringListResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hosts_in_group**
> AgentsInGroupListResult get_hosts_in_group(ctm, hostgroup)

get hostgroup agents

Get the agents that compose the specified hostgroup

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server the hostgroup belongs to.
hostgroup = 'hostgroup_example' # str | The hostgroup name

try:
    # get hostgroup agents
    api_response = api_instance.get_hosts_in_group(ctm, hostgroup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_hosts_in_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server the hostgroup belongs to. | 
 **hostgroup** | **str**| The hostgroup name | 

### Return type

[**AgentsInGroupListResult**](AgentsInGroupListResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remote_host_properties**
> AddRemoteHostParams get_remote_host_properties(ctm, remotehost)

get a remote host configuration from Control-M Server

Get the remote host configuration properties from the Control-M Server

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server the remote host  is connected to.
remotehost = 'remotehost_example' # str | The name of the remote host.

try:
    # get a remote host configuration from Control-M Server
    api_response = api_instance.get_remote_host_properties(ctm, remotehost)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_remote_host_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server the remote host  is connected to. | 
 **remotehost** | **str**| The name of the remote host. | 

### Return type

[**AddRemoteHostParams**](AddRemoteHostParams.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remote_hosts**
> StringListResult get_remote_hosts(ctm)

get Control-M Server remote hosts

Get all the remote hosts of the specified Control-M Server.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server to query.

try:
    # get Control-M Server remote hosts
    api_response = api_instance.get_remote_hosts(ctm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_remote_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server to query. | 

### Return type

[**StringListResult**](StringListResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> RoleData get_role(role)

Get Authorization Role

Get Authorization Role

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
role = 'role_example' # str | The Role name.

try:
    # Get Authorization Role
    api_response = api_instance.get_role(role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The Role name. | 

### Return type

[**RoleData**](RoleData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_associates**
> list[AssociateData] get_role_associates(role)

Get all authorization entities associated with role

Get all authorization entities associated with role

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
role = 'role_example' # str | role name.

try:
    # Get all authorization entities associated with role
    api_response = api_instance.get_role_associates(role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_role_associates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| role name. | 

### Return type

[**list[AssociateData]**](AssociateData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_as_user**
> RunAsUserData get_run_as_user(ctm, agent, user)

Get Run-as user

Get Run-as user details from Control-M server.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server.
agent = 'agent_example' # str | The Control-M Agent
user = 'user_example' # str | The user name

try:
    # Get Run-as user
    api_response = api_instance.get_run_as_user(ctm, agent, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_run_as_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server. | 
 **agent** | **str**| The Control-M Agent | 
 **user** | **str**| The user name | 

### Return type

[**RunAsUserData**](RunAsUserData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_as_users_list**
> RunAsUsersList get_run_as_users_list(ctm, user=user, agent=agent)

Get Run-as user list that match the requested search criteria.

Get Run-as user list that match the requested search criteria from Control-M server.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server.
user = 'user_example' # str | The Run-as user. (optional)
agent = 'agent_example' # str | The agent. (optional)

try:
    # Get Run-as user list that match the requested search criteria.
    api_response = api_instance.get_run_as_users_list(ctm, user=user, agent=agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_run_as_users_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server. | 
 **user** | **str**| The Run-as user. | [optional] 
 **agent** | **str**| The agent. | [optional] 

### Return type

[**RunAsUsersList**](RunAsUsersList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_parameters**
> KeyValueListResult get_server_parameters(ctm)

get Control-M Server parameters

Get all the parameters of the specified Control-M Server.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server to query.

try:
    # get Control-M Server parameters
    api_response = api_instance.get_server_parameters(ctm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_server_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server to query. | 

### Return type

[**KeyValueListResult**](KeyValueListResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_servers**
> CtmDetailsList get_servers()

get all the Control-M Servers name and hostname in the system

Get the names and hostnames of all Control-M Servers in the system.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))

try:
    # get all the Control-M Servers name and hostname in the system
    api_response = api_instance.get_servers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_servers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CtmDetailsList**](CtmDetailsList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserData get_user(user)

Get user

Get user

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
user = 'user_example' # str | The user name.

try:
    # Get user
    api_response = api_instance.get_user(user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The user name. | 

### Return type

[**UserData**](UserData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_secrets**
> StringListResult list_secrets()

Get list of secret names

Get the list of names of all the secrets in the vault

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))

try:
    # Get list of secret names
    api_response = api_instance.list_secrets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->list_secrets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StringListResult**](StringListResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_agent**
> SuccessData ping_agent(ctm, agent, body=body)

ping to the agent in the Control-M Server

Ping a Control-M agent.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server.
agent = 'agent_example' # str | The Control-M agent.
body = controlm_client.PingAgentParams() # PingAgentParams |  (optional)

try:
    # ping to the agent in the Control-M Server
    api_response = api_instance.ping_agent(ctm, agent, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->ping_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server. | 
 **agent** | **str**| The Control-M agent. | 
 **body** | [**PingAgentParams**](PingAgentParams.md)|  | [optional] 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_controlm_server**
> SuccessData remove_controlm_server(ctm)

Delete Control-M server

Delete Control-M server

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | Control-M Server host name.

try:
    # Delete Control-M server
    api_response = api_instance.remove_controlm_server(ctm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->remove_controlm_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| Control-M Server host name. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_role_from_user**
> SuccessData remove_role_from_user(user, role)

Remove a role from a user

Remove a role from a user

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
user = 'user_example' # str | Name of user
role = 'role_example' # str | Name of role

try:
    # Remove a role from a user
    api_response = api_instance.remove_role_from_user(user, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->remove_role_from_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Name of user | 
 **role** | **str**| Name of role | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_agent_parameter**
> KeyValue set_agent_parameter(ctm, agent, name, body)

set agent parameter

Set the value of the specified parameter in the specified agent.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server the agent is connected to.
agent = 'agent_example' # str | The name of the agent to update.
name = 'name_example' # str | The parameter name.
body = controlm_client.Value() # Value | The new parameter value.

try:
    # set agent parameter
    api_response = api_instance.set_agent_parameter(ctm, agent, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->set_agent_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server the agent is connected to. | 
 **agent** | **str**| The name of the agent to update. | 
 **name** | **str**| The parameter name. | 
 **body** | [**Value**](Value.md)| The new parameter value. | 

### Return type

[**KeyValue**](KeyValue.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_system_param**
> SuccessData set_system_param(name, new_value)

set value of a an em system parameter

Set value of an enterprise management system parameter

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
name = 'name_example' # str | Parameter name
new_value = controlm_client.Value() # Value | Param new value

try:
    # set value of a an em system parameter
    api_response = api_instance.set_system_param(name, new_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->set_system_param: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Parameter name | 
 **new_value** | [**Value**](Value.md)| Param new value | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setasprimary**
> SuccessData setasprimary(ctm)

Set secondary server as Primary on a specified Control-M Server

Set secondary server as Primary on a specified Control-M Server

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | 

try:
    # Set secondary server as Primary on a specified Control-M Server
    api_response = api_instance.setasprimary(ctm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->setasprimary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**|  | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_run_as_user**
> SuccessData test_run_as_user(ctm, agent, user, run_as_user_details_data=run_as_user_details_data)

Test existed Run-as user

Test existing Run-as user in Control-M server.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server.
agent = 'agent_example' # str | The Control-M Agent
user = 'user_example' # str | The user name
run_as_user_details_data = controlm_client.RunAsUserDetailsData() # RunAsUserDetailsData | Run as user details data (optional)

try:
    # Test existed Run-as user
    api_response = api_instance.test_run_as_user(ctm, agent, user, run_as_user_details_data=run_as_user_details_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->test_run_as_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server. | 
 **agent** | **str**| The Control-M Agent | 
 **user** | **str**| The user name | 
 **run_as_user_details_data** | [**RunAsUserDetailsData**](RunAsUserDetailsData.md)| Run as user details data | [optional] 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> SuccessData update_role(role, role_file)

Update Authorization Role

Update Authorization Role

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
role = 'role_example' # str | The Role name.
role_file = '/path/to/file.txt' # file | File with contenet of Role Data.

try:
    # Update Authorization Role
    api_response = api_instance.update_role(role, role_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The Role name. | 
 **role_file** | **file**| File with contenet of Role Data. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_run_as_user**
> SuccessData update_run_as_user(ctm, agent, user, run_as_user_details_data)

Update Run-as user

Update Run-as user details in Control-M server.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M Server.
agent = 'agent_example' # str | The Control-M Agent
user = 'user_example' # str | The user name
run_as_user_details_data = controlm_client.RunAsUserDetailsData() # RunAsUserDetailsData | Run as user details data

try:
    # Update Run-as user
    api_response = api_instance.update_run_as_user(ctm, agent, user, run_as_user_details_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->update_run_as_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M Server. | 
 **agent** | **str**| The Control-M Agent | 
 **user** | **str**| The user name | 
 **run_as_user_details_data** | [**RunAsUserDetailsData**](RunAsUserDetailsData.md)| Run as user details data | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_secret**
> SuccessData update_secret(name, value=value)

Update an existing secret

Update an existing secret in the secrets vault.

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
name = 'name_example' # str | The name of the secret to update
value = controlm_client.SecretValue() # SecretValue | The new value for the secret (optional)

try:
    # Update an existing secret
    api_response = api_instance.update_secret(name, value=value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->update_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the secret to update | 
 **value** | [**SecretValue**](SecretValue.md)| The new value for the secret | [optional] 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> SuccessData update_user(user, user_file)

Update user

Update user

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
api_instance = controlm_client.ConfigApi(controlm_client.ApiClient(configuration))
user = 'user_example' # str | The user name.
user_file = '/path/to/file.txt' # file | File with contenet of user data.

try:
    # Update user
    api_response = api_instance.update_user(user, user_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The user name. | 
 **user_file** | **file**| File with contenet of user data. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

