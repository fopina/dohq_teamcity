# coding: utf-8

from teamcity.base_model import TeamcityObject



class Items(TeamcityObject):
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
        'item': 'list[str]'
    }

    attribute_map = {
        'item': 'item'
    }

    def __init__(self, item=None):  # noqa: E501
        """Items - a model defined in Swagger"""  # noqa: E501
        super(Items, self).__init__()

        self._item = None
        self.discriminator = None

        if item is not None:
            self.item = item

    @property
    def item(self):
        """Gets the item of this Items.  # noqa: E501


        :return: The item of this Items.  # noqa: E501
        :rtype: list[str]
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this Items.


        :param item: The item of this Items.  # noqa: E501
        :type: list[str]
        """

        self._item = item

