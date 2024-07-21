import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'be1880559a4d64e0627621a25db08df7'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '4124'


def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response.status_code == 200

def test_check_name():
    response_name = requests.get(url = f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response_name.json()['data'][0]['trainer_name'] == 'Valkyrie'

@pytest.mark.parametrize('key, value',[('trainer_name','Valkyrie'),('id',TRAINER_ID),('level', '5')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response_parametrize.json()['data'][0][key] == value
