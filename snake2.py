import pygame
import random

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000,1000))
    pygame.mixer.music.load('snake.mp3')
    pygame.mixer.music.play(-1)
    link_x = 500
    link_y = 480
    num_links = 1
    linkArray = [[link_x, link_y]]

    clock = pygame.time.Clock()  

    xa = random.randrange(20, 980, 5)
    ya = random.randrange(20, 950, 5)
    score = 0
    done = False
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    direction = 0 # 0 = right, 1 = left, 2 = up, 3 = down

    while not done:
        time_passed = clock.tick(17)

        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True
        
        screen.fill((0, 0, 0))

        screen.blit(pygame.image.load("apple.png").convert_alpha(), (xa, ya))
        scoresurface = myfont.render("Score: " + str(score), False, (255, 255, 255))
        screen.blit(scoresurface,(20,20))

        for peice in linkArray:
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(peice[0] , peice[1], 20, 20))
            

        if link_x > 1000 or link_x < 0 or link_y > 1000 or link_y < 0:
            done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: 
            if direction != 3 and direction != 2:
                direction = 2
        if pressed[pygame.K_DOWN]: 
            if direction != 2 and direction != 3:
                direction = 3               
        if pressed[pygame.K_LEFT]: 
            if direction != 0 and direction != 1:
                direction = 1              
        if pressed[pygame.K_RIGHT]:
            if direction != 1 and direction != 0:
                direction = 0
        
        if direction == 0:
            link_x += 20
        elif direction == 1:
            link_x -= 20 
        elif direction == 3:
            link_y += 20 
        elif direction == 2:
            link_y -= 20 

        if linkArray[len(linkArray)-1][0] != link_x or linkArray[len(linkArray)-1][1]!= link_y:
            linkArray.append([link_x, link_y])

        if abs(link_x - xa) < 17 and abs(link_y - ya) < 17:
            linkArray.append([linkArray[len(linkArray)-2][0], linkArray[len(linkArray)-2][1]])
            xa = random.randrange(20, 980, 5)
            ya = random.randrange(20, 950, 5)
            score += 1
            num_links += 1
   
        for l in linkArray:
            if len(linkArray) == num_links:
                break
            else:
                linkArray.remove(l)

        pygame.display.flip()

        for luko in range(len(linkArray)-2):
            if len(linkArray) < 5:
                break
            else:
                if linkArray[luko][0] == link_x and linkArray[luko][1] == link_y:
                    done = True

    textsurface = myfont.render('You lose', False, (255, 255, 255))
    screen.blit(textsurface,(485,470))
    pygame.display.flip()

if __name__ == "__main__":
    main()
