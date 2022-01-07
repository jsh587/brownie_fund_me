from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    deploy_mocks,
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()
    print(account)
    # pass the price feed address to our fundMe contract
    # if we are on a persistent network like rinkeby, use the associated address
    # otherwise, deploy mocks.
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get(
            "verify"
        ),  # ,get() make your lives a little bit easier if we forget to add verify in config file. preventing index error..
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
