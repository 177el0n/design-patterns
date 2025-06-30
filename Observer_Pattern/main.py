from subject import Subject
from observer import Observer, PhoneDisplay, PCDisplay

def main():
    credit_service = Subject()

    phone1 = PhoneDisplay("南波六太")
    phone2 = PhoneDisplay("南波日々人")
    pc1 = PCDisplay("Nanba Mutta")
    pc2 = PCDisplay("Nanba Hibito")

    credit_service.register_observer(phone1)
    credit_service.register_observer(phone2)
    credit_service.register_observer(pc1)
    credit_service.register_observer(pc2)

    print("2025年1月1日の利用額です。")
    credit_service.set_used_store(phone1, "Convenience Store", 1000)
    print("2025年1月2日の利用額です。")
    credit_service.set_used_store(phone1, "Book Store", 500)
    print("2025年1月3日の利用額です。")
    credit_service.set_used_store(pc2, "Supermarket", 2000)

if __name__ == "__main__":
    main()
