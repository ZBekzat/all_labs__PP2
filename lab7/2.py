import pygame
import os


pygame.init()
screen = pygame.display.set_mode((500, 500))
black = (0, 0, 0)
screen.fill(black)


MUSIC_FOLDER = r"c:\Users\bekaz\OneDrive\Рабочий стол\New Folder\labs\lab7\sounds"


if not os.path.exists(MUSIC_FOLDER):
    print(f"Ошибка: Папка '{MUSIC_FOLDER}' не найдена!")
    exit()


sounds = [os.path.join(MUSIC_FOLDER, f) for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]


if not sounds:
    print(f"Ошибка: В папке '{MUSIC_FOLDER}' нет MP3-файлов!")
    exit()

index = 0  
isPaused = False
isPlayed = False  

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            index = (index + 1) % len(sounds)
            isPaused = False
            isPlayed = True
        
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            index = (index - 1) % len(sounds)
            isPaused = False
            isPlayed = True

        
        if event.type == pygame.KEYDOWN:
            if isPlayed:
                if isPaused:
                    pygame.mixer.music.unpause()
                    isPaused = False
                else:
                    pygame.mixer.music.load(sounds[index])
                    pygame.mixer.music.play()
            else:
                pygame.mixer.music.pause()
                isPaused = True
            isPlayed = not isPlayed

        
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.mixer.music.pause()
            isPaused = True
            isPlayed = False

    pygame.display.flip()
