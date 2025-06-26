from application import Application
from money import British, France, America


def main():
    """
    日本円を各国の通貨に変換
    """
    amount = int(input())
    application = Application(British)
    translate = application.currency(amount)
    print(translate)


if __name__ == main():
    main()
