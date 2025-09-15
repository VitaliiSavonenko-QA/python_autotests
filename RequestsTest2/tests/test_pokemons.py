import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '{Токен}'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '39743'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][1]['name'] == 'Жучка'


@pytest.mark.parametrize('key, value', [('name', 'Жучка'), ('trainer_id', TRAINER_ID), ('id', '390277')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()['data'][1][key] == value

def test_status_code_trainer():
    response_trainer = requests.get(url = f'{URL}/trainers')
    assert response_trainer.status_code == 200

def test_my_trainer():
    response_my_trainer = requests.get(url = f'{URL}/trainers/{TRAINER_ID}', params = {'trainer_id' : TRAINER_ID})

    assert response_my_trainer.json()['trainer_name'] == 'Gante'
