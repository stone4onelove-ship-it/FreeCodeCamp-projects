class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self,string):
        new_value = 0
        for letter in string:
            new_value += ord(letter)
        return new_value

    def add(self,key,value):
        if self.hash(key) in self.collection:
            self.collection[self.hash(key)][key] = value
        else:
            self.collection[self.hash(key)] = {key : value}

    def remove(self,key):
        if self.hash(key) in self.collection:
            del self.collection[self.hash(key)][key]

    def lookup(self,key):
        if self.hash(key) in self.collection:
            return self.collection[self.hash(key)][key]
        else:
            return None

fuf = HashTable()
print(fuf.hash('hkoi'))
fuf.add('gug', 56)
fuf.add('gufg', 52)
fuf.remove('gug')
print(fuf.collection)
print(fuf.lookup('gufg'))