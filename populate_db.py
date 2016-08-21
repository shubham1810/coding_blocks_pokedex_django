import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pokemonGo.settings")

import django
django.setup()

from search.models import Pokedex
from search.views import search_pokemon
from search.pokemon_data_file import pokemon_data


def populate():
    for pokemon in search_pokemon('*'):
        print pokemon[0], pokemon[1]
        try:
            add(p_name=pokemon[0], p_img=pokemon[1])
            print "==================================="
        except:
            pass
    print "database populated"

def showDB():
    for pokemon in Pokedex.objects.all():
        print pokemon, pokemon.id


def add(p_name, p_img, p_type=''):
    p = Pokedex.objects.get_or_create(pokemon_name=p_name, pokemon_type=p_type,
            pokemon_image=p_img)[0]
    p.save()


if __name__ == '__main__':
    # add(p_name="Pikachu", p_img="foo.png")
    # showDB()
    # populate()
    # print "Showing Data .... "
    showDB()
