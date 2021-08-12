import pypokedex

def getPokemonByName(name):
    return pypokedex.get(name=name)

def getPokemonType(pokemon):
    return pokemon.types

def getPokemonImage(pokemon):
    return pokemon.sprites