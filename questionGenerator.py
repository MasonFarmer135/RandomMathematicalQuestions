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
#Titles
font1 = pygame.font.SysFont('rockwell', 70, bold=True)
#Headings1
font2 = pygame.font.SysFont('rockwell', 70, bold=False)
#Headings2
font3 = pygame.font.SysFont('rockwell', 50, bold=False)
#Questions
font4 = pygame.font.SysFont('rockwell', 70, bold=False)
#Hearts
font5 = pygame.font.SysFont('rockwell', 50, bold=False)
#Shield
font6 = pygame.font.SysFont('rockwell', 50, bold=False)
#Text1
font7 = pygame.font.SysFont('rockwell', 40, bold=False)
#Text2 (+ buttons)
font8 = pygame.font.SysFont('rockwell', 60, bold=False)
#Text3 (1 buttons)
font9 = pygame.font.SysFont('rockwell', 60, bold=False)
#Text4
font10 = pygame.font.SysFont('rockwell', 46, bold=False)

###Text settings.
##Display 1a
#Titles
text1 = font1.render("Random Mathematical Questions", True, ("#FFFFFF"))
text1Center = text1.get_rect(center = (windowWidth / 2, windowHeight / 2 - 200))
#Text1
text2 = font7.render('Press the "Enter" key to continue', True, ("#FFFFFF"))
text2Center = text2.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text3 = font7.render('Press the "Space" key to view the leaderboard', True, ("#FFFFFF"))
text3Center = text3.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))

##Display 1b
#Headings1
text4 = font2.render("Select a arithmetic operation", True, ("#FFFFFF"))
text4Center = text4.get_rect(center = (windowWidth / 2, windowHeight / 2 - 200))
#Text2
text5 = font8.render("+", True, ("#FFFFFF"))
text5Center = text5.get_rect(center = (windowWidth / 2 - 460, windowHeight / 2 + 50))
text6 = font8.render("-", True, ("#FFFFFF"))
text6Center = text6.get_rect(center = (windowWidth / 2 - 154, windowHeight / 2 + 43))
text7 = font8.render("×", True, ("#FFFFFF"))
text7Center = text7.get_rect(center = (windowWidth / 2 + 152.4, windowHeight / 2 + 50))
text8 = font8.render("÷", True, ("#FFFFFF"))
text8Center = text8.get_rect(center = (windowWidth / 2 + 459, windowHeight / 2 + 50))
text9 = font8.render("+", True, ("#808080"))
text9Center = text9.get_rect(center = (windowWidth / 2 - 460, windowHeight / 2 + 50))
text10 = font8.render("-", True, ("#808080"))
text10Center = text10.get_rect(center = (windowWidth / 2 - 154, windowHeight / 2 + 43))
text11 = font8.render("×", True, ("#808080"))
text11Center = text11.get_rect(center = (windowWidth / 2 + 152.4, windowHeight / 2 + 50))
text12 = font8.render("÷", True, ("#808080"))
text12Center = text12.get_rect(center = (windowWidth / 2 + 459, windowHeight / 2 + 50))

##Display 1c
#Headings1
text13 = font2.render("Select a digit count", True, ("#FFFFFF"))
text13Center = text13.get_rect(center = (windowWidth / 2, windowHeight / 2 - 200))
#Text3
text14 = font9.render("1", True, ("#FFFFFF"))
text14Center = text14.get_rect(center = (windowWidth / 2 - 460, windowHeight / 2 + 50))
text15 = font9.render("2", True, ("#FFFFFF"))
text15Center = text15.get_rect(center = (windowWidth / 2 - 153, windowHeight / 2 + 50))
text16 = font9.render("3", True, ("#FFFFFF"))
text16Center = text16.get_rect(center = (windowWidth / 2 + 153, windowHeight / 2 + 50))
text17 = font9.render("4", True, ("#FFFFFF"))
text17Center = text17.get_rect(center = (windowWidth / 2 + 459, windowHeight / 2 + 50))
text18 = font9.render("1", True, ("#808080"))
text18Center = text18.get_rect(center = (windowWidth / 2 - 460, windowHeight / 2 + 50))
text19 = font9.render("2", True, ("#808080"))
text19Center = text19.get_rect(center = (windowWidth / 2 - 153, windowHeight / 2 + 50))
text20 = font9.render("3", True, ("#808080"))
text20Center = text20.get_rect(center = (windowWidth / 2 + 153, windowHeight / 2 + 50))
text21 = font9.render("4", True, ("#808080"))
text21Center = text21.get_rect(center = (windowWidth / 2 + 459, windowHeight / 2 + 50))

##Display 2
#Questions
text22 = font4.render("", True, ("#FFFFFF"))
text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
#Hearts
text23 = font5.render("", True, ("#FFFFFF"))
text23Center = text23.get_rect(center = (windowWidth / 2, windowHeight / 2))

##Display 3
#Headings1
text24 = font2.render(("Your Score:"), True, ("#FFFFFF"))
text24Center = text24.get_rect(center = (windowWidth / 2, windowHeight / 2))
#Headings2
text25 = font3.render(("Operation:"), True, ("#FFFFFF"))
text25Center = text25.get_rect(center = (windowWidth / 2, windowHeight / 2))
text26 = font3.render("digit numbers", True, ("#FFFFFF"))
text26Center = text26.get_rect(center = (windowWidth / 2, windowHeight / 2))

