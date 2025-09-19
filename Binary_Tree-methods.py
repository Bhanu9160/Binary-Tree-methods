class Node:
    def __init__(self, key=0, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor = self.minValueNode(root.right)
                root.key = successor.key
                root.right = self.delete(root.right, successor.key)
        return root

    def minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")

    def level_order(self, root):
        if root is None:
            return
        queue = [root]
        while queue:
            node = queue.pop(0)
            print(node.key, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

if __name__ == "__main__":
    bst = BST()
    root = None
    for key in [50, 30, 20, 40, 70, 60, 80]:
        root = bst.insert(root, key)

    print("Inorder Traversal: ", end="")
    bst.inorder(root)

    print("\nPreorder Traversal: ", end="")
    bst.preorder(root)

    print("\nPostorder Traversal: ", end="")
    bst.postorder(root)

    print("\nLevel Order Traversal: ", end="")
    bst.level_order(root)

    # Search
    print("\n\nSearch 40:", "Found" if bst.search(root, 40) else "Not found")
    print("Search 100:", "Found" if bst.search(root, 100) else "Not found")

    # Delete nodes
    root = bst.delete(root, 20)
    print("\nAfter deleting 20 (Inorder): ", end="")
    bst.inorder(root)

    root = bst.delete(root, 30)
    print("\nAfter deleting 30 (Inorder): ", end="")
    bst.inorder(root)

    root = bst.delete(root, 50)
    print("\nAfter deleting 50 (Inorder): ", end="")
    bst.inorder(root)
    print()
