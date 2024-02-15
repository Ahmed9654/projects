class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.len = 0

    def enqueue(self,val):
        node = Node(val)
        if(self.len == 0):
            self.first = node
            self.last = node
        else:
            self.last.next = Node(val)
            self.last = self.last.next
        self.len+=1
    def peak(self):
        print(self.first)

    def dequeue(self):
        res = self.first
        self.first = self.first.next
        print(res.val)
        self.len-=1
    def __repr__(self):
        return f"{self.first.val}\n{self.last.val}\n{self.len}"
q = Queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.dequeue()
print(q)