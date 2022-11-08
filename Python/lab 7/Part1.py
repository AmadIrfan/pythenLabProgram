#created class keyNodes
class KeyNode:
    value=0
    key=''
    def __init__(self,key,value):
        self.value=value
        self.key=key

class MyHashTable:
    arr=[]
    size=0
    KeysOccupied=0
    def __init__(self,size,KeysOccupied):
        self.arr=[None]*size
        self.size=size
        self.KeysOccupied=KeysOccupied 
    
    def Constructor(hsize):
        arr=[]
    
    def GetNumberofKeys(self):
        return self.keysOccuide
    
    def GetHashTableSize(self):
        return self.size
    
    def UpdateKey(key,value):
        print(key)
    
    def SearchKey(key):
        print(key)
    
    def Rehash():
        print()
    def HashFunction(self,KeyNode):
        sum=0
        for i in (KeyNode.key):
            sum+=ord(i)
            sum=sum % self.size
        return sum

print(MyHashTable.HashFunction('amad'))