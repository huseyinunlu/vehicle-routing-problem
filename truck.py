class truck:
    def __init__(self):
        self.packagesKeys = []
        self.locations=[]
        self.leavingTime = ''
        self.loadedCargo=0
    def addCargo(self,key):
        self.packagesKeys.append(key)
        self.locations.append(get_hash_table().getValue(key)[0:2])
        self.loadedCargo +=1
        get_hash_table().getValue(key)[8] = "loaded"