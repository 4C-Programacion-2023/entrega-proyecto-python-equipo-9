def buscar(a, b):
    i = 0
    while i < len(a):
        if a[i].numero == b:
            return i
        i = i + 1
    else:
        print("numero no encontrado")


class pokedex:
    def __init__(self, nombre, tipo1, tipo2, numero, hp, atk, defn, satk, sdefn, vel):
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.numero = numero
        self.hp = hp
        self.atk = atk
        self.defn = defn
        self.satk = satk
        self.sdefn = sdefn
        self.vel = vel


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
    pokedex("Venusaur", tipos[4], tipos[14], 3, 80, 82, 83, 100, 100, 80),
    pokedex("Charizard", tipos[10], tipos[1], 6, 78, 84, 78, 109, 85, 100),
    pokedex("Blastoise", tipos[2], tipos[18], 9, 79, 83, 100, 85, 105, 78),
    pokedex("Butterfree", tipos[5], tipos[1], 12, 60, 45, 50, 90, 80, 70),
    pokedex("Pidgeot", tipos[7], tipos[1], 18, 83, 80, 75, 70, 70, 101),
    pokedex("Ratata", tipos[7], tipos[18], 19, 30, 56, 35, 25, 35, 72),
    pokedex("Pikachu", tipos[6], tipos[18], 25, 45, 55, 50, 50, 60, 120),
    pokedex("Nidoking", tipos[14], tipos[9], 34, 81, 102, 77, 85, 75, 85),
    pokedex("Meowth", tipos[7], tipos[18], 52, 40, 45, 35, 40, 40, 90),
    pokedex("Psyduck", tipos[2], tipos[18], 54, 50, 52, 48, 65, 50, 55),
    pokedex("Alakazam", tipos[13], tipos[18], 65, 55, 50, 45, 135, 95, 120),
    pokedex("Slowbro", tipos[2], tipos[13], 80, 95, 75, 110, 100, 80, 30),
    pokedex("Magneton", tipos[6], tipos[0], 82, 50, 60, 95, 120, 70, 70),
    pokedex("Gengar", tipos[16], tipos[14], 94, 60, 65, 60, 130, 75, 110),
    pokedex("Onix", tipos[8], tipos[9], 95, 35, 45, 160, 30, 45, 70),
    pokedex("Magikarp", tipos[2], tipos[18], 129, 20, 10, 55, 15, 20, 80),
    pokedex("Gyarados", tipos[2], tipos[18], 130, 95, 125, 79, 60, 100, 81),
    pokedex("Aerodactyl", tipos[8], tipos[1], 142, 80, 105, 65, 60, 75, 130),
    pokedex("Snorlax", tipos[7], tipos[18], 143, 160, 110, 65, 65, 110, 30),
    pokedex("Dragonite", tipos[1], tipos[15], 149, 91, 134, 95, 100, 100, 80),
    pokedex("Meganuium", tipos[4], tipos[18], 154, 80, 82, 100, 83, 100, 80),
    pokedex("Typhlosion", tipos[10], tipos[18], 157, 78, 84, 78, 109, 85, 100),
    pokedex("Feraligatr", tipos[2], tipos[18], 160, 85, 105, 100, 79, 83, 78),
    pokedex("Togepi", tipos[12], tipos[18], 175, 35, 20, 65, 40, 65, 20),
    pokedex("Quagsire", tipos[2], tipos[9], 195, 95, 85, 85, 65, 65, 35),
    pokedex("Umbreon", tipos[17], tipos[18], 197, 95, 65, 110, 60, 130, 65),
    pokedex("Shuckle", tipos[5], tipos[8], 213, 20, 10, 230, 10, 230, 5),
    pokedex("Heracross", tipos[5], tipos[11], 214, 80, 125, 75, 40, 95, 85),
    pokedex("Tyranitar", tipos[9], tipos[17], 248, 100, 134, 110, 95, 100, 61),
    pokedex("Linguini", tipos[7], tipos[10], 201, 60, 80, 63, 269, 220, 78),
    pokedex("Mew", tipos[13], tipos[18], 151, 100, 100, 100, 100, 100, 100),
]
while True:
    inp = int(input("numero del pokemon: \n >>> "))
    entry = buscar(pokedex_actual, inp)
    print(f"numero del pokemon: {pokedex_actual[entry].numero}")
    print(f"nombre del pokemon: {pokedex_actual[entry].nombre}")
    print(f"tipo: {pokedex_actual[entry].tipo1} - {pokedex_actual[entry].tipo2}")
    print(f"hp: {pokedex_actual[entry].hp}  atk: {pokedex_actual[entry].atk}  def: {pokedex_actual[entry].defn}  satk: {pokedex_actual[entry].satk}  sdef: {pokedex_actual[entry].sdefn}  vel: {pokedex_actual[entry].vel}" )
    print("-" * 10)