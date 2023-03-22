from datastructure.tree.BinaryTree import BinaryTree

bt = BinaryTree()
bt.add(6)
bt.add(4)
bt.add(5)
bt.add(7)
bt.add(6)
bt.add(9)
bt.add(3)

# bt.traversal()
# bt.traversal("PRE")
# bt.traversal("IN")
# bt.traversal("POST")

bt2 = BinaryTree()
bt2.insert(1)
bt2.traversal()

bt2.insert(2)
bt2.traversal()

bt2.insert(3)
bt2.traversal()

bt2.insert(4)
bt2.traversal()

bt2.insert(5)
bt2.traversal()
