import requests
import pprint
import json
from tqdm import tqdm

pp = pprint.PrettyPrinter(indent=2)
baseUrl = "https://pokeapi.co/api/v2/"



def capitalize(word):
    if type(word) is not str:
        return word
    else:
        newWord = word
        for i, char in enumerate(word):
            if char.isalpha():
                if (i == 0):
                    newWord = word[0].upper() + word[1:]
                elif (i < (len(word) - 1)):
                    newWord = word[0:i - 1] + word[i].upper() + word[i + 1:]
                else:
                    newWord = word[0:i - 1] + word[i].upper()
                return newWord
            else:
                pass
        return newWord


class Pokemon():
    def __init__(self, dict):
        self.__dict__ = dict

    def show(self):
        print('-' * 25)
        print(str(self.id) + " - " + capitalize(self.name))
        types = [capitalize(t['type']['name']) for t in self.types]
        print('/'.join(types))
        print("Base Exp: " + str(self.base_experience))
        print("Height: " + str(self.height))
        print("Weight: " + str(self.weight))
        print('-' * 25)


class Pokedex():
    def __init__(self, pokelist=None):
        if not pokelist:
            self.pokemon = []
        else:
            self.pokemon = pokelist

    def populate(self, N=9):
        self.pokemon = []
        print("Retrieving {} Pokemon from PokeApi...".format(N))
        for id in tqdm(range(1, N + 1)):
            response = requests.get(baseUrl + "pokemon/" + str(id))
            pokemon = Pokemon(response.json())
            self.pokemon.append(pokemon)

    def show(self):
        for poke in self.pokemon:
            poke.show()


pokedex = Pokedex()
pokedex.populate()
pokedex.show()
