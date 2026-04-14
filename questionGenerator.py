import sys
import pygame
import random

#Initializing
##pygame.
pygame.init()

##Application window settings.
resolution = (1280,720)
pygame.display.set_caption("RandomMathematicalQuestions")
window = pygame.display.set_mode(resolution)
windowWidth = window.get_width()
windowHeight = window.get_height()
windowClock = pygame.time.Clock()

##Font settings.
font1 = pygame.font.SysFont('rockwell', 70, bold=True)
font2 = pygame.font.SysFont('rockwell', 50, bold=False)
font3 = pygame.font.SysFont('rockwell', 50, bold=False)
font4 = pygame.font.SysFont('rockwell', 50, bold=False)
font5 = pygame.font.SysFont('rockwell', 40, bold=True)
font6 = pygame.font.SysFont('rockwell', 70, bold=False)
font7 = pygame.font.SysFont('rockwell', 40, bold=True)
font8 = pygame.font.SysFont('rockwell', 70, bold=False)
font9 = pygame.font.SysFont('rockwell', 40, bold=False)
font10 = pygame.font.SysFont('rockwell', 60, bold=False)

##Text settings.
text1 = font1.render("Random Mathematical Questions", True, ("#FFFFFF"))
text1Center = text1.get_rect(center = (windowWidth / 2, windowHeight / 2 - 200))
text2 = font2.render("Click here to continue", True, ("#FFFFFF"))
text2Center = text2.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text3 = font3.render("Click here to continue", True, ("#808080"))
text3Center = text3.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text4 = font4.render("Addition, Subtraction, Multiplication or Division?", True, ("#FFFFFF"))
text4Center = text4.get_rect(center = (windowWidth / 2, windowHeight / 2 - 200))
text5 = font5.render("+", True, ("#FFFFFF"))
text5Center = text5.get_rect(center = (windowWidth / 2 - 450, windowHeight / 2 + 50))
text6 = font5.render("-", True, ("#FFFFFF"))
text6Center = text6.get_rect(center = (windowWidth / 2 - 150, windowHeight / 2 + 50))
text7 = font5.render("×", True, ("#FFFFFF"))
text7Center = text7.get_rect(center = (windowWidth / 2 + 150, windowHeight / 2 + 50))
text8 = font5.render("÷", True, ("#FFFFFF"))
text8Center = text8.get_rect(center = (windowWidth / 2 + 450, windowHeight / 2 + 50))
text9 = font5.render("+", True, ("#808080"))
text9Center = text9.get_rect(center = (windowWidth / 2 - 450, windowHeight / 2 + 50))
text10 = font5.render("-", True, ("#808080"))
text10Center = text10.get_rect(center = (windowWidth / 2 - 150, windowHeight / 2 + 50))
text11 = font5.render("×", True, ("#808080"))
text11Center = text11.get_rect(center = (windowWidth / 2 + 150, windowHeight / 2 + 50))
text12 = font5.render("÷", True, ("#808080"))
text12Center = text12.get_rect(center = (windowWidth / 2 + 450, windowHeight / 2 + 50))
text13 = font6.render("How many digits?", True, ("#FFFFFF"))
text13Center = text13.get_rect(center = (windowWidth / 2, windowHeight / 2 - 200))
text14 = font7.render("1", True, ("#FFFFFF"))
text14Center = text14.get_rect(center = (windowWidth / 2 - 450, windowHeight / 2 + 50))
text15 = font7.render("2", True, ("#FFFFFF"))
text15Center = text15.get_rect(center = (windowWidth / 2 - 150, windowHeight / 2 + 50))
text16 = font7.render("3", True, ("#FFFFFF"))
text16Center = text16.get_rect(center = (windowWidth / 2 + 150, windowHeight / 2 + 50))
text17 = font7.render("4", True, ("#FFFFFF"))
text17Center = text17.get_rect(center = (windowWidth / 2 + 450, windowHeight / 2 + 50))
text18 = font7.render("1", True, ("#808080"))
text18Center = text18.get_rect(center = (windowWidth / 2 - 450, windowHeight / 2 + 50))
text19 = font7.render("2", True, ("#808080"))
text19Center = text19.get_rect(center = (windowWidth / 2 - 150, windowHeight / 2 + 50))
text20 = font7.render("3", True, ("#808080"))
text20Center = text20.get_rect(center = (windowWidth / 2 + 150, windowHeight / 2 + 50))
text21 = font7.render("4", True, ("#808080"))
text21Center = text21.get_rect(center = (windowWidth / 2 + 450, windowHeight / 2 + 50))
text22 = font8.render("", True, ("#FFFFFF"))
text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
text23 = font9.render("", True, ("#FFFFFF"))
text23Center = text23.get_rect(center = (windowWidth / 2, windowHeight / 2))
text24 = font8.render(("Your Score: ?"), True, ("#FFFFFF"))
text24Center = text24.get_rect(center = (windowWidth / 2, windowHeight / 2))
text25 = font8.render(("Game Mode: ?"), True, ("#FFFFFF"))
text25Center = text25.get_rect(center = (windowWidth / 2, windowHeight / 2))
text26 = font8.render("Difficulty: ?", True, ("#FFFFFF"))
text26Center = text26.get_rect(center = (windowWidth / 2, windowHeight / 2))

text27 = font10.render("Restart Round", True, ("#FFFFFF"))
text27Center = text27.get_rect(center = (windowWidth / 2, windowHeight / 2 + 250))
text28 = font10.render("Restart Game", True, ("#FFFFFF"))
text28Center = text28.get_rect(center = (windowWidth / 2, windowHeight / 2 + 250))
text29 = font10.render("Change Mode", True, ("#FFFFFF"))
text29Center = text29.get_rect(center = (windowWidth / 2, windowHeight / 2 + 250))
text30 = font10.render("Change Difficulty", True, ("#FFFFFF"))
text30Center = text30.get_rect(center = (windowWidth / 2, windowHeight / 2 + 250))
text31 = font9.render("", True, ("#FFFFFF"))
text31Center = text31.get_rect(center = (windowWidth / 2, windowHeight / 2))

