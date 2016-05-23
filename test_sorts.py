'''This module contains functions for unit testing the sort_algos module using py.test'''

from sort_algos import Sorts

def test_integer_sort_1():
    testobject = Sorts([-100,-23,-10000,2,10000000,45,0,0,0,45,-2])
    assert testobject.merge_sort() == [-10000,-100,-23,-2,0,0,0,2,45,45,10000000]
def test_decimal_sort_1():
    testobject = Sorts([0.01,0.0002,-0.01,1,1000,100.45,100.29,100.11])
    assert testobject.merge_sort() == [-0.01,0.0002,0.01,1,100.11,100.29,100.45,1000]
def test_words_sort_1():
    testobject = Sorts(["dog","cat","elephant","camel","emu","raccoon"])
    assert testobject.merge_sort() == ["camel","cat","dog","elephant","emu","raccoon"]
def test_integer_sort_2():
    testobject = Sorts([-100,-23,-10000,2,10000000,45,0,0,0,45,-2])
    assert testobject.selection_sort() == [-10000,-100,-23,-2,0,0,0,2,45,45,10000000]
def test_decimal_sort_2():
    testobject = Sorts([0.01,0.0002,-0.01,1,1000,100.45,100.29,100.11])
    assert testobject.selection_sort() == [-0.01,0.0002,0.01,1,100.11,100.29,100.45,1000]
def test_words_sort_2():
    testobject = Sorts(["dog","cat","elephant","camel","emu","raccoon"])
    assert testobject.selection_sort() == ["camel","cat","dog","elephant","emu","raccoon"]
def test_integer_sort_3():
    testobject = Sorts([-100,-23,-10000,2,10000000,45,0,0,0,45,-2])
    assert testobject.insert_sort() == [-10000,-100,-23,-2,0,0,0,2,45,45,10000000]
def test_decimal_sort_3():
    testobject = Sorts([0.01,0.0002,-0.01,1,1000,100.45,100.29,100.11])
    assert testobject.insert_sort() == [-0.01,0.0002,0.01,1,100.11,100.29,100.45,1000]
def test_words_sort_3():
    testobject = Sorts(["dog","cat","elephant","camel","emu","raccoon"])
    assert testobject.insert_sort() == ["camel","cat","dog","elephant","emu","raccoon"]





