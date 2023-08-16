import pygame
import sys

pygame.init()

# Ventana
width_main = 1365
height_main = 710

# Colores
lila_color = (200, 160, 255)
celeste_color = (100, 200, 255)
gris_oscuro_color = (50, 50, 50)

# imagenes
imagen_path = "imagen.png"  # Asegúrate de tener la imagen en el mismo directorio que el script
imagen = pygame.image.load('gardevoir.gif')
imagen = pygame.transform.scale(imagen, (200, 200))  # Redimensionar la imagen a 200x200 píxeles

class Window:
    def __init__(self, title, bg_color):
        self.window = pygame.display.set_mode((width_main, height_main))
        self.title = title
        pygame.display.set_caption(title)
        self.bg_color = bg_color

    def show(self):
        self.window.fill(self.bg_color)
        pygame.display.set_caption(self.title)
        self.window.blit(imagen, (width_main//2 - imagen.get_width()//2, 100))  # Mostrar la imagen en la parte superior
        pygame.display.flip()

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

# Funciones para mostrar las ventanas de colores
def show_lila_window():
    lila_window = Window("Ventana Lila", lila_color)
    lila_window.title = "Ventana Lila"  # Establecer el título de la ventana
    button_grey = Button(25, 25, 50, 50, gris_oscuro_color, show_grey_window)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            button_grey.handle_event(event)
        lila_window.show()
        lila_window.window.blit(imagen, (width_main // 2 - imagen.get_width() // 2, 30))
        button_grey.draw(lila_window.window)
        pygame.display.flip()

    pygame.quit()

def show_celeste_window():
    celeste_window = Window("Ventana Celeste", celeste_color)
    button_grey = Button(25, 25, 50, 50, gris_oscuro_color, show_grey_window)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            button_grey.handle_event(event)
        celeste_window.show()
        button_grey.draw(celeste_window.window)
        pygame.display.flip()

    pygame.quit()

def show_grey_window():
    grey_window = Window("Ventana Gris Oscuro", gris_oscuro_color)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        grey_window.show()
        pygame.display.flip()

    pygame.quit()


main_window = Window("Ventana de 1920x1080", (255, 255, 255))
button_lila = Button(width_main//2 - 125, height_main//2 - 25, 100, 50, lila_color, show_lila_window)
button_celeste = Button(width_main//2 + 25, height_main//2 - 25, 100, 50, celeste_color, show_celeste_window)
button_exit = Button(width_main//2 - 50, height_main//2 + 75, 100, 50, (255, 0, 0), pygame.quit)

running = True
main_window.show()
button_lila.draw(main_window.window)
button_celeste.draw(main_window.window)
button_exit.draw(main_window.window)
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        button_lila.handle_event(event)
        button_celeste.handle_event(event)
        button_exit.handle_event(event)

pygame.quit()
sys.exit()
