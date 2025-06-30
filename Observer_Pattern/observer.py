
class Observer:
    def update(self, credit):
        """
        Observerが更新される際に呼び出されるメソッド。
        """
        raise NotImplementedError("Subclasses must implement this method.")
    
class PhoneDisplay(Observer):
    def __init__(self, name="PhoneDisplay"):
        self.name = name
        self._current_user = None
        self._current_store = None
        self._current_credit = None
    
    def update(self, user, store, credit):
        self._current_user = user
        self._current_store = store
        self._current_credit = credit
        print(f"For {self.name}: used {self._current_credit} at {self._current_store}.")

class PCDisplay(Observer):
    def __init__(self, name="PCDisplay"):
        self.name = name
        self._current_user = None
        self._current_store = None
        self._current_credit = None
    
    def update(self, user, store, credit):
        self._current_user = user
        self._current_store = store
        self._current_credit = credit
        print(f"For {self.name}: used {self._current_credit} at {self._current_store}.")
