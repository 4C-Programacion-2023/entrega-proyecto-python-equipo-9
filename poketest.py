class tipo:
    def __init__(self, debil, fuerte):
        self.debil = debil
        self.fuerte = fuerte

class TipoPokemon:
    GANAR = {
        "metal": ["hada", "hielo", "roca"],
        "volador": ["bicho, planta, lucha"],
        "agua": ["roca", "tierra", "fuego"],
        "hielo": ["volador", "dragon", "tierra", "planta"],
        "planta": ["tierra", "roca", "agua"],
        "bicho": ["planta", "psiquico", "siniestro"],
        "electrico": ["volador", "agua"],
        "normal": [""],
        "roca": ["fuego", "hielo", "bicho", "volador"],
        "tierra": ["electrico", "roca", "veneno", "fuego", "metal"],
        "fuego": ["hielo", "planta", "bicho", "metal"],
        "lucha": ["hielo", "normal", "roca", "siniestro", "metal"],
        "hada": ["lucha", "dragon", "siniestro"],
        "psiquico": ["lucha", "veneno"],
        "veneno": ["planta", "hada"],
        "dragon": ["dragon"],
        "fantasma": ["psiquico", "fantasma"],
        "siniestro": ["psiquico", "fantasma"],
    }
    PERDER = {
        "metal": ["agua", "electrico", "fuego", "metal"],
        "volador": ["electrico", "roca", "metal"],
        "agua": ["agua", "planta", "dragon"],
        "hielo": ["hielo", "agua", "fuego", "metal"],
        "planta": ["volador", "planta", "bicho", "fuego", "veneno", "dragon", "metal"],
        "bicho": ["volador", "fuego", "lucha", "hada", "veneno", "fantasma", "metal"],
        "electrico": ["planta", "electrico", "dragon"],
        "normal": ["roca", "metal"],
        "roca": ["tierra", "lucha", "metal"],
        "tierra": ["planta", "bicho"],
        "fuego": ["agua", "roca", "fuego", "dragon"],
        "lucha": ["volador", "bicho", "hada", "psiquico", "veneno"],
        "hada": ["fuego", "veneno", "metal"],
        "psiquico": ["metal", "psiquico"],
        "veneno": ["roca", "tierra", "veneno", "fantasma"],
        "dragon": ["metal"],
        "fantasma": ["siniestro"],
        "siniestro": ["hada", "lucha", "siniestro"],

    }

    def __init__(self, nombre):
        self.nombre = nombre

    def __gt__(self, otro_tipo):
        if otro_tipo.nombre in self.GANAR[self.nombre]:
            print("TRUE")
            return True
        else:
            print("false")
            return False
class PokemonPokedex:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def gana_a_pokemon(self, otro_pokemon):
        return self.tipo > otro_pokemon.base.tipo

class Pokemon:
    def __init__(self, pokemon_base, nombre, nivel):
        self.base = pokemon_base
        self.nombre = nombre
        self.nivel = nivel

    def __str__(self):
        return f"{self.nivel}"

tipos = [
    TipoPokemon("metal"),
    TipoPokemon("volador"),
    TipoPokemon("agua"),
    TipoPokemon("hielo"),
    TipoPokemon("planta"),
    TipoPokemon("bicho"),
    TipoPokemon("electrico"),
    TipoPokemon("normal"),
    TipoPokemon("roca"),
    TipoPokemon("tierra"),
    TipoPokemon("fuego"),
    TipoPokemon("lucha"),
    TipoPokemon("hada"),
    TipoPokemon("psiquico"),
    TipoPokemon("veneno"),
    TipoPokemon("dragon"),
    TipoPokemon("fantasma"),
    TipoPokemon("siniestro"),
]

pokedex = [
    PokemonPokedex("Pickachu", tipos[1]),
    PokemonPokedex("pinplup", tipos[6]),
]
print('Hola, Bienvenido a PokeTest')
print('Deseas ver las indicaciones?(y/n)')
R = input('>>>> ')
if R == 'y':
    print('Hola, este es un juego basado en la primera y segunda generacion de la famosa saga Pokemon. \n En este juego podras batallar frenrte a tus amigos creando ya sea tu propio pokemon o con alguno de los que incluya el juego \n')
    print('los pokemon disponibles son: Venusuar(#3), Charizard(#6), Blastoise(#9), Butterfree(#12),\n Pidgeot(#18), Ratata(#19), Pikachu(#25), Nidoking(#34), Meowth(#52), Psyduck(#54), Alakazam(#65), Slowbro(#80), Farfetch d(#83),\n Gengar(#94), Magikarp(#129), Gyarados(#130), Aerodactyl(#142), Snorlax(#143), Dragonite(#149),\n Meganium(#154), Typhlosion(#157), Feraligatr(#160), Togepi(#175), Quagsire(#195), Shuckle(#213), Heracross(#214) y Tyranitar(#248)')
elif R == 'n':
    print('___')
else:
    print('Valor no valido')

equipo = [
    Pokemon(pokedex[0], "Pepito", 5),
    Pokemon(pokedex[1], "Otro picachu", 2),
]
print(equipo[0].base.gana_a_pokemon(equipo[1]))
print(tipos[3])
