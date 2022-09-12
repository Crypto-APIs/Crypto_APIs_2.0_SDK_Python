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
    from cryptoapis.model.list_latest_mined_blocks_ribsb import ListLatestMinedBlocksRIBSB
    from cryptoapis.model.list_latest_mined_blocks_ribsbc import ListLatestMinedBlocksRIBSBC
    from cryptoapis.model.list_latest_mined_blocks_ribsbsc import ListLatestMinedBlocksRIBSBSC
    from cryptoapis.model.list_latest_mined_blocks_ribsd import ListLatestMinedBlocksRIBSD
    from cryptoapis.model.list_latest_mined_blocks_ribsd2 import ListLatestMinedBlocksRIBSD2
    from cryptoapis.model.list_latest_mined_blocks_ribsec import ListLatestMinedBlocksRIBSEC
    from cryptoapis.model.list_latest_mined_blocks_ribsl import ListLatestMinedBlocksRIBSL
    from cryptoapis.model.list_latest_mined_blocks_ribsx import ListLatestMinedBlocksRIBSX
    from cryptoapis.model.list_latest_mined_blocks_ribsx_total_coins import ListLatestMinedBlocksRIBSXTotalCoins
    from cryptoapis.model.list_latest_mined_blocks_ribsx_total_fees import ListLatestMinedBlocksRIBSXTotalFees
    from cryptoapis.model.list_latest_mined_blocks_ribsz import ListLatestMinedBlocksRIBSZ
    from cryptoapis.model.list_latest_mined_blocks_ribsz2 import ListLatestMinedBlocksRIBSZ2
    globals()['ListLatestMinedBlocksRIBSB'] = ListLatestMinedBlocksRIBSB
    globals()['ListLatestMinedBlocksRIBSBC'] = ListLatestMinedBlocksRIBSBC
    globals()['ListLatestMinedBlocksRIBSBSC'] = ListLatestMinedBlocksRIBSBSC
    globals()['ListLatestMinedBlocksRIBSD'] = ListLatestMinedBlocksRIBSD
    globals()['ListLatestMinedBlocksRIBSD2'] = ListLatestMinedBlocksRIBSD2
    globals()['ListLatestMinedBlocksRIBSEC'] = ListLatestMinedBlocksRIBSEC
    globals()['ListLatestMinedBlocksRIBSL'] = ListLatestMinedBlocksRIBSL
    globals()['ListLatestMinedBlocksRIBSX'] = ListLatestMinedBlocksRIBSX
    globals()['ListLatestMinedBlocksRIBSXTotalCoins'] = ListLatestMinedBlocksRIBSXTotalCoins
    globals()['ListLatestMinedBlocksRIBSXTotalFees'] = ListLatestMinedBlocksRIBSXTotalFees
    globals()['ListLatestMinedBlocksRIBSZ'] = ListLatestMinedBlocksRIBSZ
    globals()['ListLatestMinedBlocksRIBSZ2'] = ListLatestMinedBlocksRIBSZ2


