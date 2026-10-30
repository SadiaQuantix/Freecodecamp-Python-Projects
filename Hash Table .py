class HashTable:
    def __init__(self):
        # storage for hash table
        self.collection = {}
     
    # hash function for converting string into number
    def hash(self, string=str):
        hashed_value = 0
        for char in string:
            hashed_value += ord(char)
        return hashed_value
    
    # add function for storing key-value pair
    def add(self, key, value):
        hashed_key = self.hash(key)

        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}

        self.collection[hashed_key][key] = value

    # remove function for deleting key-value pair
    def remove(self, key):
        hashed_key = self.hash(key)

        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                del self.collection[hashed_key][key]

    # lookup function for retrieving value by key
    def lookup(self, key):
        hashed_key = self.hash(key)

        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                return self.collection[hashed_key][key]

        return None  