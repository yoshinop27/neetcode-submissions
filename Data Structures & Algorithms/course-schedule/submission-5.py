class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Adjacency List
        dct = {}
        # Build an Adjacency List
        for course,prereq in prerequisites:
            if course in dct:
                dct[course].append(prereq)
            else:
                dct[course] = [prereq]
        # dfs until you reach a "intro" class
        def dfs(course, seen) -> bool:
            # Reach an intro class
            if course not in dct:
                return True
            if course in seen:
                return False
            
            seen.add(course)
            for prereq in dct[course]:
                if not dfs(prereq, seen):
                    seen.remove(course)
                    return False
            seen.remove(course)
            return True

        for i in range(numCourses):
            seen = set()
            if not dfs(i, seen):
                return False
        return True
            
