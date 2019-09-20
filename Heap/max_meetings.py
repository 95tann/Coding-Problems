'''
Topic   : Heap 
Problem : Max Meetings

Description
-----------
A company founder wants to have meetings with potential investors to discuss investments for his company.
Investors are flying in to meet the founder and are constrained for dates. 
Each investor has an arrival date and departure date. These dates are stored in two arrays:
--> arrival = [1,4,1]
--> departure = [2,4,4]

The date arrays above indicate that:
--> investor 0 is available on day 1 and 2
--> investor 1 is availbale on day 4
--> investor 2 is available on day 1, 2, 3, 4

The founder would like to meet with all investors but unfortunatley can only conduct 1 meeting per day. 
Determine the maximum no. of meetings that the founder can have given the availabilty dates of all investors

Example
-------
arrival   = [1,2,3,3,3]
departure = [2,2,3,4,4] 

The founder can have a maximum of 4 days of meetings:
   - Day 1: meet investor 0
   - Day 2: meet invester 1
   - Day 3: meet investor 2
   - Day 4: meet investor 3 or 4 
'''
import heapq as hq

def max_meetings(arrival, departure):
	min_heap = []
	for i in range(len(arrival)):
		duration = departure[i] - arrival[i]
		hq.heappush(min_heap, (duration, (i, arrival[i], departure[i])))

	booked_days = {}
	while(min_heap):
		investor, arr,dep = hq.heappop(min_heap)[1]
		for day in range(arr,dep+1):
			if day not in booked_days:
				booked_days[day] = investor
				break
	
	return len(booked_days)

# Test Cases
print(max_meetings([1,2,3,3,3],[2,2,3,4,4]) == 4)
print(max_meetings([1,1,2],[1,2,2]) == 2)
print(max_meetings([],[]) == 0)
print(max_meetings([1],[3]) == 1)
print(max_meetings([1,1,1,5,3,2],[2,2,5,5,4,5]) == 5)
print(max_meetings([2,2,2],[2,2,2]) == 1)
print(max_meetings([1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]) == 8)
print(max_meetings([1,2,2],[3,2,3]) == 3)