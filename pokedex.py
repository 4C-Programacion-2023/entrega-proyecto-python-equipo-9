def buscar(a, b):
    i = 0
    while i < len(a):
        if a[i].numero == b:
            return i
        i = i + 1
    else:
        print("numero no encontrado")

class pokedex:
    def __init__(self, nombre, tipo1, tipo2, numero):
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.numero = numero

tipos = [
    "metal",
    "volador",
    "agua",
    "hielo",
    "planta",
    "bicho",
    "electrico",
    "normal",
    "roca",
    "tierra",
    "fuego",
    "lucha",
    "hada",
    "psiquico",
    "veneno",
    "dragon",
    "fantasma",
    "siniestro",
    "ninguno",
]
pokedex_actual = [
    pokedex("Venusaur", tipos[4], tipos[14], 3),
    pokedex("Charizard", tipos[10], tipos[1], 6),
    pokedex("Blastoise", tipos[2], tipos[18], 9),
    pokedex("Butterfree", tipos[5], tipos[1], 12),
    pokedex("Pidgeot", tipos[7], tipos[1], 18),
    pokedex("Ratata", tipos[7], tipos[18], 19),
    pokedex("Pikachu", tipos[6], tipos[18], 25),
    pokedex("Nidoking", tipos[14], tipos[9], 34),
    pokedex("Meowth", tipos[7], tipos[18], 52),
    pokedex("Psyduck", tipos[2], tipos[18], 54),
    pokedex("Alakazam", tipos[13], tipos[18], 65),
    pokedex("Slowbro", tipos[2], tipos[13], 80),
    pokedex("Magneton", tipos[6], tipos[0], 82),
    pokedex("Gengar", tipos[16], tipos[14], 94),
    pokedex("Onix", tipos[8], tipos[9], 95),
    pokedex("Magikarp", tipos[2], tipos[18], 129),
    pokedex("Gyarados", tipos[2], tipos[18], 130),
    pokedex("Aerodactyl", tipos[8], tipos[1], 142),
    pokedex("Snorlax", tipos[7], tipos[18], 143),
    pokedex("Dragonite", tipos[1], tipos[15], 149),
    pokedex("Meganuium", tipos[4], tipos[18], 154),
    pokedex("Typhlosion", tipos[10], tipos[18], 157),
    pokedex("Feraligatr", tipos[2], tipos[18], 160),
    pokedex("Togepi", tipos[12], tipos[18], 175),
    pokedex("Quagsire", tipos[2], tipos[9], 195),
    pokedex("Umbreon", tipos[17], tipos[18], 197),
    pokedex("Shuckle", tipos[5], tipos[8], 213),
    pokedex("Heracross", tipos[5], tipos[11], 214),
    pokedex("Tyranitar", tipos[9], tipos[17], 248),
    pokedex("Linguini", tipos[16], tipos[4], 201),
    pokedex("Mew", tipos[13], tipos[18], 151),
]
while True:
    inp = int(input("numero del pokemon: \n >>>"))
    entry = buscar(pokedex_actual, inp)
    print(f"nombre del pokemon: {pokedex_actual[entry].nombre}")
    print(f"tipo: {pokedex_actual[entry].tipo1} - {pokedex_actual[entry].tipo2}")
    print(f"numero del pokemon: {pokedex_actual[entry].numero}")
    print("-" * 8)
