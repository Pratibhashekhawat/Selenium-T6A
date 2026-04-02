import pytest
#smoke test
@pytest.mark.smoke
def test_equal():
    #assert
    assert 'hello' == 'hello'

#regression test
@pytest.mark.regression
def test_addition():
    assert 5 + 5 == 10

#skip test
# @pytest.mark.skip
# def test_in():
#     l=[1,2,3]
#     assert 3 in l, "not in the list"

#skip if
@pytest.mark.skipif(True, reason="not in list")
def test_in():
    l=[1,2,3]
    assert 3 in l, "in the list"


