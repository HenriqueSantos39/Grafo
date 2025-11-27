# transport/graph.py
from collections import defaultdict, deque
from heapq import heappush, heappop

class TransitGraph:
    def __init__(self):
        self._adj = defaultdict(list)

    def add_station(self, name):
        if name not in self._adj:
            self._adj[name] = []

    def remove_station(self, name):
        self._adj.pop(name, None)
        for s in list(self._adj):
            self._adj[s] = [e for e in self._adj[s] if e[0] != name]

    def add_connection(self, a, b, time_minutes):
        self.add_station(a); self.add_station(b)
        self._adj[a].append((b, time_minutes))
        self._adj[b].append((a, time_minutes))

    def remove_connection(self, a, b):
        if a in self._adj:
            self._adj[a] = [e for e in self._adj[a] if e[0] != b]
        if b in self._adj:
            self._adj[b] = [e for e in self._adj[b] if e[0] != a]

    def outgoing(self, station):
        return list(self._adj.get(station, []))

    def exists_path(self, a, b):
        q = deque([a])
        seen = {a}
        while q:
            u = q.popleft()
            if u == b: return True
            for v,_ in self._adj.get(u, []):
                if v not in seen:
                    seen.add(v); q.append(v)
        return False

    def dijkstra(self, src, dst):
        pq=[]; heappush(pq,(0,src,[])); dist={src:0}
        while pq:
            d,u,path = heappop(pq)
            if u==dst: return d, path+[u]
            if d>dist.get(u,1e18): continue
            for v,w in self._adj.get(u,[]): 
                nd=d+w
                if nd<dist.get(v,1e18):
                    dist[v]=nd; heappush(pq,(nd,v,path+[u]))
        return None, []
