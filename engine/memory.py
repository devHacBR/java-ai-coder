# engine/memory.py

class SessionMemory:
    def __init__(self):
        self.history = []

    def add_entry(self, user_input, parsed_data):
        self.history.append({
            "user_input": user_input,
            "parsed_data": parsed_data
        })

    def get_history(self):
        return self.history

    def last_intent(self):
        if self.history:
            return self.history[-1]["parsed_data"].get("intent")
        return None

    def last_user_input(self):
        if self.history:
            return self.history[-1]["user_input"]
        return None
