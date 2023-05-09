import pygame
from pygame.locals import *
import random
#יבוא של הקבצים מתוך המחשב לוקאלי לאחר התקנה של ספריה דרך CMD ניתן להוריד את הקבצים מאתר PYGAME

#באן אנחנו מגדרים
size = width, height = (800, 800)
road_w = int(width/1.6)
#מידות לכביש
roadmark_w = int(width/80)
#גבולות כבישים
right_lane = width/2 +road_w/4
left_lene = width/2 - road_w/4
#משתנה של מהירות
speed = 1

#פקודת איתחול המשחק והספת משתה ריצה
pygame.init()
running = True
screen = pygame.display.set_mode(size)
#כאן אנחנו מציירים , הגדרת תצוגה רוחב וגובה
pygame.display.set_caption("first  pygame-car's")
screen.fill((60, 200, 0))


#פקודת השמה שמעדכנת את התצוגה
pygame.display.update()
#load images-user car
car = pygame.image.load("car_1.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height*0.8 #right
#load images-enemy car
car2 = pygame.image.load("car_2.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lene, height*0.2 #left
#לולאות אירועים עבור כדי שמשתמש יסגור  את התוכנית

counter = 0
while running:
    counter += 1
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("level up", speed)
    car2_loc[1] += speed
    if car2_loc[1 ] > height:
        if random.randint(0,1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lene, -200
    #end game
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] -180:
        print("GAME OVER!")
        break

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:#פקודת שימוש בכפתורים מקלדת
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w / 2), 0])


    pygame.draw.rect(
        screen,  # עובר דרך המסך
        (50, 50, 50),  # (צבע אפור)
        (width / 2 - road_w / 2, 0, road_w, height))  # (ציר X, צייר Y,הצורה הכוללת, גובה)
    pygame.draw.rect(
        screen,
        (255, 240, 60),  # (צבע צהוב)
        (width / 2 - roadmark_w / 2, 0, roadmark_w, height))  # קו הפרדה
    pygame.draw.rect(
        screen,
        (255, 255, 255),  # (צבע לבן)
        (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height))  # שוולאים לבנים
    pygame.draw.rect(
        screen,
        (255, 255, 255),  # (צבע לבן)
        (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height))

    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    pygame.display.update()

pygame.quit()
#פקודת יציאה של התוכנה