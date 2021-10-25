
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.assets_api import AssetsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from cryptoapis.api.assets_api import AssetsApi
from cryptoapis.api.automatic_coins_forwarding_api import AutomaticCoinsForwardingApi
from cryptoapis.api.automatic_tokens_forwarding_api import AutomaticTokensForwardingApi
from cryptoapis.api.create_subscriptions_for_api import CreateSubscriptionsForApi
from cryptoapis.api.exchange_rates_api import ExchangeRatesApi
from cryptoapis.api.features_api import FeaturesApi
from cryptoapis.api.generating_api import GeneratingApi
from cryptoapis.api.hd_wallets_api import HDWalletsApi
from cryptoapis.api.informative_api import InformativeApi
from cryptoapis.api.manage_subscriptions_api import ManageSubscriptionsApi
from cryptoapis.api.metadata_api import MetadataApi
from cryptoapis.api.omni_layer_api import OmniLayerApi
from cryptoapis.api.tokens_api import TokensApi
from cryptoapis.api.transactions_api import TransactionsApi
from cryptoapis.api.utxo_based_api import UTXOBasedApi
from cryptoapis.api.unified_endpoints_api import UnifiedEndpointsApi
from cryptoapis.api.xrp__ripple_api import XRPRippleApi
from cryptoapis.api.zilliqa_api import ZilliqaApi
from cryptoapis.api.internal_api import InternalApi
