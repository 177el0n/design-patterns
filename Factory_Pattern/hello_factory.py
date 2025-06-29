from hello_world import British, France, Italia

class HelloFactory:
    @staticmethod
    def create_hello(country):
        if country == "British":
            return British()
        elif country == "France":
            return France()
        elif country == "Italia":
            return Italia()
        else:
            print(f"{country}のデータはありません。")
