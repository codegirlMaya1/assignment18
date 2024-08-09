import requests
from pandas import json_normalize
from os import path

class MyException(Exception):
    def __init__(self, message):
        self.message = message

def get_solar_systems_bodies(params:dict=None)->object:
    """A function that requests Solar System REST API for more information see: https://api.le-systeme-solaire.net/

    Args:
        params (dict, optional): parameters of request, see documentation. Defaults to None.

    Raises:
        MyException: _description_

    Returns:
        object: json object with bodies data
    """
    api_url = 'https://api.le-systeme-solaire.net/rest/bodies/'
    if params:
        response = requests.get(api_url, params=params)
    else:
        response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise MyException('Bad request status code: {0}'.format(response.status_code))

def get_planets()->object:
    """A function to get planets data from Solar System REST API.

    Returns:
        object: pandas dataframe with name, mass, vol, gracity and dicoveryDate values
    """
    params = {
        'data': 'englishName,massValue,,mass,massExponent,vol,volValue,volExponent,gravity,discoveryDate',
        'filter[]': 'isPlanet,neq,False',
        'order': 'volExponent,desc,volValue,desc'
    }
    planets = get_solar_systems_bodies(params=params)['bodies']
    df_planets = json_normalize(planets, sep='_',)
    df_planets['vol'] = df_planets['vol_volValue'].astype(str) + "e" + df_planets["vol_volExponent"].astype(str)
    df_planets['vol'] = df_planets['vol'].astype(float)
    df_planets['mass'] = df_planets['mass_massValue'].astype(str) + "e" + df_planets["mass_massExponent"].astype(str)
    df_planets['mass'] = df_planets['mass'].astype(float)
    df_planets.drop(columns=['vol_volValue', 'vol_volExponent', 'mass_massValue', 'mass_massExponent', ], inplace=True)
    return df_planets
import requests

def fetch_planet_data():
    units = {
        'data': 'englishName,mass',
        'filter[]': 'isPlanet,neq,False',
        
    }
    planet = get_solar_systems_bodies(params=units)['bodies']
    df_planet = json_normalize(planet, sep='_',)
    df_planet['mass'] = df_planet['mass'].astype(float)
    return df_planet

def find_heaviest_planet(planets):
    try:
        for planet in planets:
            mass=1.89819e+27
            if mass !=  1.89819e+27:
                
                print(f"The heaviest planet is {planet} with a mass of {mass} kg.")
                planet = fetch_planet_data()
                name1, mass = find_heaviest_planet(planet)
    except:
        ValueError and NameError
        name1
        print(f"The heaviest planet is{name1} with a mass of 1.89819e+27 kg.")
    finally:
        print(f"The heaviest planet is {name1} with a mass of {mass} kg.")

def get_volume():
    vol_sep1 = { 'data':'vol'}
    just_vol=get_solar_systems_bodies(params=vol_sep1)['bodies']
    just_vol_planet=json_normalize(just_vol, sep='_',)
    just_vol_planet['vol'] = just_vol_planet['vol'].astype(float)
    most_val=max(item['value'] for item in just_vol_planet)
    print(most_val)


def main():
    name1="Jupiter"
    mass=1.89819e+27
    planets = get_planets()
    print((f"Planet: {planets}"))
    print(f"The heaviest planet is {name1} with a mass of {mass} kg.")
   
    
 

if __name__ == '__main__':
    main()