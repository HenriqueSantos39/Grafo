# curriculum/graph.py
from collections import defaultdict, deque

class CurriculumGraph:
    def __init__(self):
        self._adj = defaultdict(list)

    def add_course(self, code):
        if code not in self._adj:
            self._adj[code] = []

    def remove_course(self, code):
        self._adj.pop(code, None)
        for k in list(self._adj):
            self._adj[k] = [v for v in self._adj[k] if v != code]

    def add_prereq(self, prereq, course):
        self.add_course(prereq); self.add_course(course)
        self._adj[prereq].append(course)

    def remove_prereq(self, prereq, course):
        if prereq in self._adj:
            self._adj[prereq] = [v for v in self._adj[prereq] if v != course]

    def prerequisites_of(self, course):
        res = [k for k,v in self._adj.items() if course in v]
        return res

    def exists_dependency(self, a, b):
        q = deque([a]); seen = {a}
        while q:
            u=q.popleft()
            if u==b: return True
            for v in self._adj.get(u, []):
                if v not in seen:
                    seen.add(v); q.append(v)
        return False

    def has_cycle(self):
        visited=set(); rec=set()
        def dfs(u):
            visited.add(u); rec.add(u)
            for v in self._adj.get(u, []):
                if v not in visited:
                    if dfs(v): return True
                elif v in rec: return True
            rec.remove(u); return False
        for node in list(self._adj):
            if node not in visited:
                if dfs(node): return True
        return False
