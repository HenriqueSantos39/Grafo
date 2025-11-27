# tests/test_social.py
from social.graph import SocialGraph

def test_social_basic():
    g = SocialGraph()
    g.add_connection('a','b')
    g.add_connection('b','c')
    assert g.connected('a','c') is True
    suggestions = g.suggest_friends('a')
    assert isinstance(suggestions, list)
