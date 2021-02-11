import requests
import pygame

map_file = 'map.png'
map_file1 = 'map.jpg'


def gm(ln, lt, m):
    global map_file, mod
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={ln},{lt}&spn={m},{str(float(m) / 2)}&size=500,450&l={mod}"
    response = requests.get(map_request)
    if str(response) != '<Response [404]>':
        print('OK')
        if mod != 'map':
            with open(map_file1, 'wb') as file:
                file.write(response.content)
        else:
            with open(map_file, 'wb') as file:
                file.write(response.content)
    else:
        print('Error')


pygame.init()
pygame.display.set_caption('Maps api')
screen = pygame.display.set_mode((500, 500))
running = True

lnn = input('Введите долготу')
ltt = input('Введите широту')
mm = input('Введите масштаб 0-17')
mod = 'map'
p = 0

gm(lnn, ltt, mm)

screen.blit(pygame.image.load(map_file), (0, 0))


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and (float(ltt) + float(mm) < 90):
                ltt = str(float(ltt) + 0.5 * float(mm))
                gm(lnn, ltt, mm)
                screen.blit(pygame.image.load(map_file), (0, 0))
            if event.key == pygame.K_DOWN and (float(ltt) - float(mm) > -90):
                ltt = str(float(ltt) - 0.5 * float(mm))
                gm(lnn, ltt, mm)
                screen.blit(pygame.image.load(map_file), (0, 0))
            if event.key == pygame.K_LEFT and (float(lnn) - float(mm) > -180):
                lnn = str(float(lnn) - 0.5 * float(mm))
                gm(lnn, ltt, mm)
                screen.blit(pygame.image.load(map_file), (0, 0))
            if event.key == pygame.K_RIGHT and (float(lnn) + float(mm) < 180):
                lnn = str(float(lnn) + 0.5 * float(mm))
                gm(lnn, ltt, mm)
                screen.blit(pygame.image.load(map_file), (0, 0))

            if event.key == pygame.K_PAGEUP and (float(mm) < 175):
                mm = str(float(lnn) + 5)
                gm(lnn, ltt, mm)
                screen.blit(pygame.image.load(map_file), (0, 0))
            if event.key == pygame.K_PAGEDOWN and (float(mm) > 5):
                mm = str(float(lnn) + 5)
                gm(lnn, ltt, mm)
                screen.blit(pygame.image.load(map_file), (0, 0))

            if event.key == pygame.K_0:
                if p == 0:
                    mod = 'sat'
                    gm(lnn, ltt, mm)
                    p = p + 1
                    screen.blit(pygame.image.load(map_file1), (0, 0))
                elif p == 1:
                    mod = 'sat,skl'
                    gm(lnn, ltt, mm)
                    p = p + 1
                    screen.blit(pygame.image.load(map_file1), (0, 0))
                elif p == 2:
                    mod = 'map'
                    print(123)
                    gm(lnn, ltt, mm)
                    p = 0
                    screen.blit(pygame.image.load(map_file), (0, 0))

    pygame.display.flip()
pygame.quit()
