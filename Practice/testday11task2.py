import pytest
#smoke test
@pytest.mark.smoke
def test_equal():
    #assert
    assert 'hello' == 'hello'
@pytest.mark.smoke
def test_not_equal():
    assert 'world' == 'worlD'

#regression test

@pytest.mark.regression
def test_addition():
    assert 5 + 5 == 10
@pytest.mark.regression
def test_subtraction():
    assert 5 - 5 == 0






