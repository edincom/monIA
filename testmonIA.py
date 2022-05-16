import pytest
import monIa

def test_coord():
    assert monIa.coord(8) == 1,0

def test_add():
    assert monIa.add((1,2),(3,4)) == 4,6

def test_index():
    assert monIa.index(1,2) == 10

def test_isInside():
    assert monIa.IsInside(4,5) == True, True


def test_willBeTaken():
    assert monIa.willBeTaken(10,[
            [28, 35],
            [27, 36]
        ])





def test_walk():
    assert monIa.walk((4,5),(1,3)) == 5,8


# def test_clienttoserver():
    # assert 



# def test_possibleMoves():
    # assert 

