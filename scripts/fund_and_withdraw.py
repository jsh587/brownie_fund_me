from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund(
        {"from": account, "value": entrance_fee}
    )  # any low level transaction data that we want to send with our transaction and function calls will added in this little bracket piece


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