image1 = pygame.image.load("images/userHearts/IMG_1.png")
image1Center = image1.get_rect(center = (windowWidth / 2, windowHeight / 2))
image2 = pygame.image.load("images/userHearts/IMG_2.png")
image2Center = image2.get_rect(center = (windowWidth / 2, windowHeight / 2))
image3 = pygame.image.load("images/userHearts/IMG_3.png")
image3Center = image3.get_rect(center = (windowWidth / 2, windowHeight / 2))
image4 = pygame.image.load("images/userHearts/IMG_4.png")
image4Center = image4.get_rect(center = (windowWidth / 2, windowHeight / 2))
image5 = pygame.image.load("images/userHearts/IMG_5.png")
image5Center = image5.get_rect(center = (windowWidth / 2, windowHeight / 2))
image6 = pygame.image.load("images/userHearts/IMG_6.png")
image6Center = image6.get_rect(center = (windowWidth / 2, windowHeight / 2))
image7 = pygame.image.load("images/userStreak/IMG_1.png")
image7Center = image7.get_rect(center = (windowWidth / 2, windowHeight / 2))
image8 = pygame.image.load("images/Background/IMG_1.png")
image8Center = image8.get_rect(center = (windowWidth / 2, windowHeight / 2))

#Variables
##Initializing main menu
display = 1
mainMenuNum = 1
mainMenu1Num = 1
mainMenu2Num = 1
mainMenu3Num = 1
display3Num = 1
RandomLevelNum1 = False
RandomLevelNum2 = False

userInput = ""
userAnswer = ""
userStreak = 0
userTimer = True
userScore = 0
userHearts = 3
userHeartsNum = 0
userMode = ""
userDifficulty = ""
userModeNum = 0
questionNum = ["?", "?", "?"]
questionNum2 = ["?", "?", "?"]
question = True

def mainMenu1():
    window.fill(("#000000"))
    window.blit(text1,text1Center)
    pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 3.55, windowHeight / 2.1, 563, 150])
    pygame.draw.rect(window,("#000000"),[windowWidth / 3.55 + 5, windowHeight / 2.1 + 5, 563 - 10, 150 - 10])
    window.blit(text2,text2Center)

def mainMenu2():
    ##Background colour
    window.fill(("#000000"))

    #Title text
    window.blit(text4,text4Center)

    #+ button
    pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 11, windowHeight / 2.1, 150, 150])
    pygame.draw.rect(window,("#000000"),[windowWidth / 11 + 5, windowHeight / 2.1 + 5, 150 - 10, 150 - 10])
    window.blit(text5,text5Center)

    #- button
    pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 3.08, windowHeight / 2.1, 150, 150])
    pygame.draw.rect(window,("#000000"),[windowWidth / 3.08 + 5, windowHeight / 2.1 + 5, 150 - 10, 150 - 10])
    window.blit(text6,text6Center)

    #× button
    pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 1.79, windowHeight / 2.1, 150, 150])
    pygame.draw.rect(window,("#000000"),[windowWidth / 1.79 + 5, windowHeight / 2.1 + 5, 150 - 10, 150 - 10])
    window.blit(text7,text7Center)

    #÷ button
    pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 1.26, windowHeight / 2.1, 150, 150])
    pygame.draw.rect(window,("#000000"),[windowWidth / 1.26 + 5, windowHeight / 2.1 + 5, 150 - 10, 150 - 10])
    window.blit(text8,text8Center)

def mainMenu3():
    #UI (User Interface) elements
    ##Background colour
    window.fill(("#000000"))

    ##Title text
    window.blit(text13,text13Center)

    ##1 button
    pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 11, windowHeight / 2.1, 150, 150])
    pygame.draw.rect(window,("#000000"),[windowWidth / 11 + 5, windowHeight / 2.1 + 5, 150 - 10, 150 - 10])
    window.blit(text14,text14Center)

    ##2 button
    pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 3.08, windowHeight / 2.1, 150, 150])
    pygame.draw.rect(window,("#000000"),[windowWidth / 3.08 + 5, windowHeight / 2.1 + 5, 150 - 10, 150 - 10])
    window.blit(text15,text15Center)

    ##3 button
    pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 1.79, windowHeight / 2.1, 150, 150])
    pygame.draw.rect(window,("#000000"),[windowWidth / 1.79 + 5, windowHeight / 2.1 + 5, 150 - 10, 150 - 10])
    window.blit(text16,text16Center)

    ##4 button
    pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 1.26, windowHeight / 2.1, 150, 150])
    pygame.draw.rect(window,("#000000"),[windowWidth / 1.26 + 5, windowHeight / 2.1 + 5, 150 - 10, 150 - 10])
    window.blit(text17,text17Center)

