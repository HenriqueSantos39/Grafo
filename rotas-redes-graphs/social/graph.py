# social/graph.py
from collections import defaultdict, deque

class SocialGraph:
    def __init__(self):
        self._adj = defaultdict(set)

    def add_user(self, user_id):
        if user_id not in self._adj:
            self._adj[user_id] = set()

    def remove_user(self, user_id):
        self._adj.pop(user_id, None)
        for u in self._adj:
            self._adj[u].discard(user_id)

    def add_connection(self, a, b):
        self.add_user(a); self.add_user(b)
        self._adj[a].add(b); self._adj[b].add(a)

    def remove_connection(self, a, b):
        self._adj.get(a, set()).discard(b)
        self._adj.get(b, set()).discard(a)

    def friends(self, user_id):
        return set(self._adj.get(user_id, set()))

    def connected(self, a, b):
        q = deque([a]); seen={a}
        while q:
            u=q.popleft()
            if u==b: return True
            for v in self._adj.get(u,[]): 
                if v not in seen:
                    seen.add(v); q.append(v)
        return False

    def suggest_friends(self, user_id, k=5):
        suggestions = {}
        for friend in self._adj.get(user_id, []):
            for foaf in self._adj.get(friend, []):
                if foaf==user_id or foaf in self._adj[user_id]: continue
                suggestions[foaf] = suggestions.get(foaf, 0) + 1
        return sorted(suggestions.items(), key=lambda x: -x[1])[:k]
