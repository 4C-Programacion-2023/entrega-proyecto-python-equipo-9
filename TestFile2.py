import pygame
import sys

pygame.init()

# Ventana
width, height = 1920, 1080

# Colores
lilacolor = (200, 160, 255)
lightbluecolor = (100, 200, 255)
colorhumilde = (50, 50, 50)

# --imagenes--
# img fondo 1
imagenfondo1 = "background.png"
imagenf1 = pygame.image.load('background.jpg')
imagenf1 = pygame.transform.scale(imagenf1, (1540, 880))

# img pokemon 1
imagenp1 = "img.png"
imagen_p1 = pygame.image.load('gardevoir.gif')
imagen_p1 = pygame.transform.scale(imagen_p1, (width, height))


class Window:
    def __init__(self, title, bg_color):
        self.window = pygame.display.set_mode((width, height))
        self.title = title
        pygame.display.set_caption(title)
        self.bg_color = bg_color

    def show(self):
        self.window.fill(self.bg_color)
        pygame.display.set_caption(self.title)
        self.window.blit(imagenf1, (width // 2 - imagenf1.get_width() // 2, 100))
        pygame.display.flip()

        pygame.display.set_caption(self.title)
        pygame.display.flip()


def close_window(window):
    pygame.display.set_caption("Cerrando ventana...")
    pygame.time.wait(1000)  # Espera de 1 segundo para simular cierre de la ventana
    pygame.display.set_caption(window.title)  # Restaurar el título de la ventana anterior
    pygame.display.quit()


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


# Ventanas
def show_lila_window():
    lila_window = Window("Ventana Lila", lilacolor, imagenf1)
    lila_window.title = "Ventana Lila"
    button_grey = Button(25, 25, 50, 50, colorhumilde, show_grey_window)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            button_grey.handle_event(event)
        lila_window.show()
        button_grey.draw(lila_window.window)
        pygame.display.flip()
    pygame.quit()

def show_celeste_window():
    celeste_window = Window("Ventana Celeste", lightbluecolor, imagenf1)
    button_grey = Button(25, 25, 50, 50, colorhumilde, show_grey_window)
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
    grey_window = Window("Ventana Gris Oscuro", colorhumilde)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        grey_window.show()
        pygame.display.flip()

    pygame.quit()


main_window = Window("Ventana de 1920x1080", (255, 255, 255))
button_lila = Button(width // 2 - 700, height // 2 + 0, 500, 100, (78, 158, 92), show_lila_window)
button_celeste = Button(width // 2 - 700, height // 2 + 150, 500, 100, (105, 155, 210), show_celeste_window)
button_exit = Button(width // 2 - 700, height // 2 + 300, 500, 100, (192, 4, 18), pygame.quit)

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
