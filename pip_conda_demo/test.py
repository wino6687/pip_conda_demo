from pip_conda_demo import pip_conda_demo
import pytest

def test_hello():
    '''pytest works by defining functions that beging with "test"

    You start by performing an action your library should be capabale of doing,
    then assert that the action yielded the expected result!
    '''
    response = pip_conda_demo.demo()
    assert response == 'hello world!'
