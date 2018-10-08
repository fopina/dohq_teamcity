# coding: utf-8

from teamcity.base_model import TeamcityObject


# from teamcity.models.user import User  # noqa: F401,E501


class Users(TeamcityObject):
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
        'count': 'int',
        'user': 'list[User]'
    }

    attribute_map = {
        'count': 'count',
        'user': 'user'
    }

    def __init__(self, count=None, user=None):  # noqa: E501
        """Users - a model defined in Swagger"""  # noqa: E501
        super(Users, self).__init__()

        self._count = None
        self._user = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if user is not None:
            self.user = user

    @property
    def count(self):
        """Gets the count of this Users.  # noqa: E501


        :return: The count of this Users.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Users.


        :param count: The count of this Users.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def user(self):
        """Gets the user of this Users.  # noqa: E501


        :return: The user of this Users.  # noqa: E501
        :rtype: list[User]
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Users.


        :param user: The user of this Users.  # noqa: E501
        :type: list[User]
        """

        self._user = user

