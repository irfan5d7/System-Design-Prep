from enum import Enum
from typing import List, Tuple

class Item(Enum):
    COKE = ("Coke", 25)
    PEPSI = ("Pepsi", 35)
    SODA = ("Soda", 45)

    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

class Coin(Enum):
    PENNY = 1
    NICKEL = 5
    DIME = 10
    QUARTER = 25

class NotFullPaidException(Exception):
    pass

class NotSufficientChangeException(Exception):
    pass

class SoldOutException(Exception):
    pass

class State:
    def select_item(self, vending_machine: 'VendingMachine', selected_item: Item) -> None:
        pass

    def insert_coin(self, vending_machine: 'VendingMachine', coin: Coin) -> None:
        pass

    def collect_item_and_change(self, vending_machine: 'VendingMachine') -> Tuple[Item, List[Coin]]:
        pass

    def refund(self, vending_machine: 'VendingMachine') -> List[Coin]:
        pass

class Idle(State):
    def select_item(self, vending_machine: 'VendingMachine', selected_item: Item) -> None:
        if vending_machine.inventory.has_item(selected_item):
            vending_machine.current_item = selected_item
            vending_machine.set_state(SelectingItem())
        else:
            raise SoldOutException("Item is sold out")

class SelectingItem(State):
    def insert_coin(self, vending_machine: 'VendingMachine', coin: Coin) -> None:
        vending_machine.current_balance += coin.value

    def collect_item_and_change(self, vending_machine: 'VendingMachine') -> Tuple[Item, List[Coin]]:
        if vending_machine.current_balance >= vending_machine.current_item.price:
            change = vending_machine.inventory.deduct_change(vending_machine.current_balance - vending_machine.current_item.price)
            item = vending_machine.current_item
            vending_machine.inventory.deduct_item(item)
            vending_machine.current_item = None
            vending_machine.current_balance = 0
            vending_machine.set_state(Idle())
            return item, change
        else:
            raise NotFullPaidException("Amount not fully paid")

    def refund(self, vending_machine: 'VendingMachine') -> List[Coin]:
        change = vending_machine.inventory.deduct_change(vending_machine.current_balance)
        vending_machine.current_balance = 0
        vending_machine.current_item = None
        vending_machine.set_state(Idle())
        return change

class ProcessingTransaction(State):
    def select_item(self, vending_machine: 'VendingMachine', selected_item: Item) -> None:
        raise NotFullPaidException("Transaction in progress. Please wait.")

    def insert_coin(self, vending_machine: 'VendingMachine', coin: Coin) -> None:
        raise NotFullPaidException("Transaction in progress. Please wait.")

    def collect_item_and_change(self, vending_machine: 'VendingMachine') -> Tuple[Item, List[Coin]]:
        raise NotFullPaidException("Transaction in progress. Please wait.")

    def refund(self, vending_machine: 'VendingMachine') -> List[Coin]:
        change = vending_machine.inventory.deduct_change(vending_machine.current_balance)
        vending_machine.current_balance = 0
        vending_machine.current_item = None
        vending_machine.set_state(Idle())
        return change

class Inventory:
    def __init__(self):
        self.items = {item: 5 for item in Item}
        self.coins = {coin: 5 for coin in Coin}

    def has_item(self, item: Item) -> bool:
        return self.items.get(item, 0) > 0

    def deduct_item(self, item: Item) -> None:
        if self.has_item(item):
            self.items[item] -= 1
        else:
            raise SoldOutException("Item is sold out")

    def add_item(self, item: Item) -> None:
        self.items[item] += 1

    def has_change(self, amount: int) -> bool:
        return amount <= sum(coin.value * count for coin, count in self.coins.items())

    def deduct_change(self, amount: int) -> List[Coin]:
        change = []
        remaining = amount
        for coin in sorted(Coin, key=lambda x: x.value, reverse=True):
            while remaining >= coin.value and self.coins[coin] > 0:
                change.append(coin)
                remaining -= coin.value
                self.coins[coin] -= 1
        if remaining != 0:
            raise NotSufficientChangeException("Not sufficient change available")
        return change

    def add_change(self, coins: List[Coin]) -> None:
        for coin in coins:
            self.coins[coin] += 1

class VendingMachine:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.inventory = Inventory()
            cls._instance.current_balance = 0
            cls._instance.current_item = None
            cls._instance.state = Idle()
        return cls._instance

    def set_state(self, state: State) -> None:
        self.state = state

    def select_item(self, selected_item: Item) -> None:
        self.state.select_item(self, selected_item)

    def insert_coin(self, coin: Coin) -> None:
        self.state.insert_coin(self, coin)

    def collect_item_and_change(self) -> Tuple[Item, List[Coin]]:
        return self.state.collect_item_and_change(self)

    def refund(self) -> List[Coin]:
        return self.state.refund(self)

    def reset(self) -> None:
        self.inventory = Inventory()
        self.current_balance = 0
        self.current_item = None
        self.state = Idle()

# Test the Vending Machine
if __name__ == "__main__":
    vending_machine = VendingMachine()

    # Test case 1: Selecting and purchasing an item with exact change
    print("Test case 1: Selecting and purchasing an item with exact change")
    vending_machine.select_item(Item.COKE)
    vending_machine.insert_coin(Coin.QUARTER)
    vending_machine.insert_coin(Coin.QUARTER)
    vending_machine.insert_coin(Coin.QUARTER)
    vending_machine.insert_coin(Coin.QUARTER)
    item, change = vending_machine.collect_item_and_change()
    print("Purchased item:", item.name)
    print("Change returned:", [coin.name for coin in change])

    # Test case 2: Selecting an item without enough balance
    print("\nTest case 2: Selecting an item without enough balance")
    vending_machine.select_item(Item.PEPSI)
    try:
        vending_machine.collect_item_and_change()
    except NotFullPaidException as e:
        print(e)

    # Test case 3: Refunding the remaining balance
    print("\nTest case 3: Refunding the remaining balance")
    refund_coins = vending_machine.refund()
    print("Refunded coins:", [coin.name for coin in refund_coins])
