from hello_factory import HelloFactory

def main():
    country = input().strip()
    choose = HelloFactory.create_hello(country)
    hello = choose.hello()


if __name__ == "__main__":
    main()