class ListLatestMinedBlocksRIBS(ModelComposed):
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
            'total_coins': (ListLatestMinedBlocksRIBSXTotalCoins,),  # noqa: E501
            'bits': (str,),  # noqa: E501
            'chainwork': (str,),  # noqa: E501
            'difficulty': (str,),  # noqa: E501
            'merkle_root': (str,),  # noqa: E501
            'nonce': (str,),  # noqa: E501
            'size': (int,),  # noqa: E501
            'stripped_size': (int,),  # noqa: E501
            'version': (int,),  # noqa: E501
            'version_hex': (str,),  # noqa: E501
            'weight': (int,),  # noqa: E501
            'extra_data': (str,),  # noqa: E501
            'gas_limit': (int,),  # noqa: E501
            'gas_used': (int,),  # noqa: E501
            'mined_in_seconds': (int,),  # noqa: E501
            'sha3_uncles': (str,),  # noqa: E501
            'total_difficulty': (str,),  # noqa: E501
            'uncles': ([str],),  # noqa: E501
            'ds_block': (int,),  # noqa: E501
            'ds_difficulty': (str,),  # noqa: E501
            'ds_leader': (str,),  # noqa: E501
            'micro_blocks': ([str],),  # noqa: E501
            'total_fees': (ListLatestMinedBlocksRIBSXTotalFees,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'total_coins': 'totalCoins',  # noqa: E501
        'bits': 'bits',  # noqa: E501
        'chainwork': 'chainwork',  # noqa: E501
        'difficulty': 'difficulty',  # noqa: E501
        'merkle_root': 'merkleRoot',  # noqa: E501
        'nonce': 'nonce',  # noqa: E501
        'size': 'size',  # noqa: E501
        'stripped_size': 'strippedSize',  # noqa: E501
        'version': 'version',  # noqa: E501
        'version_hex': 'versionHex',  # noqa: E501
        'weight': 'weight',  # noqa: E501
        'extra_data': 'extraData',  # noqa: E501
        'gas_limit': 'gasLimit',  # noqa: E501
        'gas_used': 'gasUsed',  # noqa: E501
        'mined_in_seconds': 'minedInSeconds',  # noqa: E501
        'sha3_uncles': 'sha3Uncles',  # noqa: E501
        'total_difficulty': 'totalDifficulty',  # noqa: E501
        'uncles': 'uncles',  # noqa: E501
        'ds_block': 'dsBlock',  # noqa: E501
        'ds_difficulty': 'dsDifficulty',  # noqa: E501
        'ds_leader': 'dsLeader',  # noqa: E501
        'micro_blocks': 'microBlocks',  # noqa: E501
        'total_fees': 'totalFees',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ListLatestMinedBlocksRIBS - a model defined in OpenAPI

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
            total_coins (ListLatestMinedBlocksRIBSXTotalCoins): [optional]  # noqa: E501
            bits (str): Represents a specific sub-unit of Zcash. Bits have two-decimal precision. [optional]  # noqa: E501
            chainwork (str): Represents a hexadecimal number of all the hashes necessary to produce the current chain. E.g., when converting 0000000000000000000000000000000000000000000086859f7a841475b236fd to a decimal you get 635262017308958427068157 hashes, or 635262 exahashes.. [optional]  # noqa: E501
            difficulty (str): Represents a mathematical value of how hard it is to find a valid hash for this block.. [optional]  # noqa: E501
            merkle_root (str): Defines the single and final (root) node of a Merkle tree. It is the combined hash of all transactions' hashes that are part of a blockchain block.. [optional]  # noqa: E501
            nonce (str): Represents a random value that can be adjusted to satisfy the proof of work. [optional]  # noqa: E501
            size (int): Represents the total size of the block in Bytes.. [optional]  # noqa: E501
            stripped_size (int): Defines the numeric representation of the block size excluding the witness data.. [optional]  # noqa: E501
            version (int): Represents the transaction version number.. [optional]  # noqa: E501
            version_hex (str): Is the hexadecimal string representation of the block's version.. [optional]  # noqa: E501
            weight (int): Represents a measurement to compare the size of different transactions to each other in proportion to the block size limit.. [optional]  # noqa: E501
            extra_data (str): Represents any data that can be included by the miner in the block.. [optional]  # noqa: E501
            gas_limit (int): Represents the maximum amount of gas allowed in the block in order to determine how many transactions it can fit.. [optional]  # noqa: E501
            gas_used (int): Defines how much of the gas for the block has been used.. [optional]  # noqa: E501
            mined_in_seconds (int): Specifies the amount of time required for the block to be mined in second. [optional]  # noqa: E501
            sha3_uncles (str): Defines the combined hash of all uncles for a given parent.. [optional]  # noqa: E501
            total_difficulty (str): Defines the total difficulty of the chain until this block, i.e. how difficult it is for a specific miner to mine a new block. [optional]  # noqa: E501
            uncles ([str]): [optional]  # noqa: E501
            ds_block (int): Represents the Directory Service block which contains metadata about the miners who participate in the consensus protocol.. [optional]  # noqa: E501
            ds_difficulty (str): Defines how difficult it is to mine the dsBlocks.. [optional]  # noqa: E501
            ds_leader (str): Represents a part of the DS Committee which leads the consensus protocol for the epoch.. [optional]  # noqa: E501
            micro_blocks ([str]): [optional]  # noqa: E501
            total_fees (ListLatestMinedBlocksRIBSXTotalFees): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
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
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """ListLatestMinedBlocksRIBS - a model defined in OpenAPI

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
            total_coins (ListLatestMinedBlocksRIBSXTotalCoins): [optional]  # noqa: E501
            bits (str): Represents a specific sub-unit of Zcash. Bits have two-decimal precision. [optional]  # noqa: E501
            chainwork (str): Represents a hexadecimal number of all the hashes necessary to produce the current chain. E.g., when converting 0000000000000000000000000000000000000000000086859f7a841475b236fd to a decimal you get 635262017308958427068157 hashes, or 635262 exahashes.. [optional]  # noqa: E501
            difficulty (str): Represents a mathematical value of how hard it is to find a valid hash for this block.. [optional]  # noqa: E501
            merkle_root (str): Defines the single and final (root) node of a Merkle tree. It is the combined hash of all transactions' hashes that are part of a blockchain block.. [optional]  # noqa: E501
            nonce (str): Represents a random value that can be adjusted to satisfy the proof of work. [optional]  # noqa: E501
            size (int): Represents the total size of the block in Bytes.. [optional]  # noqa: E501
            stripped_size (int): Defines the numeric representation of the block size excluding the witness data.. [optional]  # noqa: E501
            version (int): Represents the transaction version number.. [optional]  # noqa: E501
            version_hex (str): Is the hexadecimal string representation of the block's version.. [optional]  # noqa: E501
            weight (int): Represents a measurement to compare the size of different transactions to each other in proportion to the block size limit.. [optional]  # noqa: E501
            extra_data (str): Represents any data that can be included by the miner in the block.. [optional]  # noqa: E501
            gas_limit (int): Represents the maximum amount of gas allowed in the block in order to determine how many transactions it can fit.. [optional]  # noqa: E501
            gas_used (int): Defines how much of the gas for the block has been used.. [optional]  # noqa: E501
            mined_in_seconds (int): Specifies the amount of time required for the block to be mined in second. [optional]  # noqa: E501
            sha3_uncles (str): Defines the combined hash of all uncles for a given parent.. [optional]  # noqa: E501
            total_difficulty (str): Defines the total difficulty of the chain until this block, i.e. how difficult it is for a specific miner to mine a new block. [optional]  # noqa: E501
            uncles ([str]): [optional]  # noqa: E501
            ds_block (int): Represents the Directory Service block which contains metadata about the miners who participate in the consensus protocol.. [optional]  # noqa: E501
            ds_difficulty (str): Defines how difficult it is to mine the dsBlocks.. [optional]  # noqa: E501
            ds_leader (str): Represents a part of the DS Committee which leads the consensus protocol for the epoch.. [optional]  # noqa: E501
            micro_blocks ([str]): [optional]  # noqa: E501
            total_fees (ListLatestMinedBlocksRIBSXTotalFees): [optional]  # noqa: E501
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
          ],
          'oneOf': [
              ListLatestMinedBlocksRIBSB,
              ListLatestMinedBlocksRIBSBC,
              ListLatestMinedBlocksRIBSBSC,
              ListLatestMinedBlocksRIBSD,
              ListLatestMinedBlocksRIBSD2,
              ListLatestMinedBlocksRIBSEC,
              ListLatestMinedBlocksRIBSL,
              ListLatestMinedBlocksRIBSX,
              ListLatestMinedBlocksRIBSZ,
              ListLatestMinedBlocksRIBSZ2,
          ],
        }
