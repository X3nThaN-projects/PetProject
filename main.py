from Menu import Menu
from settings import Settings
import pygame

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("resources/Eternal Sands.mp3")
    font = pygame.font.Font(None, 32)
    settings = Settings(800, 600, font)
    screen = pygame.display.set_mode(settings.getWND_SIZE())

    main_menu = Menu(
        pygame= pygame, 
        settings= settings,
        screen= screen,
        items= ["Continue", "New Game", "Options", "Exit"],
        background = "resources/main_menu.jpg")
    
    options_menu = Menu(
        pygame= pygame, 
        settings= settings,
        screen= screen,
        items= ["Video", "Controls", "Audio", "Back"])
    
    current_menu = main_menu
    
    pygame.mixer.music.play()
    
    while True:
        screen.fill((255, 255, 255))
        
        current_menu.render_items()
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    print(".......")
                    print("Saving process")
                    #TODO GAMESAVE
                    print("Saving complete")
                    print("Exiting...")
                    exit(0)
                    break
                case pygame.MOUSEBUTTONDOWN:
                    print("Click!")
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos != None:
                        #TODO MENUING
                        break                    

                    break
                case pygame.KEYDOWN:
                    match event.key:     
                        case pygame.K_w:
                            current_menu.set_point(current_menu.get_point() - 1)
                            break
                        
                        case pygame.K_s:
                            current_menu.set_point(current_menu.get_point() + 1)
                            break

                        case pygame.K_KP_ENTER:
                            #TODO SELECT
                            break
                    break


        pygame.display.flip()