#Text4
text27 = font10.render("Restart Round", True, ("#FFFFFF"))
text27Center = text27.get_rect(center = (windowWidth / 2 - 250, windowHeight / 2 - 15))
text28 = font10.render("Restart Game", True, ("#FFFFFF"))
text28Center = text28.get_rect(center = (windowWidth / 2 + 250, windowHeight / 2 - 15))
text29 = font10.render("Change Operations", True, ("#FFFFFF"))
text29Center = text29.get_rect(center = (windowWidth / 2 - 250, windowHeight / 2 + 105))
text30 = font10.render("Change Digits", True, ("#FFFFFF"))
text30Center = text30.get_rect(center = (windowWidth / 2 + 250, windowHeight / 2 + 105))
text31 = font10.render("Save Score", True, ("#FFFFFF"))
text31Center = text31.get_rect(center = (windowWidth / 2 - 250, windowHeight / 2 + 225))
text32 = font10.render("View Leaderboard", True, ("#FFFFFF"))
text32Center = text32.get_rect(center = (windowWidth / 2 + 250, windowHeight / 2 + 225))
text33 = font10.render("Restart Round", True, ("#808080"))
text33Center = text33.get_rect(center = (windowWidth / 2 - 250, windowHeight / 2 - 15))
text34 = font10.render("Restart Game", True, ("#808080"))
text34Center = text34.get_rect(center = (windowWidth / 2 + 250, windowHeight / 2 - 15))
text35 = font10.render("Change Operations", True, ("#808080"))
text35Center = text35.get_rect(center = (windowWidth / 2 - 250, windowHeight / 2 + 105))
text36 = font10.render("Change Digits", True, ("#808080"))
text36Center = text36.get_rect(center = (windowWidth / 2 + 250, windowHeight / 2 + 105))
text37 = font10.render("Save Score", True, ("#808080"))
text37Center = text37.get_rect(center = (windowWidth / 2 - 250, windowHeight / 2 + 225))
text38 = font10.render("View Leaderboard", True, ("#808080"))
text38Center = text38.get_rect(center = (windowWidth / 2 + 250, windowHeight / 2 + 225))

#Shield
text39 = font6.render("", True, ("#FFFFFF"))
text39Center = text39.get_rect(center = (windowWidth / 2, windowHeight / 2))

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
userOperation = ""
userDigits = ""
userOperationNum = 0
questionNum = ["?", "?", "?"]
questionNum2 = ["?", "?", "?"]
question = True
LeaderboardUpdate = True

def mainMenu1():
    window.fill(("#000000"))
    window.blit(text1,text1Center)

def mainMenu2():
    ##Background colour
    window.fill(("#000000"))

    #Title text
    window.blit(text4,text4Center)

    #+ button
    pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 535, windowHeight / 2 - 19, 151, 151])
    pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 535 + 5, windowHeight / 2 - 19 + 5, 151 - 10, 151 - 10])
    window.blit(text5,text5Center)

    #- button
    pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 229, windowHeight / 2 - 19, 151, 151])
    pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 229 + 5, windowHeight / 2 - 19 + 5, 151 - 10, 151 - 10])
    window.blit(text6,text6Center)

    #× button
    pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 77, windowHeight / 2 - 19, 151, 151])
    pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 77 + 5, windowHeight / 2 - 19 + 5, 151 - 10, 151 - 10])
    window.blit(text7,text7Center)

    #÷ button
    pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 383, windowHeight / 2 - 19, 151, 151])
    pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 383 + 5, windowHeight / 2 - 19 + 5, 151 - 10, 151 - 10])
    window.blit(text8,text8Center)

def mainMenu3():
    #UI (User Interface) elements
    ##Background colour
    window.fill(("#000000"))

    ##Title text
    window.blit(text13,text13Center)

    #1 button
    pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 535, windowHeight / 2 - 19, 151, 151])
    pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 535 + 5, windowHeight / 2 - 19 + 5, 151 - 10, 151 - 10])
    window.blit(text14,text14Center)

    #2 button
    pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 229, windowHeight / 2 - 19, 151, 151])
    pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 229 + 5, windowHeight / 2 - 19 + 5, 151 - 10, 151 - 10])
    window.blit(text15,text15Center)

    #3 button
    pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 77, windowHeight / 2 - 19, 151, 151])
    pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 77 + 5, windowHeight / 2 - 19 + 5, 151 - 10, 151 - 10])
    window.blit(text16,text16Center)

    #4 button
    pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 383, windowHeight / 2 - 19, 151, 151])
    pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 383 + 5, windowHeight / 2 - 19 + 5, 151 - 10, 151 - 10])
    window.blit(text17,text17Center)

