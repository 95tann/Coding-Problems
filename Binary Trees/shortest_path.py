''' 
Topic   : Trees
Problem : Shortest Path
Link    : https://practice.geeksforgeeks.org/problems/shortest-path-between-cities/1
'''
def shortest_path(x, y):
    import math
	if x == y: return 0
	
	anc_x, anc_y = x, y
	dist_x, dist_y = 0, 0
	lvl_x = int(math.log(x,2))
	lvl_y = int(math.log(y,2))

	if lvl_x > lvl_y:
		for i in range(lvl_x - lvl_y):
			anc_x = anc_x // 2
			dist_x += 1
	if lvl_y > lvl_x:
		for i in range(lvl_y - lvl_x):
			anc_y = anc_y // 2
			dist_y += 1
	
	while(anc_x != anc_y):
		anc_x = anc_x // 2
		anc_y = anc_y // 2
		dist_x += 1
		dist_y += 1
		
	return dist_x + dist_y