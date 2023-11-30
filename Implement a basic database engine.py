# In-memory key-value store
class SimpleDatabase:
    def __init__(self):
        self.data = {}

    def insert(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key, None)

# Usage
db = SimpleDatabase()
db.insert("name", "John")
print("Value for key 'name':", db.get("name"))