#Main Application
while True:
    windowMouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            sys.exit()

        if (display == 1 and mainMenuNum == 1):
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_SPACE):
                    pygame.time.wait(50)
                    print ("Leaderboards")
                    #display = 4
                if (event.key == pygame.K_RETURN):
                    pygame.time.wait(50)
                    mainMenuNum = 2

        elif (display == 1 and mainMenuNum == 2):
            if (windowMouse[1] >= 340 and windowMouse[1] <= 491) and (windowMouse[0] >= 104 and windowMouse[0] <= 256):
                mainMenu2Num = 2
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(500)
                    userOperation = "+"
                    mainMenuNum = 3
                
            elif (windowMouse[1] >= 340 and windowMouse[1] <= 491) and (windowMouse[0] >= 410 and windowMouse[0] <= 561):
                mainMenu2Num = 3
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(500)
                    userOperation = "-"
                    mainMenuNum = 3
                
            elif (windowMouse[1] >= 340 and windowMouse[1] <= 491) and (windowMouse[0] >= 717 and windowMouse[0] <= 867):
                mainMenu2Num = 4
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(500)
                    userOperation = "×"
                    mainMenuNum = 3
                
            elif (windowMouse[1] >= 340 and windowMouse[1] <= 491) and (windowMouse[0] >= 1021 and windowMouse[0] <= 1172):
                mainMenu2Num = 5

                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(500)
                    userOperation = "÷"
                    mainMenuNum = 3
            
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    print ("Secret Level Unlocked !")
                    RandomLevelNum1 = True
                    mainMenuNum = 3
        
            else: 
                mainMenu2Num = 1

        elif (display == 1 and mainMenuNum == 3 and userDigits == ""):
            if (windowMouse[1] >= 340 and windowMouse[1] <= 491) and (windowMouse[0] >= 104 and windowMouse[0] <= 256):
                mainMenu3Num = 2
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(500)
                    userDigits = 1
                    display = 2
                
            elif (windowMouse[1] >= 340 and windowMouse[1] <= 491) and (windowMouse[0] >= 410 and windowMouse[0] <= 561):
                mainMenu3Num = 3
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(500)
                    userDigits = 2
                    display = 2
                
            elif (windowMouse[1] >= 340 and windowMouse[1] <= 491) and (windowMouse[0] >= 717 and windowMouse[0] <= 867):
                mainMenu3Num = 4
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(500)
                    userDigits = 3
                    display = 2
                
            elif (windowMouse[1] >= 340 and windowMouse[1] <= 491) and (windowMouse[0] >= 1021 and windowMouse[0] <= 1172):
                mainMenu3Num = 5
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(500)
                    userDigits = 4
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

            if (LeaderboardUpdate == True):
                #restart round.
                if (windowMouse[1] >= 299 and windowMouse[1] <= 399) and (windowMouse[0] >= 165 and windowMouse[0] <= 616):
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
                elif (windowMouse[1] >= 299 and windowMouse[1] <= 399) and (windowMouse[0] >= 660 and windowMouse[0] <= 1110):
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
                        userOperation = ""
                        userDigits = ""
                        userOperationNum = 0
                        questionNum = ["?", "?", "?"]
                        questionNum2 = ["?", "?", "?"]
                        question = True

                #Change Mode.
                elif (windowMouse[1] >= 419 and windowMouse[1] <= 519) and (windowMouse[0] >= 165 and windowMouse[0] <= 616):
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
                        #userOperation = ""
                        #userDigits = 1
                        userOperationNum = 0
                        questionNum = ["?", "?", "?"]
                        questionNum2 = ["?", "?", "?"]
                        question = True
                        
                #Change Difficulty.
                elif (windowMouse[1] >= 419 and windowMouse[1] <= 519) and (windowMouse[0] >= 660 and windowMouse[0] <= 1110):
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
                        userDigits = ""
                        userTimer = True
                        userScore = 0
                        userHearts = 3
                        userHeartsNum = 0
                        questionNum = ["?", "?", "?"]
                        questionNum2 = ["?", "?", "?"]
                        question = True

                #Save Score.
                elif (windowMouse[1] >= 539 and windowMouse[1] <= 639) and (windowMouse[0] >= 165 and windowMouse[0] <= 616):
                    display3Num = 6
                    if pygame.mouse.get_pressed()[0] == 1:
                        print ("Save Score")

                #Leaderboards.
                elif (windowMouse[1] >= 539 and windowMouse[1] <= 639) and (windowMouse[0] >= 660 and windowMouse[0] <= 1110):
                    display3Num = 7
                    if pygame.mouse.get_pressed()[0] == 1:
                        print ("Leaderboards")

                else:
                    display3Num = 1

            if (LeaderboardUpdate == False):
                #restart round.
                if (windowMouse[1] >= 299 and windowMouse[1] <= 399) and (windowMouse[0] >= 165 and windowMouse[0] <= 616):
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
                elif (windowMouse[1] >= 299 and windowMouse[1] <= 399) and (windowMouse[0] >= 660 and windowMouse[0] <= 1110):
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
                        userOperation = ""
                        userDigits = ""
                        userOperationNum = 0
                        questionNum = ["?", "?", "?"]
                        questionNum2 = ["?", "?", "?"]
                        question = True

                #Change Mode.
                elif (windowMouse[1] >= 419 and windowMouse[1] <= 519) and (windowMouse[0] >= 165 and windowMouse[0] <= 616):
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
                        #userOperation = ""
                        #userDigits = 1
                        userOperationNum = 0
                        questionNum = ["?", "?", "?"]
                        questionNum2 = ["?", "?", "?"]
                        question = True
                        
                #Change Difficulty.
                elif (windowMouse[1] >= 419 and windowMouse[1] <= 519) and (windowMouse[0] >= 660 and windowMouse[0] <= 1110):
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
                        userDigits = ""
                        userTimer = True
                        userScore = 0
                        userHearts = 3
                        userHeartsNum = 0
                        questionNum = ["?", "?", "?"]
                        questionNum2 = ["?", "?", "?"]
                        question = True

                #Leaderboards.
                elif (windowMouse[1] >= 539 and windowMouse[1] <= 639) and (windowMouse[0] >= 165 and windowMouse[0] <= 1110):
                    display3Num = 7
                    if pygame.mouse.get_pressed()[0] == 1:
                        print ("Leaderboards")

                else:
                    display3Num = 1

        else:
            display = 2

    if (display == 1 and mainMenuNum == 1):
        #Enter Text
        if (mainMenu1Num == 1):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 2

        elif (mainMenu1Num == 2):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 3

        elif (mainMenu1Num == 3):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 4

        elif (mainMenu1Num == 4):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 5

        elif (mainMenu1Num == 5):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 6

        elif (mainMenu1Num == 6):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 7

        elif (mainMenu1Num == 7):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 8

        elif (mainMenu1Num == 8):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 9

        elif (mainMenu1Num == 9):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 10

        elif (mainMenu1Num == 10):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 11

        if (mainMenu1Num == 11):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 12

        elif (mainMenu1Num == 12):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 13

        elif (mainMenu1Num == 13):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 14

        elif (mainMenu1Num == 14):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 15

        elif (mainMenu1Num == 15):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 16

        elif (mainMenu1Num == 16):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 17

        elif (mainMenu1Num == 17):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 18

        elif (mainMenu1Num == 18):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 19

        elif (mainMenu1Num == 19):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 20

        elif (mainMenu1Num == 20):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 21

        elif (mainMenu1Num == 21):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 22

        elif (mainMenu1Num == 22):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 23

        elif (mainMenu1Num == 23):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 24

        elif (mainMenu1Num == 24):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 25

        elif (mainMenu1Num == 25):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 26

        elif (mainMenu1Num == 26):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 27

        elif (mainMenu1Num == 27):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 28

        elif (mainMenu1Num == 28):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 29

        elif (mainMenu1Num == 29):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 30

        elif (mainMenu1Num == 30):
            mainMenu1()
            window.blit(text2,text2Center)
            pygame.time.wait(100)
            mainMenu1Num = 31

        # Enter Blank Screen
        elif (mainMenu1Num == 31):
            mainMenu1()
            pygame.time.wait(100)
            mainMenu1Num = 32

        elif (mainMenu1Num == 32):
            mainMenu1()
            pygame.time.wait(100)
            mainMenu1Num = 33

        elif (mainMenu1Num == 33):
            mainMenu1()
            pygame.time.wait(100)
            mainMenu1Num = 34

        elif (mainMenu1Num == 34):
            mainMenu1()
            pygame.time.wait(100)
            mainMenu1Num = 35

        elif (mainMenu1Num == 35):
            mainMenu1()
            pygame.time.wait(100)
            mainMenu1Num = 36

        #Space Text
        elif (mainMenu1Num == 36):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 37

        elif (mainMenu1Num == 37):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 38

        elif (mainMenu1Num == 38):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 39

        elif (mainMenu1Num == 39):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 40

        elif (mainMenu1Num == 40):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 41

        elif (mainMenu1Num == 41):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 42

        elif (mainMenu1Num == 42):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 43

        elif (mainMenu1Num == 43):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 44

        elif (mainMenu1Num == 44):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 45

        elif (mainMenu1Num == 45):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 46

        elif (mainMenu1Num == 46):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 47

        elif (mainMenu1Num == 47):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 48

        elif (mainMenu1Num == 48):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 49

        elif (mainMenu1Num == 49):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 50

        elif (mainMenu1Num == 50):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 51

        elif (mainMenu1Num == 51):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 52

        elif (mainMenu1Num == 52):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 53

        elif (mainMenu1Num == 53):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 54

        elif (mainMenu1Num == 54):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 55

        elif (mainMenu1Num == 55):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 56

        elif (mainMenu1Num == 56):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 57

        elif (mainMenu1Num == 57):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 58

        elif (mainMenu1Num == 58):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 59

        elif (mainMenu1Num == 59):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 60

        elif (mainMenu1Num == 60):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 61

        elif (mainMenu1Num == 61):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 62

        elif (mainMenu1Num == 62):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 63

        elif (mainMenu1Num == 63):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 64

        elif (mainMenu1Num == 64):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 65

        elif (mainMenu1Num == 65):
            mainMenu1()
            window.blit(text3,text3Center)
            pygame.time.wait(100)
            mainMenu1Num = 66

        #Space Blank
        elif (mainMenu1Num == 66):
            mainMenu1()
            pygame.time.wait(100)
            mainMenu1Num = 67

        elif (mainMenu1Num == 67):
            mainMenu1()
            pygame.time.wait(100)
            mainMenu1Num = 68
        
        elif (mainMenu1Num == 68):
            mainMenu1()
            pygame.time.wait(100)
            mainMenu1Num = 69

        elif (mainMenu1Num == 69):
            mainMenu1()
            pygame.time.wait(100)
            mainMenu1Num = 70

        elif (mainMenu1Num == 70):
            mainMenu1()
            pygame.time.wait(100)
            mainMenu1Num = 1

    elif (display == 1 and mainMenuNum == 2):
        if (mainMenu2Num == 1):
            mainMenu2()

        elif (mainMenu2Num == 2):
            #+ button
            mainMenu2()
            pygame.draw.rect(window,("#808080"),[windowWidth / 2 - 535, windowHeight / 2 - 19, 151, 151])
            pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 535 + 5, windowHeight / 2 - 19 + 5, 151 - 10, 151 - 10])
            window.blit(text9,text9Center)

        elif (mainMenu2Num == 3):
            ##- button
            mainMenu2()
            pygame.draw.rect(window,("#808080"),[windowWidth / 2 - 229, windowHeight / 2 - 19, 151, 151])
            pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 229 + 5, windowHeight / 2 - 19 + 5, 151 - 10, 151 - 10])
            window.blit(text10,text10Center)
            
        elif (mainMenu2Num == 4):
            ##× button
            mainMenu2()
            pygame.draw.rect(window,("#808080"),[windowWidth / 2 + 77, windowHeight / 2 - 19, 151, 151])
            pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 77 + 5, windowHeight / 2 - 19 + 5, 151 - 10, 151 - 10])
            window.blit(text11,text11Center)

        elif (mainMenu2Num == 5):
            ##÷ button
            mainMenu2()
            pygame.draw.rect(window,("#808080"),[windowWidth / 2 + 383, windowHeight / 2 - 19, 151, 151])
            pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 383 + 5, windowHeight / 2 - 19 + 5, 151 - 10, 151 - 10])
            window.blit(text12,text12Center)

    elif (display == 1 and mainMenuNum == 3):
        if (mainMenu3Num == 1):
            mainMenu3()

        elif (mainMenu3Num == 2):
            #1 button
            mainMenu3()
            pygame.draw.rect(window,("#808080"),[windowWidth / 2 - 535, windowHeight / 2 - 19, 151, 151])
            pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 535 + 5, windowHeight / 2 - 19 + 5, 151 - 10, 151 - 10])
            window.blit(text18,text18Center)

        elif (mainMenu3Num == 3):
            #2 button
            mainMenu3()
            pygame.draw.rect(window,("#808080"),[windowWidth / 2 - 229, windowHeight / 2 - 19, 151, 151])
            pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 229 + 5, windowHeight / 2 - 19 + 5, 151 - 10, 151 - 10])
            window.blit(text19,text19Center)
        
        elif (mainMenu3Num == 4):
            #3 button
            mainMenu3()
            pygame.draw.rect(window,("#808080"),[windowWidth / 2 + 77, windowHeight / 2 - 19, 151, 151])
            pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 77 + 5, windowHeight / 2 - 19 + 5, 151 - 10, 151 - 10])
            window.blit(text20,text20Center)
        
        elif (mainMenu3Num == 5):
            #4 button
            mainMenu3()
            pygame.draw.rect(window,("#808080"),[windowWidth / 2 + 383, windowHeight / 2 - 19, 151, 151])
            pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 383 + 5, windowHeight / 2 - 19 + 5, 151 - 10, 151 - 10])
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
                text23 = font5.render(str(userTimerDisplay), True, ("#808080"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 584, windowHeight / 2 - 320))
                window.blit(text23,text23Center)
            else:
                text23 = font5.render(("1"), True, ("#808080"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 584, windowHeight / 2 - 320))
                window.blit(text23,text23Center)

        elif (userHearts == 1):
            window.blit(image2,image2Center)
            if (userTimerDisplay > 0):
                text23 = font5.render(str(userTimerDisplay), True, ("#FFFFFF"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 584, windowHeight / 2 - 320))
                window.blit(text23,text23Center)
            else:
                text23 = font5.render(("1"), True, ("#FFFFFF"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 584, windowHeight / 2 - 320))
                window.blit(text23,text23Center)

        elif (userHearts == 1.5):
            window.blit(image3,image3Center)
            if (userTimerDisplay > 0):
                text23 = font5.render(str(userTimerDisplay), True, ("#808080"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 475.5, windowHeight / 2 - 320))
                window.blit(text23,text23Center)
            else:
                text23 = font5.render(("1"), True, ("#808080"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 475.5, windowHeight / 2 - 320))
                window.blit(text23,text23Center)

        elif (userHearts == 2):
            window.blit(image4,image4Center)
            if (userTimerDisplay > 0):
                text23 = font5.render(str(userTimerDisplay), True, ("#FFFFFF"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 475.5, windowHeight / 2 - 320))
                window.blit(text23,text23Center)
            else:
                text23 = font5.render(("1"), True, ("#FFFFFF"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 475.5, windowHeight / 2 - 320))
                window.blit(text23,text23Center)
            
        elif (userHearts == 2.5):
            window.blit(image5,image5Center)
            if (userTimerDisplay > 0):
                text23 = font5.render(str(userTimerDisplay), True, ("#808080"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 368.45, windowHeight / 2 - 320))
                window.blit(text23,text23Center)
            else:
                text23 = font5.render(("1"), True, ("#808080"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 368.45, windowHeight / 2 - 320))
                window.blit(text23,text23Center)

        elif (userHearts >= 3):
            window.blit(image6,image6Center)
            if (userTimerDisplay > 0):
                text23 = font5.render(str(userTimerDisplay), True, ("#FFFFFF"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 368.45, windowHeight / 2 - 320))
                window.blit(text23,text23Center)
            else:
                text23 = font5.render(("1"), True, ("#FFFFFF"))
                text23Center = text23.get_rect(center = (windowWidth / 2 + 368.45, windowHeight / 2 - 320))
                window.blit(text23,text23Center)

            userStreak = 0
            
        text22 = font4.render(str(questionNum[0]) + " " + userOperation + " " + str(questionNum[1]) + " = " + userInput, True, ("#FFFFFF"))
        text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
        window.blit(text22,text22Center)

        if userStreak > 0:
            window.blit(image7,image7Center)
            text39 = font6.render(str(userStreak), True, ("#FFFFFF"))
            text39Center = text39.get_rect(center = (windowWidth / 2 - 592.5, windowHeight / 2 - 320))
            window.blit(text39,text39Center)

        if (question == True and RandomLevelNum1 == True and RandomLevelNum2 == False):
            userOperationNum = random.randint (1,4)
            if (userOperationNum == 1):
                userOperation = "+"
            elif (userOperationNum == 2):
                userOperation = "-"
            elif (userOperationNum == 3):
                userOperation = "×"
            elif (userOperationNum == 4):
                userOperation = "÷"

        elif (question == True and RandomLevelNum2 == True and RandomLevelNum1 == False):
            userDigitsNum = random.randint (1,4)
            if (userDigitsNum == 1):
                userDigits = 1
            elif (userDigitsNum == 2):
                userDigits = 2
            elif (userDigitsNum == 3):
                userDigits = 3
            elif (userDigitsNum == 4):
                userDigits = 4
        
        elif (question == True and RandomLevelNum1 == True and RandomLevelNum2 == True):
            userOperationNum = random.randint (1,4)
            if (userOperationNum == 1):
                userOperation = "+"
            elif (userOperationNum == 2):
                userOperation = "-"
            elif (userOperationNum == 3):
                userOperation = "×"
            elif (userOperationNum == 4):
                userOperation = "÷"
        
            userDigitsNum = random.randint (1,4)
            if (userDigitsNum == 1):
                userDigits = 1
            elif (userDigitsNum == 2):
                userDigits = 2
            elif (userDigitsNum == 3):
                userDigits = 3
            elif (userDigitsNum == 4):
                userDigits = 4
        
        if (userOperation == "+"):
            if (question == True and userDigits == 1):
                #60fps x 6 seconds = 360
                userTimer = 360
                questionNum[0] = random.randint(0,9)
                questionNum[1] = random.randint(0,9)
                questionNum[2] = questionNum[0] + questionNum[1]
                question = False
            elif (question == True and userDigits == 2):
                #60fps x 11 seconds = 660
                userTimer = 660
                questionNum[0] = random.randint(10,99)
                questionNum[1] = random.randint(10,99)
                questionNum[2] = questionNum[0] + questionNum[1]
                question = False
            elif (question == True and userDigits == 3):
                #60fps x 6 seconds = 960
                userTimer = 960
                questionNum[0] = random.randint(100,999)
                questionNum[1] = random.randint(100,999)
                questionNum[2] = questionNum[0] + questionNum[1]
                question = False
            elif (question == True and userDigits == 4):
                #60fps x 21 seconds = 1260
                userTimer = 1260
                questionNum[0] = random.randint(1000,9999)
                questionNum[1] = random.randint(1000,9999)
                questionNum[2] = questionNum[0] + questionNum[1]
                question = False
            
            #userTimer
            if userTimer <= 0:
                window.blit(image8,image8Center)
                text22 = font4.render(str(questionNum[0]) + " + " + str(questionNum[1]) + " = " + str(userInput), True, ("#808080"))
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
                text22 = font4.render(str(questionNum[0]) + " + " + str(questionNum[1]) + " = " + userInput, True, ("#FFFFFF"))
            else:
                text22 = font4.render(str(questionNum[0]) + " + " + str(questionNum[1]) + " = " + "?", True, ("#FFFFFF"))

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
                        text22 = font4.render(str(questionNum[0]) + " + " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#00FF00"))
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
                        text22 = font4.render(str(questionNum[0]) + " + " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#FF0000"))
                        text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                        window.blit(text22,text22Center)
                        pygame.display.update()
                        pygame.time.wait(250)

                        if (userDigits == 1):
                            #60fps x 6 seconds = 360
                            userTimer = 360
                        elif (userDigits == 2):
                            #60fps x 11 seconds = 660
                            userTimer = 660
                        elif (userDigits == 3):
                            #60fps x 16 seconds = 960
                            userTimer = 960
                        elif (userDigits == 4):
                            #60fps x 21 seconds = 1260
                            userTimer = 1260

                        question = False
                        userAnswer = ""

        if (userOperation == "-"):
            if (question == True and userDigits == 1):
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

            elif (question == True and userDigits == 2):
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

            elif (question == True and userDigits == 3):
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


            elif (question == True and userDigits == 4):
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
                text22 = font4.render(str(questionNum[0]) + " - " + str(questionNum[1]) + " = " + str(userInput), True, ("#808080"))
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
                text22 = font4.render(str(questionNum[0]) + " - " + str(questionNum[1]) + " = " + userInput, True, ("#FFFFFF"))
            else:
                text22 = font4.render(str(questionNum[0]) + " - " + str(questionNum[1]) + " = " + "?", True, ("#FFFFFF"))

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
                        text22 = font4.render(str(questionNum[0]) + " - " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#00FF00"))
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
                        text22 = font4.render(str(questionNum[0]) + " - " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#FF0000"))
                        text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                        window.blit(text22,text22Center)
                        pygame.display.update()
                        pygame.time.wait(250)

                        if (userDigits == 1):
                            #60fps x 6 seconds = 360
                            userTimer = 360
                        elif (userDigits == 2):
                            #60fps x 11 seconds = 660
                            userTimer = 660
                        elif (userDigits == 3):
                            #60fps x 16 seconds = 960
                            userTimer = 960
                        elif (userDigits == 4):
                            #60fps x 21 seconds = 1260
                            userTimer = 1260

                        question = False
                        userAnswer = ""

        if (userOperation == "×"):
            if (question == True and userDigits == 1):
                #60fps x 6 seconds = 360
                userTimer = 360
                questionNum[0] = random.randint(0,9)
                questionNum[1] = random.randint(0,9)
                questionNum[2] = questionNum[0] * questionNum[1]
                question = False
            elif (question == True and userDigits == 2):
                #60fps x 11 seconds = 660
                userTimer = 660
                questionNum[0] = random.randint(0,99)
                questionNum[1] = random.randint(0,9)
                questionNum[2] = questionNum[0] * questionNum[1]
                question = False
            elif (question == True and userDigits == 3):
                #60fps x 6 seconds = 960
                userTimer = 960
                questionNum[0] = random.randint(0,999)
                questionNum[1] = random.randint(0,9)
                questionNum[2] = questionNum[0] * questionNum[1]
                question = False
            elif (question == True and userDigits == 4):
                #60fps x 21 seconds = 1260
                userTimer = 1260
                questionNum[0] = random.randint(0,9999)
                questionNum[1] = random.randint(0,9)
                questionNum[2] = questionNum[0] * questionNum[1]
                question = False
            
            #userTimer
            if userTimer <= 0:
                window.blit(image8,image8Center)
                text22 = font4.render(str(questionNum[0]) + " × " + str(questionNum[1]) + " = " + str(userInput), True, ("#808080"))
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
                text22 = font4.render(str(questionNum[0]) + " × " + str(questionNum[1]) + " = " + userInput, True, ("#FFFFFF"))
            else:
                text22 = font4.render(str(questionNum[0]) + " × " + str(questionNum[1]) + " = " + "?", True, ("#FFFFFF"))

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
                        text22 = font4.render(str(questionNum[0]) + " × " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#00FF00"))
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
                        text22 = font4.render(str(questionNum[0]) + " × " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#FF0000"))
                        text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                        window.blit(text22,text22Center)
                        pygame.display.update()
                        pygame.time.wait(250)

                        if (userDigits == 1):
                            #60fps x 6 seconds = 360
                            userTimer = 360
                        elif (userDigits == 2):
                            #60fps x 11 seconds = 660
                            userTimer = 660
                        elif (userDigits == 3):
                            #60fps x 16 seconds = 960
                            userTimer = 960
                        elif (userDigits == 4):
                            #60fps x 21 seconds = 1260
                            userTimer = 1260

                        question = False
                        userAnswer = ""

        if (userOperation == "÷"):
            if (question == True and userDigits == 1):
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

            elif (question == True and userDigits == 2):
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

            elif (question == True and userDigits == 3):
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

            elif (question == True and userDigits == 4):
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
                text22 = font4.render(str(questionNum[0]) + " ÷ " + str(questionNum[1]) + " = " + str(userInput), True, ("#808080"))
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
                text22 = font4.render(str(questionNum[0]) + " ÷ " + str(questionNum[1]) + " = " + userInput, True, ("#FFFFFF"))
            else:
                text22 = font4.render(str(questionNum[0]) + " ÷ " + str(questionNum[1]) + " = " + "?", True, ("#FFFFFF"))

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
                        text22 = font4.render(str(questionNum[0]) + " ÷ " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#00FF00"))
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
                        text22 = font4.render(str(questionNum[0]) + " ÷ " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#FF0000"))
                        text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                        window.blit(text22,text22Center)
                        pygame.display.update()
                        pygame.time.wait(250)

                        if (userDigits == 1):
                            #60fps x 6 seconds = 360
                            userTimer = 360
                        elif (userDigits == 2):
                            #60fps x 11 seconds = 660
                            userTimer = 660
                        elif (userDigits == 3):
                            #60fps x 16 seconds = 960
                            userTimer = 960
                        elif (userDigits == 4):
                            #60fps x 21 seconds = 1260
                            userTimer = 1260

                        question = False
                        userAnswer = ""
        
    elif (display == 3):
        window.fill(("#000000"))
        text24 = font2.render("Your Score: " + str(userScore), True, ("#FFFFFF"))
        text24Center = text24.get_rect(center = (windowWidth / 2, windowHeight / 2 - 300))
        window.blit(text24,text24Center)

        if (RandomLevelNum1 != True):
            text25 = font3.render("Operation: " + str(userOperation), True, ("#FFFFFF"))
            text25Center = text25.get_rect(center = (windowWidth / 2, windowHeight / 2 - 220))
            window.blit(text25,text25Center)
        else:
            text25 = font3.render("Operation: ?" , True, ("#FFFFFF"))
            text25Center = text25.get_rect(center = (windowWidth / 2, windowHeight / 2 - 220))
            window.blit(text25,text25Center)
        
        if (RandomLevelNum2 != True):
            text26 = font3.render(str(userDigits) + " digit numbers", True, ("#FFFFFF"))
            text26Center = text26.get_rect(center = (windowWidth / 2, windowHeight / 2 - 150))
            window.blit(text26,text26Center)
        else:
            text26 = font3.render("? digit numbers" , True, ("#FFFFFF"))
            text26Center = text26.get_rect(center = (windowWidth / 2, windowHeight / 2 - 150))
            window.blit(text26,text26Center)

        if (display3Num == 1):
            
            if (LeaderboardUpdate == True):
                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text27,text27Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text29,text29Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 180, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 180 + 5, 450 - 10, 100 - 10])
                window.blit(text31,text31Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text28,text28Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text30,text30Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 + 180, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 + 180 + 5, 450 - 10, 100 - 10])
                window.blit(text32,text32Center)
            
            elif (LeaderboardUpdate == False):
                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text27,text27Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text29,text29Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text28,text28Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text30,text30Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 180, 945, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 180 + 5, 945 - 10, 100 - 10])
                text32Center = text32.get_rect(center = (windowWidth / 2, windowHeight / 2 + 225))
                window.blit(text32,text32Center)

        elif (display3Num == 2):
            if (LeaderboardUpdate == True):
                pygame.draw.rect(window,("#808080"),[windowWidth / 2 - 473, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text33,text33Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text29,text29Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 180, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 180 + 5, 450 - 10, 100 - 10])
                window.blit(text31,text31Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text28,text28Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text30,text30Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 + 180, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 + 180 + 5, 450 - 10, 100 - 10])
                window.blit(text32,text32Center)
            
            elif (LeaderboardUpdate == False):
                pygame.draw.rect(window,("#808080"),[windowWidth / 2 - 473, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text33,text33Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text29,text29Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text28,text28Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text30,text30Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 180, 945, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 180 + 5, 945 - 10, 100 - 10])
                text32Center = text32.get_rect(center = (windowWidth / 2, windowHeight / 2 + 225))
                window.blit(text32,text32Center)

        elif (display3Num == 3): 
            if (LeaderboardUpdate == True):
                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text27,text27Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text29,text29Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 180, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 180 + 5, 450 - 10, 100 - 10])
                window.blit(text31,text31Center)

                pygame.draw.rect(window,("#808080"),[windowWidth / 2 + 22, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text34,text34Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text30,text30Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 + 180, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 + 180 + 5, 450 - 10, 100 - 10])
                window.blit(text32,text32Center)
            
            elif (LeaderboardUpdate == False):
                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text27,text27Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text29,text29Center)

                pygame.draw.rect(window,("#808080"),[windowWidth / 2 + 22, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text34,text34Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text30,text30Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 180, 945, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 180 + 5, 945 - 10, 100 - 10])
                text32Center = text32.get_rect(center = (windowWidth / 2, windowHeight / 2 + 225))
                window.blit(text32,text32Center)

        elif (display3Num == 4):
            
            if (LeaderboardUpdate == True):
                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text27,text27Center)

                pygame.draw.rect(window,("#808080"),[windowWidth / 2 - 473, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text35,text35Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 180, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 180 + 5, 450 - 10, 100 - 10])
                window.blit(text31,text31Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text28,text28Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text30,text30Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 + 180, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 + 180 + 5, 450 - 10, 100 - 10])
                window.blit(text32,text32Center)
            
            elif (LeaderboardUpdate == False):
                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text27,text27Center)

                pygame.draw.rect(window,("#808080"),[windowWidth / 2 - 473, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text35,text35Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text28,text28Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text30,text30Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 180, 945, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 180 + 5, 945 - 10, 100 - 10])
                text32Center = text32.get_rect(center = (windowWidth / 2, windowHeight / 2 + 225))
                window.blit(text32,text32Center)

        elif (display3Num == 5):
            
            if (LeaderboardUpdate == True):
                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text27,text27Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text29,text29Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 180, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 180 + 5, 450 - 10, 100 - 10])
                window.blit(text31,text31Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text28,text28Center)

                pygame.draw.rect(window,("#808080"),[windowWidth / 2 + 22, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text36,text36Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 + 180, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 + 180 + 5, 450 - 10, 100 - 10])
                window.blit(text32,text32Center)
            
            elif (LeaderboardUpdate == False):
                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text27,text27Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text29,text29Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text28,text28Center)

                pygame.draw.rect(window,("#808080"),[windowWidth / 2 + 22, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text36,text36Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 180, 945, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 180 + 5, 945 - 10, 100 - 10])
                text32Center = text32.get_rect(center = (windowWidth / 2, windowHeight / 2 + 225))
                window.blit(text32,text32Center)

        elif (display3Num == 6):
            if (LeaderboardUpdate == True):
                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text27,text27Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text29,text29Center)

                pygame.draw.rect(window,("#808080"),[windowWidth / 2 - 473, windowHeight / 2 + 180, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 180 + 5, 450 - 10, 100 - 10])
                window.blit(text37,text37Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text28,text28Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text30,text30Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 + 180, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 + 180 + 5, 450 - 10, 100 - 10])
                window.blit(text32,text32Center)
            
            elif (LeaderboardUpdate == False):
                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text27,text27Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text29,text29Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text28,text28Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text30,text30Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 180, 945, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 180 + 5, 945 - 10, 100 - 10])
                text32Center = text32.get_rect(center = (windowWidth / 2, windowHeight / 2 + 225))
                window.blit(text32,text32Center)

        elif (display3Num == 7):
            if (LeaderboardUpdate == True):
                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text27,text27Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text29,text29Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 180, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 180 + 5, 450 - 10, 100 - 10])
                window.blit(text31,text31Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text28,text28Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text30,text30Center)

                pygame.draw.rect(window,("#808080"),[windowWidth / 2 + 22, windowHeight / 2 + 180, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 + 180 + 5, 450 - 10, 100 - 10])
                window.blit(text38,text38Center)
            
            elif (LeaderboardUpdate == False):
                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text27,text27Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 473, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text29,text29Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 - 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 - 60 + 5, 450 - 10, 100 - 10])
                window.blit(text28,text28Center)

                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 + 22, windowHeight / 2 + 60, 450, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 + 22 + 5, windowHeight / 2 + 60 + 5, 450 - 10, 100 - 10])
                window.blit(text30,text30Center)

                pygame.draw.rect(window,("#808080"),[windowWidth / 2 - 473, windowHeight / 2 + 180, 945, 100])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 473 + 5, windowHeight / 2 + 180 + 5, 945 - 10, 100 - 10])
                text38Center = text38.get_rect(center = (windowWidth / 2, windowHeight / 2 + 225))
                window.blit(text38,text38Center)

    elif (display == 4):
        print ("Leaderboards!")

    #60 frames per second
    windowClock.tick(60)
    pygame.display.update()
