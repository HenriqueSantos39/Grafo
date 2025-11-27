# tests/test_curriculum.py
from curriculum.graph import CurriculumGraph

def test_cycle_detection():
    g = CurriculumGraph()
    g.add_prereq('A','B')
    g.add_prereq('B','C')
    assert g.exists_dependency('A','C') is True
    g.add_prereq('C','A')
    assert g.has_cycle() is True
