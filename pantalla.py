import pygame
import sys
from battle import *

pygame.font.init()

pygame.init()

# Ventana
width_main = 1365
height_main = 710

# Colores
gris_oscuro_color = (50, 50, 50)
verde_opaco_color = (50, 150, 50)

# imagenes
imagen1 = pygame.image.load('gardevoir.gif')
imagen1 = pygame.transform.scale(imagen1, (200, 200))
imagen2 = pygame.image.load('WhatsApp Image 2023-08-23 at 12.07.33.jpeg')
imagen2 = pygame.transform.scale(imagen2, (1365, 710))
bcg = pygame.image.load('bcg 1.jpg')
bcg = pygame.transform.scale(bcg, (1365, 710))
conexion = pygame.image.load("conexion.jpg")
conexion = pygame.transform.scale(conexion, (1365, 710))
battalla = pygame.image.load("batallaa.jpg")
battalla = pygame.transform.scale(battalla, (1365, 710))

# Ventanas
class Window:
    def __init__(self, title):
        self.window = pygame.display.set_mode((width_main, height_main))
        self.title = title
        pygame.display.set_caption(title)

    def show(self, image):
        pygame.display.set_caption(self.title)
        self.window.blit(image, (width_main // 2 - image.get_width() // 2, 0))
        pygame.display.flip()

    def show_input_text(self, max_values=6):
        input_font = pygame.font.Font(None, 36)
        input_text = ""
        input_active = True
        border_color = (0, 0, 0)
        text_color = (100, 100, 100)
        input_rect = pygame.Rect(100, height_main - 100, width_main - 200, 50)
        scroll_y = 0

        while input_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if input_text:
                            input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        # Modificar esta parte
                        if len(input_text) < max_values:
                            if event.unicode:  # Asegurarse de que el evento tenga un carácter
                                input_text += event.unicode
            pygame.draw.rect(self.window, border_color, input_rect, 2)
            pygame.draw.rect(self.window, text_color, input_rect.inflate(-4, -4))
            text_surface = input_font.render(input_text, True, border_color)
            self.window.blit(text_surface, (input_rect.x + 2, input_rect.y + 2 - scroll_y))
            pygame.display.flip()

        return input_text


# Botones
class Button:
    def __init__(self, x, y, width, height, color, callback):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.callback = callback

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                if self.rect.collidepoint(x, y):
                    self.callback()


def show_gris_oscuro_window():
    gris_window = Window("--------SELECTOR DE EQUIPO--------")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        gris_window.show(bcg)
        pygame.display.flip()
        input_number = gris_window.show_input_text(max_values=15)
        inp = input_number
        pokemon1 = pokemon_activo(inp)
        gris_window = Window("--------server--------")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            gris_window.show(conexion)
            server_tipo = gris_window.show_input_text(max_values=1)

            import random
            a = int(random.randint(0, 27))

            b = pokedex_actual[a].nombre
            print(b)

            enemigo = pokemon_activo(b)
            pokemon_enemigo = pygame.image.load(f"ani_e_{enemigo.poke_n}.gif")
            pokemon_enemigo = pygame.transform.scale(pokemon_enemigo, (300, 300))
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    gris_window = Window("---!ENCUENTRO SALVAJE¡---")
                gris_window.show(battalla)
                gris_window.show(pokemon_enemigo)
    pygame.quit()


main_window = Window("--------POKEMON BATTLE--------")  # Cambio de color aquí
button_green = Button(width_main // 2 - 550, height_main // 2 + 50, 500, 100, verde_opaco_color,
                      show_gris_oscuro_window)  # Cambio de nombre y color aquí
button_exit = Button(width_main // 2 - 550, height_main // 2 + 185, 500, 100, (205, 0, 0), pygame.quit)

running = True
main_window.show(imagen2)
button_green.draw(main_window.window)  # Cambio de nombre aquí
button_exit.draw(main_window.window)
pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        button_green.handle_event(event)  # Cambio de nombre aquí
        button_exit.handle_event(event)

pygame.quit()
sys.exit()
