import requests
import json

#Retrieving data from Pokeman API
response= requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
json_data=response.text

#Converting JSON to Python Object
pikachu_data = json.loads(json_data)

#Accessing data
print(pikachu_data["name"])
print(pikachu_data["types"])

def fetch_pokemon_data(pokemon_name):
    return #json response

def calculate_average_weight(pokemon_list):
    return #average weight

pokemon_names = ["pikachu", "bulbasaur", "charmander"]

response1= requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
json_data=response1.text

response2= requests.get('https://pokeapi.co/api/v2/pokemon/bulbasaur')
json_data1=response2.text

response3= requests.get('https://pokeapi.co/api/v2/pokemon/charmander')
json_data2=response3.text

bulbasaur_data = json.loads(json_data1)
charmander_data = json.loads(json_data2)


print(pikachu_data["name"])
print(pikachu_data["types"])
print(pikachu_data["weight"])

print(bulbasaur_data["name"])
print(bulbasaur_data["types"])
print(bulbasaur_data["weight"])

print(charmander_data["name"])
print(charmander_data["types"])
print(charmander_data["weight"])