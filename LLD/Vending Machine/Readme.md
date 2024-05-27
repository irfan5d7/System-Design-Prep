# Problem Statement

Design a Vending Machine system that simulates the functionality of a real-world vending machine. The system should allow users to select products, insert coins, receive products, receive change if applicable, and refund their money if they change their mind.

# Functional Requirements

1. **Accept Coins**:
   - The vending machine should accept coins of denominations: 1, 5, 10, and 25 cents.

2. **Select Product**:
   - Users should be able to select products available in the vending machine, including Coke, Pepsi, and Soda.

3. **Refund**:
   - Users should have the option to cancel their request and receive a refund if they have inserted coins without completing a purchase.

4. **Dispense Product**:
   - Upon successful selection and payment, the vending machine should dispense the selected product.

5. **Dispense Change**:
   - If the user inserts more money than required, the vending machine should dispense the selected product along with any remaining change.

6. **Reset**:
   - The vending machine supplier should have the capability to reset the vending machine to its initial state, including restocking items and coins.

# Classes and Explanation

1. **Item** (Enum):
   - Represents the items available in the vending machine, each with a name and price.

2. **Coin** (Enum):
   - Represents the denominations of coins accepted by the vending machine.

3. **NotFullPaidException** (Exception):
   - Exception raised when the user has not paid the full amount for the selected product.

4. **NotSufficientChangeException** (Exception):
   - Exception raised when the vending machine does not have sufficient change to return to the user.

5. **SoldOutException** (Exception):
   - Exception raised when the selected product is sold out.

6. **State** (Abstract Class):
   - Defines the interface for various states of the vending machine.

7. **Idle**, **SelectingItem**, **ProcessingTransaction** (Concrete States):
   - Represent different states of the vending machine such as idle, selecting an item, and processing a transaction, respectively.

8. **Inventory**:
   - Manages the inventory of items and coins in the vending machine.

9. **VendingMachine** (Singleton):
   - Represents the vending machine itself and orchestrates the interactions between different states and the inventory.

# Design Pattern Used: State Pattern

The State Pattern is used to represent the varying behavior of the vending machine based on its internal state. It allows the vending machine to change its behavior (e.g., accepting coins, dispensing products) dynamically based on its state (e.g., idle, selecting item, processing transaction). By encapsulating each state in a separate class and allowing the vending machine to switch between these states, the State Pattern simplifies the management of complex state-dependent behaviors and promotes better code organization and extensibility.
