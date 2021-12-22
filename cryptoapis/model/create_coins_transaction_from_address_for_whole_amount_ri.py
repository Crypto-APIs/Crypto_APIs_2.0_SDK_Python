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
    from cryptoapis.model.create_coins_transaction_from_address_for_whole_amount_ri_recipients import CreateCoinsTransactionFromAddressForWholeAmountRIRecipients
    from cryptoapis.model.create_coins_transaction_from_address_for_whole_amount_ri_senders import CreateCoinsTransactionFromAddressForWholeAmountRISenders
    globals()['CreateCoinsTransactionFromAddressForWholeAmountRIRecipients'] = CreateCoinsTransactionFromAddressForWholeAmountRIRecipients
    globals()['CreateCoinsTransactionFromAddressForWholeAmountRISenders'] = CreateCoinsTransactionFromAddressForWholeAmountRISenders


class CreateCoinsTransactionFromAddressForWholeAmountRI(ModelNormal):
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
        ('fee_priority',): {
            'SLOW': "slow",
            'STANDARD': "standard",
            'FAST': "fast",
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
            'fee_priority': (str,),  # noqa: E501
            'recipients': ([CreateCoinsTransactionFromAddressForWholeAmountRIRecipients],),  # noqa: E501
            'senders': (CreateCoinsTransactionFromAddressForWholeAmountRISenders,),  # noqa: E501
            'transaction_request_id': (str,),  # noqa: E501
            'transaction_request_status': (str,),  # noqa: E501
            'callback_secret_key': (str,),  # noqa: E501
            'callback_url': (str,),  # noqa: E501
            'note': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'fee_priority': 'feePriority',  # noqa: E501
        'recipients': 'recipients',  # noqa: E501
        'senders': 'senders',  # noqa: E501
        'transaction_request_id': 'transactionRequestId',  # noqa: E501
        'transaction_request_status': 'transactionRequestStatus',  # noqa: E501
        'callback_secret_key': 'callbackSecretKey',  # noqa: E501
        'callback_url': 'callbackUrl',  # noqa: E501
        'note': 'note',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, fee_priority, recipients, senders, transaction_request_id, transaction_request_status, *args, **kwargs):  # noqa: E501
        """CreateCoinsTransactionFromAddressForWholeAmountRI - a model defined in OpenAPI

        Args:
            fee_priority (str): Represents the fee priority of the automation, whether it is \"slow\", \"standard\" or \"fast\".
            recipients ([CreateCoinsTransactionFromAddressForWholeAmountRIRecipients]): Defines the destination for the transaction, i.e. the recipient(s).
            senders (CreateCoinsTransactionFromAddressForWholeAmountRISenders):
            transaction_request_id (str): Represents a unique identifier of the transaction request (the request sent to make a transaction), which helps in identifying which callback and which `referenceId` concern that specific transaction request.
            transaction_request_status (str): Defines the status of the transaction, e.g. \"created, \"await_approval\", \"pending\", \"prepared\", \"signed\", \"broadcasted\", \"success\", \"failed\", \"rejected\", mined\".

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
            callback_secret_key (str): Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our [Documentation](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-security).. [optional]  # noqa: E501
            callback_url (str): Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs.. [optional]  # noqa: E501
            note (str): Represents an optional note to add a free text in, explaining or providing additional detail on the transaction request.Optional Transaction note with additional details. [optional]  # noqa: E501
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

        self.fee_priority = fee_priority
        self.recipients = recipients
        self.senders = senders
        self.transaction_request_id = transaction_request_id
        self.transaction_request_status = transaction_request_status
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
    def __init__(self, fee_priority, recipients, senders, transaction_request_id, transaction_request_status, *args, **kwargs):  # noqa: E501
        """CreateCoinsTransactionFromAddressForWholeAmountRI - a model defined in OpenAPI

        Args:
            fee_priority (str): Represents the fee priority of the automation, whether it is \"slow\", \"standard\" or \"fast\".
            recipients ([CreateCoinsTransactionFromAddressForWholeAmountRIRecipients]): Defines the destination for the transaction, i.e. the recipient(s).
            senders (CreateCoinsTransactionFromAddressForWholeAmountRISenders):
            transaction_request_id (str): Represents a unique identifier of the transaction request (the request sent to make a transaction), which helps in identifying which callback and which `referenceId` concern that specific transaction request.
            transaction_request_status (str): Defines the status of the transaction, e.g. \"created, \"await_approval\", \"pending\", \"prepared\", \"signed\", \"broadcasted\", \"success\", \"failed\", \"rejected\", mined\".

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
            callback_secret_key (str): Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our [Documentation](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-security).. [optional]  # noqa: E501
            callback_url (str): Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs.. [optional]  # noqa: E501
            note (str): Represents an optional note to add a free text in, explaining or providing additional detail on the transaction request.Optional Transaction note with additional details. [optional]  # noqa: E501
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

        self.fee_priority = fee_priority
        self.recipients = recipients
        self.senders = senders
        self.transaction_request_id = transaction_request_id
        self.transaction_request_status = transaction_request_status
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
