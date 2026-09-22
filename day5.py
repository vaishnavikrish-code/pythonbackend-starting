class treenode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None



root = treenode(1)
root.left=treenode(2)
root.right=treenode(3)
root.left.left=treenode(4)
root.left.right=treenode(5)

print(f"{root.val}")
print(f"{root.left.val}")
print(f"{root.right.val}")
print(f"{root.left.left.val}")
print(f"{root.left.right.val}")

#traversal:

def inorder(node):
    if node is None:
        return[]
    result=[]
    result+=inorder(node.left)
    result.append(node.val)
    result+=inorder(node.right)

    return result
result = inorder(root)
print(f"{result}")

def preorder(node):
    if node is None:
        return[]
    result=[]
    result.append(node.val)
    result+=preorder(node.left)
    result+=preorder(node.right)

    return result

result=preorder(root)
print(f"{result}")


def postorder(node):
    if node is None:
        return[]
    result=[]
    result+=postorder(node.left)
    result+=postorder(node.right)
    result.append(node.val)

    return result

result=postorder(root)
print(f"{result}")

from collections import deque
def levelorder(root):
    if not root:
        return []
    result = []

    queue= deque ([root])
    while queue:
        node=queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
result=levelorder(root)
print(f"{result}")




class treenode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class bts:
    def __init__(self):
        self.root = None
    def insert(self,val):
        if self.root is None:
            self.root = treenode(val)
        else:
            self._insert_recursive(self.root,val)
    def _insert_recursive(self,node,val):
        if val < node.val:
            if node.left is None:
                node.left= treenode(val)
            else:
                self._insert_recursive(node.left,val)
        else:
            if node.right is None:
                node.right=treenode(val)
            else:
                self._insert_recursive(node.right,val)
    def search(self,val):
        return self._search_recursive(self.root,val)
    def _search_recusive(self,node,val):
        if node is None:
            return False
        if val == node.val:
            return True
        elif val < node.val:
            return self._search_recusive(node.left,val)
        else:
            return self._search_recusive(node.right,val)
    def get_inorder(self):
        return inorder(self.root)

BST = bts()
values = [5,3,8,1,4,9]
print(f"{values}")
for val in values:
    BST.insertr(val)
print(f"{BST.get_inorder()}")
print(f"{BST.search(4)}")
print(f"{BST.search(99)}")
print()
    
    
    
    

        

















    






