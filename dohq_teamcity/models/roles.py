# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.role import Role  # noqa: F401,E501


class Roles(TeamCityObject):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'role': 'list[Role]'
    }

    attribute_map = {
        'role': 'role'
    }

    def __init__(self, role=None, teamcity=None):  # noqa: E501
        """Roles - a model defined in Swagger"""  # noqa: E501

        self._role = None
        self.discriminator = None

        if role is not None:
            self.role = role
        super(Roles, self).__init__(teamcity=teamcity)

    @property
    def role(self):
        """Gets the role of this Roles.  # noqa: E501


        :return: The role of this Roles.  # noqa: E501
        :rtype: list[Role]
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Roles.


        :param role: The role of this Roles.  # noqa: E501
        :type: list[Role]
        """

        self._role = role

