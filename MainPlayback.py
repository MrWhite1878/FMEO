from treelib import Node, Tree

tree = Tree()

tree.create_node("Harry", "harry")  # root node
tree.create_node("Jane", "jane", parent="harry")    # child node
tree.show(line_type='ascii')