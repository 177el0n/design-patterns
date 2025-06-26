from money_strategy import MoneyStrategy



class Application:

    def __init__(self, money: MoneyStrategy):
        self.money = money

    def currency(self, amount):
        return self.money.how_mach(amount)
