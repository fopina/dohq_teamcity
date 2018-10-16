# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.vcs_root_instance import VcsRootInstance  # noqa: F401,E501


class VcsRootInstances(TeamCityObject):
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
        'href': 'str',
        'next_href': 'str',
        'prev_href': 'str',
        'vcs_root_instance': 'list[VcsRootInstance]'
    }

    attribute_map = {
        'count': 'count',
        'href': 'href',
        'next_href': 'nextHref',
        'prev_href': 'prevHref',
        'vcs_root_instance': 'vcs-root-instance'
    }

    def __init__(self, count=None, href=None, next_href=None, prev_href=None, vcs_root_instance=None, teamcity=None):  # noqa: E501
        """VcsRootInstances - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._href = None
        self._next_href = None
        self._prev_href = None
        self._vcs_root_instance = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if href is not None:
            self.href = href
        if next_href is not None:
            self.next_href = next_href
        if prev_href is not None:
            self.prev_href = prev_href
        if vcs_root_instance is not None:
            self.vcs_root_instance = vcs_root_instance
        super(VcsRootInstances, self).__init__(teamcity=teamcity)

    @property
    def count(self):
        """Gets the count of this VcsRootInstances.  # noqa: E501


        :return: The count of this VcsRootInstances.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this VcsRootInstances.


        :param count: The count of this VcsRootInstances.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def href(self):
        """Gets the href of this VcsRootInstances.  # noqa: E501


        :return: The href of this VcsRootInstances.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this VcsRootInstances.


        :param href: The href of this VcsRootInstances.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def next_href(self):
        """Gets the next_href of this VcsRootInstances.  # noqa: E501


        :return: The next_href of this VcsRootInstances.  # noqa: E501
        :rtype: str
        """
        return self._next_href

    @next_href.setter
    def next_href(self, next_href):
        """Sets the next_href of this VcsRootInstances.


        :param next_href: The next_href of this VcsRootInstances.  # noqa: E501
        :type: str
        """

        self._next_href = next_href

    @property
    def prev_href(self):
        """Gets the prev_href of this VcsRootInstances.  # noqa: E501


        :return: The prev_href of this VcsRootInstances.  # noqa: E501
        :rtype: str
        """
        return self._prev_href

    @prev_href.setter
    def prev_href(self, prev_href):
        """Sets the prev_href of this VcsRootInstances.


        :param prev_href: The prev_href of this VcsRootInstances.  # noqa: E501
        :type: str
        """

        self._prev_href = prev_href

    @property
    def vcs_root_instance(self):
        """Gets the vcs_root_instance of this VcsRootInstances.  # noqa: E501


        :return: The vcs_root_instance of this VcsRootInstances.  # noqa: E501
        :rtype: list[VcsRootInstance]
        """
        return self._vcs_root_instance

    @vcs_root_instance.setter
    def vcs_root_instance(self, vcs_root_instance):
        """Sets the vcs_root_instance of this VcsRootInstances.


        :param vcs_root_instance: The vcs_root_instance of this VcsRootInstances.  # noqa: E501
        :type: list[VcsRootInstance]
        """

        self._vcs_root_instance = vcs_root_instance

