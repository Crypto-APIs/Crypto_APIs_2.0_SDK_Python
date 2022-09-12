"""
    CryptoAPIs

    Crypto APIs is a complex and innovative infrastructure layer that radically simplifies the development of any Blockchain and Crypto related applications. Organized around REST, Crypto APIs can assist both novice Bitcoin/Ethereum enthusiasts and crypto experts with the development of their blockchain applications. Crypto APIs provides unified endpoints and data, raw data, automatic tokens and coins forwardings, callback functionalities, and much more.  # noqa: E501

    The version of the OpenAPI document: 2021-03-20
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
    from cryptoapis.model.list_xrp_ripple_transactions_by_block_hash_ri_fee import ListXRPRippleTransactionsByBlockHashRIFee
    from cryptoapis.model.list_xrp_ripple_transactions_by_block_hash_ri_offer import ListXRPRippleTransactionsByBlockHashRIOffer
    from cryptoapis.model.list_xrp_ripple_transactions_by_block_hash_ri_receive import ListXRPRippleTransactionsByBlockHashRIReceive
    from cryptoapis.model.list_xrp_ripple_transactions_by_block_hash_ri_recipients_inner import ListXRPRippleTransactionsByBlockHashRIRecipientsInner
    from cryptoapis.model.list_xrp_ripple_transactions_by_block_hash_ri_senders_inner import ListXRPRippleTransactionsByBlockHashRISendersInner
    from cryptoapis.model.list_xrp_ripple_transactions_by_block_hash_ri_value import ListXRPRippleTransactionsByBlockHashRIValue
    globals()['ListXRPRippleTransactionsByBlockHashRIFee'] = ListXRPRippleTransactionsByBlockHashRIFee
    globals()['ListXRPRippleTransactionsByBlockHashRIOffer'] = ListXRPRippleTransactionsByBlockHashRIOffer
    globals()['ListXRPRippleTransactionsByBlockHashRIReceive'] = ListXRPRippleTransactionsByBlockHashRIReceive
    globals()['ListXRPRippleTransactionsByBlockHashRIRecipientsInner'] = ListXRPRippleTransactionsByBlockHashRIRecipientsInner
    globals()['ListXRPRippleTransactionsByBlockHashRISendersInner'] = ListXRPRippleTransactionsByBlockHashRISendersInner
    globals()['ListXRPRippleTransactionsByBlockHashRIValue'] = ListXRPRippleTransactionsByBlockHashRIValue


class ListXRPRippleTransactionsByBlockHashRI(ModelNormal):
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
            'index': (int,),  # noqa: E501
            'mined_in_block_height': (int,),  # noqa: E501
            'recipients': ([ListXRPRippleTransactionsByBlockHashRIRecipientsInner],),  # noqa: E501
            'senders': ([ListXRPRippleTransactionsByBlockHashRISendersInner],),  # noqa: E501
            'sequence': (int,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'timestamp': (int,),  # noqa: E501
            'transaction_hash': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'fee': (ListXRPRippleTransactionsByBlockHashRIFee,),  # noqa: E501
            'offer': (ListXRPRippleTransactionsByBlockHashRIOffer,),  # noqa: E501
            'receive': (ListXRPRippleTransactionsByBlockHashRIReceive,),  # noqa: E501
            'value': (ListXRPRippleTransactionsByBlockHashRIValue,),  # noqa: E501
            'additional_data': (str,),  # noqa: E501
            'destination_tag': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'index': 'index',  # noqa: E501
        'mined_in_block_height': 'minedInBlockHeight',  # noqa: E501
        'recipients': 'recipients',  # noqa: E501
        'senders': 'senders',  # noqa: E501
        'sequence': 'sequence',  # noqa: E501
        'status': 'status',  # noqa: E501
        'timestamp': 'timestamp',  # noqa: E501
        'transaction_hash': 'transactionHash',  # noqa: E501
        'type': 'type',  # noqa: E501
        'fee': 'fee',  # noqa: E501
        'offer': 'offer',  # noqa: E501
        'receive': 'receive',  # noqa: E501
        'value': 'value',  # noqa: E501
        'additional_data': 'additionalData',  # noqa: E501
        'destination_tag': 'destinationTag',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, index, mined_in_block_height, recipients, senders, sequence, status, timestamp, transaction_hash, type, fee, offer, receive, value, *args, **kwargs):  # noqa: E501
        """ListXRPRippleTransactionsByBlockHashRI - a model defined in OpenAPI

        Args:
            index (int): Represents the index position of the transaction in the specific block.
            mined_in_block_height (int): Represents the hight of the block where this transaction was mined/confirmed for first time. The height is defined as the number of blocks in the blockchain preceding this specific block.
            recipients ([ListXRPRippleTransactionsByBlockHashRIRecipientsInner]): Represents an object of addresses that receive the transactions.
            senders ([ListXRPRippleTransactionsByBlockHashRISendersInner]): Represents an object of addresses that provide the funds.
            sequence (int): Defines the transaction input's sequence as an integer, which is is used when transactions are replaced with newer versions before LockTime.
            status (str): Defines the status of the transaction.
            timestamp (int): Defines the exact date/time in Unix Timestamp when this transaction was mined, confirmed or first seen in Mempool, if it is unconfirmed.
            transaction_hash (str): Represents the same as `transactionId` for account-based protocols like Ethereum, while it could be different in UTXO-based protocols like Bitcoin. E.g., in UTXO-based protocols `hash` is different from `transactionId` for SegWit transactions.
            type (str): Defines the type of the transaction.
            fee (ListXRPRippleTransactionsByBlockHashRIFee):
            offer (ListXRPRippleTransactionsByBlockHashRIOffer):
            receive (ListXRPRippleTransactionsByBlockHashRIReceive):
            value (ListXRPRippleTransactionsByBlockHashRIValue):

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
            additional_data (str): Represents any additional data that may be needed.. [optional]  # noqa: E501
            destination_tag (int): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
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

        self.index = index
        self.mined_in_block_height = mined_in_block_height
        self.recipients = recipients
        self.senders = senders
        self.sequence = sequence
        self.status = status
        self.timestamp = timestamp
        self.transaction_hash = transaction_hash
        self.type = type
        self.fee = fee
        self.offer = offer
        self.receive = receive
        self.value = value
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
    def __init__(self, index, mined_in_block_height, recipients, senders, sequence, status, timestamp, transaction_hash, type, fee, offer, receive, value, *args, **kwargs):  # noqa: E501
        """ListXRPRippleTransactionsByBlockHashRI - a model defined in OpenAPI

        Args:
            index (int): Represents the index position of the transaction in the specific block.
            mined_in_block_height (int): Represents the hight of the block where this transaction was mined/confirmed for first time. The height is defined as the number of blocks in the blockchain preceding this specific block.
            recipients ([ListXRPRippleTransactionsByBlockHashRIRecipientsInner]): Represents an object of addresses that receive the transactions.
            senders ([ListXRPRippleTransactionsByBlockHashRISendersInner]): Represents an object of addresses that provide the funds.
            sequence (int): Defines the transaction input's sequence as an integer, which is is used when transactions are replaced with newer versions before LockTime.
            status (str): Defines the status of the transaction.
            timestamp (int): Defines the exact date/time in Unix Timestamp when this transaction was mined, confirmed or first seen in Mempool, if it is unconfirmed.
            transaction_hash (str): Represents the same as `transactionId` for account-based protocols like Ethereum, while it could be different in UTXO-based protocols like Bitcoin. E.g., in UTXO-based protocols `hash` is different from `transactionId` for SegWit transactions.
            type (str): Defines the type of the transaction.
            fee (ListXRPRippleTransactionsByBlockHashRIFee):
            offer (ListXRPRippleTransactionsByBlockHashRIOffer):
            receive (ListXRPRippleTransactionsByBlockHashRIReceive):
            value (ListXRPRippleTransactionsByBlockHashRIValue):

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
            additional_data (str): Represents any additional data that may be needed.. [optional]  # noqa: E501
            destination_tag (int): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
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

        self.index = index
        self.mined_in_block_height = mined_in_block_height
        self.recipients = recipients
        self.senders = senders
        self.sequence = sequence
        self.status = status
        self.timestamp = timestamp
        self.transaction_hash = transaction_hash
        self.type = type
        self.fee = fee
        self.offer = offer
        self.receive = receive
        self.value = value
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
