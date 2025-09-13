import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '9c73e6bcf09e809f77fe2ca382c20daf'
HEADER = {'Content-Type' : 'application/json',
          'trainer_token' : TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "vitaliy-95@mail.ru",
    "password": "Ubnfhf140898.",
    "password_re": "Ubnfhf140898."
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Жучка",
    "photo_id": 555
}
body_change = {
    "pokemon_id": "390277",
    "name": "Жлобка",
    "photo_id": 643
}
body_pokeball = {
    "pokemon_id": "390277"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)