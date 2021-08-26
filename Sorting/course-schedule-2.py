''' 
Topic   : Topological Sort
Problem : Course Schedule II
Link    : https://leetcode.com/problems/course-schedule-ii/
'''
def DFS(course, visited, cycle, prereqs, ordering):
    # course has 3 possible states
    # 1. visited   : course has been added to output
    # 2. visiting  : course not added to output but added to cycle
    # 3. unvisited : course not added to output or cycle
    if course in visited: return True
    if course in cycle: return False
    
    cycle.add(course)
    for req in prereqs[course]:
        if DFS(req,visited,cycle,prereqs,ordering) == False:
            return False
    
    ordering.append(course)
    visited.add(course)
    cycle.add(course)
    return True

def findOrder(numCourses, prerequisites):
    visited = set()
    cycle = set()
    course_ordering = []
    prereqs = { course:[] for course in range(numCourses) }
    
    for item in prerequisites:
        course, req = item[0], item[1]
        prereqs[course].append(req)
        
    for c in range(numCourses):
        if DFS(c, visited, cycle, prereqs, course_ordering) == False:
            return []
        
    return course_ordering 