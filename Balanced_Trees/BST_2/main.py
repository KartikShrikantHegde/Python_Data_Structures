from Tree import BinarySearchTree

my_tree=BinarySearchTree()

my_tree.insert(100)
my_tree.insert(200)
my_tree.insert(50)
my_tree.insert(75)
my_tree.insert(150)

my_tree.inorder(my_tree.root)