
class Subject:
    def __init__(self):
        self._observers = []
        self._store = None
        self._credit = 0
        self._user = None
    
    def register_observer(self, observer):
        "Observerの登録"
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"Observer {observer.__class__.__name__} registered.")
    
    def remove_observer(self, observer):
        "Observerの削除"
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"Observer {observer.__class__.__name__} removed.")
    
    def notify_observers(self):
        "登録されているObserversに通知"
        for observer in self._observers:
            observer.update(self._user, self._store, self._credit)
    
    def set_used_store(self, user, store, amount):
        "クレジットの設定とObserversへの通知"
        self._user = user
        self._store = store
        self._credit = amount
        print(f"Used store: {self._store}, Used amount: {self._credit}.")
        self.notify_observers()

