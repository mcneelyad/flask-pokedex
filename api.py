import pypokedex

# @param name: the name of the pokemon
# return: pokemon name
def getPokemonByName(name):
    return pypokedex.get(name=name)

# @param pokemon: the pokemon object
# return: the pokemon's type(s)
def getPokemonType(pokemon):
    return pokemon.types

# @param pokemon: the pokemon object
# return: the pokemon's images
def getPokemonImage(pokemon):
    return pokemon.sprites