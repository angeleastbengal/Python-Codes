
class Node:

    """
    A constructor is used to initialize the data, left_add, and right_add variables. The variable data
    stores the data item, whereas the left_add and the right_add variable stores the address of the left and right child.
    """
    def __init__(self,data,left_add=None,right_add=None):
        self.data=data
        self.left_add=left_add
        self.right_add=right_add

    """
    insert() is used to add value to a binary tree. Remember the rules discussed above:
    1. The left subtree of a node contains values smaller than the root
    2. The right subtree of a node contains values larger than the root
    3. The left and right subtree each must also be a binary search tree without any duplicate values
    """
    def insert_data(self,item):
        #--Decision trees can't have duplicates, hence the condition is checked before an item is inserted
        if self.data==item:
            return False

        elif item<self.data: #--if data to be inserted is smaller than the data at root node
            if self.left_add: #--Check if the left child exists
                self.left_add.insert_data(item)
            else:
                self.left_add=Node(item) #--Else add a node and store the object address in left_add
                return True
        #--Similar methodology discussed above is followed when item is greater than the item in the root node
        else:
            if self.right_add:
                self.right_add.insert_data(item)
            else:
                self.right_add = Node(item)
                return True
    """
    find() is used to search for a particular value in the tree. It follows the similar structure used for inserting an element.
    Remember binary tree uses a node based approach that has three components to it.
    1. Data item
    2. left address to store object address of the left child
    3. right address to store the object address of the right child
    """
    def find_data(self,item):

        if self.data==item:
            return True
        elif item<self.data:
            if self.left_add:
                self.left_add.find_data(item)
            else:
                return False
        else:
            if self.right_add:
                self.right_add.find_data(item)
            else:
                return False

    def preorderTraversal(self, list_item):
        #--Traverses the binary tree
        #--first element is the element from the root
        list_item.append(self.data)

        #--If left_add is present then it adds element from the left child to the list
        #--Once all items from the left of the tree are added, it moves to the right child

        if self.left_add:
            self.left_add.preorderTraversal(list_item)
        if self.right_add:
            self.right_add.preorderTraversal(list_item)
        return list_item

    def inorderTraversal(self,list_item):

        if self.left_add:
            self.left_add.inorderTraversal(list_item)

        list_item.append(self.data)

        if self.right_add:
            self.right_add.inorderTraversal(list_item)

        return list_item

    def postorderTraversal(self,list_item):

        if self.left_add:
            self.left_add.inorderTraversal(list_item)
        if self.right_add:
            self.right_add.inorderTraversal(list_item)

        list_item.append(self.data)

        return list_item


"""
"""

class BinarySearchTree(object):

    def __init__(self):
        self.root=None


    def insert(self, d):

        if self.root:
            return self.root.insert_data(d)
        else:
            self.root = Node(d)
            return True

    def find(self, d):

        if self.root:
            return self.root.find_data(d)
        else:
            return False

    def __str__(self):
        # return list of data elements resulting from preorder tree traversal
        if self.root:
            return ",".join(map(str, self.root.postorderTraversal([])))
        else:
            return "the tree is empty"


if __name__ == "__main__":
    test_tree = BinarySearchTree()  # initialize the binary search tree
    # add elements to the tree
    items = [3, 5, 4, 7, 6, 1]
    for item in items:
        test_tree.insert(item)

    print(test_tree)  # tree traversal
    print(test_tree.find(10))  # tree search


