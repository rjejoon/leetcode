from typing import List


class Solution:
    def __init__(self):
        self.graph = []
        self.dfs_state = []  # -1: unvisited, 0: explored, 1: visited

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.dfs_state = [-1] * numCourses
        self.graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            self.graph[prereq].append(course)

        for prereq in range(numCourses):
            if self.dfs_state[prereq] == -1 and self.has_cycle(prereq):
                return False

        return True

    def has_cycle(self, prereq):
        self.dfs_state[prereq] = 0
        for course in self.graph[prereq]:
            if self.dfs_state[course] == -1:
                if self.has_cycle(course):
                    return True
            elif self.dfs_state[course] == 0:
                return True

        self.dfs_state[prereq] = 1
        return False


if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    # print(Solution().canFinish(numCourses, prerequisites))

    numCourses = 2
    prerequisites = [[0, 1]]
    print(Solution().canFinish(numCourses, prerequisites))

    numCourses = 1
    prerequisites = []
    # print(Solution().canFinish(numCourses, prerequisites))
