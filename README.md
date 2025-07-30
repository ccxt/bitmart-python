# bitmart-python
Python SDK (sync and async) for Bitmart cryptocurrency exchange with Rest and WS capabilities.

- You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/bitmart)
- You can check Bitmart's docs here: [Docs](https://www.google.com/search?q=google+bitmart+cryptocurrency+exchange+api+docs)
- Github repo: https://github.com/ccxt/bitmart-python
- Pypi package: https://pypi.org/project/bitmart


## Installation

```
pip install bitmart
```

## Usage

### Sync

```Python
from bitmart import BitmartSync

def main():
    instance = BitmartSync({})
    ob =  instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = instance.fetch_balance()
    # order = instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

main()
```

### Async

```Python
import sys
import asyncio
from bitmart import BitmartAsync

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = BitmartAsync({})
    ob =  await instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = await instance.fetch_balance()
    # order = await instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```



### Websockets

```Python
import sys
from bitmart import BitmartWs

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = BitmartWs({})
    while True:
        ob = await instance.watch_order_book("BTC/USDC")
        print(ob)
        # orders = await instance.watch_orders("BTC/USDC")

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```





#### Raw call

You can also construct custom requests to available "implicit" endpoints

```Python
        request = {
            'type': 'candleSnapshot',
            'req': {
                'coin': coin,
                'interval': tf,
                'startTime': since,
                'endTime': until,
            },
        }
        response = await instance.public_post_info(request)
```


## Available methods

### REST Unified

