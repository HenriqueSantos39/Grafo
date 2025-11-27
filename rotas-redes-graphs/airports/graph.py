# airports/graph.py
from heapq import heappush, heappop
from collections import defaultdict, deque

class DirectedWeightedGraph:
    """Grafo direcionado com arestas ponderadas. Cada aresta: (dst, time_minutes, cost, flight_id).
    API principal implementada conforme requisitos do enunciado."""
    def __init__(self):
        self._adj = defaultdict(list)

    def add_airport(self, code: str):
        if code not in self._adj:
            self._adj[code] = []

    def remove_airport(self, code: str):
        self._adj.pop(code, None)
        for src in list(self._adj):
            self._adj[src] = [e for e in self._adj[src] if e[0] != code]

    def add_route(self, src: str, dst: str, time_minutes: int, cost: float=None, flight_id: str=None):
        self.add_airport(src)
        self.add_airport(dst)
        self._adj[src].append((dst, time_minutes, cost, flight_id))

    def remove_route(self, src: str, dst: str, flight_id: str=None):
        if src in self._adj:
            if flight_id is None:
                self._adj[src] = [e for e in self._adj[src] if e[0] != dst]
            else:
                self._adj[src] = [e for e in self._adj[src] if not (e[0]==dst and e[3]==flight_id)]

    def outgoing(self, src: str):
        return list(self._adj.get(src, []))

    def exists_path(self, src: str, dst: str) -> bool:
        q = deque([src])
        seen = {src}
        while q:
            u = q.popleft()
            if u == dst:
                return True
            for v, *_ in self._adj.get(u, []):
                if v not in seen:
                    seen.add(v)
                    q.append(v)
        return False

    def dijkstra(self, src: str, dst: str, use_cost: bool=False):
        # use_cost=False -> weight = time_minutes (index 1). True -> weight = cost (index 2)
        weight_index = 2 if use_cost else 1
        pq = []
        heappush(pq, (0, src, []))
        dist = {src: 0}
        while pq:
            d, u, path = heappop(pq)
            if u == dst:
                return d, path + [u]
            if d > dist.get(u, float('inf')):
                continue
            for edge in self._adj.get(u, []):
                v = edge[0]
                w = edge[weight_index] if edge[weight_index] is not None else None
                if w is None:
                    continue
                nd = d + w
                if nd < dist.get(v, float('inf')):
                    dist[v] = nd
                    heappush(pq, (nd, v, path + [u]))
        return None, []

    def fastest_with_connections(self, src: str, dst: str, min_connection=30):
        raise NotImplementedError("Use event-expanded graph for connection-aware routing.")
