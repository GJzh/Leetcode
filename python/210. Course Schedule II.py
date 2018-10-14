from Queue import Queue
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        n = len(prerequisites)
        status = {}
        indegree = [0] * numCourses
        for course1, course2 in prerequisites:
            if course2 not in status:
                status[course2] = []
            status[course2].append(course1)
            indegree[course1] += 1
        # find 0-indegrees
        cur = Queue()
        for i in range(numCourses):
            if indegree[i] == 0:
                cur.put(i)
        schedule = []
        while cur.qsize() > 0:
            course = cur.get()
            schedule.append(course)
            if course not in status: continue
            for nextCourse in status[course]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    cur.put(nextCourse)
        
        return schedule if len(schedule) == numCourses else []