- `create_market_buy_order_with_cost(self, symbol: str, cost: float, params={})`
- `create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_orders(self, orders: List[OrderRequest], params={})`
- `create_spot_order_request(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_swap_order_request(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `fetch_balance(self, params={})`
- `fetch_borrow_interest(self, code: Str = None, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_canceled_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_closed_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_contract_markets(self, params={})`
- `fetch_currencies(self, params={})`
- `fetch_deposit_address(self, code: str, params={})`
- `fetch_deposit_withdraw_fee(self, code: str, params={})`
- `fetch_deposit(self, id: str, code: Str = None, params={})`
- `fetch_deposits(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_rate_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_rate(self, symbol: str, params={})`
- `fetch_isolated_borrow_rate(self, symbol: str, params={})`
- `fetch_isolated_borrow_rates(self, params={})`
- `fetch_ledger(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_markets(self, params={})`
- `fetch_my_liquidations(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_ohlcv(self, symbol: str, timeframe='1m', since: Int = None, limit: Int = None, params={})`
- `fetch_open_interest(self, symbol: str, params={})`
- `fetch_open_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_order_book(self, symbol: str, limit: Int = None, params={})`
- `fetch_order_trades(self, id: str, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_order(self, id: str, symbol: Str = None, params={})`
- `fetch_orders_by_status(self, status, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_position_mode(self, symbol: Str = None, params={})`
- `fetch_position(self, symbol: str, params={})`
- `fetch_positions(self, symbols: Strings = None, params={})`
- `fetch_spot_markets(self, params={})`
- `fetch_status(self, params={})`
- `fetch_ticker(self, symbol: str, params={})`
- `fetch_tickers(self, symbols: Strings = None, params={})`
- `fetch_time(self, params={})`
- `fetch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `fetch_trading_fee(self, symbol: str, params={})`
- `fetch_transaction_fee(self, code: str, params={})`
- `fetch_transactions_by_type(self, type, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_transactions_request(self, flowType: Int = None, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_transfers(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_withdraw_addresses(self, code: str, note=None, networkCode=None, params={})`
- `fetch_withdrawal(self, id: str, code: Str = None, params={})`
- `fetch_withdrawals(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `borrow_isolated_margin(self, symbol: str, code: str, amount: float, params={})`
- `cancel_all_orders(self, symbol: Str = None, params={})`
- `cancel_order(self, id: str, symbol: Str = None, params={})`
- `cancel_orders(self, ids: List[str], symbol: Str = None, params={})`
- `custom_parse_balance(self, response, marketType)`
- `describe(self)`
- `edit_order(self, id: str, symbol: str, type: OrderType, side: OrderSide, amount: Num = None, price: Num = None, params={})`
- `get_currency_id_from_code_and_network(self, currencyCode: Str, networkCode: Str)`
- `nonce(self)`
- `repay_isolated_margin(self, symbol: str, code: str, amount, params={})`
- `set_leverage(self, leverage: Int, symbol: Str = None, params={})`
- `set_position_mode(self, hedged: bool, symbol: Str = None, params={})`
- `transfer(self, code: str, amount: float, fromAccount: str, toAccount: str, params={})`
- `withdraw(self, code: str, amount: float, address: str, tag=None, params={})`

### REST Raw

- `public_get_system_time(request)`
- `public_get_system_service(request)`
- `public_get_spot_v1_currencies(request)`
- `public_get_spot_v1_symbols(request)`
- `public_get_spot_v1_symbols_details(request)`
- `public_get_spot_quotation_v3_tickers(request)`
- `public_get_spot_quotation_v3_ticker(request)`
- `public_get_spot_quotation_v3_lite_klines(request)`
- `public_get_spot_quotation_v3_klines(request)`
- `public_get_spot_quotation_v3_books(request)`
- `public_get_spot_quotation_v3_trades(request)`
- `public_get_spot_v1_ticker(request)`
- `public_get_spot_v2_ticker(request)`
- `public_get_spot_v1_ticker_detail(request)`
- `public_get_spot_v1_steps(request)`
- `public_get_spot_v1_symbols_kline(request)`
- `public_get_spot_v1_symbols_book(request)`
- `public_get_spot_v1_symbols_trades(request)`
- `public_get_contract_v1_tickers(request)`
- `public_get_contract_public_details(request)`
- `public_get_contract_public_depth(request)`
- `public_get_contract_public_open_interest(request)`
- `public_get_contract_public_funding_rate(request)`
- `public_get_contract_public_funding_rate_history(request)`
- `public_get_contract_public_kline(request)`
- `public_get_account_v1_currencies(request)`
- `public_get_contract_public_markprice_kline(request)`
- `private_get_account_sub_account_v1_transfer_list(request)`
- `private_get_account_sub_account_v1_transfer_history(request)`
- `private_get_account_sub_account_main_v1_wallet(request)`
- `private_get_account_sub_account_main_v1_subaccount_list(request)`
- `private_get_account_contract_sub_account_main_v1_wallet(request)`
- `private_get_account_contract_sub_account_main_v1_transfer_list(request)`
- `private_get_account_contract_sub_account_v1_transfer_history(request)`
- `private_get_account_v1_wallet(request)`
- `private_get_account_v1_currencies(request)`
- `private_get_spot_v1_wallet(request)`
- `private_get_account_v1_deposit_address(request)`
- `private_get_account_v1_withdraw_charge(request)`
- `private_get_account_v2_deposit_withdraw_history(request)`
- `private_get_account_v1_deposit_withdraw_detail(request)`
- `private_get_account_v1_withdraw_address_list(request)`
- `private_get_spot_v1_order_detail(request)`
- `private_get_spot_v2_orders(request)`
- `private_get_spot_v1_trades(request)`
- `private_get_spot_v2_trades(request)`
- `private_get_spot_v3_orders(request)`
- `private_get_spot_v2_order_detail(request)`
- `private_get_spot_v1_margin_isolated_borrow_record(request)`
- `private_get_spot_v1_margin_isolated_repay_record(request)`
- `private_get_spot_v1_margin_isolated_pairs(request)`
- `private_get_spot_v1_margin_isolated_account(request)`
- `private_get_spot_v1_trade_fee(request)`
- `private_get_spot_v1_user_fee(request)`
- `private_get_spot_v1_broker_rebate(request)`
- `private_get_contract_private_assets_detail(request)`
- `private_get_contract_private_order(request)`
- `private_get_contract_private_order_history(request)`
- `private_get_contract_private_position(request)`
- `private_get_contract_private_position_v2(request)`
- `private_get_contract_private_get_open_orders(request)`
- `private_get_contract_private_current_plan_order(request)`
- `private_get_contract_private_trades(request)`
- `private_get_contract_private_position_risk(request)`
- `private_get_contract_private_affilate_rebate_list(request)`
- `private_get_contract_private_affilate_trade_list(request)`
- `private_get_contract_private_transaction_history(request)`
- `private_get_contract_private_get_position_mode(request)`
- `private_post_account_sub_account_main_v1_sub_to_main(request)`
- `private_post_account_sub_account_sub_v1_sub_to_main(request)`
- `private_post_account_sub_account_main_v1_main_to_sub(request)`
- `private_post_account_sub_account_sub_v1_sub_to_sub(request)`
- `private_post_account_sub_account_main_v1_sub_to_sub(request)`
- `private_post_account_contract_sub_account_main_v1_sub_to_main(request)`
- `private_post_account_contract_sub_account_main_v1_main_to_sub(request)`
- `private_post_account_contract_sub_account_sub_v1_sub_to_main(request)`
- `private_post_account_v1_withdraw_apply(request)`
- `private_post_spot_v1_submit_order(request)`
- `private_post_spot_v1_batch_orders(request)`
- `private_post_spot_v2_cancel_order(request)`
- `private_post_spot_v1_cancel_orders(request)`
- `private_post_spot_v4_query_order(request)`
- `private_post_spot_v4_query_client_order(request)`
- `private_post_spot_v4_query_open_orders(request)`
- `private_post_spot_v4_query_history_orders(request)`
- `private_post_spot_v4_query_trades(request)`
- `private_post_spot_v4_query_order_trades(request)`
- `private_post_spot_v4_cancel_orders(request)`
- `private_post_spot_v4_cancel_all(request)`
- `private_post_spot_v4_batch_orders(request)`
- `private_post_spot_v3_cancel_order(request)`
- `private_post_spot_v2_batch_orders(request)`
- `private_post_spot_v2_submit_order(request)`
- `private_post_spot_v1_margin_submit_order(request)`
- `private_post_spot_v1_margin_isolated_borrow(request)`
- `private_post_spot_v1_margin_isolated_repay(request)`
- `private_post_spot_v1_margin_isolated_transfer(request)`
- `private_post_account_v1_transfer_contract_list(request)`
- `private_post_account_v1_transfer_contract(request)`
- `private_post_contract_private_submit_order(request)`
- `private_post_contract_private_cancel_order(request)`
- `private_post_contract_private_cancel_orders(request)`
- `private_post_contract_private_submit_plan_order(request)`
- `private_post_contract_private_cancel_plan_order(request)`
- `private_post_contract_private_submit_leverage(request)`
- `private_post_contract_private_submit_tp_sl_order(request)`
- `private_post_contract_private_modify_plan_order(request)`
- `private_post_contract_private_modify_preset_plan_order(request)`
- `private_post_contract_private_modify_limit_order(request)`
- `private_post_contract_private_modify_tp_sl_order(request)`
- `private_post_contract_private_submit_trail_order(request)`
- `private_post_contract_private_cancel_trail_order(request)`
- `private_post_contract_private_set_position_mode(request)`

### WS Unified

- `describe(self)`
- `subscribe(self, channel, symbol, type, params={})`
- `subscribe_multiple(self, channel: str, type: str, symbols: Strings = None, params={})`
- `watch_balance(self, params={})`
- `set_balance_cache(self, client: Client, type, subscribeHash)`
- `load_balance_snapshot(self, client, messageHash, type)`
- `watch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `watch_trades_for_symbols(self, symbols: List[str], since: Int = None, limit: Int = None, params={})`
- `get_params_for_multiple_sub(self, methodName: str, symbols: List[str], limit: Int = None, params={})`
- `watch_ticker(self, symbol: str, params={})`
- `watch_tickers(self, symbols: Strings = None, params={})`
- `watch_bids_asks(self, symbols: Strings = None, params={})`
- `watch_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `watch_positions(self, symbols: Strings = None, since: Int = None, limit: Int = None, params={})`
- `watch_ohlcv(self, symbol: str, timeframe='1m', since: Int = None, limit: Int = None, params={})`
- `watch_order_book(self, symbol: str, limit: Int = None, params={})`
- `watch_order_book_for_symbols(self, symbols: List[str], limit: Int = None, params={})`
- `authenticate(self, type, params={})`

## Contribution
- Give us a star :star:
- Fork and Clone! Awesome
- Select existing issues or create a new issue.