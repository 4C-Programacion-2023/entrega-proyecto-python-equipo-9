from pokedex import *


class pokemon_activo:
    def __init__(self, poke):
        entry = buscar(pokedex_actual, poke)
        self.poke_n = pokedex_actual[entry].numero
        self.hp_actual = pokedex_actual[entry].hp
        print(f"numero del pokemon: {pokedex_actual[entry].numero}")
        print(f"nombre del pokemon: {pokedex_actual[entry].nombre}")
        print(f"tipo: {pokedex_actual[entry].tipo1} - {pokedex_actual[entry].tipo2}")
        print(
            f"hp: {pokedex_actual[entry].hp}  atk: {pokedex_actual[entry].atk} "
            f" def: {pokedex_actual[entry].defn}  satk: {pokedex_actual[entry].satk}  "
            f"sdef: {pokedex_actual[entry].sdefn}  vel: {pokedex_actual[entry].vel}")
        print("-" * 10)
