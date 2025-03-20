# bitmart-python
Python SDK (sync and async) for Bitmart with Rest and WS capabilities.

You can check Bitmart's docs here: [Docs](https://ccxt.com)


You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/bitmart)

*This package derives from CCXT and allows you to call pretty much every endpoint by either using the unified CCXT API or calling the endpoints directly*

## Installation

```
pip install bitmart
```

## Usage

### Async

```Python
from bitmart import BitmartAsync

async def main():
    instance = BitmartAsync({})
    order = await instance.create_order(__EXAMPLE_SYMBOL__, "limit", "buy", 1, 100000)
```

### Sync

```Python
from bitmart import BitmartSync

def main():
    instance = BitmartSync({})
    order =  instance.create_order(__EXAMPLE_SYMBOL__, "limit", "buy", 1, 100000)
```

### Websockets

```Python
from bitmart import BitmartWs

async def main():
    instance = BitmartWs({})
    while True:
        orders = await instance.watch_orders(__EXAMPLE_SYMBOL__)
```

