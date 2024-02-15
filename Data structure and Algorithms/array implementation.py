class Myarray():
    def __init__(self):
        self.data = {}
        self.len = 0
    def get(self,index):
        return self.data[index]
    def push(self,item):
        self.data[self.len] = item
        self.len +=1
    def pop(self):
        lastitem = self.data[self.len-1]
        del self.data[self.len-1]
        self.len-=1
        return lastitem
    def delete(self,index):

        for i in range(index,self.len-1):
            self.data[i] = self.data[i+1]
        self.len-=1
        del self.data[self.len]



arr = Myarray()
arr.push(5)
arr.push(7)
arr.push(9)
arr.push(11)
print(arr.data,arr.len)
print(arr.delete(1))
print(arr.data,arr.len)