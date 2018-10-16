# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.build import Build  # noqa: F401,E501
# from dohq_teamcity.models.mute import Mute  # noqa: F401,E501
# from dohq_teamcity.models.test import Test  # noqa: F401,E501
# from dohq_teamcity.models.test_occurrence import TestOccurrence  # noqa: F401,E501
# from dohq_teamcity.models.test_occurrences import TestOccurrences  # noqa: F401,E501


class TestOccurrence(TeamCityObject):
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
        'build': 'Build',
        'currently_investigated': 'bool',
        'currently_muted': 'bool',
        'details': 'str',
        'duration': 'int',
        'first_failed': 'TestOccurrence',
        'href': 'str',
        'id': 'str',
        'ignore_details': 'str',
        'ignored': 'bool',
        'invocations': 'TestOccurrences',
        'mute': 'Mute',
        'muted': 'bool',
        'name': 'str',
        'next_fixed': 'TestOccurrence',
        'run_order': 'str',
        'status': 'str',
        'test': 'Test'
    }

    attribute_map = {
        'build': 'build',
        'currently_investigated': 'currentlyInvestigated',
        'currently_muted': 'currentlyMuted',
        'details': 'details',
        'duration': 'duration',
        'first_failed': 'firstFailed',
        'href': 'href',
        'id': 'id',
        'ignore_details': 'ignoreDetails',
        'ignored': 'ignored',
        'invocations': 'invocations',
        'mute': 'mute',
        'muted': 'muted',
        'name': 'name',
        'next_fixed': 'nextFixed',
        'run_order': 'runOrder',
        'status': 'status',
        'test': 'test'
    }

    def __init__(self, build=None, currently_investigated=False, currently_muted=False, details=None, duration=None, first_failed=None, href=None, id=None, ignore_details=None, ignored=False, invocations=None, mute=None, muted=False, name=None, next_fixed=None, run_order=None, status=None, test=None, teamcity=None):  # noqa: E501
        """TestOccurrence - a model defined in Swagger"""  # noqa: E501

        self._build = None
        self._currently_investigated = None
        self._currently_muted = None
        self._details = None
        self._duration = None
        self._first_failed = None
        self._href = None
        self._id = None
        self._ignore_details = None
        self._ignored = None
        self._invocations = None
        self._mute = None
        self._muted = None
        self._name = None
        self._next_fixed = None
        self._run_order = None
        self._status = None
        self._test = None
        self.discriminator = None

        if build is not None:
            self.build = build
        if currently_investigated is not None:
            self.currently_investigated = currently_investigated
        if currently_muted is not None:
            self.currently_muted = currently_muted
        if details is not None:
            self.details = details
        if duration is not None:
            self.duration = duration
        if first_failed is not None:
            self.first_failed = first_failed
        if href is not None:
            self.href = href
        if id is not None:
            self.id = id
        if ignore_details is not None:
            self.ignore_details = ignore_details
        if ignored is not None:
            self.ignored = ignored
        if invocations is not None:
            self.invocations = invocations
        if mute is not None:
            self.mute = mute
        if muted is not None:
            self.muted = muted
        if name is not None:
            self.name = name
        if next_fixed is not None:
            self.next_fixed = next_fixed
        if run_order is not None:
            self.run_order = run_order
        if status is not None:
            self.status = status
        if test is not None:
            self.test = test
        super(TestOccurrence, self).__init__(teamcity=teamcity)

    @property
    def build(self):
        """Gets the build of this TestOccurrence.  # noqa: E501


        :return: The build of this TestOccurrence.  # noqa: E501
        :rtype: Build
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this TestOccurrence.


        :param build: The build of this TestOccurrence.  # noqa: E501
        :type: Build
        """

        self._build = build

    @property
    def currently_investigated(self):
        """Gets the currently_investigated of this TestOccurrence.  # noqa: E501


        :return: The currently_investigated of this TestOccurrence.  # noqa: E501
        :rtype: bool
        """
        return self._currently_investigated

    @currently_investigated.setter
    def currently_investigated(self, currently_investigated):
        """Sets the currently_investigated of this TestOccurrence.


        :param currently_investigated: The currently_investigated of this TestOccurrence.  # noqa: E501
        :type: bool
        """

        self._currently_investigated = currently_investigated

    @property
    def currently_muted(self):
        """Gets the currently_muted of this TestOccurrence.  # noqa: E501


        :return: The currently_muted of this TestOccurrence.  # noqa: E501
        :rtype: bool
        """
        return self._currently_muted

    @currently_muted.setter
    def currently_muted(self, currently_muted):
        """Sets the currently_muted of this TestOccurrence.


        :param currently_muted: The currently_muted of this TestOccurrence.  # noqa: E501
        :type: bool
        """

        self._currently_muted = currently_muted

    @property
    def details(self):
        """Gets the details of this TestOccurrence.  # noqa: E501


        :return: The details of this TestOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this TestOccurrence.


        :param details: The details of this TestOccurrence.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def duration(self):
        """Gets the duration of this TestOccurrence.  # noqa: E501


        :return: The duration of this TestOccurrence.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TestOccurrence.


        :param duration: The duration of this TestOccurrence.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def first_failed(self):
        """Gets the first_failed of this TestOccurrence.  # noqa: E501


        :return: The first_failed of this TestOccurrence.  # noqa: E501
        :rtype: TestOccurrence
        """
        return self._first_failed

    @first_failed.setter
    def first_failed(self, first_failed):
        """Sets the first_failed of this TestOccurrence.


        :param first_failed: The first_failed of this TestOccurrence.  # noqa: E501
        :type: TestOccurrence
        """

        self._first_failed = first_failed

    @property
    def href(self):
        """Gets the href of this TestOccurrence.  # noqa: E501


        :return: The href of this TestOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this TestOccurrence.


        :param href: The href of this TestOccurrence.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this TestOccurrence.  # noqa: E501


        :return: The id of this TestOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TestOccurrence.


        :param id: The id of this TestOccurrence.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ignore_details(self):
        """Gets the ignore_details of this TestOccurrence.  # noqa: E501


        :return: The ignore_details of this TestOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._ignore_details

    @ignore_details.setter
    def ignore_details(self, ignore_details):
        """Sets the ignore_details of this TestOccurrence.


        :param ignore_details: The ignore_details of this TestOccurrence.  # noqa: E501
        :type: str
        """

        self._ignore_details = ignore_details

    @property
    def ignored(self):
        """Gets the ignored of this TestOccurrence.  # noqa: E501


        :return: The ignored of this TestOccurrence.  # noqa: E501
        :rtype: bool
        """
        return self._ignored

    @ignored.setter
    def ignored(self, ignored):
        """Sets the ignored of this TestOccurrence.


        :param ignored: The ignored of this TestOccurrence.  # noqa: E501
        :type: bool
        """

        self._ignored = ignored

    @property
    def invocations(self):
        """Gets the invocations of this TestOccurrence.  # noqa: E501


        :return: The invocations of this TestOccurrence.  # noqa: E501
        :rtype: TestOccurrences
        """
        return self._invocations

    @invocations.setter
    def invocations(self, invocations):
        """Sets the invocations of this TestOccurrence.


        :param invocations: The invocations of this TestOccurrence.  # noqa: E501
        :type: TestOccurrences
        """

        self._invocations = invocations

    @property
    def mute(self):
        """Gets the mute of this TestOccurrence.  # noqa: E501


        :return: The mute of this TestOccurrence.  # noqa: E501
        :rtype: Mute
        """
        return self._mute

    @mute.setter
    def mute(self, mute):
        """Sets the mute of this TestOccurrence.


        :param mute: The mute of this TestOccurrence.  # noqa: E501
        :type: Mute
        """

        self._mute = mute

    @property
    def muted(self):
        """Gets the muted of this TestOccurrence.  # noqa: E501


        :return: The muted of this TestOccurrence.  # noqa: E501
        :rtype: bool
        """
        return self._muted

    @muted.setter
    def muted(self, muted):
        """Sets the muted of this TestOccurrence.


        :param muted: The muted of this TestOccurrence.  # noqa: E501
        :type: bool
        """

        self._muted = muted

    @property
    def name(self):
        """Gets the name of this TestOccurrence.  # noqa: E501


        :return: The name of this TestOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TestOccurrence.


        :param name: The name of this TestOccurrence.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def next_fixed(self):
        """Gets the next_fixed of this TestOccurrence.  # noqa: E501


        :return: The next_fixed of this TestOccurrence.  # noqa: E501
        :rtype: TestOccurrence
        """
        return self._next_fixed

    @next_fixed.setter
    def next_fixed(self, next_fixed):
        """Sets the next_fixed of this TestOccurrence.


        :param next_fixed: The next_fixed of this TestOccurrence.  # noqa: E501
        :type: TestOccurrence
        """

        self._next_fixed = next_fixed

    @property
    def run_order(self):
        """Gets the run_order of this TestOccurrence.  # noqa: E501


        :return: The run_order of this TestOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._run_order

    @run_order.setter
    def run_order(self, run_order):
        """Sets the run_order of this TestOccurrence.


        :param run_order: The run_order of this TestOccurrence.  # noqa: E501
        :type: str
        """

        self._run_order = run_order

    @property
    def status(self):
        """Gets the status of this TestOccurrence.  # noqa: E501


        :return: The status of this TestOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TestOccurrence.


        :param status: The status of this TestOccurrence.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def test(self):
        """Gets the test of this TestOccurrence.  # noqa: E501


        :return: The test of this TestOccurrence.  # noqa: E501
        :rtype: Test
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this TestOccurrence.


        :param test: The test of this TestOccurrence.  # noqa: E501
        :type: Test
        """

        self._test = test

