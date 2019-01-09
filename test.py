from conda_demo import conda_demo
import pytest

def test_hello():
    response = conda_demo.demo()
    assert response = 'hello world!'