#Main Application
while True:
    windowMouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            sys.exit()

        if (display == 1 and mainMenuNum == 1):
            if (windowMouse[1] >= 340 and windowMouse[1] <= 490) and (windowMouse[0] >= 359 and windowMouse[0] <= 922):
                mainMenu1Num = 2

                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(500)
                    mainMenuNum = 2
            else:
                mainMenu1Num = 1

        elif (display == 1 and mainMenuNum == 2):
            if (windowMouse[1] >= 340 and windowMouse[1] <= 490) and (windowMouse[0] >= 115 and windowMouse[0] <= 265):
                mainMenu2Num = 2
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(500)
                    userMode = "+"
                    mainMenuNum = 3
                
            elif (windowMouse[1] >= 340 and windowMouse[1] <= 490) and (windowMouse[0] >= 414 and windowMouse[0] <= 564):
                mainMenu2Num = 3
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(500)
                    userMode = "-"
                    mainMenuNum = 3
                
            elif (windowMouse[1] >= 340 and windowMouse[1] <= 490) and (windowMouse[0] >= 714 and windowMouse[0] <= 864):
                mainMenu2Num = 4
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(500)
                    userMode = "×"
                    mainMenuNum = 3
                
            elif (windowMouse[1] >= 340 and windowMouse[1] <= 490) and (windowMouse[0] >= 1014 and windowMouse[0] <= 1164):
                mainMenu2Num = 5

                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(500)
                    userMode = "÷"
                    mainMenuNum = 3
            
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    print ("Secret Level Unlocked !")
                    RandomLevelNum1 = True
                    mainMenuNum = 3
        
            else: 
                mainMenu2Num = 1

        elif (display == 1 and mainMenuNum == 3 and userDifficulty == ""):
            if (windowMouse[1] >= 340 and windowMouse[1] <= 490) and (windowMouse[0] >= 115 and windowMouse[0] <= 265):
                mainMenu3Num = 2
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(500)
                    userDifficulty = 1
                    display = 2
                
            elif (windowMouse[1] >= 340 and windowMouse[1] <= 490) and (windowMouse[0] >= 414 and windowMouse[0] <= 564):
                mainMenu3Num = 3
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(500)
                    userDifficulty = 2
                    display = 2
                
            elif (windowMouse[1] >= 340 and windowMouse[1] <= 490) and (windowMouse[0] >= 714 and windowMouse[0] <= 864):
                mainMenu3Num = 4
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(500)
                    userDifficulty = 3
                    display = 2
                
            elif (windowMouse[1] >= 340 and windowMouse[1] <= 490) and (windowMouse[0] >= 1014 and windowMouse[0] <= 1164):
                mainMenu3Num = 5
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(500)
                    userDifficulty = 4
                    display = 2

            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    RandomLevelNum2 = True
                    display = 2

            else:
                mainMenu3Num = 1

        elif (display == 2):
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_0) or (event.key == pygame.K_1) or (event.key == pygame.K_2) or (event.key == pygame.K_3) or (event.key == pygame.K_4) or (event.key == pygame.K_5) or (event.key == pygame.K_6) or (event.key == pygame.K_7) or (event.key == pygame.K_8) or (event.key == pygame.K_9):
                    userInput += event.unicode
                if (event.key == pygame.K_BACKSPACE):
                    userInput = userInput [0:-1] 
                if (event.key == pygame.K_RETURN):
                    userAnswer = userInput
                    userInput = ""
        
        elif (display == 3):
            #restart round.
            if (windowMouse[1] >= 340 and windowMouse[1] <= 490) and (windowMouse[0] >= 115 and windowMouse[0] <= 265):
                display3Num = 2
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(500)
                    display3Num = 1
                    display = 2
                    userInput = ""
                    userAnswer = ""
                    userStreak = 0
                    userTimer = True
                    userScore = 0
                    userHearts = 3
                    userHeartsNum = 0
                    questionNum = ["?", "?", "?"]
                    questionNum2 = ["?", "?", "?"]
                    question = True

            #Restart the game.
            elif (windowMouse[1] >= 340 and windowMouse[1] <= 490) and (windowMouse[0] >= 414 and windowMouse[0] <= 564):
                display3Num = 3
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(500)
                    display3Num = 1
                    display = 1
                    mainMenuNum = 1
                    mainMenu1Num = 1
                    mainMenu2Num = 1
                    mainMenu3Num = 1
                    RandomLevelNum1 = False
                    RandomLevelNum2 = False

                    userInput = ""
                    userAnswer = ""
                    userStreak = 0
                    userTimer = True
                    userScore = 0
                    userHearts = 3
                    userHeartsNum = 0
                    userMode = ""
                    userDifficulty = ""
                    userModeNum = 0
                    questionNum = ["?", "?", "?"]
                    questionNum2 = ["?", "?", "?"]
                    question = True

            #Change Mode.
            elif (windowMouse[1] >= 340 and windowMouse[1] <= 490) and (windowMouse[0] >= 714 and windowMouse[0] <= 864):
                display3Num = 4
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(500)
                    display3Num = 1
                    display = 1
                    mainMenuNum = 2
                    #mainMenu1Num = 1
                    mainMenu2Num = 1
                    #mainMenu3Num = 1
                    RandomLevelNum1 = False

                    userInput = ""
                    userAnswer = ""
                    userStreak = 0
                    userTimer = True
                    userScore = 0
                    userHearts = 3
                    userHeartsNum = 0
                    #userMode = ""
                    #userDifficulty = 1
                    userModeNum = 0
                    questionNum = ["?", "?", "?"]
                    questionNum2 = ["?", "?", "?"]
                    question = True
                    
            #Change Difficulty.
            elif (windowMouse[1] >= 340 and windowMouse[1] <= 490) and (windowMouse[0] >= 1014 and windowMouse[0] <= 1164):
                display3Num = 5
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(500)
                    display3Num = 1
                    display = 1
                    mainMenuNum = 3
                    mainMenu3Num = 1
                    RandomLevelNum2 = False

                    userInput = ""
                    userAnswer = ""
                    userStreak = 0
                    userDifficulty = ""
                    userTimer = True
                    userScore = 0
                    userHearts = 3
                    userHeartsNum = 0
                    questionNum = ["?", "?", "?"]
                    questionNum2 = ["?", "?", "?"]
                    question = True

            else:
                display3Num = 1
        else:
            display = 2

    if (display == 1 and mainMenuNum == 1):
        if (mainMenu1Num == 1):
            mainMenu1()
        elif (mainMenu1Num == 2):
            pygame.draw.rect(window,("#808080"),[windowWidth / 3.55, windowHeight / 2.1, 563, 150])
            pygame.draw.rect(window,("#000000"),[windowWidth / 3.55 + 5, windowHeight / 2.1 + 5, 563 - 10, 150 - 10])
            window.blit(text3,text3Center)

    elif (display == 1 and mainMenuNum == 2):
        if (mainMenu2Num == 1):
            mainMenu2()

        elif (mainMenu2Num == 2):
            ##+ button
            pygame.draw.rect(window,("#808080"),[windowWidth / 11, windowHeight / 2.1, 150, 150])
            pygame.draw.rect(window,("#000000"),[windowWidth / 11 + 5, windowHeight / 2.1 + 5, 150 - 10, 150 - 10])
            window.blit(text9,text9Center)

        elif (mainMenu2Num == 3):
            ##- button
            pygame.draw.rect(window,("#808080"),[windowWidth / 3.08, windowHeight / 2.1, 150, 150])
            pygame.draw.rect(window,("#000000"),[windowWidth / 3.08 + 5, windowHeight / 2.1 + 5, 150 - 10, 150 - 10])
            window.blit(text10,text10Center)
            
        elif (mainMenu2Num == 4):
            ##× button
            pygame.draw.rect(window,("#808080"),[windowWidth / 1.79, windowHeight / 2.1, 150, 150])
            pygame.draw.rect(window,("#000000"),[windowWidth / 1.79 + 5, windowHeight / 2.1 + 5, 150 - 10, 150 - 10])
            window.blit(text11,text11Center)

        elif (mainMenu2Num == 5):
            ##÷ button
            pygame.draw.rect(window,("#808080"),[windowWidth / 1.26, windowHeight / 2.1, 150, 150])
            pygame.draw.rect(window,("#000000"),[windowWidth / 1.26 + 5, windowHeight / 2.1 + 5, 150 - 10, 150 - 10])
            window.blit(text12,text12Center)

    elif (display == 1 and mainMenuNum == 3):
        if (mainMenu3Num == 1):
            mainMenu3()
        elif (mainMenu3Num == 2):
            pygame.draw.rect(window,("#808080"),[windowWidth / 11, windowHeight / 2.1, 150, 150])
            pygame.draw.rect(window,("#000000"),[windowWidth / 11 + 5, windowHeight / 2.1 + 5, 150 - 10, 150 - 10])
            window.blit(text18,text18Center)

        elif (mainMenu3Num == 3):
            pygame.draw.rect(window,("#808080"),[windowWidth / 3.08, windowHeight / 2.1, 150, 150])
            pygame.draw.rect(window,("#000000"),[windowWidth / 3.08 + 5, windowHeight / 2.1 + 5, 150 - 10, 150 - 10])
            window.blit(text19,text19Center)
        
        elif (mainMenu3Num == 4):
            pygame.draw.rect(window,("#808080"),[windowWidth / 1.79, windowHeight / 2.1, 150, 150])
            pygame.draw.rect(window,("#000000"),[windowWidth / 1.79 + 5, windowHeight / 2.1 + 5, 150 - 10, 150 - 10])
            window.blit(text20,text20Center)
        
        elif (mainMenu3Num == 5):
            pygame.draw.rect(window,("#808080"),[windowWidth / 1.26, windowHeight / 2.1, 150, 150])
            pygame.draw.rect(window,("#000000"),[windowWidth / 1.26 + 5, windowHeight / 2.1 + 5, 150 - 10, 150 - 10])
            window.blit(text21,text21Center)

    elif (display == 2):

        window.fill("#000000")

        #userTimer
        userTimer = userTimer - 1
        userTimerDisplay = userTimer
        userTimerDisplay = int (userTimerDisplay / 60)

        #userHearts
        if (userHearts <= 3 and userStreak == 10):
            userHearts = userHearts + 1
            userStreak = 0

        if (userHearts <= 0):
            display = 3

        elif (userHearts == 0.5):
            window.blit(image1,image1Center)
            if (userTimerDisplay > 0):
                text23 = font9.render(str(userTimerDisplay), True, ("#808080"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 584, windowHeight / 2 - 320))
                window.blit(text23,text23Center)
            else:
                text23 = font9.render(("1"), True, ("#808080"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 584, windowHeight / 2 - 320))
                window.blit(text23,text23Center)

        elif (userHearts == 1):
            window.blit(image2,image2Center)
            if (userTimerDisplay > 0):
                text23 = font9.render(str(userTimerDisplay), True, ("#FFFFFF"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 584, windowHeight / 2 - 320))
                window.blit(text23,text23Center)
            else:
                text23 = font9.render(("1"), True, ("#FFFFFF"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 584, windowHeight / 2 - 320))
                window.blit(text23,text23Center)

        elif (userHearts == 1.5):
            window.blit(image3,image3Center)
            if (userTimerDisplay > 0):
                text23 = font9.render(str(userTimerDisplay), True, ("#808080"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 475.5, windowHeight / 2 - 320))
                window.blit(text23,text23Center)
            else:
                text23 = font9.render(("1"), True, ("#808080"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 475.5, windowHeight / 2 - 320))
                window.blit(text23,text23Center)

        elif (userHearts == 2):
            window.blit(image4,image4Center)
            if (userTimerDisplay > 0):
                text23 = font9.render(str(userTimerDisplay), True, ("#FFFFFF"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 475.5, windowHeight / 2 - 320))
                window.blit(text23,text23Center)
            else:
                text23 = font9.render(("1"), True, ("#FFFFFF"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 475.5, windowHeight / 2 - 320))
                window.blit(text23,text23Center)
            
        elif (userHearts == 2.5):
            window.blit(image5,image5Center)
            if (userTimerDisplay > 0):
                text23 = font9.render(str(userTimerDisplay), True, ("#808080"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 368.45, windowHeight / 2 - 320))
                window.blit(text23,text23Center)
            else:
                text23 = font9.render(("1"), True, ("#808080"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 368.45, windowHeight / 2 - 320))
                window.blit(text23,text23Center)

        elif (userHearts >= 3):
            window.blit(image6,image6Center)
            if (userTimerDisplay > 0):
                text23 = font9.render(str(userTimerDisplay), True, ("#FFFFFF"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 368.45, windowHeight / 2 - 320))
                window.blit(text23,text23Center)
            else:
                text23 = font9.render(("1"), True, ("#FFFFFF"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 368.45, windowHeight / 2 - 320))
                window.blit(text23,text23Center)

            userStreak = 0
            
        text22 = font8.render(str(questionNum[0]) + " " + userMode + " " + str(questionNum[1]) + " = " + userInput, True, ("#FFFFFF"))
        text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
        window.blit(text22,text22Center)

        if userStreak > 0:
            window.blit(image7,image7Center)
            text31 = font9.render(str(userStreak), True, ("#FFFFFF"))
            text31Center = text31.get_rect(center = (windowWidth / 2 - 592.5, windowHeight / 2 - 320))
            window.blit(text31,text31Center)

        if (question == True and RandomLevelNum1 == True and RandomLevelNum2 == False):
            userModeNum = random.randint (1,4)
            if (userModeNum == 1):
                userMode = "+"
            elif (userModeNum == 2):
                userMode = "-"
            elif (userModeNum == 3):
                userMode = "×"
            elif (userModeNum == 4):
                userMode = "÷"

        elif (question == True and RandomLevelNum2 == True and RandomLevelNum1 == False):
            userDifficultyNum = random.randint (1,4)
            if (userDifficultyNum == 1):
                userDifficulty = 1
            elif (userDifficultyNum == 2):
                userDifficulty = 2
            elif (userDifficultyNum == 3):
                userDifficulty = 3
            elif (userDifficultyNum == 4):
                userDifficulty = 4
        
        elif (question == True and RandomLevelNum1 == True and RandomLevelNum2 == True):
            userModeNum = random.randint (1,4)
            if (userModeNum == 1):
                userMode = "+"
            elif (userModeNum == 2):
                userMode = "-"
            elif (userModeNum == 3):
                userMode = "×"
            elif (userModeNum == 4):
                userMode = "÷"
        
            userDifficultyNum = random.randint (1,4)
            if (userDifficultyNum == 1):
                userDifficulty = 1
            elif (userDifficultyNum == 2):
                userDifficulty = 2
            elif (userDifficultyNum == 3):
                userDifficulty = 3
            elif (userDifficultyNum == 4):
                userDifficulty = 4
        
        if (userMode == "+"):
            if (question == True and userDifficulty == 1):
                #60fps x 6 seconds = 360
                userTimer = 360
                questionNum[0] = random.randint(0,9)
                questionNum[1] = random.randint(0,9)
                questionNum[2] = questionNum[0] + questionNum[1]
                question = False
            elif (question == True and userDifficulty == 2):
                #60fps x 11 seconds = 660
                userTimer = 660
                questionNum[0] = random.randint(10,99)
                questionNum[1] = random.randint(10,99)
                questionNum[2] = questionNum[0] + questionNum[1]
                question = False
            elif (question == True and userDifficulty == 3):
                #60fps x 6 seconds = 960
                userTimer = 960
                questionNum[0] = random.randint(100,999)
                questionNum[1] = random.randint(100,999)
                questionNum[2] = questionNum[0] + questionNum[1]
                question = False
            elif (question == True and userDifficulty == 4):
                #60fps x 21 seconds = 1260
                userTimer = 1260
                questionNum[0] = random.randint(1000,9999)
                questionNum[1] = random.randint(1000,9999)
                questionNum[2] = questionNum[0] + questionNum[1]
                question = False
            
            #userTimer
            if userTimer <= 0:
                window.blit(image8,image8Center)
                text22 = font8.render(str(questionNum[0]) + " + " + str(questionNum[1]) + " = " + str(userInput), True, ("#808080"))
                text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                window.blit(text22,text22Center)
                pygame.display.update()
                pygame.time.wait(250)
                userHearts = userHearts - 0.5
                userInput = ""
                userAnswer = ""
                userStreak = 0
                question = True

            if (userInput != ""):
                text22 = font8.render(str(questionNum[0]) + " + " + str(questionNum[1]) + " = " + userInput, True, ("#FFFFFF"))
            else:
                text22 = font8.render(str(questionNum[0]) + " + " + str(questionNum[1]) + " = " + "?", True, ("#FFFFFF"))

            if userAnswer != "":
                userAnswer = int(userAnswer)
                if (userAnswer == questionNum[2]):
                    userStreak = userStreak + 1
                    userScore = userScore + 1

                    #userHearts
                    if (userHearts <= 3 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0

                    if (userHearts <= 0):
                        display = 3

                    elif (userHearts == 0.5):
                        window.blit(image1,image1Center)

                    elif (userHearts == 1):
                        window.blit(image2,image2Center)

                    elif (userHearts == 1.5):
                        window.blit(image3,image3Center)

                    elif (userHearts == 2):
                        window.blit(image4,image4Center)

                    elif (userHearts == 2.5):
                        window.blit(image5,image5Center)

                    elif (userHearts >= 3):
                        window.blit(image6,image6Center)

                    if (display != 3):
                        window.blit(image8,image8Center)
                        text22 = font8.render(str(questionNum[0]) + " + " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#00FF00"))
                        text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                        window.blit(text22,text22Center)
                        pygame.display.update()
                        pygame.time.wait(250)
                        question = True
                        userAnswer = ""

                elif (userAnswer != questionNum[2]):
                    userHearts = userHearts - 1
                    userStreak = 0
                    #userHearts
                    if (userHearts <= 3 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0

                    if (userHearts <= 0):
                        display = 3

                    elif (userHearts == 0.5):
                        window.blit(image1,image1Center)

                    elif (userHearts == 1):
                        window.blit(image2,image2Center)

                    elif (userHearts == 1.5):
                        window.blit(image3,image3Center)

                    elif (userHearts == 2):
                        window.blit(image4,image4Center)

                    elif (userHearts == 2.5):
                        window.blit(image5,image5Center)

                    elif (userHearts >= 3):
                        window.blit(image6,image6Center)

                    if (display != 3):
                        window.blit(image8,image8Center)
                        text22 = font8.render(str(questionNum[0]) + " + " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#FF0000"))
                        text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                        window.blit(text22,text22Center)
                        pygame.display.update()
                        pygame.time.wait(250)

                        if (userDifficulty == 1):
                            #60fps x 6 seconds = 360
                            userTimer = 360
                        elif (userDifficulty == 2):
                            #60fps x 11 seconds = 660
                            userTimer = 660
                        elif (userDifficulty == 3):
                            #60fps x 16 seconds = 960
                            userTimer = 960
                        elif (userDifficulty == 4):
                            #60fps x 21 seconds = 1260
                            userTimer = 1260

                        question = False
                        userAnswer = ""

        if (userMode == "-"):
            if (question == True and userDifficulty == 1):
                #60fps x 6 seconds = 360
                userTimer = 360
                questionNum = ["?", "?", "?"]
                questionNum2[0] = random.randint(1,9)
                questionNum2[1] = random.randint(1,9)

                if (questionNum2[0] >= (questionNum2[1])):
                    questionNum2[2] = questionNum2[0] - questionNum2[1]
                    questionNum[0] = questionNum2[0]
                    questionNum[1] = questionNum2[1]
                    questionNum[2] = questionNum2[2]
                    question = False

                else:
                    questionNum2[2] = questionNum2[1] - questionNum2[0]
                    questionNum[0] = questionNum2[1]
                    questionNum[1] = questionNum2[0]
                    questionNum[2] = questionNum2[2]
                    question = False

            elif (question == True and userDifficulty == 2):
                #60fps x 11 seconds = 660
                userTimer = 660
                questionNum = ["?", "?", "?"]
                questionNum2[0] = random.randint(10,99)
                questionNum2[1] = random.randint(10,99)

                if (questionNum2[0] >= (questionNum2[1])):
                    questionNum2[2] = questionNum2[0] - questionNum2[1]
                    questionNum[0] = questionNum2[0]
                    questionNum[1] = questionNum2[1]
                    questionNum[2] = questionNum2[2]
                    question = False

                else:
                    questionNum2[2] = questionNum2[1] - questionNum2[0]
                    questionNum[0] = questionNum2[1]
                    questionNum[1] = questionNum2[0]
                    questionNum[2] = questionNum2[2]
                    question = False

            elif (question == True and userDifficulty == 3):
                #60fps x 16 seconds = 960
                userTimer = 960
                questionNum = ["?", "?", "?"]
                questionNum2[0] = random.randint(100,999)
                questionNum2[1] = random.randint(100,999)

                if (questionNum2[0] >= (questionNum2[1])):
                    questionNum2[2] = questionNum2[0] - questionNum2[1]
                    questionNum[0] = questionNum2[0]
                    questionNum[1] = questionNum2[1]
                    questionNum[2] = questionNum2[2]
                    question = False

                else:
                    questionNum2[2] = questionNum2[1] - questionNum2[0]
                    questionNum[0] = questionNum2[1]
                    questionNum[1] = questionNum2[0]
                    questionNum[2] = questionNum2[2]
                    question = False


            elif (question == True and userDifficulty == 4):
                #60fps x 21 seconds = 1260
                userTimer = 1260
                questionNum = ["?", "?", "?"]
                questionNum2[0] = random.randint(1000,9999)
                questionNum2[1] = random.randint(1000,9999)

                if (questionNum2[0] >= (questionNum2[1])):
                    questionNum2[2] = questionNum2[0] - questionNum2[1]
                    questionNum[0] = questionNum2[0]
                    questionNum[1] = questionNum2[1]
                    questionNum[2] = questionNum2[2]
                    question = False

                else:
                    questionNum2[2] = questionNum2[1] - questionNum2[0]
                    questionNum[0] = questionNum2[1]
                    questionNum[1] = questionNum2[0]
                    questionNum[2] = questionNum2[2]
                    question = False     
            
            #userTimer
            if userTimer <= 0:
                window.blit(image8,image8Center)
                text22 = font8.render(str(questionNum[0]) + " - " + str(questionNum[1]) + " = " + str(userInput), True, ("#808080"))
                text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                window.blit(text22,text22Center)
                pygame.display.update()
                pygame.time.wait(250)
                userHearts = userHearts - 0.5
                userInput = ""
                userAnswer = ""
                userStreak = 0
                question = True

            if (userInput != ""):
                text22 = font8.render(str(questionNum[0]) + " - " + str(questionNum[1]) + " = " + userInput, True, ("#FFFFFF"))
            else:
                text22 = font8.render(str(questionNum[0]) + " - " + str(questionNum[1]) + " = " + "?", True, ("#FFFFFF"))

            if userAnswer != "":
                userAnswer = int(userAnswer)
                if (userAnswer == questionNum[2]):
                    userStreak = userStreak + 1
                    userScore = userScore + 1

                    #userHearts
                    if (userHearts <= 3 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0

                    if (userHearts <= 0):
                        display = 3

                    elif (userHearts == 0.5):
                        window.blit(image1,image1Center)

                    elif (userHearts == 1):
                        window.blit(image2,image2Center)

                    elif (userHearts == 1.5):
                        window.blit(image3,image3Center)

                    elif (userHearts == 2):
                        window.blit(image4,image4Center)

                    elif (userHearts == 2.5):
                        window.blit(image5,image5Center)

                    elif (userHearts >= 3):
                        window.blit(image6,image6Center)

                    if (display != 3):
                        window.blit(image8,image8Center)
                        text22 = font8.render(str(questionNum[0]) + " - " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#00FF00"))
                        text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                        window.blit(text22,text22Center)
                        pygame.display.update()
                        pygame.time.wait(250)
                        question = True
                        userAnswer = ""

                elif (userAnswer != questionNum[2]):
                    userHearts = userHearts - 1
                    userStreak = 0
                    #userHearts
                    if (userHearts <= 3 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0

                    if (userHearts <= 0):
                        display = 3

                    elif (userHearts == 0.5):
                        window.blit(image1,image1Center)

                    elif (userHearts == 1):
                        window.blit(image2,image2Center)

                    elif (userHearts == 1.5):
                        window.blit(image3,image3Center)

                    elif (userHearts == 2):
                        window.blit(image4,image4Center)

                    elif (userHearts == 2.5):
                        window.blit(image5,image5Center)

                    elif (userHearts >= 3):
                        window.blit(image6,image6Center)

                    if (display != 3):
                        window.blit(image8,image8Center)
                        text22 = font8.render(str(questionNum[0]) + " - " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#FF0000"))
                        text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                        window.blit(text22,text22Center)
                        pygame.display.update()
                        pygame.time.wait(250)

                        if (userDifficulty == 1):
                            #60fps x 6 seconds = 360
                            userTimer = 360
                        elif (userDifficulty == 2):
                            #60fps x 11 seconds = 660
                            userTimer = 660
                        elif (userDifficulty == 3):
                            #60fps x 16 seconds = 960
                            userTimer = 960
                        elif (userDifficulty == 4):
                            #60fps x 21 seconds = 1260
                            userTimer = 1260

                        question = False
                        userAnswer = ""

        if (userMode == "×"):
            if (question == True and userDifficulty == 1):
                #60fps x 6 seconds = 360
                userTimer = 360
                questionNum[0] = random.randint(0,9)
                questionNum[1] = random.randint(0,9)
                questionNum[2] = questionNum[0] * questionNum[1]
                question = False
            elif (question == True and userDifficulty == 2):
                #60fps x 11 seconds = 660
                userTimer = 660
                questionNum[0] = random.randint(0,99)
                questionNum[1] = random.randint(0,9)
                questionNum[2] = questionNum[0] * questionNum[1]
                question = False
            elif (question == True and userDifficulty == 3):
                #60fps x 6 seconds = 960
                userTimer = 960
                questionNum[0] = random.randint(0,999)
                questionNum[1] = random.randint(0,9)
                questionNum[2] = questionNum[0] * questionNum[1]
                question = False
            elif (question == True and userDifficulty == 4):
                #60fps x 21 seconds = 1260
                userTimer = 1260
                questionNum[0] = random.randint(0,9999)
                questionNum[1] = random.randint(0,9)
                questionNum[2] = questionNum[0] * questionNum[1]
                question = False
            
            #userTimer
            if userTimer <= 0:
                window.blit(image8,image8Center)
                text22 = font8.render(str(questionNum[0]) + " × " + str(questionNum[1]) + " = " + str(userInput), True, ("#808080"))
                text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                window.blit(text22,text22Center)
                pygame.display.update()
                pygame.time.wait(250)
                userHearts = userHearts - 0.5
                userInput = ""
                userAnswer = ""
                userStreak = 0
                question = True

            if (userInput != ""):
                text22 = font8.render(str(questionNum[0]) + " × " + str(questionNum[1]) + " = " + userInput, True, ("#FFFFFF"))
            else:
                text22 = font8.render(str(questionNum[0]) + " × " + str(questionNum[1]) + " = " + "?", True, ("#FFFFFF"))

            if userAnswer != "":
                userAnswer = int(userAnswer)
                if (userAnswer == questionNum[2]):
                    userStreak = userStreak + 1
                    userScore = userScore + 1

                    #userHearts
                    if (userHearts <= 3 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0

                    if (userHearts <= 0):
                        display = 3

                    elif (userHearts == 0.5):
                        window.blit(image1,image1Center)

                    elif (userHearts == 1):
                        window.blit(image2,image2Center)

                    elif (userHearts == 1.5):
                        window.blit(image3,image3Center)

                    elif (userHearts == 2):
                        window.blit(image4,image4Center)

                    elif (userHearts == 2.5):
                        window.blit(image5,image5Center)

                    elif (userHearts >= 3):
                        window.blit(image6,image6Center)

                    if (display != 3):
                        window.blit(image8,image8Center)
                        text22 = font8.render(str(questionNum[0]) + " × " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#00FF00"))
                        text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                        window.blit(text22,text22Center)
                        pygame.display.update()
                        pygame.time.wait(250)
                        question = True
                        userAnswer = ""

                elif (userAnswer != questionNum[2]):
                    userHearts = userHearts - 1
                    userStreak = 0
                    #userHearts
                    if (userHearts <= 3 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0

                    if (userHearts <= 0):
                        display = 3

                    elif (userHearts == 0.5):
                        window.blit(image1,image1Center)

                    elif (userHearts == 1):
                        window.blit(image2,image2Center)

                    elif (userHearts == 1.5):
                        window.blit(image3,image3Center)

                    elif (userHearts == 2):
                        window.blit(image4,image4Center)

                    elif (userHearts == 2.5):
                        window.blit(image5,image5Center)

                    elif (userHearts >= 3):
                        window.blit(image6,image6Center)

                    if (display != 3):
                        window.blit(image8,image8Center)
                        text22 = font8.render(str(questionNum[0]) + " × " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#FF0000"))
                        text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                        window.blit(text22,text22Center)
                        pygame.display.update()
                        pygame.time.wait(250)

                        if (userDifficulty == 1):
                            #60fps x 6 seconds = 360
                            userTimer = 360
                        elif (userDifficulty == 2):
                            #60fps x 11 seconds = 660
                            userTimer = 660
                        elif (userDifficulty == 3):
                            #60fps x 16 seconds = 960
                            userTimer = 960
                        elif (userDifficulty == 4):
                            #60fps x 21 seconds = 1260
                            userTimer = 1260

                        question = False
                        userAnswer = ""

        if (userMode == "÷"):
            if (question == True and userDifficulty == 1):
                #60fps x 6 seconds = 360
                userTimer = 360
                questionNum = ["?", "?", "?"]
                questionNum2[0] = random.randint(1,9)
                questionNum2[1] = random.randint(1,9)
                questionNum2[2] = questionNum2[0] / questionNum2[1]

                if (questionNum2[2] == int(questionNum2[2])):
                    questionNum2[2] = int(questionNum2[2])
                    questionNum[0] = questionNum2[0]
                    questionNum[1] = questionNum2[1]
                    questionNum[2] = questionNum2[2]
                    question = False

            elif (question == True and userDifficulty == 2):
                #60fps x 11 seconds = 660
                userTimer = 660
                questionNum = ["?", "?", "?"]
                questionNum2[0] = random.randint(10,99)
                questionNum2[1] = random.randint(1,9)
                questionNum2[2] = questionNum2[0] / questionNum2[1]

                if (questionNum2[2] == int(questionNum2[2])):
                    questionNum2[2] = int(questionNum2[2])
                    questionNum[0] = questionNum2[0]
                    questionNum[1] = questionNum2[1]
                    questionNum[2] = questionNum2[2]
                    question = False

            elif (question == True and userDifficulty == 3):
                #60fps x 16 seconds = 960
                userTimer = 960
                questionNum = ["?", "?", "?"]
                questionNum2[0] = random.randint(100,999)
                questionNum2[1] = random.randint(1,9)
                questionNum2[2] = questionNum2[0] / questionNum2[1]

                if (questionNum2[2] == int(questionNum2[2])):
                    questionNum2[2] = int(questionNum2[2])
                    questionNum[0] = questionNum2[0]
                    questionNum[1] = questionNum2[1]
                    questionNum[2] = questionNum2[2]
                    question = False

            elif (question == True and userDifficulty == 4):
                #60fps x 21 seconds = 1260
                userTimer = 1260
                questionNum = ["?", "?", "?"]
                questionNum2[0] = random.randint(1000,9999)
                questionNum2[1] = random.randint(1,9)
                questionNum2[2] = questionNum2[0] / questionNum2[1]

                if (questionNum2[2] == int(questionNum2[2])):
                    questionNum2[2] = int(questionNum2[2])
                    questionNum[0] = questionNum2[0]
                    questionNum[1] = questionNum2[1]
                    questionNum[2] = questionNum2[2]
                    question = False
            
            #userTimer
            if userTimer <= 0:
                window.blit(image8,image8Center)
                text22 = font8.render(str(questionNum[0]) + " ÷ " + str(questionNum[1]) + " = " + str(userInput), True, ("#808080"))
                text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                window.blit(text22,text22Center)
                pygame.display.update()
                pygame.time.wait(250)
                userHearts = userHearts - 0.5
                userInput = ""
                userAnswer = ""
                userStreak = 0
                question = True

            if (userInput != ""):
                text22 = font8.render(str(questionNum[0]) + " ÷ " + str(questionNum[1]) + " = " + userInput, True, ("#FFFFFF"))
            else:
                text22 = font8.render(str(questionNum[0]) + " ÷ " + str(questionNum[1]) + " = " + "?", True, ("#FFFFFF"))

            if userAnswer != "":
                userAnswer = int(userAnswer)
                if (userAnswer == questionNum[2]):
                    userStreak = userStreak + 1
                    userScore = userScore + 1

                    #userHearts
                    if (userHearts <= 3 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0

                    if (userHearts <= 0):
                        display = 3

                    elif (userHearts == 0.5):
                        window.blit(image1,image1Center)

                    elif (userHearts == 1):
                        window.blit(image2,image2Center)

                    elif (userHearts == 1.5):
                        window.blit(image3,image3Center)

                    elif (userHearts == 2):
                        window.blit(image4,image4Center)

                    elif (userHearts == 2.5):
                        window.blit(image5,image5Center)

                    elif (userHearts >= 3):
                        window.blit(image6,image6Center)

                    if (display != 3):
                        window.blit(image8,image8Center)
                        text22 = font8.render(str(questionNum[0]) + " ÷ " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#00FF00"))
                        text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                        window.blit(text22,text22Center)
                        pygame.display.update()
                        pygame.time.wait(250)
                        question = True
                        userAnswer = ""

                elif (userAnswer != questionNum[2]):
                    userHearts = userHearts - 1
                    userStreak = 0
                    #userHearts
                    if (userHearts <= 3 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0

                    if (userHearts <= 0):
                        display = 3

                    elif (userHearts == 0.5):
                        window.blit(image1,image1Center)

                    elif (userHearts == 1):
                        window.blit(image2,image2Center)

                    elif (userHearts == 1.5):
                        window.blit(image3,image3Center)

                    elif (userHearts == 2):
                        window.blit(image4,image4Center)

                    elif (userHearts == 2.5):
                        window.blit(image5,image5Center)

                    elif (userHearts >= 3):
                        window.blit(image6,image6Center)

                    if (display != 3):
                        window.blit(image8,image8Center)
                        text22 = font8.render(str(questionNum[0]) + " ÷ " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#FF0000"))
                        text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                        window.blit(text22,text22Center)
                        pygame.display.update()
                        pygame.time.wait(250)

                        if (userDifficulty == 1):
                            #60fps x 6 seconds = 360
                            userTimer = 360
                        elif (userDifficulty == 2):
                            #60fps x 11 seconds = 660
                            userTimer = 660
                        elif (userDifficulty == 3):
                            #60fps x 16 seconds = 960
                            userTimer = 960
                        elif (userDifficulty == 4):
                            #60fps x 21 seconds = 1260
                            userTimer = 1260

                        question = False
                        userAnswer = ""
        
    elif (display == 3):
        if (display3Num == 1):
            window.fill(("#000000"))
            text24 = font8.render("Your Score: " + str(userScore), True, ("#FFFFFF"))
            text24Center = text24.get_rect(center = (windowWidth / 2, windowHeight / 2 - 300))
            window.blit(text24,text24Center)

            if (RandomLevelNum1 != True):
                text25 = font8.render("Mode: " + str(userMode), True, ("#FFFFFF"))
                text25Center = text25.get_rect(center = (windowWidth / 2 - 200, windowHeight / 2 - 210))
                window.blit(text25,text25Center)
            else:
                text25 = font8.render("Mode: Random" , True, ("#FFFFFF"))
                text25Center = text25.get_rect(center = (windowWidth / 2 - 300, windowHeight / 2 - 210))
                window.blit(text25,text25Center)
            
            if (RandomLevelNum2 != True):
                text26 = font8.render("Difficulty: " + str(userDifficulty), True, ("#FFFFFF"))
                text26Center = text26.get_rect(center = (windowWidth / 2 + 200, windowHeight / 2 - 210))
                window.blit(text26,text26Center)
            else:
                text26 = font8.render("Difficulty: Random" , True, ("#FFFFFF"))
                text26Center = text26.get_rect(center = (windowWidth / 2 + 300, windowHeight / 2 - 210))
                window.blit(text26,text26Center)
            
            ##1 button
            pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 11, windowHeight / 2.1, 150, 150])
            pygame.draw.rect(window,("#000000"),[windowWidth / 11 + 5, windowHeight / 2.1 + 5, 150 - 10, 150 - 10])
            window.blit(text14,text14Center)

            ##2 button
            pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 3.08, windowHeight / 2.1, 150, 150])
            pygame.draw.rect(window,("#000000"),[windowWidth / 3.08 + 5, windowHeight / 2.1 + 5, 150 - 10, 150 - 10])
            window.blit(text15,text15Center)

            ##3 button
            pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 1.79, windowHeight / 2.1, 150, 150])
            pygame.draw.rect(window,("#000000"),[windowWidth / 1.79 + 5, windowHeight / 2.1 + 5, 150 - 10, 150 - 10])
            window.blit(text16,text16Center)

            ##4 button
            pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 1.26, windowHeight / 2.1, 150, 150])
            pygame.draw.rect(window,("#000000"),[windowWidth / 1.26 + 5, windowHeight / 2.1 + 5, 150 - 10, 150 - 10])
            window.blit(text17,text17Center)

        elif (display3Num == 2):
            pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 3.55, windowHeight / 2 + 180, 563, 150])
            pygame.draw.rect(window,("#000000"),[windowWidth / 3.55 + 5, windowHeight / 2 + 185, 563 - 10, 150 - 10])
            window.blit(text27,text27Center)

        elif (display3Num == 3):
            pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 3.55, windowHeight / 2 + 180, 563, 150])
            pygame.draw.rect(window,("#000000"),[windowWidth / 3.55 + 5, windowHeight / 2 + 185, 563 - 10, 150 - 10])
            window.blit(text28,text28Center)

        elif (display3Num == 4):
            pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 3.55, windowHeight / 2 + 180, 563, 150])
            pygame.draw.rect(window,("#000000"),[windowWidth / 3.55 + 5, windowHeight / 2 + 185, 563 - 10, 150 - 10])
            window.blit(text29,text29Center)

        elif (display3Num == 5):
            pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 3.55, windowHeight / 2 + 180, 563, 150])
            pygame.draw.rect(window,("#000000"),[windowWidth / 3.55 + 5, windowHeight / 2 + 185, 563 - 10, 150 - 10])
            window.blit(text30,text30Center)

    #60 frames per second
    windowClock.tick(60)
    pygame.display.update()
