import collections
from typing import List


class UnionFind:
    def __init__(self, N):
        self.parent = list(range(N))
        self.size = [1 for _ in range(N)]

    def make_set(self, s):
        self.parent[s] = s
        self.size[s] = 1

    def find_set(self, s):
        if (s == self.parent[s]):
            return s
        self.parent[s] = self.find_set(self.parent[s])
        return self.parent[s]

    def union_sets(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if (a != b):
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.parent[b] = a
            self.size[a] += self.size[b]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        ownership = {}

        for i, act in enumerate(accounts):
            _, emails = act[0], act[1:]
            for e in emails:
                if e in ownership:
                    uf.union_sets(i, ownership[e])
                ownership[e] = i

        ret = collections.defaultdict(list)
        for e, owner in ownership.items():
            ret[uf.find_set(owner)].append(e)

        return [[accounts[i][0]] + sorted(emails) for i, emails in ret.items()]


if __name__ == '__main__':
    accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com",
                                                                          "john00@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]
    print(Solution().accountsMerge(accounts))
