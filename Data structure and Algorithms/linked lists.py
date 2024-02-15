class LinkedList:
    def __init__(self, value):
        self.head = {'value': value, 'next': None}
        self.tail = self.head
        self.length = 1

    def append(self,val):
        self.tail['next'] = {'value':val,'next':None}
        self.tail = self.tail['next']

        self.length+=1

    def insert(self,index,val):
        if(index >= self.length):
            self.append(val)

        else:
            node = {'value': val, 'next': None}
            curr = self.head
            for i in range(index-1):
                curr = curr['next']
            node['next'] = curr['next']
            curr['next'] = node
            self.length+=1
    def prepend(self,val):
        node = {'value':val,'next':self.head}
        self.head = node
        self.length+=1

    def __repr__(self):
        return str((f"{self.head} \n {self.tail} \n {self.length}"))

    def remove(self,index):
        if index >= self.length:
            index = self.length-1
            curr1 = self.head
            for i in range(self.length-2):
                curr1 = curr1['next']
            self.tail = curr1
        curr = self.head
        for i in range(index-1):
            curr = curr['next']
        curr['next'] = curr['next']['next']
        self.length-=1

    def reverse(self):
        curr = self.head

        prev = None
        while curr:
            next = curr['next']
            curr['next'] = prev
            prev = curr
            curr = next

        self.tail = self.head
        self.head = prev

l = LinkedList(5)
l.append(10)
l.append(20)
l.prepend(9)
l.insert(2,99)
l.insert(100,100)
l.remove(20000)
l.append(50)
l.reverse()
print(l)

