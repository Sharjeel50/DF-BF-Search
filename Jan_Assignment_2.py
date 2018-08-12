class Node(object):
    """
    Node class
    """
    def __init__(self,id):
        """
        Default constructor

        Parameters
        ----------
        id : int
        """
        self.id = id
        self.children = []
        self.parent=None

    def set_parent(self,parent):
        self.parent = parent


    def get_parent(self):
        return self.parent

    def add_child(self,child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def kill_child(self):
        del self.children[len(self.children)-1]

    def set_content(content):
        self.content = content

    def get_content(content):
        return self.content

    def __str__(self):
        child_ids = [c.id for c in self.children]
        if self.get_parent()==None:
            return "({})".format(self.id)
        else:
            return "({})".format(self.id)

    def __repr__(self):
        return self.__str__()

class Tree(object):
    def __init__(self,description_file):
        self.description_file = description_file
        self.tree_list = self.make_tree()

    def make_tree(self):
        ids, edges = self.get_ids_and_edges() 
        
        ## create the Tree
        
        nodes = []
        for curr_id in ids:
            node = Node(curr_id)
            nodes.append(node)
        print(nodes)
        for edge in edges:
            first_id = edge.split(",")
            first_id = int(first_id[0])
            first_node = nodes[first_id]
            second_id = int(edge[2])
            second_node = nodes[second_id]
            first_node.add_child(second_node)
            second_node.set_parent(first_node)

        first_edge = edge[0]
        root_id = first_edge[0]
        #self.root = nodes[root_id]

        #test_node = nodes[]
        #print("Test Node Children", test_node.get_children())
        return nodes

    def get_all_nodes_BF(self):
        ## fill the list with all nodes in Breadth-First order
        bf_nodes = []
  


        for i in self.tree_list:
            if i not in bf_nodes:      #if 1,2,3,4,5 is not in add it
                bf_nodes.append(i)
            if i.get_children != []:
                children = i.get_children()
                for new in children:
                    if new not in bf_nodes:
                        bf_nodes.append(new)



        #add first node to bf_nodes
        #add it's Children
        #add it's children's Children

        return bf_nodes

    def get_all_nodes_DF(self):
        df_nodes = []

        node = self.tree_list[0]

        while len(df_nodes) != len(self.tree_list):
            if node not in df_nodes:
                df_nodes.append(node)

            if node.get_children():
                node = node.get_children()
                if len(node) > 1:
                    node = node[len(node)-1] #get last child
                else:
                    node = node[0]
            else:
                node = node.get_parent()
                node.kill_child()

        ## return the created list of nodes
        return df_nodes

    def get_ids_and_edges(self):
        """read the tree description file and retrieve the nodes
        and edges in between of them"""
        f = open(self.description_file)
        new_file = f.readlines()

        ids = []
        edges = []

        for edge in new_file:

            edge = edge.strip()
            edges.append(edge)

            ids.append(int(edge[0]))

            ids.append(int(edge[2]))

        ids = list(set(ids))
        print("Ids: ",ids)
        print("edges:",edges)

        return ids,edges

"""This is the code used for testing.
DO NOT MODIFY.
"""
tree_description = "tree_description_01.txt"
tree = Tree(tree_description)
bf_nodes = tree.get_all_nodes_BF()
print("bf_nodes: {}".format(bf_nodes))
print("tree list: ", tree.tree_list)
df_nodes = tree.get_all_nodes_DF()
print("df_nodes: {}".format(df_nodes))
