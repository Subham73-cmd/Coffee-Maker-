Certainly! Here’s a revised README for your Coffee Machine Simulator **without** the resource requirements table or section:

# Coffee Machine Simulator

Welcome to the **Coffee Machine Simulator**! This Python program simulates a coffee machine that serves espresso, latte, and cappuccino. It manages payments, prepares drinks, and tracks profits, all through a user-friendly command-line interface.

## Features

- **Three Coffee Options**: Order espresso, latte, or cappuccino
- **Coin Payment System**: Accepts quarters, dimes, nickels, and pennies
- **Profit Tracking**: Keeps a running total of money earned
- **Maintenance Mode**: Easily turn the machine off
- **Reporting**: Check current profits and ingredient levels
- **Resource Checking**: Notifies if ingredients are insufficient

## How to Use

### Running the Program
1. Save the code as `coffee_machine.py`
2. Run in terminal:
   ```bash
   python coffee_machine.py
   ```

### Commands
- **Order Coffee**: Type `espresso`, `latte`, or `cappuccino`
- **Maintenance**: Type `off` to turn off the machine
- **Report**: Type `report` to see current ingredient levels and profit

### Payment Process
When ordering:
1. Insert coins when prompted:
   - Quarters ($0.25)
   - Dimes ($0.10)
   - Nickels ($0.05)
   - Pennies ($0.01)
2. The machine calculates your total and provides change if needed
3. If payment is sufficient, your drink is prepared!

## Code Structure
Key functions:
- `resource_sufficient()`: Checks if enough resources exist
- `count_coins()`: Calculates total money inserted
- `transaction_status()`: Verifies payment and processes transaction
- `prepare_coffee()`: Deducts resources and prepares drink

## Example Usage
```
What would you like? (Espresso/Latte/Cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 5
How many nickels?: 2
How many pennies?: 4
Here is $0.09 in change
Here is your latte, Enjoy.
```

## Requirements
- Python 3.x

## Maintenance
- Type `off` to turn off the machine
- Type `report` to check current ingredient levels and profit:
  ```
  Water: 100ml
  Milk: 50ml
  Coffee: 40g
  Profit: $5.50
  ```

## Customization
You can modify:
- Ingredient quantities in the `resources` dictionary
- Drink recipes and prices in the `MENU` dictionary

## Author

- [Subham Nayak](https://github.com/Subham73-cmd)


Enjoy your virtual coffee experience! ☕
