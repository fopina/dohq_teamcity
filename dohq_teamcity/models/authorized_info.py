# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.comment import Comment  # noqa: F401,E501


class AuthorizedInfo(TeamCityObject):
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
        'comment': 'Comment',
        'status': 'bool'
    }

    attribute_map = {
        'comment': 'comment',
        'status': 'status'
    }

    def __init__(self, comment=None, status=False, teamcity=None):  # noqa: E501
        """AuthorizedInfo - a model defined in Swagger"""  # noqa: E501

        self._comment = None
        self._status = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if status is not None:
            self.status = status
        super(AuthorizedInfo, self).__init__(teamcity=teamcity)

    @property
    def comment(self):
        """Gets the comment of this AuthorizedInfo.  # noqa: E501


        :return: The comment of this AuthorizedInfo.  # noqa: E501
        :rtype: Comment
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AuthorizedInfo.


        :param comment: The comment of this AuthorizedInfo.  # noqa: E501
        :type: Comment
        """

        self._comment = comment

    @property
    def status(self):
        """Gets the status of this AuthorizedInfo.  # noqa: E501


        :return: The status of this AuthorizedInfo.  # noqa: E501
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AuthorizedInfo.


        :param status: The status of this AuthorizedInfo.  # noqa: E501
        :type: bool
        """

        self._status = status

