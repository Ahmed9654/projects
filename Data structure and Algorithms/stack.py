class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.len = 0
    def push(self,val):
        node = Node(val)
        if(self.len == 0):
            self.top = node
            self.bottom = node

        else:
            temp =self.top
            self.top = Node(val)
            self.top.next = temp
        self.len+=1

    def peak(self):
        print(self.top.val)

    def pop(self):
        if(self.len<2):
            self.top = None
            self.bottom = None
            self.len = 0
        else:
            self.top = self.top.next
            self.len-=1

    def __repr__(self):
        return f'{self.top.val} \n{self.bottom.val} \n{self.len}'

s = Stack()
s.push('google')
s.push('udemy')
s.push('facebook')
s.pop()
s.pop()
print(s)