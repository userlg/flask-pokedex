from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

from ..models.models import Pokemon
from ..utils.db import db

import requests

views = Blueprint("views", __name__)



def get_pokemon_description(name : str) -> str:
    r = requests.get(f'https://courses.cs.washington.edu/courses/cse154/webservices/pokedex/pokedex.php?pokemon={name}').json()

    return r['info']['description']


def get_pokemon_type(pokemons) -> list:
    list_type = []

    for result in pokemons['types']:
        
            list_type.append(result['type']['name'])
    
    if len(list_type) == 1:
        list_type.append('None')

    return list_type


@views.route('/',methods=['GET'])
def  index():
    r = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151&offset=0')
    
    print(r.status_code)
    r = r.json()
    i = 0
    for pokemon in r['results']:
        i += 1
        name = pokemon['name']
        description = get_pokemon_description(name)
        print(f'{i} --> {name} <--> captured ')

        end_point = f'https://pokeapi.co/api/v2/pokemon-form/{i}/'
        t =requests.get(end_point).json()
        
        list_of_type = []
        list_of_type = get_pokemon_type(t)

        poke = Pokemon(name, list_of_type[0],list_of_type[1], description)
        db.session.add(poke)
        db.session.commit()

        list_of_type.clear()

    return render_template('index.html')



@views.route('/get_pokemon_image',methods=['GET'])
def get_pokemon_image():
    pokeid = 0
    while(pokeid <= 151):
      r = requests.get(f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokeid}.png").content
      image_name = f'{pokeid}.png'
      with open(f'app/static/pokemons/{image_name}','wb') as handler:
          handler.write(r)
      pokeid += 1
      print(f'\t Downloaded-->{pokeid}')

    return 'Welcome about route'
    
