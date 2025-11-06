import sys
import bitmart.ccxt as ccxt_module
sys.modules['ccxt'] = ccxt_module

from bitmart.ccxt import bitmart as BitmartSync
from bitmart.ccxt.async_support.bitmart import bitmart as BitmartAsync
from bitmart.ccxt.pro.bitmart import bitmart as BitmartWs
