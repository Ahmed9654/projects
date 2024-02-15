
class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        curr = Node(val)
        if not self.root:
            self.root = curr
        else:
            node = self.root
            while True:
                if node.val > val:
                    if node.left:
                        node = node.left
                    else:
                        node.left = curr
                        break
                elif node.val < val:
                    if node.right:
                        node = node.right
                    else:
                        node.right = curr
                        break

    def lookup(self,val):
        node = self.root
        while node:
            if node.val > val:
                node = node.left
            elif node.val < val:
                node = node.right
            else:
                return node.val
        return "doesn't exist"

    # remove needs more optimization to control all cases
    def remove(self,val):
        node = self.root
        temp = None
        while True:
            if node.val > val:
                node = node.left
            elif node.val < val:
                node = node.right
            elif node.val == val:
                temp = node
                break
            else:
                return 'not found'
        node = node.right
        while node.left:
            node = node.left
        temp.val = node.val
        node.val = None

    def BeadthFisrtSearch(self):
        list = []
        queue = []
        queue.append(self.root)
        while len(queue) != 0:
            curr = queue.pop(0)
            list.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        print(list)

    def RecurBeadthFisrtSearch(self,queue = [],list = []):
        if not queue:
            print(list)
        else:
            curr = queue.pop(0)
            list.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            return self.RecurBeadthFisrtSearch(queue,list)
    def DFSinOrder(self,root,list = []):
        if root.left:
            self.DFSinOrder(root.left,list)
        list.append(root.val)
        if root.right:
            self.DFSinOrder(root.right,list)
        return list

    def DFSPreOrder(self,root,list = []):
        list.append(root.val)
        if root.left:
            self.DFSPreOrder(root.left,list)

        if root.right:
            self.DFSPreOrder(root.right,list)
        return list
    # preorder is useful when recreating a tree
    def DFSPostOrder(self,root,list = []):

        if root.left:
            self.DFSPostOrder(root.left,list)

        if root.right:
            self.DFSPostOrder(root.right,list)
        list.append(root.val)
        return list

b = BinarySearchTree()
b.insert(9)
b.insert(4)
b.insert(20)
b.insert(1)
b.insert(6)
b.insert(15)
b.insert(170)
b.BeadthFisrtSearch()
b.RecurBeadthFisrtSearch([b.root])
print(b.DFSinOrder(b.root))
print(b.DFSPreOrder(b.root))
print(b.DFSPostOrder(b.root))