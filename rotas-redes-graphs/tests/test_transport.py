# tests/test_transport.py
from transport.graph import TransitGraph

def test_transport_dijkstra():
    g = TransitGraph()
    g.add_connection('X','Y',10)
    g.add_connection('Y','Z',5)
    d, p = g.dijkstra('X','Z')
    assert d == 15
    assert p == ['X','Y','Z']
