import requests
import pytest


# GET запрос без параметров

# response = requests.get('http://reqres.in/api/users/2')

@pytest.fixture
def fact_url_test1():
    return 'http://reqres.in/api/users/2'


@pytest.fixture
def fact_url_test2():
    return 'http://reqres.in/api/unknown'


@pytest.fixture
def fact_url_test3():
    return 'http://reqres.in/api/unknown/2'


@pytest.mark.smoke1
def test_smoke1(fact_url_test1):
    reply = requests.get(fact_url_test1)
    assert reply.status_code == requests.codes.ok


@pytest.mark.smoke2
def test_smoke2(fact_url_test2):
    reply = requests.get(fact_url_test2)
    assert reply.status_code == requests.codes.ok


@pytest.mark.smoke3
def test_smoke3(fact_url_test3):
    reply = requests.get(fact_url_test3)
    assert reply.status_code == requests.codes.ok

