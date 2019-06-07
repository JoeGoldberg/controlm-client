# coding: utf-8

"""
    Control-M Services

    Provides access to BMC Control-M Services  # noqa: E501

    OpenAPI spec version: 9.18.3
    Contact: support@bmc.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class OrderFolderParameters(object):
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
        'ctm': 'str',
        'folder': 'str',
        'jobs': 'str',
        'create_duplicate': 'bool',
        'hold': 'bool',
        'ignore_criteria': 'bool',
        'independent_flow': 'bool',
        'order_date': 'str',
        'order_into_folder': 'str',
        'wait_for_order_date': 'bool',
        'variables': 'list[dict(str, str)]'
    }

    attribute_map = {
        'ctm': 'ctm',
        'folder': 'folder',
        'jobs': 'jobs',
        'create_duplicate': 'createDuplicate',
        'hold': 'hold',
        'ignore_criteria': 'ignoreCriteria',
        'independent_flow': 'independentFlow',
        'order_date': 'orderDate',
        'order_into_folder': 'orderIntoFolder',
        'wait_for_order_date': 'waitForOrderDate',
        'variables': 'variables'
    }

    def __init__(self, ctm=None, folder=None, jobs=None, create_duplicate=None, hold=None, ignore_criteria=None, independent_flow=None, order_date=None, order_into_folder=None, wait_for_order_date=None, variables=None):  # noqa: E501
        """OrderFolderParameters - a model defined in Swagger"""  # noqa: E501

        self._ctm = None
        self._folder = None
        self._jobs = None
        self._create_duplicate = None
        self._hold = None
        self._ignore_criteria = None
        self._independent_flow = None
        self._order_date = None
        self._order_into_folder = None
        self._wait_for_order_date = None
        self._variables = None
        self.discriminator = None

        if ctm is not None:
            self.ctm = ctm
        if folder is not None:
            self.folder = folder
        if jobs is not None:
            self.jobs = jobs
        if create_duplicate is not None:
            self.create_duplicate = create_duplicate
        if hold is not None:
            self.hold = hold
        if ignore_criteria is not None:
            self.ignore_criteria = ignore_criteria
        if independent_flow is not None:
            self.independent_flow = independent_flow
        if order_date is not None:
            self.order_date = order_date
        if order_into_folder is not None:
            self.order_into_folder = order_into_folder
        if wait_for_order_date is not None:
            self.wait_for_order_date = wait_for_order_date
        if variables is not None:
            self.variables = variables

    @property
    def ctm(self):
        """Gets the ctm of this OrderFolderParameters.  # noqa: E501

        The Control-M Server to order from. REQUIRED.  # noqa: E501

        :return: The ctm of this OrderFolderParameters.  # noqa: E501
        :rtype: str
        """
        return self._ctm

    @ctm.setter
    def ctm(self, ctm):
        """Sets the ctm of this OrderFolderParameters.

        The Control-M Server to order from. REQUIRED.  # noqa: E501

        :param ctm: The ctm of this OrderFolderParameters.  # noqa: E501
        :type: str
        """

        self._ctm = ctm

    @property
    def folder(self):
        """Gets the folder of this OrderFolderParameters.  # noqa: E501

        The folder to order. REQUIRED.  # noqa: E501

        :return: The folder of this OrderFolderParameters.  # noqa: E501
        :rtype: str
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """Sets the folder of this OrderFolderParameters.

        The folder to order. REQUIRED.  # noqa: E501

        :param folder: The folder of this OrderFolderParameters.  # noqa: E501
        :type: str
        """

        self._folder = folder

    @property
    def jobs(self):
        """Gets the jobs of this OrderFolderParameters.  # noqa: E501

        Filter the jobs to order.  # noqa: E501

        :return: The jobs of this OrderFolderParameters.  # noqa: E501
        :rtype: str
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this OrderFolderParameters.

        Filter the jobs to order.  # noqa: E501

        :param jobs: The jobs of this OrderFolderParameters.  # noqa: E501
        :type: str
        """

        self._jobs = jobs

    @property
    def create_duplicate(self):
        """Gets the create_duplicate of this OrderFolderParameters.  # noqa: E501

        Is it allowed to order the same jobs more than once to the same SMART folder. HIDDEN.  # noqa: E501

        :return: The create_duplicate of this OrderFolderParameters.  # noqa: E501
        :rtype: bool
        """
        return self._create_duplicate

    @create_duplicate.setter
    def create_duplicate(self, create_duplicate):
        """Sets the create_duplicate of this OrderFolderParameters.

        Is it allowed to order the same jobs more than once to the same SMART folder. HIDDEN.  # noqa: E501

        :param create_duplicate: The create_duplicate of this OrderFolderParameters.  # noqa: E501
        :type: bool
        """

        self._create_duplicate = create_duplicate

    @property
    def hold(self):
        """Gets the hold of this OrderFolderParameters.  # noqa: E501

        Are jobs ordered in a HOLD state. HIDDEN.  # noqa: E501

        :return: The hold of this OrderFolderParameters.  # noqa: E501
        :rtype: bool
        """
        return self._hold

    @hold.setter
    def hold(self, hold):
        """Sets the hold of this OrderFolderParameters.

        Are jobs ordered in a HOLD state. HIDDEN.  # noqa: E501

        :param hold: The hold of this OrderFolderParameters.  # noqa: E501
        :type: bool
        """

        self._hold = hold

    @property
    def ignore_criteria(self):
        """Gets the ignore_criteria of this OrderFolderParameters.  # noqa: E501

        Is scheduling criteria to be ignored. HIDDEN.  # noqa: E501

        :return: The ignore_criteria of this OrderFolderParameters.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_criteria

    @ignore_criteria.setter
    def ignore_criteria(self, ignore_criteria):
        """Sets the ignore_criteria of this OrderFolderParameters.

        Is scheduling criteria to be ignored. HIDDEN.  # noqa: E501

        :param ignore_criteria: The ignore_criteria of this OrderFolderParameters.  # noqa: E501
        :type: bool
        """

        self._ignore_criteria = ignore_criteria

    @property
    def independent_flow(self):
        """Gets the independent_flow of this OrderFolderParameters.  # noqa: E501

        Whether to generate new flow in this order. HIDDEN.  # noqa: E501

        :return: The independent_flow of this OrderFolderParameters.  # noqa: E501
        :rtype: bool
        """
        return self._independent_flow

    @independent_flow.setter
    def independent_flow(self, independent_flow):
        """Sets the independent_flow of this OrderFolderParameters.

        Whether to generate new flow in this order. HIDDEN.  # noqa: E501

        :param independent_flow: The independent_flow of this OrderFolderParameters.  # noqa: E501
        :type: bool
        """

        self._independent_flow = independent_flow

    @property
    def order_date(self):
        """Gets the order_date of this OrderFolderParameters.  # noqa: E501

        The order date that is attached to this order command. HIDDEN.  # noqa: E501

        :return: The order_date of this OrderFolderParameters.  # noqa: E501
        :rtype: str
        """
        return self._order_date

    @order_date.setter
    def order_date(self, order_date):
        """Sets the order_date of this OrderFolderParameters.

        The order date that is attached to this order command. HIDDEN.  # noqa: E501

        :param order_date: The order_date of this OrderFolderParameters.  # noqa: E501
        :type: str
        """

        self._order_date = order_date

    @property
    def order_into_folder(self):
        """Gets the order_into_folder of this OrderFolderParameters.  # noqa: E501

        Policy for placing the jobs in a SMART folder. HIDDEN.  # noqa: E501

        :return: The order_into_folder of this OrderFolderParameters.  # noqa: E501
        :rtype: str
        """
        return self._order_into_folder

    @order_into_folder.setter
    def order_into_folder(self, order_into_folder):
        """Sets the order_into_folder of this OrderFolderParameters.

        Policy for placing the jobs in a SMART folder. HIDDEN.  # noqa: E501

        :param order_into_folder: The order_into_folder of this OrderFolderParameters.  # noqa: E501
        :type: str
        """

        self._order_into_folder = order_into_folder

    @property
    def wait_for_order_date(self):
        """Gets the wait_for_order_date of this OrderFolderParameters.  # noqa: E501

        Whether to wait for the order date when running the jobs. HIDDEN.  # noqa: E501

        :return: The wait_for_order_date of this OrderFolderParameters.  # noqa: E501
        :rtype: bool
        """
        return self._wait_for_order_date

    @wait_for_order_date.setter
    def wait_for_order_date(self, wait_for_order_date):
        """Sets the wait_for_order_date of this OrderFolderParameters.

        Whether to wait for the order date when running the jobs. HIDDEN.  # noqa: E501

        :param wait_for_order_date: The wait_for_order_date of this OrderFolderParameters.  # noqa: E501
        :type: bool
        """

        self._wait_for_order_date = wait_for_order_date

    @property
    def variables(self):
        """Gets the variables of this OrderFolderParameters.  # noqa: E501

        Job Variables for this run. HIDDEN.  # noqa: E501

        :return: The variables of this OrderFolderParameters.  # noqa: E501
        :rtype: list[dict(str, str)]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this OrderFolderParameters.

        Job Variables for this run. HIDDEN.  # noqa: E501

        :param variables: The variables of this OrderFolderParameters.  # noqa: E501
        :type: list[dict(str, str)]
        """

        self._variables = variables

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(OrderFolderParameters, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OrderFolderParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
