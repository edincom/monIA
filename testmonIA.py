from monIa import coord
from monIa import add
from monIa import index
from monIa import isInside
from monIa import willBeTaken
from monIa import walk


def test_coord():
    assert coord(8) == (1,0)
    assert coord(10) == (1,2)

def test_add():
    assert add((1,2),(3,4)) == (4,6)
    assert add((4,2),(3,4))== (7,6)
    assert add((3,1),(3,8))==(6,9)

def test_index():
    assert index(1,2) == 10
    assert index(4,4) == 36

def test_isInside():
    assert isInside(4,5) == True
    assert isInside(6,9) == False



def test_willBeTaken():
    assert willBeTaken(10,[
            [28, 35],
            [27, 36]
        ])


def test_walk():
    assert walk((4,5),(1,3)) == 5,8


