# coding: utf-8

"""
    TeamCity REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import dohq_teamcity
from dohq_teamcity.api.group_api import GroupApi  # noqa: E501
from dohq_teamcity.rest import ApiException


class TestGroupApi(unittest.TestCase):
    """GroupApi unit test stubs"""

    def setUp(self):
        self.api = dohq_teamcity.api.group_api.GroupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_group(self):
        """Test case for add_group

        """
        pass

    def test_add_role(self):
        """Test case for add_role

        """
        pass

    def test_add_role_put(self):
        """Test case for add_role_put

        """
        pass

    def test_add_role_simple(self):
        """Test case for add_role_simple

        """
        pass

    def test_delete_group(self):
        """Test case for delete_group

        """
        pass

    def test_delete_role(self):
        """Test case for delete_role

        """
        pass

    def test_get_permissions(self):
        """Test case for get_permissions

        """
        pass

    def test_get_properties(self):
        """Test case for get_properties

        """
        pass

    def test_list_role(self):
        """Test case for list_role

        """
        pass

    def test_list_roles(self):
        """Test case for list_roles

        """
        pass

    def test_put_user_property(self):
        """Test case for put_user_property

        """
        pass

    def test_remove_user_property(self):
        """Test case for remove_user_property

        """
        pass

    def test_serve_group(self):
        """Test case for serve_group

        """
        pass

    def test_serve_groups(self):
        """Test case for serve_groups

        """
        pass

    def test_serve_user_properties(self):
        """Test case for serve_user_properties

        """
        pass


if __name__ == '__main__':
    unittest.main()
