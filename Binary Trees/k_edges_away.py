import queue

''' 
Topic   : Binary Trees
Problem : Given a binary tree, an int k, and a starting node s, 
          find all nodes from s that are k edges away

    	  Tree is made up of nodes where each 
    	  node has following 3 attributes:
   			  Node.value (int) 
    		  Node.left  (left child)
    		  Node.right (right child)
'''
parents = {}
visitied = {}
parents[root] = None
visited[root] = False

def assign_parents(node,parent_node):
	if start_node != None:
		parents[node.value] = parent_node
		visited[node.value] = False
		assign_parents(node.left, node)
		assign_parents(node.right, node)

def k_nodes(start_node,k):
	Q = queue.Queue()
	Q.enqueue(start_node)
	
	while(k > 0):
		curr_node = Q.dequeue()
		visited[curr_node.value] = True

        	lc = curr_node.left
        	rc = curr_node.right
        	parent = parents[curr_node.value]

		if(lc and visited[lc.value] == False):
			Q.enqueue(lc)

		if(rc and visited[rc.value] == False):
			Q.enqueue(rc)

		if(parent and visited[parent.value] == False):
			Q.enqueue(parent)

		k -= 1

	return Q

# Function Calls 
assign_parents(root.left,root)
assign_parents(root.right,root)
k_nodes(start_node,k)
