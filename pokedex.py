def buscar(a, b):
    i = 0
    while i < len(a):
        if a[i].nombre == b:
            return i
        i = i + 1
    else:
        print("numero no encontrado")


class atkss:
    def __init__(self, tipo, tatk):
        self.tatk = tatk
        self.tipo = tipo


class pokedex:
    def __init__(self, nombre, tipo1, tipo2, numero, hp, atk, defn, satk, sdefn, vel, ataque1, ataque2, ataque3,
                 ataque4):
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
        self.ataque1 = ataque1
        self.ataque2 = ataque2
        self.ataque3 = ataque3
        self.ataque4 = ataque4


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
tiposatk = [
    "Me-olvide-que-el-primero-era-0",
    "normal",
    "special",
]
atkss = [
    atkss(tipos[0], tiposatk[1]),  # metal
    atkss(tipos[0], tiposatk[2]),
    atkss(tipos[1], tiposatk[1]),  # volador
    atkss(tipos[1], tiposatk[2]),
    atkss(tipos[2], tiposatk[1]),  # agua
    atkss(tipos[2], tiposatk[2]),
    atkss(tipos[3], tiposatk[1]),  # hielo
    atkss(tipos[3], tiposatk[2]),
    atkss(tipos[4], tiposatk[1]),  # planta
    atkss(tipos[4], tiposatk[2]),
    atkss(tipos[5], tiposatk[1]),  # bicho
    atkss(tipos[5], tiposatk[2]),
    atkss(tipos[6], tiposatk[1]),  # electrico
    atkss(tipos[6], tiposatk[2]),
    atkss(tipos[7], tiposatk[1]),  # normal
    atkss(tipos[7], tiposatk[2]),
    atkss(tipos[8], tiposatk[1]),  # roca
    atkss(tipos[8], tiposatk[2]),
    atkss(tipos[9], tiposatk[1]),  # tierra
    atkss(tipos[9], tiposatk[2]),
    atkss(tipos[10], tiposatk[1]),  # fuego
    atkss(tipos[10], tiposatk[2]),
    atkss(tipos[11], tiposatk[1]),  # lucha
    atkss(tipos[11], tiposatk[2]),
    atkss(tipos[12], tiposatk[1]),  # hada
    atkss(tipos[12], tiposatk[2]),
    atkss(tipos[13], tiposatk[1]),  # psiquico
    atkss(tipos[13], tiposatk[2]),
    atkss(tipos[14], tiposatk[1]),  # veneno
    atkss(tipos[14], tiposatk[2]),
    atkss(tipos[15], tiposatk[1]),  # dragon
    atkss(tipos[15], tiposatk[2]),
    atkss(tipos[16], tiposatk[1]),  # fantasma
    atkss(tipos[16], tiposatk[2]),
    atkss(tipos[17], tiposatk[1]),  # siniestro
    atkss(tipos[17], tiposatk[2]),
]
pokedex_actual = [
    pokedex("Venusaur", tipos[4], tipos[14], 3, 80, 82, 83, 100, 100, 80, atkss[14], atkss[8], atkss[9], atkss[29]),
    pokedex("Charizard", tipos[10], tipos[1], 6, 78, 84, 78, 109, 85, 100, atkss[14], atkss[3], atkss[21], atkss[30]),
    pokedex("Blastoise", tipos[2], tipos[18], 9, 79, 83, 100, 85, 105, 78, atkss[14], atkss[4], atkss[5], atkss[7]),
    pokedex("Butterfree", tipos[5], tipos[1], 12, 60, 45, 50, 90, 80, 70, atkss[14], atkss[3], atkss[10], atkss[11]),
    pokedex("Pidgeot", tipos[7], tipos[1], 17, 83, 80, 75, 70, 70, 101, atkss[14], atkss[15], atkss[2], atkss[3]),
    pokedex("Ratata", tipos[7], tipos[18], 19, 30, 56, 35, 25, 35, 72, atkss[14], atkss[15], atkss[22], atkss[35]),
    pokedex("Pikachu", tipos[6], tipos[18], 25, 45, 55, 50, 50, 60, 120, atkss[14], atkss[0], atkss[12], atkss[13]),
    pokedex("Nidoking", tipos[14], tipos[9], 34, 81, 102, 77, 85, 75, 85, atkss[14], atkss[22], atkss[18], atkss[28]),
    pokedex("Meowth", tipos[7], tipos[18], 52, 40, 45, 35, 40, 40, 90, atkss[14], atkss[15], atkss[22], atkss[35]),
    pokedex("Psyduck", tipos[2], tipos[18], 54, 50, 52, 48, 65, 50, 55, atkss[14], atkss[4], atkss[5], atkss[27]),
    pokedex("Alakazam", tipos[13], tipos[18], 65, 55, 50, 45, 135, 95, 120, atkss[26], atkss[27], atkss[34], atkss[33]),
    pokedex("Slowbro", tipos[2], tipos[13], 80, 95, 75, 110, 100, 80, 30, atkss[26], atkss[27], atkss[7], atkss[5]),
    pokedex("Magneton", tipos[6], tipos[0], 82, 50, 60, 95, 120, 70, 70, atkss[0], atkss[1], atkss[12], atkss[13]),
    pokedex("Gengar", tipos[16], tipos[14], 94, 60, 65, 60, 130, 75, 110, atkss[32], atkss[33], atkss[29], atkss[35]),
    pokedex("Onix", tipos[8], tipos[9], 95, 35, 45, 160, 30, 45, 70, atkss[18], atkss[16], atkss[17], atkss[1]),
    pokedex("Magikarp", tipos[2], tipos[18], 129, 20, 10, 55, 15, 20, 80, atkss[14], atkss[15], atkss[4], atkss[5]),
    pokedex("Gyarados", tipos[2], tipos[18], 130, 95, 125, 79, 60, 100, 81, atkss[2], atkss[4], atkss[31], atkss[7]),
    pokedex("Aerodactyl", tipos[8], tipos[1], 142, 80, 105, 65, 60, 75, 130, atkss[2], atkss[16], atkss[17], atkss[30]),
    pokedex("Snorlax", tipos[7], tipos[18], 143, 160, 110, 65, 65, 110, 30, atkss[14], atkss[15], atkss[18], atkss[22]),
    pokedex("Dragonite", tipos[1], tipos[15], 149, 91, 134, 95, 100, 100, 80, atkss[14], atkss[30], atkss[31], atkss[2]),
    pokedex("Meganuium", tipos[4], tipos[18], 154, 80, 82, 100, 83, 100, 80, atkss[14], atkss[8], atkss[9], atkss[30]),
    pokedex("Typhlosion", tipos[10], tipos[18], 157, 78, 84, 78, 109, 85, 100, atkss[14], atkss[20], atkss[21], atkss[35]),
    pokedex("Feraligatr", tipos[2], tipos[18], 160, 85, 105, 100, 79, 83, 78, atkss[14], atkss[4], atkss[5], atkss[7]),
    pokedex("Togepi", tipos[12], tipos[18], 175, 35, 20, 65, 40, 65, 20, atkss[15], atkss[23], atkss[24], atkss[25]),
    pokedex("Quagsire", tipos[2], tipos[9], 195, 95, 85, 85, 65, 65, 35, atkss[4], atkss[6], atkss[18], atkss[19]),
    pokedex("Umbreon", tipos[17], tipos[18], 197, 95, 65, 110, 60, 130, 65, atkss[23], atkss[28], atkss[34], atkss[35]),
    pokedex("Shuckle", tipos[5], tipos[8], 213, 20, 10, 230, 10, 230, 5, atkss[14], atkss[0], atkss[10], atkss[11]),
    pokedex("Heracross", tipos[5], tipos[11], 214, 80, 125, 75, 40, 95, 85, atkss[14], atkss[2], atkss[10], atkss[22]),
    pokedex("Tyranitar", tipos[9], tipos[17], 248, 100, 134, 110, 95, 100, 61, atkss[22], atkss[16], atkss[17], atkss[35]),
    pokedex("Linguini", tipos[7], tipos[10], 6900, 60, 80, 63, 269, 220, 78, atkss[14], atkss[21], atkss[11], atkss[7]),
    pokedex("Mew", tipos[13], tipos[18], 151, 100, 100, 100, 100, 100, 100, atkss[26], atkss[27], atkss[24], atkss[15]),
]
