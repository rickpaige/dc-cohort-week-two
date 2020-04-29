import json

data = [
    {'name': "name"},
    {'age': "age"}
]

def make_json():
    with open('name.json', 'w') as file:
        json.dump(data, file)

while True:
    name = input('What is your name? ')
    age = input('How old are you? ')
    data.append({'name': name})
    make_json()
    break