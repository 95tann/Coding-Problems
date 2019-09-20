'''
Topic   : Heaps
Problem : Production Planning

Description
-----------
There are numerous products that a company needs to produce. Every product has a worstCase cost and an averageCase cost. 
Products can be produced in any order, however the company must have cash greater than or equal to worstCase cost of product x
before choosing to produce product x. If a product is selected for production, it is produced at its average cost.
Determine the minimum cash needed at beginning of production in order to produce all products


Example
-------
worstcase = [6,5,7]
avgCase = [4,2,1]

The optimal production order that minimizes beginning cash is product 2, then product 1, then product 0
The minimum cash required is 9
'''
import heapq as hq

def min_cost(worst_cost, avg_cost):
	max_heap = []
	for i in range(len(worst_cost)):
		diff = worst_cost[i] - avg_cost[i]
		hq.heappush(max_heap, (-diff, i))

	min_cost = curr_cost = max(worst_cost)
	
	while(max_heap):
		index = hq.heappop(max_heap)[1]

		if curr_cost < worst_cost[index]:
			min_cost += (worst_cost[index] - curr_cost)
			curr_cost = worst_cost[index] - avg_cost[index]
		else:
			curr_cost -= avg_cost[index]
		
	return min_cost

# Test Cases
print(min_cost([6,5,7,8],[4,2,1,1]) == 10)
print(min_cost([6,5,7],[4,2,1]) == 9)
print(min_cost([6,7,8],[4,4,7]) == 16)
