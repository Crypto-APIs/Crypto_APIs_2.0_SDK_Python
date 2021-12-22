"""
    CryptoAPIs

    Crypto APIs 2.0 is a complex and innovative infrastructure layer that radically simplifies the development of any Blockchain and Crypto related applications. Organized around REST, Crypto APIs 2.0 can assist both novice Bitcoin/Ethereum enthusiasts and crypto experts with the development of their blockchain applications. Crypto APIs 2.0 provides unified endpoints and data, raw data, automatic tokens and coins forwardings, callback functionalities, and much more.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: developers@cryptoapis.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cryptoapis.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from cryptoapis.exceptions import ApiAttributeError


def lazy_import():
    from cryptoapis.model.get_transaction_request_details_ri_recipients import GetTransactionRequestDetailsRIRecipients
    globals()['GetTransactionRequestDetailsRIRecipients'] = GetTransactionRequestDetailsRIRecipients


class GetTransactionRequestDetailsRI(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('blockchain',): {
            'BITCOIN': "bitcoin",
            'BITCOIN-CASH': "bitcoin-cash",
            'LITECOIN': "litecoin",
            'DOGECOIN': "dogecoin",
            'DASH': "dash",
            'ETHEREUM': "ethereum",
            'ETHEREUM-CLASSIC': "ethereum-classic",
            'ZCASH': "zcash",
        },
        ('fee_priority',): {
            'SLOW': "slow",
            'STANDARD': "standard",
            'FAST': "fast",
        },
        ('network',): {
            'MAINNET': "mainnet",
            'TESTNET': "testnet",
            'ROPSTEN': "ropsten",
            'MORDOR': "mordor",
        },
        ('transaction_request_status',): {
            'CREATED': "created",
            'AWAIT-APPROVAL': "await-approval",
            'PENDING': "pending",
            'PREPARED': "prepared",
            'SIGNED': "signed",
            'BROADCASTED': "broadcasted",
            'SUCCESS': "success",
            'FAILED': "failed",
            'REJECTED': "rejected",
            'MINED': "mined",
        },
        ('transaction_type',): {
            'COIN': "coin",
            'TOKEN': "token",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'additional_details': (str,),  # noqa: E501
            'blockchain': (str,),  # noqa: E501
            'fee_priority': (str,),  # noqa: E501
            'network': (str,),  # noqa: E501
            'recipients': ([GetTransactionRequestDetailsRIRecipients],),  # noqa: E501
            'total_transaction_amount': (str,),  # noqa: E501
            'transaction_request_status': (str,),  # noqa: E501
            'transaction_type': (str,),  # noqa: E501
            'unit': (str,),  # noqa: E501
            'wallet_id': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'additional_details': 'additionalDetails',  # noqa: E501
        'blockchain': 'blockchain',  # noqa: E501
        'fee_priority': 'feePriority',  # noqa: E501
        'network': 'network',  # noqa: E501
        'recipients': 'recipients',  # noqa: E501
        'total_transaction_amount': 'totalTransactionAmount',  # noqa: E501
        'transaction_request_status': 'transactionRequestStatus',  # noqa: E501
        'transaction_type': 'transactionType',  # noqa: E501
        'unit': 'unit',  # noqa: E501
        'wallet_id': 'walletId',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, additional_details, blockchain, fee_priority, network, recipients, total_transaction_amount, transaction_request_status, transaction_type, unit, wallet_id, *args, **kwargs):  # noqa: E501
        """GetTransactionRequestDetailsRI - a model defined in OpenAPI

        Args:
            additional_details (str): Defines an optional note for additional details.
            blockchain (str): Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
            fee_priority (str): Defines the priority for the fee, if it is \"slow\", \"standard\" or \"fast\".
            network (str): Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
            recipients ([GetTransactionRequestDetailsRIRecipients]): Represents a list of recipient addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list.
            total_transaction_amount (str): Defines the total transaction amount.
            transaction_request_status (str): Defines the status of the transaction request, e.g. pending.
            transaction_type (str): Defines the transaction type, if it is for coins or tokens.
            unit (str): Defines the unit of the amount.
            wallet_id (str): Defines the unique ID of the Wallet.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.additional_details = additional_details
        self.blockchain = blockchain
        self.fee_priority = fee_priority
        self.network = network
        self.recipients = recipients
        self.total_transaction_amount = total_transaction_amount
        self.transaction_request_status = transaction_request_status
        self.transaction_type = transaction_type
        self.unit = unit
        self.wallet_id = wallet_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, additional_details, blockchain, fee_priority, network, recipients, total_transaction_amount, transaction_request_status, transaction_type, unit, wallet_id, *args, **kwargs):  # noqa: E501
        """GetTransactionRequestDetailsRI - a model defined in OpenAPI

        Args:
            additional_details (str): Defines an optional note for additional details.
            blockchain (str): Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
            fee_priority (str): Defines the priority for the fee, if it is \"slow\", \"standard\" or \"fast\".
            network (str): Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
            recipients ([GetTransactionRequestDetailsRIRecipients]): Represents a list of recipient addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list.
            total_transaction_amount (str): Defines the total transaction amount.
            transaction_request_status (str): Defines the status of the transaction request, e.g. pending.
            transaction_type (str): Defines the transaction type, if it is for coins or tokens.
            unit (str): Defines the unit of the amount.
            wallet_id (str): Defines the unique ID of the Wallet.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.additional_details = additional_details
        self.blockchain = blockchain
        self.fee_priority = fee_priority
        self.network = network
        self.recipients = recipients
        self.total_transaction_amount = total_transaction_amount
        self.transaction_request_status = transaction_request_status
        self.transaction_type = transaction_type
        self.unit = unit
        self.wallet_id = wallet_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
