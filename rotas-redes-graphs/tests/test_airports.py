# tests/test_airports.py
from airports.graph import DirectedWeightedGraph

def test_basic_dijkstra():
    g = DirectedWeightedGraph()
    g.add_route('A','B',60)
    g.add_route('B','C',50)
    g.add_route('A','C',150)
    dist, path = g.dijkstra('A','C')
    assert dist == 110
    assert path == ['A','B','C']
