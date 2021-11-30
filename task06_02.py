import requests
import pytest


#GET запрос без параметров

#response = requests.get('http://reqres.in/api/users/2')


@pytest.fixture
def fact_url_test4():
    return 'https://reqres.in/api/users'
@pytest.fixture
def fact_url_test5():
    return 'https://reqres.in/api/register'


@pytest.mark.smoke4
def test_smoke4(fact_url_test4):
    create_user = dict(name= "morpheus",job= "leader")
    response = requests.post(fact_url_test4,data = create_user )
    assert response.status_code == 201

@pytest.mark.smoke5
def test_smoke5(fact_url_test5):
    register_user = dict(email= "eve.holt@reqres.in",password= "pistol")
    response = requests.post(fact_url_test5,data = register_user  )
    assert response.status_code == 200
