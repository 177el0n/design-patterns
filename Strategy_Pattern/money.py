from money_strategy import MoneyStrategy

class British(MoneyStrategy):

    def how_mach(amount):
        # GBP:イギリスポンド
        GBP = amount * 0.00507
        return GBP


class France(MoneyStrategy):

    def how_mach(amount):
        # EUR:ユーロ
        EUR = amount * 0.00595
        return EUR


class America(MoneyStrategy):

    def how_mach(amount):
        # USD:アメリカドル
        USD = amount * 0.0069
        return USD
