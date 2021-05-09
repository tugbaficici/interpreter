from treelib import Node, Tree

tree = Tree()
tree.create_node("P", "P") #root
tree.create_node("C","C1",parent="P" )
tree.create_node("C","C2",parent="P" )
tree.create_node("A","A",parent="C1" )
tree.create_node("W","W",parent="C2" )
tree.show()
count=0

nested_dict = { 'dictA': {'key_1': 'value_1'},
                'dictB': {'key_2': 'value_2'}}

               

print(nested_dict["P"])
