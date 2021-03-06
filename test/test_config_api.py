# coding: utf-8

"""
    Control-M Services

    Provides access to BMC Control-M Services  # noqa: E501

    OpenAPI spec version: 9.18.3
    Contact: support@bmc.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import controlm_client
from controlm_client.api.config_api import ConfigApi  # noqa: E501
from controlm_client.rest import ApiException


class TestConfigApi(unittest.TestCase):
    """ConfigApi unit test stubs"""

    def setUp(self):
        self.api = controlm_client.api.config_api.ConfigApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_agent(self):
        """Test case for add_agent

        add agent to Control-M Server  # noqa: E501
        """
        pass

    def test_add_host_to_hostgroup(self):
        """Test case for add_host_to_hostgroup

        add agent to hostgroup  # noqa: E501
        """
        pass

    def test_add_remote_host(self):
        """Test case for add_remote_host

        add remote host to Control-M Server  # noqa: E501
        """
        pass

    def test_add_role(self):
        """Test case for add_role

        Add Authorization Role  # noqa: E501
        """
        pass

    def test_add_role_to_ldap_group(self):
        """Test case for add_role_to_ldap_group

        Add a role to LDAP group  # noqa: E501
        """
        pass

    def test_add_role_to_user(self):
        """Test case for add_role_to_user

        Add a role to user  # noqa: E501
        """
        pass

    def test_add_secret(self):
        """Test case for add_secret

        Add a new secret  # noqa: E501
        """
        pass

    def test_add_server(self):
        """Test case for add_server

        add Control-M server to the system  # noqa: E501
        """
        pass

    def test_add_user(self):
        """Test case for add_user

        Add user  # noqa: E501
        """
        pass

    def test_authorize_ssh_known_remotehost(self):
        """Test case for authorize_ssh_known_remotehost

        Authorize  # noqa: E501
        """
        pass

    def test_change_user_password(self):
        """Test case for change_user_password

        Change user password  # noqa: E501
        """
        pass

    def test_create_run_as_user(self):
        """Test case for create_run_as_user

        Add a new Run-as user  # noqa: E501
        """
        pass

    def test_delete_agent(self):
        """Test case for delete_agent

        delete an agent from Control-M Server  # noqa: E501
        """
        pass

    def test_delete_authorization_role(self):
        """Test case for delete_authorization_role

        Delete Authorization Role  # noqa: E501
        """
        pass

    def test_delete_host_from_group(self):
        """Test case for delete_host_from_group

        delete an agent from a hostgroup  # noqa: E501
        """
        pass

    def test_delete_remote_host(self):
        """Test case for delete_remote_host

        delete a remote host from Control-M Server  # noqa: E501
        """
        pass

    def test_delete_role_from_ldap_group(self):
        """Test case for delete_role_from_ldap_group

        Delete a role from LDAP group  # noqa: E501
        """
        pass

    def test_delete_run_as_user(self):
        """Test case for delete_run_as_user

        delete Run-as user  # noqa: E501
        """
        pass

    def test_delete_secret(self):
        """Test case for delete_secret

        Delete an existing secret  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Delete user  # noqa: E501
        """
        pass

    def test_disable_agent(self):
        """Test case for disable_agent

        disable agent from the Control-M Server  # noqa: E501
        """
        pass

    def test_enable_agent(self):
        """Test case for enable_agent

        enable agent from the Control-M Server  # noqa: E501
        """
        pass

    def test_failover(self):
        """Test case for failover

        Perform Manual Failover on a specified Control-M Server  # noqa: E501
        """
        pass

    def test_get_agent_parameters(self):
        """Test case for get_agent_parameters

        get agent parameters  # noqa: E501
        """
        pass

    def test_get_agents(self):
        """Test case for get_agents

        get Control-M Server agents  # noqa: E501
        """
        pass

    def test_get_all_authorization_roles(self):
        """Test case for get_all_authorization_roles

        Get Authorization Roles  # noqa: E501
        """
        pass

    def test_get_all_roles_associated_with_ldap(self):
        """Test case for get_all_roles_associated_with_ldap

        Get Authorization Roles associated with an LDAP group  # noqa: E501
        """
        pass

    def test_get_all_users(self):
        """Test case for get_all_users

        Get users  # noqa: E501
        """
        pass

    def test_get_hostgroups(self):
        """Test case for get_hostgroups

        get Control-M Server hostgroups  # noqa: E501
        """
        pass

    def test_get_hosts_in_group(self):
        """Test case for get_hosts_in_group

        get hostgroup agents  # noqa: E501
        """
        pass

    def test_get_remote_host_properties(self):
        """Test case for get_remote_host_properties

        get a remote host configuration from Control-M Server  # noqa: E501
        """
        pass

    def test_get_remote_hosts(self):
        """Test case for get_remote_hosts

        get Control-M Server remote hosts  # noqa: E501
        """
        pass

    def test_get_role(self):
        """Test case for get_role

        Get Authorization Role  # noqa: E501
        """
        pass

    def test_get_role_associates(self):
        """Test case for get_role_associates

        Get all authorization entities associated with role  # noqa: E501
        """
        pass

    def test_get_run_as_user(self):
        """Test case for get_run_as_user

        Get Run-as user  # noqa: E501
        """
        pass

    def test_get_run_as_users_list(self):
        """Test case for get_run_as_users_list

        Get Run-as user list that match the requested search criteria.  # noqa: E501
        """
        pass

    def test_get_server_parameters(self):
        """Test case for get_server_parameters

        get Control-M Server parameters  # noqa: E501
        """
        pass

    def test_get_servers(self):
        """Test case for get_servers

        get all the Control-M Servers name and hostname in the system  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Get user  # noqa: E501
        """
        pass

    def test_list_secrets(self):
        """Test case for list_secrets

        Get list of secret names  # noqa: E501
        """
        pass

    def test_ping_agent(self):
        """Test case for ping_agent

        ping to the agent in the Control-M Server  # noqa: E501
        """
        pass

    def test_remove_controlm_server(self):
        """Test case for remove_controlm_server

        Delete Control-M server  # noqa: E501
        """
        pass

    def test_remove_role_from_user(self):
        """Test case for remove_role_from_user

        Remove a role from a user  # noqa: E501
        """
        pass

    def test_set_agent_parameter(self):
        """Test case for set_agent_parameter

        set agent parameter  # noqa: E501
        """
        pass

    def test_set_system_param(self):
        """Test case for set_system_param

        set value of a an em system parameter  # noqa: E501
        """
        pass

    def test_setasprimary(self):
        """Test case for setasprimary

        Set secondary server as Primary on a specified Control-M Server  # noqa: E501
        """
        pass

    def test_test_run_as_user(self):
        """Test case for test_run_as_user

        Test existed Run-as user  # noqa: E501
        """
        pass

    def test_update_role(self):
        """Test case for update_role

        Update Authorization Role  # noqa: E501
        """
        pass

    def test_update_run_as_user(self):
        """Test case for update_run_as_user

        Update Run-as user  # noqa: E501
        """
        pass

    def test_update_secret(self):
        """Test case for update_secret

        Update an existing secret  # noqa: E501
        """
        pass

    def test_update_user(self):
        """Test case for update_user

        Update user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
