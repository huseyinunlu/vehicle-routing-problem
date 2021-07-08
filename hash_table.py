
class HashTable:
    def __init__(self):
        self.table=[]

    def add(self, key, values):
        self.table.append([key, values])
        
    def getValue(self, key):
        result = None
        for obj in self.table:
            if key == obj[0]:
                result = obj[1]
        if result == None:
            print("invalid key ", key)
        else:
            return result
    def getKey(self, value):
        result = None
        for obj in self.table:
            if value == obj[1]:
                result = obj[0]
        if result == None:
            print("invalid key")
            exit(0)
        else:
            return result