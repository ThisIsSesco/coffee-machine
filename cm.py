class CoffeeMachine:
    water = 400
    milk = 540
    coffee_bean = 120
    cups = 9
    money = 550

    def __init__(self, action):
        self.action = action

    def buy_coffee(self, coffee_type):
        if coffee_type.get('water') > CoffeeMachine.water:
            print('Sorry, not enough water!')
        elif coffee_type.get('milk') > CoffeeMachine.milk:
            print('Sorry, not enough milk!')
        elif coffee_type.get('coffee_bean') > CoffeeMachine.coffee_bean:
            print('Sorry, not enough beans!')
        elif coffee_type.get('cups') > CoffeeMachine.cups:
            print('Sorry, not enough cups!')
        else:
            print('I have enough resources, making you a coffee!')
            CoffeeMachine.water -= coffee_type.get('water')
            CoffeeMachine.milk -= coffee_type.get('milk')
            CoffeeMachine.coffee_bean -= coffee_type.get('coffee_bean')
            CoffeeMachine.cups -= coffee_type.get('cups')
            CoffeeMachine.money += coffee_type.get('money')

    def fill_coffee(self, add_water, add_milk, add_beans, add_cups):
        CoffeeMachine.water += add_water
        CoffeeMachine.milk += add_milk
        CoffeeMachine.coffee_bean += add_beans
        CoffeeMachine.cups += add_cups

    def take_money(self):
        print('I gave you $' + str(CoffeeMachine.money))
        CoffeeMachine.money = 0

    def remainder(self):
        print('The coffee machine has:')
        print(str(CoffeeMachine.water) + ' of water')
        print(str(CoffeeMachine.milk) + ' of milk')
        print(str(CoffeeMachine.coffee_bean) + ' of coffee beans')
        print(str(CoffeeMachine.cups) + ' of disposable cups')
        if CoffeeMachine.money > 0:
            print('$' + str(CoffeeMachine.money) + ' of money')
        else:
            print(str(CoffeeMachine.money) + ' of money')


while True:
    action = input('Write action (buy, fill, take, remaining, exit):\n')
    coffee = CoffeeMachine(action)
    espresso = {
        'water': 250,
        'coffee_bean': 16,
        'milk': 0,
        'cups': 1,
        'money': 4
    }
    latte = {
        'water': 350,
        'coffee_bean': 20,
        'milk': 75,
        'cups': 1,
        'money': 7
    }
    cappuccino = {
        'water': 200,
        'coffee_bean': 12,
        'milk': 100,
        'cups': 1,
        'money': 6
    }
    if action == 'buy':
        print()
        user_input = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:'
                           '\n')
        if user_input == '1':
            coffee.buy_coffee(espresso)
        elif user_input == '2':
            coffee.buy_coffee(latte)
        elif user_input == '3':
            coffee.buy_coffee(cappuccino)
        elif user_input == 'back':
            pass
        else:
            print('Invalid')
        print()
    elif action == 'fill':
        print()
        add_water = int(input('Write how many ml of water do you want to add:\n'))
        add_milk = int(input('Write how many ml of milk do you want to add:\n'))
        add_coffee_beans = int(input('Write how many grams of coffee beans do you want to add:\n'))
        add_cups = int(input('Write how many disposable cups of coffee do you want to add:\n'))
        coffee.fill_coffee(add_water, add_milk, add_coffee_beans, add_cups)
        print()
    elif action == 'take':
        print()
        coffee.take_money()
        print()
    elif action == 'remaining':
        print()
        coffee.remainder()
        print()
    elif action == 'exit':
        exit()
