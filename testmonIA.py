import pytest
import monIA

def test_coord():
    assert monIA.coord(8) == 1,0

def test_add():
    assert monIA.add((1,2),(3,4)) == 4,6

def test_index():
    assert monIA.index(1,2) == 10

def test_isInside():
    assert monIA.IsInside(4,5) == True, True


def test_willBeTaken():
    assert monIA.willBeTaken(10,[
            [28, 35],
            [27, 36]
        ])





def test_walk():
    assert monIA.walk((4,5),(1,3)) == 5,8


# def test_clienttoserver():
    # assert 



# def test_possibleMoves():
    # assert 

