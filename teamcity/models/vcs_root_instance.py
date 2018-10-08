# coding: utf-8

from teamcity.base_model import TeamcityObject


# from teamcity.models.items import Items  # noqa: F401,E501
# from teamcity.models.properties import Properties  # noqa: F401,E501
# from teamcity.models.repository_state import RepositoryState  # noqa: F401,E501
# from teamcity.models.vcs_root import VcsRoot  # noqa: F401,E501
# from teamcity.models.vcs_status import VcsStatus  # noqa: F401,E501


class VcsRootInstance(TeamcityObject):
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
        'commit_hook_mode': 'bool',
        'href': 'str',
        'id': 'str',
        'last_version': 'str',
        'last_version_internal': 'str',
        'modification_check_interval': 'int',
        'name': 'str',
        'project_locator': 'str',
        'properties': 'Properties',
        'repository_id_strings': 'Items',
        'repository_state': 'RepositoryState',
        'status': 'VcsStatus',
        'vcs_root': 'VcsRoot',
        'vcs_root_id': 'str',
        'vcs_name': 'str',
        'vcs_root_internal_id': 'str'
    }

    attribute_map = {
        'commit_hook_mode': 'commitHookMode',
        'href': 'href',
        'id': 'id',
        'last_version': 'lastVersion',
        'last_version_internal': 'lastVersionInternal',
        'modification_check_interval': 'modificationCheckInterval',
        'name': 'name',
        'project_locator': 'projectLocator',
        'properties': 'properties',
        'repository_id_strings': 'repositoryIdStrings',
        'repository_state': 'repositoryState',
        'status': 'status',
        'vcs_root': 'vcs-root',
        'vcs_root_id': 'vcs-root-id',
        'vcs_name': 'vcsName',
        'vcs_root_internal_id': 'vcsRootInternalId'
    }

    def __init__(self, commit_hook_mode=False, href=None, id=None, last_version=None, last_version_internal=None, modification_check_interval=None, name=None, project_locator=None, properties=None, repository_id_strings=None, repository_state=None, status=None, vcs_root=None, vcs_root_id=None, vcs_name=None, vcs_root_internal_id=None):  # noqa: E501
        """VcsRootInstance - a model defined in Swagger"""  # noqa: E501
        super(VcsRootInstance, self).__init__()

        self._commit_hook_mode = None
        self._href = None
        self._id = None
        self._last_version = None
        self._last_version_internal = None
        self._modification_check_interval = None
        self._name = None
        self._project_locator = None
        self._properties = None
        self._repository_id_strings = None
        self._repository_state = None
        self._status = None
        self._vcs_root = None
        self._vcs_root_id = None
        self._vcs_name = None
        self._vcs_root_internal_id = None
        self.discriminator = None

        if commit_hook_mode is not None:
            self.commit_hook_mode = commit_hook_mode
        if href is not None:
            self.href = href
        if id is not None:
            self.id = id
        if last_version is not None:
            self.last_version = last_version
        if last_version_internal is not None:
            self.last_version_internal = last_version_internal
        if modification_check_interval is not None:
            self.modification_check_interval = modification_check_interval
        if name is not None:
            self.name = name
        if project_locator is not None:
            self.project_locator = project_locator
        if properties is not None:
            self.properties = properties
        if repository_id_strings is not None:
            self.repository_id_strings = repository_id_strings
        if repository_state is not None:
            self.repository_state = repository_state
        if status is not None:
            self.status = status
        if vcs_root is not None:
            self.vcs_root = vcs_root
        if vcs_root_id is not None:
            self.vcs_root_id = vcs_root_id
        if vcs_name is not None:
            self.vcs_name = vcs_name
        if vcs_root_internal_id is not None:
            self.vcs_root_internal_id = vcs_root_internal_id

    @property
    def commit_hook_mode(self):
        """Gets the commit_hook_mode of this VcsRootInstance.  # noqa: E501


        :return: The commit_hook_mode of this VcsRootInstance.  # noqa: E501
        :rtype: bool
        """
        return self._commit_hook_mode

    @commit_hook_mode.setter
    def commit_hook_mode(self, commit_hook_mode):
        """Sets the commit_hook_mode of this VcsRootInstance.


        :param commit_hook_mode: The commit_hook_mode of this VcsRootInstance.  # noqa: E501
        :type: bool
        """

        self._commit_hook_mode = commit_hook_mode

    @property
    def href(self):
        """Gets the href of this VcsRootInstance.  # noqa: E501


        :return: The href of this VcsRootInstance.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this VcsRootInstance.


        :param href: The href of this VcsRootInstance.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this VcsRootInstance.  # noqa: E501


        :return: The id of this VcsRootInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VcsRootInstance.


        :param id: The id of this VcsRootInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_version(self):
        """Gets the last_version of this VcsRootInstance.  # noqa: E501


        :return: The last_version of this VcsRootInstance.  # noqa: E501
        :rtype: str
        """
        return self._last_version

    @last_version.setter
    def last_version(self, last_version):
        """Sets the last_version of this VcsRootInstance.


        :param last_version: The last_version of this VcsRootInstance.  # noqa: E501
        :type: str
        """

        self._last_version = last_version

    @property
    def last_version_internal(self):
        """Gets the last_version_internal of this VcsRootInstance.  # noqa: E501


        :return: The last_version_internal of this VcsRootInstance.  # noqa: E501
        :rtype: str
        """
        return self._last_version_internal

    @last_version_internal.setter
    def last_version_internal(self, last_version_internal):
        """Sets the last_version_internal of this VcsRootInstance.


        :param last_version_internal: The last_version_internal of this VcsRootInstance.  # noqa: E501
        :type: str
        """

        self._last_version_internal = last_version_internal

    @property
    def modification_check_interval(self):
        """Gets the modification_check_interval of this VcsRootInstance.  # noqa: E501


        :return: The modification_check_interval of this VcsRootInstance.  # noqa: E501
        :rtype: int
        """
        return self._modification_check_interval

    @modification_check_interval.setter
    def modification_check_interval(self, modification_check_interval):
        """Sets the modification_check_interval of this VcsRootInstance.


        :param modification_check_interval: The modification_check_interval of this VcsRootInstance.  # noqa: E501
        :type: int
        """

        self._modification_check_interval = modification_check_interval

    @property
    def name(self):
        """Gets the name of this VcsRootInstance.  # noqa: E501


        :return: The name of this VcsRootInstance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VcsRootInstance.


        :param name: The name of this VcsRootInstance.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def project_locator(self):
        """Gets the project_locator of this VcsRootInstance.  # noqa: E501


        :return: The project_locator of this VcsRootInstance.  # noqa: E501
        :rtype: str
        """
        return self._project_locator

    @project_locator.setter
    def project_locator(self, project_locator):
        """Sets the project_locator of this VcsRootInstance.


        :param project_locator: The project_locator of this VcsRootInstance.  # noqa: E501
        :type: str
        """

        self._project_locator = project_locator

    @property
    def properties(self):
        """Gets the properties of this VcsRootInstance.  # noqa: E501


        :return: The properties of this VcsRootInstance.  # noqa: E501
        :rtype: Properties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this VcsRootInstance.


        :param properties: The properties of this VcsRootInstance.  # noqa: E501
        :type: Properties
        """

        self._properties = properties

    @property
    def repository_id_strings(self):
        """Gets the repository_id_strings of this VcsRootInstance.  # noqa: E501


        :return: The repository_id_strings of this VcsRootInstance.  # noqa: E501
        :rtype: Items
        """
        return self._repository_id_strings

    @repository_id_strings.setter
    def repository_id_strings(self, repository_id_strings):
        """Sets the repository_id_strings of this VcsRootInstance.


        :param repository_id_strings: The repository_id_strings of this VcsRootInstance.  # noqa: E501
        :type: Items
        """

        self._repository_id_strings = repository_id_strings

    @property
    def repository_state(self):
        """Gets the repository_state of this VcsRootInstance.  # noqa: E501


        :return: The repository_state of this VcsRootInstance.  # noqa: E501
        :rtype: RepositoryState
        """
        return self._repository_state

    @repository_state.setter
    def repository_state(self, repository_state):
        """Sets the repository_state of this VcsRootInstance.


        :param repository_state: The repository_state of this VcsRootInstance.  # noqa: E501
        :type: RepositoryState
        """

        self._repository_state = repository_state

    @property
    def status(self):
        """Gets the status of this VcsRootInstance.  # noqa: E501


        :return: The status of this VcsRootInstance.  # noqa: E501
        :rtype: VcsStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VcsRootInstance.


        :param status: The status of this VcsRootInstance.  # noqa: E501
        :type: VcsStatus
        """

        self._status = status

    @property
    def vcs_root(self):
        """Gets the vcs_root of this VcsRootInstance.  # noqa: E501


        :return: The vcs_root of this VcsRootInstance.  # noqa: E501
        :rtype: VcsRoot
        """
        return self._vcs_root

    @vcs_root.setter
    def vcs_root(self, vcs_root):
        """Sets the vcs_root of this VcsRootInstance.


        :param vcs_root: The vcs_root of this VcsRootInstance.  # noqa: E501
        :type: VcsRoot
        """

        self._vcs_root = vcs_root

    @property
    def vcs_root_id(self):
        """Gets the vcs_root_id of this VcsRootInstance.  # noqa: E501


        :return: The vcs_root_id of this VcsRootInstance.  # noqa: E501
        :rtype: str
        """
        return self._vcs_root_id

    @vcs_root_id.setter
    def vcs_root_id(self, vcs_root_id):
        """Sets the vcs_root_id of this VcsRootInstance.


        :param vcs_root_id: The vcs_root_id of this VcsRootInstance.  # noqa: E501
        :type: str
        """

        self._vcs_root_id = vcs_root_id

    @property
    def vcs_name(self):
        """Gets the vcs_name of this VcsRootInstance.  # noqa: E501


        :return: The vcs_name of this VcsRootInstance.  # noqa: E501
        :rtype: str
        """
        return self._vcs_name

    @vcs_name.setter
    def vcs_name(self, vcs_name):
        """Sets the vcs_name of this VcsRootInstance.


        :param vcs_name: The vcs_name of this VcsRootInstance.  # noqa: E501
        :type: str
        """

        self._vcs_name = vcs_name

    @property
    def vcs_root_internal_id(self):
        """Gets the vcs_root_internal_id of this VcsRootInstance.  # noqa: E501


        :return: The vcs_root_internal_id of this VcsRootInstance.  # noqa: E501
        :rtype: str
        """
        return self._vcs_root_internal_id

    @vcs_root_internal_id.setter
    def vcs_root_internal_id(self, vcs_root_internal_id):
        """Sets the vcs_root_internal_id of this VcsRootInstance.


        :param vcs_root_internal_id: The vcs_root_internal_id of this VcsRootInstance.  # noqa: E501
        :type: str
        """

        self._vcs_root_internal_id = vcs_root_internal_id

