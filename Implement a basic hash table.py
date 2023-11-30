# Implement a basic hash table
class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def get(self, key):
        return self.table.get(key, None)

# Example usage:
hash_table = HashTable()
hash_table.insert('one', 1)
hash_table.insert('two', 2)
print("Value for key 'one':", hash_table.get('one'))