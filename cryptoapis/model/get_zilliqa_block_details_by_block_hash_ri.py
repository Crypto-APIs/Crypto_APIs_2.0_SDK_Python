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



class GetZilliqaBlockDetailsByBlockHashRI(ModelNormal):
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
        return {
            'block_height': (int,),  # noqa: E501
            'difficulty': (str,),  # noqa: E501
            'ds_block': (int,),  # noqa: E501
            'ds_difficulty': (str,),  # noqa: E501
            'ds_leader': (str,),  # noqa: E501
            'gas_limit': (int,),  # noqa: E501
            'gas_used': (int,),  # noqa: E501
            'micro_blocks': ([str],),  # noqa: E501
            'next_block_hash': (str,),  # noqa: E501
            'previous_block_hash': (str,),  # noqa: E501
            'timestamp': (int,),  # noqa: E501
            'transactions_count': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'block_height': 'blockHeight',  # noqa: E501
        'difficulty': 'difficulty',  # noqa: E501
        'ds_block': 'dsBlock',  # noqa: E501
        'ds_difficulty': 'dsDifficulty',  # noqa: E501
        'ds_leader': 'dsLeader',  # noqa: E501
        'gas_limit': 'gasLimit',  # noqa: E501
        'gas_used': 'gasUsed',  # noqa: E501
        'micro_blocks': 'microBlocks',  # noqa: E501
        'next_block_hash': 'nextBlockHash',  # noqa: E501
        'previous_block_hash': 'previousBlockHash',  # noqa: E501
        'timestamp': 'timestamp',  # noqa: E501
        'transactions_count': 'transactionsCount',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, block_height, difficulty, ds_block, ds_difficulty, ds_leader, gas_limit, gas_used, micro_blocks, next_block_hash, previous_block_hash, timestamp, transactions_count, *args, **kwargs):  # noqa: E501
        """GetZilliqaBlockDetailsByBlockHashRI - a model defined in OpenAPI

        Args:
            block_height (int): Represents the number of blocks in the blockchain preceding this specific block. Block numbers have no gaps. A blockchain usually starts with block 0 called the \"Genesis block\".
            difficulty (str): Defines how difficult it is for a specific miner to mine the block.
            ds_block (int): Represents the Directory Service block which contains metadata about the miners who participate in the consensus protocol.
            ds_difficulty (str): Defines how difficult it is to mine the dsBlocks.
            ds_leader (str): Represents a part of the DS Committee which leads the consensus protocol for the epoch.
            gas_limit (int): Represents the maximum amount of gas allowed in the block in order to determine how many transactions it can fit.
            gas_used (int): Defines how much of the gas for the block has been used.
            micro_blocks ([str]):
            next_block_hash (str): Defines the hash of the next block from the specific blockchain.
            previous_block_hash (str): Represents the hash of the previous block, also known as the parent block.
            timestamp (int): Defines the exact date/time when this block was mined in Unix Timestamp.
            transactions_count (int): Represents the total number of all transactions as part of this block.

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

        self.block_height = block_height
        self.difficulty = difficulty
        self.ds_block = ds_block
        self.ds_difficulty = ds_difficulty
        self.ds_leader = ds_leader
        self.gas_limit = gas_limit
        self.gas_used = gas_used
        self.micro_blocks = micro_blocks
        self.next_block_hash = next_block_hash
        self.previous_block_hash = previous_block_hash
        self.timestamp = timestamp
        self.transactions_count = transactions_count
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
    def __init__(self, block_height, difficulty, ds_block, ds_difficulty, ds_leader, gas_limit, gas_used, micro_blocks, next_block_hash, previous_block_hash, timestamp, transactions_count, *args, **kwargs):  # noqa: E501
        """GetZilliqaBlockDetailsByBlockHashRI - a model defined in OpenAPI

        Args:
            block_height (int): Represents the number of blocks in the blockchain preceding this specific block. Block numbers have no gaps. A blockchain usually starts with block 0 called the \"Genesis block\".
            difficulty (str): Defines how difficult it is for a specific miner to mine the block.
            ds_block (int): Represents the Directory Service block which contains metadata about the miners who participate in the consensus protocol.
            ds_difficulty (str): Defines how difficult it is to mine the dsBlocks.
            ds_leader (str): Represents a part of the DS Committee which leads the consensus protocol for the epoch.
            gas_limit (int): Represents the maximum amount of gas allowed in the block in order to determine how many transactions it can fit.
            gas_used (int): Defines how much of the gas for the block has been used.
            micro_blocks ([str]):
            next_block_hash (str): Defines the hash of the next block from the specific blockchain.
            previous_block_hash (str): Represents the hash of the previous block, also known as the parent block.
            timestamp (int): Defines the exact date/time when this block was mined in Unix Timestamp.
            transactions_count (int): Represents the total number of all transactions as part of this block.

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

        self.block_height = block_height
        self.difficulty = difficulty
        self.ds_block = ds_block
        self.ds_difficulty = ds_difficulty
        self.ds_leader = ds_leader
        self.gas_limit = gas_limit
        self.gas_used = gas_used
        self.micro_blocks = micro_blocks
        self.next_block_hash = next_block_hash
        self.previous_block_hash = previous_block_hash
        self.timestamp = timestamp
        self.transactions_count = transactions_count
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
