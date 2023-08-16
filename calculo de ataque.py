def efecto_de_tipo(ataque, tipo_enemigo1, tipo_enemigo2):
    ganar = {
        "metal": ["hada", "hielo", "roca"],
        "volador": ["bicho", "planta", "lucha"],
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
        "niguno": [""],
    }
    perder = {
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
        "niguno": [""],
    }
    tipo = 1.0
    for x1 in ganar[ataque]:
        if tipo_enemigo1 == x1:
            tipo = tipo * 2

    for y1 in ganar[ataque]:
        if tipo_enemigo2 == y1:
            tipo = tipo * 2

    for x1 in perder[ataque]:
        if tipo_enemigo1 == x1:
            tipo = tipo / 2

    for y1 in perder[ataque]:
        if tipo_enemigo2 == y1:
            tipo = tipo / 2
    return tipo
