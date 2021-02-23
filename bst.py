#
#   Create a method which will return the height of the Binary Search Tree (BST)
#
#
class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree """
    def __init__(self):
        self.root = None

    def add(self, item):
        """ Add this item to its correct position on the tree """
        # This is a non recursive add method. A recursive method would be cleaner.
        if self.root == None: # ... Empty tree ...
            self.root = Node(item, None, None) # ... so, make this the root
        else:
            # Find where to put the item
            child_tree = self.root
            while child_tree != None:
                parent = child_tree
                if item < child_tree.item: # If smaller ... 
                    child_tree = child_tree.left # ... move to the left
                else:
                    child_tree = child_tree.right

            # child_tree should be pointing to the new node, but we've gone too far
            # we need to modify the parent nodes
            if item < parent.item:
                parent.left = Node(item, None, None)
            else:
                parent.right = Node(item, None, None)

#--------------------------------------------------------------------------------------

    # find the height of the tree
    def recur_height(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + max(self.recur_height(ptr.left), self.recur_height(ptr.right))
            
    def height(self):
        return self.recur_height(self.root)

    # count how many elements are in a tree
    def count(self):
        return self.recursive_count(self.root)

    def recursive_count(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + self.recursive_count(ptr.right) + self.recursive_count(ptr.left)

    # A node is a leaf node if both left and right child nodes of it are NULL
    def count_leaves(self):
        return self.recur_leaves(self.root)
        
    def recur_leaves(self, ptr):
        if ptr == None:
            return 0
        elif ptr.left == None and ptr.right == None:
            return 1 + self.recur_leaves(ptr.left) + self.recur_leaves(ptr.right)
        else:
            return self.recur_leaves(ptr.left) + self.recur_leaves(ptr.right)

    # count the nodes that have only a child node on the right
    def count_right_only(self):
        return self.recur_right(self.root)
        
    def recur_right(self, ptr):
        if ptr == None:
            return 0
        elif ptr.left == None and ptr.right != None:
            return 1 + self.recur_right(ptr.left) + self.recur_right(ptr.right)
        else:
            return self.recur_right(ptr.left) + self.recur_right(ptr.right)

    # count the nodes that have at least one child node
    def count_non_leaves(self):
        return self.recur_non_leaves(self.root)
        
    def recur_non_leaves(self, ptr):
        if ptr == None:
            return 0
        elif ptr.left != None or ptr.right != None:
            return 1 + self.recur_non_leaves(ptr.left) + self.recur_non_leaves(ptr.right)
        else:
            return self.recur_non_leaves(ptr.left) + self.recur_non_leaves(ptr.right)

    # count a range of tree elements
    def range_count(self, lo, hi):
        return self.recursive_rcount(self.root, lo, hi)
        
    def recursive_rcount(self, ptr, lo, hi):

        if ptr == None:
            return 0
        elif ptr.item <= hi and ptr.item >= lo:
            return 1 + self.recursive_rcount(ptr.left, lo, hi) + self.recursive_rcount(ptr.right, lo, hi)
        else:
            return self.recursive_rcount(ptr.left, lo, hi) + self.recursive_rcount(ptr.right, lo, hi)

    # check if an item is present or not
    def recur_present(self, ptr, item):
        if ptr == None:
            return False
        elif ptr.item == item:
            return True
        elif self.recur_present(ptr.left, item):
            return True
        else:
            return self.recur_present(ptr.right, item)
        return False
    
    def is_present(self, item):
        return self.recur_present(self.root, item)

    # count the sum of all the elements
    def recur_total(self, ptr):
        #count = 0
        if ptr == None:
            return 0
        else:
            return ptr.item + self.recur_total(ptr.left) + self.recur_total(ptr.right)
            
    def total(self):
        return self.recur_total(self.root)

    # print the bst 
    def in_order(self, ptr):
        if ptr == None:
            return ""
        else:
            return self.in_order(ptr.left) + str(ptr.item) + "," + self.in_order(ptr.right)

    def __str__(self):
        return self.in_order(self.root)

#--------------------------------------------------------------------------

# func that takes a node and bst and return the height of the node in the bst
def nodeheight(node, bst):
    count = 1
    current = bst.root
    while node != current.item:
        if node < current.item:
            current = current.left
            count += 1

        else:
            current = current.right
            count += 1
    return count

# check if a bst is AVL balanced 
def is_avl(bst):
    if abs(bst.r_height(bst.root.left) - bst.r_height(bst.root.right)) > 1:
        return False
    else:
        return True

def rotation_type(bst):
    ptr = bst.root
    type = []
    while ptr != None:
        if ptr.right == None and ptr.left == None:
            return "".join(type)
        elif ptr.right == None:
            type.append("l")
            ptr = ptr.left
        elif ptr.left == None:
            type.append("r")
            ptr = ptr.right

# check which nodes have been visited while searching for a value
def who_searched(val, bst):
    visited = []
    current = bst.root
    visited.append(current.item)
    while val != current.item:
        if val < current.item:
            current = current.left
            visited.append(current.item)

        else:
            current = current.right
            visited.append(current.item)
    return visited

#-----------------------------------------------------------------------

items = [1, 10, 3, 7, 2, 6, 5]
bst = BST()
    
for item in items:
    bst.add(item)

print(bst.height())
#print(bst.count_leaves())
#print(bst.count_non_leaves())
print(nodeheight(3, bst))
#print(bst)
#print(bst.count_right_only())
print(who_searched(6, bst))