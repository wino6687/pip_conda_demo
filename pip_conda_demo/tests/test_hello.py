from pip_conda_demo import pip_conda_demo
import pytest
import requests
import glob

def test_hello():
    '''
    pytest works by defining functions that beging with "test"

    You start by performing an action your library should be capabale of doing,
    then assert that the action yielded the expected result!
    '''
    assert pip_conda_demo.demo() == 'hello world!'

def test_scrape():
    '''
    The mock server is started up by travis CI during testing

    Using requests we can scrape the data from our local server!
    Then we verify that the file was downloaded with glob (there are
    other ways to go about verifying the download succeeded as well)
    '''
    url = 'http://localhost:8000/data/data_file.txt'
    r = requests.get(url, allow_redirects=True)
    open('data_file.txt','wb').write(r.content)
    file_list = glob.glob("*.txt")
    assert file_list[0] == 'data_file.txt'
