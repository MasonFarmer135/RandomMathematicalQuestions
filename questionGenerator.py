import sys
import pygame
import random
import json

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
#Text5
font11 = pygame.font.SysFont('rockwell', 70, bold=False)
#Text6
font12 = pygame.font.SysFont('rockwell', 40, bold=False)
#Text7
font13 = pygame.font.SysFont('rockwell', 30, bold=False)
#Text8
font14 = pygame.font.SysFont('rockwell', 34, bold=False)

##Text settings.
#Display0
privacyPolicyTextLine1 = font2.render("Privacy Policy", True, ("#FFFFFF"))
privacyPolicyTextLine1Center = privacyPolicyTextLine1.get_rect(center = (windowWidth / 2, windowHeight / 2 - 280))
privacyPolicyTextLine2 = font13.render("By clicking accept, you agree to the following conditions:", True, ("#FFFFFF"))
privacyPolicyTextLine2Center = privacyPolicyTextLine2.get_rect(center = (windowWidth / 2, windowHeight / 2 - 210))
privacyPolicyTextLine3 = font14.render("1. Data collection:", True, ("#FFFFFF"))
privacyPolicyTextLine3Center = privacyPolicyTextLine3.get_rect(center = (windowWidth / 2 - 420, windowHeight / 2 - 140))
privacyPolicyTextLine4 = font14.render("We may collect personal information, such as usernames and scores.", True, ("#FFFFFF"))
privacyPolicyTextLine4Center = privacyPolicyTextLine3.get_rect(center = (windowWidth / 2 - 420, windowHeight / 2 - 100))
privacyPolicyTextLine5 = font14.render("This data will only be stored, if a user saves their score to the leaderboards.", True, ("#FFFFFF"))
privacyPolicyTextLine5Center = privacyPolicyTextLine3.get_rect(center = (windowWidth / 2 - 420, windowHeight / 2 - 60))
privacyPolicyTextLine6 = font14.render("2. Data processing:", True, ("#FFFFFF"))
privacyPolicyTextLine6Center = privacyPolicyTextLine3.get_rect(center = (windowWidth / 2 - 420, windowHeight / 2))
privacyPolicyTextLine7 = font14.render("Stored data will be used to calculate which user has the highest score.", True, ("#FFFFFF"))
privacyPolicyTextLine7Center = privacyPolicyTextLine3.get_rect(center = (windowWidth / 2 - 420, windowHeight / 2 + 40))
privacyPolicyTextLine8 = font14.render("The top 5 users are then displayed within the local leaderboard for each", True, ("#FFFFFF"))
privacyPolicyTextLine8Center = privacyPolicyTextLine3.get_rect(center = (windowWidth / 2 - 420, windowHeight / 2 + 80))
privacyPolicyTextLine9 = font14.render("mode and difficulty. If your score is not within the top five scores, it will", True, ("#FFFFFF"))
privacyPolicyTextLine9Center = privacyPolicyTextLine3.get_rect(center = (windowWidth / 2 - 420, windowHeight / 2 + 120))
privacyPolicyTextLine10 = font14.render("be deleted automatically. You can delete all of the data stored within", True, ("#FFFFFF"))
privacyPolicyTextLine10Center = privacyPolicyTextLine3.get_rect(center = (windowWidth / 2 - 420, windowHeight / 2 + 160))
privacyPolicyTextLine11 = font14.render("the local leaderboards, by deleting the application from your device.", True, ("#FFFFFF"))
privacyPolicyTextLine11Center = privacyPolicyTextLine3.get_rect(center = (windowWidth / 2 - 420, windowHeight / 2 + 200))
privacyPolicyButtonText1 = font14.render("Accept", True, ("#FFFFFF"))
privacyPolicyButtonText1Center = privacyPolicyButtonText1.get_rect(center = (windowWidth / 2, windowHeight / 2 + 305))
privacyPolicyButtonText2 = font14.render("Accept", True, ("#808080"))
privacyPolicyButtonText2Center = privacyPolicyButtonText2.get_rect(center = (windowWidth / 2, windowHeight / 2 + 305))

termsofServiceTextLine1 = font2.render("Terms of Service", True, ("#FFFFFF"))
termsofServiceTextLine1Center = termsofServiceTextLine1.get_rect(center = (windowWidth / 2, windowHeight / 2 - 280))
termsofServiceTextLine2 = font13.render("By clicking accept, you agree to the following conditions:", True, ("#FFFFFF"))
termsofServiceTextLine2Center = termsofServiceTextLine2.get_rect(center = (windowWidth / 2, windowHeight / 2 - 210))
termsofServiceTextLine3 = font14.render("1. User Conduct:", True, ("#FFFFFF"))
termsofServiceTextLine3Center = privacyPolicyTextLine3.get_rect(center = (windowWidth / 2 - 420, windowHeight / 2 - 140))
termsofServiceTextLine4 = font14.render("• Do not copy or share code from this application to third parties.", True, ("#FFFFFF"))
termsofServiceTextLine4Center = privacyPolicyTextLine3.get_rect(center = (windowWidth / 2 - 420, windowHeight / 2 - 100))
termsofServiceTextLine5 = font14.render("• Do not sell or rent this software to third parties.", True, ("#FFFFFF"))
termsofServiceTextLine5Center = privacyPolicyTextLine3.get_rect(center = (windowWidth / 2 - 420, windowHeight / 2 - 60))
termsofServiceTextLine6 = font14.render("• Do not attempt to hack this application.", True, ("#FFFFFF"))
termsofServiceTextLine6Center = privacyPolicyTextLine3.get_rect(center = (windowWidth / 2 - 420, windowHeight / 2 - 20))
termsofServiceTextLine7 = font14.render("• Do not change or install software to gain a unfair advantage.", True, ("#FFFFFF"))
termsofServiceTextLine7Center = privacyPolicyTextLine3.get_rect(center = (windowWidth / 2 - 420, windowHeight / 2 + 20))
termsofServiceButtonText1 = font14.render("Accept", True, ("#FFFFFF"))
termsofServiceButtonText1Center = privacyPolicyButtonText1.get_rect(center = (windowWidth / 2, windowHeight / 2 + 305))
termsofServiceButtonText2 = font14.render("Accept", True, ("#808080"))
termsofServiceButtonText2Center = privacyPolicyButtonText2.get_rect(center = (windowWidth / 2, windowHeight / 2 + 305))

endUserLicenseAgreementTextLine1 = font2.render("End User License Agreement:", True, ("#FFFFFF"))
endUserLicenseAgreementTextLine1Center = endUserLicenseAgreementTextLine1.get_rect(center = (windowWidth / 2, windowHeight / 2 - 280))
endUserLicenseAgreementTextLine2 = font13.render("By clicking accept, you agree to the following conditions:", True, ("#FFFFFF"))
endUserLicenseAgreementTextLine2Center = endUserLicenseAgreementTextLine2.get_rect(center = (windowWidth / 2, windowHeight / 2 - 210))
endUserLicenseAgreementTextLine3 = font14.render("1. Licences:", True, ("#FFFFFF"))
endUserLicenseAgreementTextLine3Center = privacyPolicyTextLine3.get_rect(center = (windowWidth / 2 - 420, windowHeight / 2 - 140))
endUserLicenseAgreementTextLine4 = font14.render("• You can only download this application, through offical channels.", True, ("#FFFFFF"))
endUserLicenseAgreementTextLine4Center = privacyPolicyTextLine3.get_rect(center = (windowWidth / 2 - 420, windowHeight / 2 - 100))
endUserLicenseAgreementTextLine5 = font14.render("• You cannot modify the software within this application.", True, ("#FFFFFF"))
endUserLicenseAgreementTextLine5Center = privacyPolicyTextLine3.get_rect(center = (windowWidth / 2 - 420, windowHeight / 2 - 60))
endUserLicenseAgreementTextLine6 = font14.render("• You cannot share or upload this software to third parties.", True, ("#FFFFFF"))
endUserLicenseAgreementTextLine6Center = privacyPolicyTextLine3.get_rect(center = (windowWidth / 2 - 420, windowHeight / 2 - 20))
endUserLicenseAgreementTextLine7 = font14.render("• You do not own the copyrights to this application.", True, ("#FFFFFF"))
endUserLicenseAgreementTextLine7Center = privacyPolicyTextLine3.get_rect(center = (windowWidth / 2 - 420, windowHeight / 2 + 20))
endUserLicenseAgreementButtonText1 = font14.render("Accept", True, ("#FFFFFF"))
endUserLicenseAgreementButtonText1Center = privacyPolicyButtonText1.get_rect(center = (windowWidth / 2, windowHeight / 2 + 305))
endUserLicenseAgreementButtonText2 = font14.render("Accept", True, ("#808080"))
endUserLicenseAgreementButtonText2Center = privacyPolicyButtonText2.get_rect(center = (windowWidth / 2, windowHeight / 2 + 305))

#Display 1a
text1 = font1.render("Random Mathematical Questions", True, ("#FFFFFF"))
text1Center = text1.get_rect(center = (windowWidth / 2, windowHeight / 2 - 200))
text2 = font7.render('Press the "Enter" key to continue', True, ("#FFFFFF"))
text2Center = text2.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text3 = font7.render('Press the "Space" key to view the leaderboard', True, ("#FFFFFF"))
text3Center = text3.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))

#Display 1b
text4 = font2.render("Select a arithmetic operation", True, ("#FFFFFF"))
text4Center = text4.get_rect(center = (windowWidth / 2, windowHeight / 2 - 200))
text5 = font8.render("+", True, ("#FFFFFF"))
text5Center = text5.get_rect(center = (windowWidth / 2 - 460, windowHeight / 2 + 50))
text6 = font8.render("-", True, ("#FFFFFF"))
text6Center = text6.get_rect(center = (windowWidth / 2 - 154, windowHeight / 2 + 50 - 6))
text7 = font8.render("×", True, ("#FFFFFF"))
text7Center = text7.get_rect(center = (windowWidth / 2 + 152.4, windowHeight / 2 + 50))
text8 = font8.render("÷", True, ("#FFFFFF"))
text8Center = text8.get_rect(center = (windowWidth / 2 + 459, windowHeight / 2 + 50))
text9 = font8.render("+", True, ("#808080"))
text9Center = text9.get_rect(center = (windowWidth / 2 - 460, windowHeight / 2 + 50))
text10 = font8.render("-", True, ("#808080"))
text10Center = text10.get_rect(center = (windowWidth / 2 - 154, windowHeight / 2 + 50 - 6))
text11 = font8.render("×", True, ("#808080"))
text11Center = text11.get_rect(center = (windowWidth / 2 + 152.4, windowHeight / 2 + 50))
text12 = font8.render("÷", True, ("#808080"))
text12Center = text12.get_rect(center = (windowWidth / 2 + 459, windowHeight / 2 + 50))

#Display 1c
text13 = font2.render("Select a digit count", True, ("#FFFFFF"))
text13Center = text13.get_rect(center = (windowWidth / 2, windowHeight / 2 - 200))
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

#Display 2
text22 = font4.render("", True, ("#FFFFFF"))
text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
text23 = font5.render("", True, ("#FFFFFF"))
text23Center = text23.get_rect(center = (windowWidth / 2, windowHeight / 2))

#Display 3
text24 = font2.render(("Your Score:"), True, ("#FFFFFF"))
text24Center = text24.get_rect(center = (windowWidth / 2, windowHeight / 2))
text25 = font3.render(("Operation:"), True, ("#FFFFFF"))
text25Center = text25.get_rect(center = (windowWidth / 2, windowHeight / 2))
text26 = font3.render("digit numbers", True, ("#FFFFFF"))
text26Center = text26.get_rect(center = (windowWidth / 2, windowHeight / 2))
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
text39 = font6.render("", True, ("#FFFFFF"))
text39Center = text39.get_rect(center = (windowWidth / 2, windowHeight / 2))
text40 = font11.render("Leader Boards", True, ("#FFFFFF"))
text40Center = text40.get_rect(center = (windowWidth / 2 - 395, windowHeight / 2 - 300))
text41 = font8.render("+", True, ("#FFFFFF"))
text41Center = text41.get_rect(center = (windowWidth / 2 - 65, windowHeight / 2 - 300))
text42 = font8.render("-", True, ("#FFFFFF"))
text42Center = text42.get_rect(center = (windowWidth / 2 + 65, windowHeight / 2 - 300 - 6))
text43 = font8.render("×", True, ("#FFFFFF"))
text43Center = text43.get_rect(center = (windowWidth / 2 + 197, windowHeight / 2 - 300))
text44 = font8.render("÷", True, ("#FFFFFF"))
text44Center = text44.get_rect(center = (windowWidth / 2 + 327, windowHeight / 2 - 300))
text45 = font8.render("?", True, ("#FFFFFF"))
text45Center = text45.get_rect(center = (windowWidth / 2 + 457, windowHeight / 2 - 300))
text46 = font8.render("<", True, ("#FFFFFF"))
text46Center = text46.get_rect(center = (windowWidth / 2 + 582, windowHeight / 2 - 300))
text47 = font8.render("+", True, ("#000000"))
text47Center = text47.get_rect(center = (windowWidth / 2 - 65, windowHeight / 2 - 300))
text48 = font8.render("-", True, ("#000000"))
text48Center = text48.get_rect(center = (windowWidth / 2 + 65, windowHeight / 2 - 300 - 6))
text49 = font8.render("×", True, ("#000000"))
text49Center = text49.get_rect(center = (windowWidth / 2 + 197, windowHeight / 2 - 300))
text50 = font8.render("÷", True, ("#000000"))
text50Center = text50.get_rect(center = (windowWidth / 2 + 327, windowHeight / 2 - 300))
text51 = font8.render("?", True, ("#000000"))
text51Center = text51.get_rect(center = (windowWidth / 2 + 457, windowHeight / 2 - 300))
text52 = font8.render("<", True, ("#000000"))
text52Center = text52.get_rect(center = (windowWidth / 2 + 582, windowHeight / 2 - 300))
text53 = font8.render("1", True, ("#FFFFFF"))
text53Center = text53.get_rect(center = (windowWidth / 2 - 522.5, windowHeight / 2 - 200))
text54 = font8.render("", True, ("#FFFFFF"))
text54Center = text54.get_rect(center = (windowWidth / 2 + 582, windowHeight / 2 - 200))
text55 = font8.render("2", True, ("#FFFFFF"))
text55Center = text55.get_rect(center = (windowWidth / 2 - 262.5, windowHeight / 2 - 200))
text56 = font8.render("", True, ("#FFFFFF"))
text56Center = text56.get_rect(center = (windowWidth / 2 + 582, windowHeight / 2 - 200))
text57 = font8.render("3", True, ("#FFFFFF"))
text57Center = text57.get_rect(center = (windowWidth / 2, windowHeight / 2 - 200))
text58 = font8.render("", True, ("#FFFFFF"))
text58Center = text58.get_rect(center = (windowWidth / 2 + 582, windowHeight / 2 - 200))
text59 = font8.render("4", True, ("#FFFFFF"))
text59Center = text59.get_rect(center = (windowWidth / 2 + 262.5, windowHeight / 2 - 200))
text60 = font8.render("", True, ("#FFFFFF"))
text60Center = text60.get_rect(center = (windowWidth / 2 + 582, windowHeight / 2 - 200))
text61 = font8.render("?", True, ("#FFFFFF"))
text61Center = text61.get_rect(center = (windowWidth / 2 + 522.5, windowHeight / 2 - 200))
text62 = font8.render("", True, ("#FFFFFF"))
text62Center = text62.get_rect(center = (windowWidth / 2 + 582, windowHeight / 2 - 200))
text63 = font12.render("1:", True, ("#FFFFFF"))
text63Center = text63.get_rect(center = (windowWidth / 2 - 600, windowHeight / 2 - 120))
text64 = font12.render("1:", True, ("#FFFFFF"))
text64Center = text64.get_rect(center = (windowWidth / 2 - 349, windowHeight / 2 - 120))
text65 = font12.render("1:", True, ("#FFFFFF"))
text65Center = text65.get_rect(center = (windowWidth / 2 - 88, windowHeight / 2 - 120))
text66 = font12.render("1:", True, ("#FFFFFF"))
text66Center = text66.get_rect(center = (windowWidth / 2 + 175, windowHeight / 2 - 120))
text67 = font12.render("1:", True, ("#FFFFFF"))
text67Center = text67.get_rect(center = (windowWidth / 2 + 436, windowHeight / 2 - 120))
text68 = font12.render("2:", True, ("#FFFFFF"))
text68Center = text68.get_rect(center = (windowWidth / 2 - 600, windowHeight / 2 - 20))
text69 = font12.render("2:", True, ("#FFFFFF"))
text69Center = text69.get_rect(center = (windowWidth / 2 - 349, windowHeight / 2 - 20))
text70 = font12.render("2:", True, ("#FFFFFF"))
text70Center = text70.get_rect(center = (windowWidth / 2 - 88, windowHeight / 2 - 20))
text71 = font12.render("2:", True, ("#FFFFFF"))
text71Center = text71.get_rect(center = (windowWidth / 2 + 175, windowHeight / 2 - 20))
text72 = font12.render("2:", True, ("#FFFFFF"))
text72Center = text72.get_rect(center = (windowWidth / 2 + 436, windowHeight / 2 - 20))
text73 = font12.render("3:", True, ("#FFFFFF"))
text73Center = text73.get_rect(center = (windowWidth / 2 - 600, windowHeight / 2 + 80))
text74 = font12.render("3:", True, ("#FFFFFF"))
text74Center = text74.get_rect(center = (windowWidth / 2 - 349, windowHeight / 2 + 80))
text75 = font12.render("3:", True, ("#FFFFFF"))
text75Center = text75.get_rect(center = (windowWidth / 2 - 88, windowHeight / 2 + 80))
text76 = font12.render("3:", True, ("#FFFFFF"))
text76Center = text76.get_rect(center = (windowWidth / 2 + 175, windowHeight / 2 + 80))
text77 = font12.render("3:", True, ("#FFFFFF"))
text77Center = text77.get_rect(center = (windowWidth / 2 + 436, windowHeight / 2 + 80))
text78 = font12.render("4:", True, ("#FFFFFF"))
text78Center = text78.get_rect(center = (windowWidth / 2 - 600, windowHeight / 2 + 180))
text79 = font12.render("4:", True, ("#FFFFFF"))
text79Center = text79.get_rect(center = (windowWidth / 2 - 349, windowHeight / 2 + 180))
text80 = font12.render("4:", True, ("#FFFFFF"))
text80Center = text80.get_rect(center = (windowWidth / 2 - 88, windowHeight / 2 + 180))
text81 = font12.render("4:", True, ("#FFFFFF"))
text81Center = text81.get_rect(center = (windowWidth / 2 + 175, windowHeight / 2 + 180))
text82 = font12.render("4:", True, ("#FFFFFF"))
text82Center = text82.get_rect(center = (windowWidth / 2 + 436, windowHeight / 2 + 180))
text83 = font12.render("5:", True, ("#FFFFFF"))
text83Center = text83.get_rect(center = (windowWidth / 2 - 600, windowHeight / 2 + 280))
text84 = font12.render("5:", True, ("#FFFFFF"))
text84Center = text84.get_rect(center = (windowWidth / 2 - 349, windowHeight / 2 + 280))
text85 = font12.render("5:", True, ("#FFFFFF"))
text85Center = text85.get_rect(center = (windowWidth / 2 - 88, windowHeight / 2 + 280))
text86 = font12.render("5:", True, ("#FFFFFF"))
text86Center = text86.get_rect(center = (windowWidth / 2 + 175, windowHeight / 2 + 280))
text87 = font12.render("5:", True, ("#FFFFFF"))
text87Center = text87.get_rect(center = (windowWidth / 2 + 436, windowHeight / 2 + 280))
text88 = font13.render("", True, ("#00FF00"))
text88Center = text88.get_rect(center = (windowWidth / 2 - 611.4, windowHeight / 2 - 80))
text89 = font13.render("", True, ("#00FF00"))
text89Center = text89.get_rect(center = (windowWidth / 2 - 360.4, windowHeight / 2 - 80))
text90 = font13.render("", True, ("#00FF00"))
text90Center = text90.get_rect(center = (windowWidth / 2 - 99.4, windowHeight / 2 - 80))
text91 = font13.render("", True, ("#00FF00"))
text91Center = text91.get_rect(center = (windowWidth / 2 + 163.6, windowHeight / 2 - 80))
text92 = font13.render("", True, ("#00FF00"))
text92Center = text92.get_rect(center = (windowWidth / 2 + 424.6, windowHeight / 2 - 80))
text93 = font13.render("", True, ("#00FF00"))
text93Center = text93.get_rect(center = (windowWidth / 2 - 611.4, windowHeight / 2 + 20))
text94 = font13.render("", True, ("#00FF00"))
text94Center = text94.get_rect(center = (windowWidth / 2 - 360.4, windowHeight / 2 + 20))
text95 = font13.render("", True, ("#00FF00"))
text95Center = text95.get_rect(center = (windowWidth / 2 - 99.4, windowHeight / 2 + 20))
text96 = font13.render("", True, ("#00FF00"))
text96Center = text96.get_rect(center = (windowWidth / 2 + 163.6, windowHeight / 2 + 20))
text97 = font13.render("", True, ("#00FF00"))
text97Center = text97.get_rect(center = (windowWidth / 2 + 424.6, windowHeight / 2 + 20))
text98 = font13.render("", True, ("#00FF00"))
text98Center = text98.get_rect(center = (windowWidth / 2 - 611.4, windowHeight / 2 + 120))
text99 = font13.render("", True, ("#00FF00"))
text99Center = text99.get_rect(center = (windowWidth / 2 - 360.4, windowHeight / 2 + 120))
text100 = font13.render("", True, ("#00FF00"))
text100Center = text100.get_rect(center = (windowWidth / 2 - 99.4, windowHeight / 2 + 120))
text101 = font13.render("", True, ("#00FF00"))
text101Center = text101.get_rect(center = (windowWidth / 2 + 163.6, windowHeight / 2 + 120))
text102 = font13.render("", True, ("#00FF00"))
text102Center = text102.get_rect(center = (windowWidth / 2 + 424.6, windowHeight / 2 + 120))
text103 = font13.render("", True, ("#00FF00"))
text103Center = text103.get_rect(center = (windowWidth / 2 - 611.4, windowHeight / 2 + 220))
text104 = font13.render("", True, ("#00FF00"))
text104Center = text104.get_rect(center = (windowWidth / 2 - 360.4, windowHeight / 2 + 220))
text105 = font13.render("", True, ("#00FF00"))
text105Center = text105.get_rect(center = (windowWidth / 2 - 99.4, windowHeight / 2 + 220))
text106 = font13.render("", True, ("#00FF00"))
text106Center = text106.get_rect(center = (windowWidth / 2 + 163.6, windowHeight / 2 + 220))
text107 = font13.render("", True, ("#00FF00"))
text107Center = text107.get_rect(center = (windowWidth / 2 + 424.6, windowHeight / 2 + 220))
text108 = font13.render("", True, ("#00FF00"))
text108Center = text108.get_rect(center = (windowWidth / 2 - 611.4, windowHeight / 2 + 320))
text109 = font13.render("", True, ("#00FF00"))
text109Center = text109.get_rect(center = (windowWidth / 2 - 360.4, windowHeight / 2 + 320))
text110 = font13.render("", True, ("#00FF00"))
text110Center = text110.get_rect(center = (windowWidth / 2 - 99.4, windowHeight / 2 + 320))
text111 = font13.render("", True, ("#00FF00"))
text111Center = text111.get_rect(center = (windowWidth / 2 + 163.6, windowHeight / 2 + 320))
text112 = font13.render("", True, ("#00FF00"))
text112Center = text112.get_rect(center = (windowWidth / 2 + 424.6, windowHeight / 2 + 320))
text113 = font2.render("Saving your score to the leaderboards", True, ("#FFFFFF"))
text113Center = text113.get_rect(center = (windowWidth / 2, windowHeight / 2 - 200))
text114 = font7.render("5%", True, ("#FFFFFF"))
text114Center = text114.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text115 = font7.render("10%", True, ("#FFFFFF"))
text115Center = text115.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text116 = font7.render("15%", True, ("#FFFFFF"))
text116Center = text116.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text117 = font7.render("20%", True, ("#FFFFFF"))
text117Center = text117.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text118 = font7.render("25%", True, ("#FFFFFF"))
text118Center = text118.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text119 = font7.render("30%", True, ("#FFFFFF"))
text119Center = text119.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text120 = font7.render("35%", True, ("#FFFFFF"))
text120Center = text120.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text121 = font7.render("40%", True, ("#FFFFFF"))
text121Center = text121.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text122 = font7.render("45%", True, ("#FFFFFF"))
text122Center = text122.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text123 = font7.render("50%", True, ("#FFFFFF"))
text123Center = text123.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text124 = font7.render("55%", True, ("#FFFFFF"))
text124Center = text124.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text125 = font7.render("60%", True, ("#FFFFFF"))
text125Center = text125.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text126 = font7.render("65%", True, ("#FFFFFF"))
text126Center = text126.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text127 = font7.render("70%", True, ("#FFFFFF"))
text127Center = text127.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text128 = font7.render("75%", True, ("#FFFFFF"))
text128Center = text128.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text129 = font7.render("80%", True, ("#FFFFFF"))
text129Center = text129.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text130 = font7.render("85%", True, ("#FFFFFF"))
text130Center = text130.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text131 = font7.render("90%", True, ("#FFFFFF"))
text131Center = text131.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text132 = font7.render("95%", True, ("#FFFFFF"))
text132Center = text132.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text133 = font7.render("100%", True, ("#FFFFFF"))
text133Center = text133.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text134 = font2.render("Save completed", True, ("#FFFFFF"))
text134Center = text134.get_rect(center = (windowWidth / 2, windowHeight / 2 - 200))
text135 = font7.render("Click any button to go back to the previous screen.", True, ("#FFFFFF"))
text135Center = text135.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
text136 = font2.render("Enter a 3 digit Username:", True, ("#FFFFFF"))
text136Center = text136.get_rect(center = (windowWidth / 2, windowHeight / 2 - 200))
text137 = font7.render("", True, ("#FFFFFF"))
text137Center = text137.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))

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

##Initializing main menu
with open("legalAgreements.json", "r") as legalAgreementsFile:
    legalAgreementsData = json.load(legalAgreementsFile)

privacyPolicy = legalAgreementsData["Documents"][0]["privacyPolicy"][0]["Value"]
termsofService = legalAgreementsData["Documents"][1]["termsofService"][0]["Value"]
endUserLicenseAgreement = legalAgreementsData["Documents"][2]["endUserLicenseAgreement"][0]["Value"]

#Variables
display = 0
display0num = 0
dislpay0Num1 = 1
dislpay0Num2 = 1
dislpay0Num3 = 1
mainMenuNum = 1
mainMenu1Num = 1
mainMenu2Num = 1
mainMenu3Num = 1
display3Num = 1
dislpay4Num1 = 1
dislpay4Num2 = ""
dislpay4Num3 = True
display5Num1 = 1
RandomLevelNum1 = False
RandomLevelNum2 = False
username = ""
userInput = ""
userInput2 = ""
userAnswer = ""
userStreak = 0
userTimer = True
userScore = 0
userHearts = 3
userOperation = ""
userDigits = ""
userOperationNum = 0
questionNum = ["?", "?", "?"]
questionNum2 = ["?", "?", "?"]
questionMask1 = ""
questionMask2 = ""
question = True
LeaderboardUpdate = False
review = True
mainMenu3Skip = False
randomLeaderboardCheck = False
minWidthOffset = 70
maxWidthOffset = windowWidth - 70
minHeightOffset = 70
maxHeightOffset = windowHeight - 70
right = True
down = True
logo = 1
logoNum = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37]
posX = windowWidth / 2
posY = windowWidth / 2

##Constants
WIDTHCENTRE = windowWidth / 2
HEIGHTCENTRE = windowHeight / 2
SPEED = 5

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
image9 = pygame.image.load("images/leaderBoards/IMG_1.png")
image9Center = image9.get_rect(center = (windowWidth / 2, windowHeight / 2))
image10 = pygame.image.load("images/leaderBoards/IMG_2.png")
image10Center = image10.get_rect(center = (windowWidth / 2, windowHeight / 2))
image11 = pygame.image.load("images/leaderBoards/IMG_3.png")
image11Center = image11.get_rect(center = (windowWidth / 2, windowHeight / 2))
image12 = pygame.image.load("images/leaderBoards/IMG_4.png")
image12Center = image12.get_rect(center = (windowWidth / 2, windowHeight / 2))
image13 = pygame.image.load("images/leaderBoards/IMG_5.png")
image13Center = image13.get_rect(center = (windowWidth / 2, windowHeight / 2))
image14 = pygame.image.load("images/leaderBoards/IMG_6.png")
image14Center = image14.get_rect(center = (windowWidth / 2, windowHeight / 2))
image15 = pygame.image.load("images/leaderBoards/IMG_7.png")
image15Center = image15.get_rect(center = (windowWidth / 2, windowHeight / 2))
image16 = pygame.image.load("images/leaderBoards/IMG_8.png")
image16Center = image16.get_rect(center = (windowWidth / 2, windowHeight / 2))
image17 = pygame.image.load("images/leaderBoards/IMG_9.png")
image17Center = image17.get_rect(center = (windowWidth / 2, windowHeight / 2))
image18 = pygame.image.load("images/leaderBoards/IMG_10.png")
image18Center = image18.get_rect(center = (windowWidth / 2, windowHeight / 2))
image19 = pygame.image.load("images/leaderBoards/IMG_11.png")
image19Center = image19.get_rect(center = (windowWidth / 2, windowHeight / 2))
image20 = pygame.image.load("images/leaderBoards/IMG_12.png")
image20Center = image20.get_rect(center = (windowWidth / 2, windowHeight / 2))
image21 = pygame.image.load("images/leaderBoards/IMG_13.png")
image21Center = image21.get_rect(center = (windowWidth / 2, windowHeight / 2))


def mainMenu1():
    window.fill(("#000000"))
    window.blit(text1,text1Center)

def mainMenu2():
    #Background colour
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
    #Background colour
    window.fill(("#000000"))

    #Title text
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

        if (display == 0 and display0num == 1):
            dislpay0Num1 = 1

            if (windowMouse[1] >= 642 and windowMouse[1] <= 693) and (windowMouse[0] >= 564 and windowMouse[0] <= 714):
                dislpay0Num1 = 2
                if pygame.mouse.get_pressed()[0] == 1:
                    with open("legalAgreements.json", "w") as legalAgreementsFile:
                        legalAgreementsData["Documents"][0]["privacyPolicy"][0]["Value"] = True
                        json.dump(legalAgreementsData, legalAgreementsFile, indent=4)

                    pygame.time.wait(500)
                    privacyPolicy = True

        elif (display == 0 and display0num == 2):
            dislpay0Num2 = 1
            if (windowMouse[1] >= 642 and windowMouse[1] <= 693) and (windowMouse[0] >= 564 and windowMouse[0] <= 714):
                dislpay0Num2 = 2
                if pygame.mouse.get_pressed()[0] == 1:
                    with open("legalAgreements.json", "w") as legalAgreementsFile:
                        legalAgreementsData["Documents"][1]["termsofService"][0]["Value"] = True
                        json.dump(legalAgreementsData, legalAgreementsFile, indent=4)

                    pygame.time.wait(500)
                    termsofService = True

        elif (display == 0 and display0num == 3):
            dislpay0Num3 = 1
            if (windowMouse[1] >= 642 and windowMouse[1] <= 693) and (windowMouse[0] >= 564 and windowMouse[0] <= 714):
                dislpay0Num3 = 2
                if pygame.mouse.get_pressed()[0] == 1:
                    with open("legalAgreements.json", "w") as legalAgreementsFile:
                        legalAgreementsData["Documents"][2]["endUserLicenseAgreement"][0]["Value"] = True
                        json.dump(legalAgreementsData, legalAgreementsFile, indent=4)

                    pygame.time.wait(500)
                    endUserLicenseAgreement = True

        elif (display == 1 and mainMenuNum == 1):
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_SPACE):
                    pygame.time.wait(100)
                    display = 4
                    dislpay4Num3 = True
                    dislpay4Num2 = random.randint(1,5)
                    if (dislpay4Num2 == 1):
                        dislpay4Num2 = "+"
                    elif (dislpay4Num2 == 2):
                        dislpay4Num2 = "-"
                    elif (dislpay4Num2 == 3):
                        dislpay4Num2 = "×"
                    elif (dislpay4Num2 == 4):
                        dislpay4Num2 = "÷"
                    elif (dislpay4Num2 == 5):
                        dislpay4Num2 = "?"

                if (event.key == pygame.K_RETURN):
                    pygame.time.wait(100)
                    mainMenuNum = 2

        elif (display == 1 and mainMenuNum == 2):
            if (windowMouse[1] >= 340 and windowMouse[1] <= 491) and (windowMouse[0] >= 104 and windowMouse[0] <= 256):
                mainMenu2Num = 2
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(600)
                    userOperation = "+"
                    dislpay4Num2 = userOperation
                    mainMenuNum = 3
                
            elif (windowMouse[1] >= 340 and windowMouse[1] <= 491) and (windowMouse[0] >= 410 and windowMouse[0] <= 561):
                mainMenu2Num = 3
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(600)
                    userOperation = "-"
                    dislpay4Num2 = userOperation
                    mainMenuNum = 3
                
            elif (windowMouse[1] >= 340 and windowMouse[1] <= 491) and (windowMouse[0] >= 717 and windowMouse[0] <= 867):
                mainMenu2Num = 4
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(600)
                    userOperation = "×"
                    dislpay4Num2 = userOperation
                    mainMenuNum = 3
                
            elif (windowMouse[1] >= 340 and windowMouse[1] <= 491) and (windowMouse[0] >= 1021 and windowMouse[0] <= 1172):
                mainMenu2Num = 5
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(600)
                    userOperation = "÷"
                    dislpay4Num2 = userOperation
                    mainMenuNum = 3
            
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_SPACE):
                    pygame.time.wait(100)
                    RandomLevelNum1 = True
                    mainMenuNum = 3
        
            else: 
                mainMenu2Num = 1

        elif (display == 1 and mainMenuNum == 3 and userDigits == ""):
            if (windowMouse[1] >= 340 and windowMouse[1] <= 491) and (windowMouse[0] >= 104 and windowMouse[0] <= 256):
                mainMenu3Num = 2
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(600)
                    userDigits = 1
                    display = 2
                
            elif (windowMouse[1] >= 340 and windowMouse[1] <= 491) and (windowMouse[0] >= 410 and windowMouse[0] <= 561):
                mainMenu3Num = 3
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(600)
                    userDigits = 2
                    display = 2
                
            elif (windowMouse[1] >= 340 and windowMouse[1] <= 491) and (windowMouse[0] >= 717 and windowMouse[0] <= 867):
                mainMenu3Num = 4
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(600)
                    userDigits = 3
                    display = 2
                
            elif (windowMouse[1] >= 340 and windowMouse[1] <= 491) and (windowMouse[0] >= 1021 and windowMouse[0] <= 1172):
                mainMenu3Num = 5
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.time.wait(600)
                    userDigits = 4
                    display = 2

            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_SPACE):
                    pygame.time.wait(100)
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
                        questionNum = ["?", "?", "?"]
                        questionNum2 = ["?", "?", "?"]
                        question = True
                        mainMenu3Skip = False
                        review = True
                        LeaderboardUpdate = False
                        username = ""

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
                        userOperation = ""
                        userDigits = ""
                        userOperationNum = 0
                        questionNum = ["?", "?", "?"]
                        questionNum2 = ["?", "?", "?"]
                        question = True
                        dislpay4Num2 = ""
                        mainMenu3Skip = False
                        review = True
                        LeaderboardUpdate = False
                        username = ""

                #Change Mode.
                elif (windowMouse[1] >= 419 and windowMouse[1] <= 519) and (windowMouse[0] >= 165 and windowMouse[0] <= 616):
                    display3Num = 4
                    if pygame.mouse.get_pressed()[0] == 1:
                        pygame.time.wait(500)
                        display3Num = 1
                        display = 1
                        mainMenuNum = 2
                        mainMenu2Num = 1
                        RandomLevelNum1 = False
                        userInput = ""
                        userAnswer = ""
                        userStreak = 0
                        userTimer = True
                        userScore = 0
                        userHearts = 3
                        userOperationNum = 0
                        questionNum = ["?", "?", "?"]
                        questionNum2 = ["?", "?", "?"]
                        question = True
                        mainMenu3Skip = True
                        review = True
                        LeaderboardUpdate = False
                        username = ""
                        
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
                        questionNum = ["?", "?", "?"]
                        questionNum2 = ["?", "?", "?"]
                        question = True
                        mainMenu3Skip = False
                        review = True
                        LeaderboardUpdate = False
                        username = ""

                #Save Score.
                elif (windowMouse[1] >= 539 and windowMouse[1] <= 639) and (windowMouse[0] >= 165 and windowMouse[0] <= 616):
                    display3Num = 6
                    if pygame.mouse.get_pressed()[0] == 1:
                        pygame.time.wait(500)
                        display = 5

                #Leaderboards.
                elif (windowMouse[1] >= 539 and windowMouse[1] <= 639) and (windowMouse[0] >= 660 and windowMouse[0] <= 1110):
                    display3Num = 7
                    if pygame.mouse.get_pressed()[0] == 1:
                        pygame.time.wait(500)
                        display = 4
                        dislpay4Num3 = False

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
                        questionNum = ["?", "?", "?"]
                        questionNum2 = ["?", "?", "?"]
                        question = True
                        mainMenu3Skip = False
                        review = True
                        LeaderboardUpdate = False
                        username = ""

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
                        userOperation = ""
                        userDigits = ""
                        userOperationNum = 0
                        questionNum = ["?", "?", "?"]
                        questionNum2 = ["?", "?", "?"]
                        question = True
                        dislpay4Num2 = ""
                        mainMenu3Skip = False
                        review = True
                        LeaderboardUpdate = False
                        username = ""

                #Change Mode.
                elif (windowMouse[1] >= 419 and windowMouse[1] <= 519) and (windowMouse[0] >= 165 and windowMouse[0] <= 616):
                    display3Num = 4
                    if pygame.mouse.get_pressed()[0] == 1:
                        pygame.time.wait(500)
                        display3Num = 1
                        display = 1
                        mainMenuNum = 2
                        mainMenu2Num = 1
                        RandomLevelNum1 = False
                        userInput = ""
                        userAnswer = ""
                        userStreak = 0
                        userTimer = True
                        userScore = 0
                        userHearts = 3
                        userOperationNum = 0
                        questionNum = ["?", "?", "?"]
                        questionNum2 = ["?", "?", "?"]
                        question = True
                        mainMenu3Skip = True
                        review = True
                        LeaderboardUpdate = False
                        username = ""
                        
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
                        questionNum = ["?", "?", "?"]
                        questionNum2 = ["?", "?", "?"]
                        question = True
                        mainMenu3Skip = False
                        review = True
                        LeaderboardUpdate = False
                        username = ""

                #Leaderboards.
                elif (windowMouse[1] >= 539 and windowMouse[1] <= 639) and (windowMouse[0] >= 165 and windowMouse[0] <= 1110):
                    display3Num = 7
                    if pygame.mouse.get_pressed()[0] == 1:
                        pygame.time.wait(500)
                        display = 4
                        dislpay4Num3 = False

                else:
                    display3Num = 1

        elif (display == 4):
            if (dislpay4Num3 == True):
                dislpay4Num1 = 1
                if (windowMouse[1] >= 0 and windowMouse[1] <= 120) and (windowMouse[0] >= 511 and windowMouse[0] <= 636):
                    dislpay4Num1 = 2
                    if pygame.mouse.get_pressed()[0] == 1:
                        dislpay4Num2 = "+"
                    
                elif (windowMouse[1] >= 0 and windowMouse[1] <= 120) and (windowMouse[0] >= 642 and windowMouse[0] <= 767):
                    dislpay4Num1 = 3
                    if pygame.mouse.get_pressed()[0] == 1:
                        dislpay4Num2 = "-"
                    
                elif (windowMouse[1] >= 0 and windowMouse[1] <= 120) and (windowMouse[0] >= 773 and windowMouse[0] <= 899):
                    dislpay4Num1 = 4
                    if pygame.mouse.get_pressed()[0] == 1:
                        dislpay4Num2 = "×"
                    
                elif (windowMouse[1] >= 0 and windowMouse[1] <= 120) and (windowMouse[0] >= 904 and windowMouse[0] <= 1029):
                    dislpay4Num1 = 5
                    if pygame.mouse.get_pressed()[0] == 1:
                        dislpay4Num2 = "÷"

                elif (windowMouse[1] >= 0 and windowMouse[1] <= 120) and (windowMouse[0] >= 1034 and windowMouse[0] <= 1158):
                    dislpay4Num1 = 6
                    if pygame.mouse.get_pressed()[0] == 1:
                        dislpay4Num2 = "?"
                    
                elif (windowMouse[1] >= 0 and windowMouse[1] <= 120) and (windowMouse[0] >= 1163 and windowMouse[0] <= 1279):
                    dislpay4Num1 = 7
                    if pygame.mouse.get_pressed()[0] == 1:
                        display = 1
                        dislpay4Num2 = userOperation
                        dislpay4Num1 = 1
                        randomLeaderboardCheck = False
            
            elif (dislpay4Num3 == False):
                dislpay4Num1 = 1
                if (windowMouse[1] >= 0 and windowMouse[1] <= 120) and (windowMouse[0] >= 511 and windowMouse[0] <= 636):
                    dislpay4Num1 = 2
                    if pygame.mouse.get_pressed()[0] == 1:
                        dislpay4Num2 = "+"
                    
                elif (windowMouse[1] >= 0 and windowMouse[1] <= 120) and (windowMouse[0] >= 642 and windowMouse[0] <= 767):
                    dislpay4Num1 = 3
                    if pygame.mouse.get_pressed()[0] == 1:
                        dislpay4Num2 = "-"
                    
                elif (windowMouse[1] >= 0 and windowMouse[1] <= 120) and (windowMouse[0] >= 773 and windowMouse[0] <= 899):
                    dislpay4Num1 = 4
                    if pygame.mouse.get_pressed()[0] == 1:
                        dislpay4Num2 = "×"
                    
                elif (windowMouse[1] >= 0 and windowMouse[1] <= 120) and (windowMouse[0] >= 904 and windowMouse[0] <= 1029):
                    dislpay4Num1 = 5
                    if pygame.mouse.get_pressed()[0] == 1:
                        dislpay4Num2 = "÷"

                elif (windowMouse[1] >= 0 and windowMouse[1] <= 120) and (windowMouse[0] >= 1034 and windowMouse[0] <= 1158):
                    dislpay4Num1 = 6
                    if pygame.mouse.get_pressed()[0] == 1:
                        dislpay4Num2 = "?"
                    
                elif (windowMouse[1] >= 0 and windowMouse[1] <= 120) and (windowMouse[0] >= 1163 and windowMouse[0] <= 1279):
                    dislpay4Num1 = 7
                    if pygame.mouse.get_pressed()[0] == 1:
                        pygame.time.wait(100)
                        display = 3
                        dislpay4Num2 = userOperation
                        dislpay4Num1 = 1 
                        randomLeaderboardCheck = False

        elif (display == 5):
            if (display5Num1 == 1):
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_a) or (event.key == pygame.K_b) or (event.key == pygame.K_c) or (event.key == pygame.K_d) or (event.key == pygame.K_e) or (event.key == pygame.K_f) or (event.key == pygame.K_g) or (event.key == pygame.K_h) or (event.key == pygame.K_i) or (event.key == pygame.K_j) or (event.key == pygame.K_k) or (event.key == pygame.K_l) or (event.key == pygame.K_m) or (event.key == pygame.K_n) or (event.key == pygame.K_o) or (event.key == pygame.K_p) or (event.key == pygame.K_q) or (event.key == pygame.K_r) or (event.key == pygame.K_s) or (event.key == pygame.K_t) or (event.key == pygame.K_u) or (event.key == pygame.K_v) or (event.key == pygame.K_w) or (event.key == pygame.K_x) or (event.key == pygame.K_y) or (event.key == pygame.K_z):
                        userInput2 += event.unicode
                        
                    if (event.key == pygame.K_BACKSPACE):
                        userInput2 = userInput2 [0:-1] 

                    if (len(userInput2) >= 4):
                        userInput2 = userInput2 [0:-1]

                    if (event.key == pygame.K_RETURN and len(userInput2) == 3):
                        userInput2 = userInput2.upper()
                        username = userInput2
                        userInput2 = ""
                        display5Num1 = 2

            elif (display5Num1 == 22):
                if (event.type == pygame.KEYDOWN):
                    pygame.time.wait(100)
                    display = 3
                    display5Num1 = 1
                    LeaderboardUpdate = False                   

    if (display == 0):
        if (privacyPolicy == False):
            display0num = 1
        elif (termsofService == False):
            display0num = 2
        elif (endUserLicenseAgreement == False):
            display0num = 3
        else:
            display0num = 4
        
        if (display0num == 1):
            window.fill("#000000")
            window.blit(privacyPolicyTextLine1, privacyPolicyTextLine1Center)
            window.blit(privacyPolicyTextLine2, privacyPolicyTextLine2Center)
            window.blit(privacyPolicyTextLine3, privacyPolicyTextLine3Center)
            window.blit(privacyPolicyTextLine4, privacyPolicyTextLine4Center)
            window.blit(privacyPolicyTextLine5, privacyPolicyTextLine5Center)
            window.blit(privacyPolicyTextLine6, privacyPolicyTextLine6Center)
            window.blit(privacyPolicyTextLine7, privacyPolicyTextLine7Center)
            window.blit(privacyPolicyTextLine8, privacyPolicyTextLine8Center)
            window.blit(privacyPolicyTextLine9, privacyPolicyTextLine9Center)
            window.blit(privacyPolicyTextLine10, privacyPolicyTextLine10Center)
            window.blit(privacyPolicyTextLine11, privacyPolicyTextLine11Center)

            if dislpay0Num1 == 1:
                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 75, windowHeight / 2 + 284, 151, 51])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 75 + 5, windowHeight / 2 + 284 + 5, 151 - 10, 51 - 10])
                window.blit(privacyPolicyButtonText1, privacyPolicyButtonText1Center)

            elif dislpay0Num1 == 2:
                pygame.draw.rect(window,("#808080"),[windowWidth / 2 - 75, windowHeight / 2 + 284, 151, 51])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 75 + 5, windowHeight / 2 + 284 + 5, 151 - 10, 51 - 10])
                window.blit(privacyPolicyButtonText2, privacyPolicyButtonText2Center)

        elif (display0num == 2):
            window.fill("#000000")
            window.blit(termsofServiceTextLine1, termsofServiceTextLine1Center)
            window.blit(termsofServiceTextLine2, termsofServiceTextLine2Center)
            window.blit(termsofServiceTextLine3, termsofServiceTextLine3Center)
            window.blit(termsofServiceTextLine4, termsofServiceTextLine4Center)
            window.blit(termsofServiceTextLine5, termsofServiceTextLine5Center)
            window.blit(termsofServiceTextLine6, termsofServiceTextLine6Center)
            window.blit(termsofServiceTextLine7, termsofServiceTextLine7Center)

            if dislpay0Num2 == 1:
                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 75, windowHeight / 2 + 284, 151, 51])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 75 + 5, windowHeight / 2 + 284 + 5, 151 - 10, 51 - 10])
                window.blit(termsofServiceButtonText1, termsofServiceButtonText1Center)

            elif dislpay0Num2 == 2:
                pygame.draw.rect(window,("#808080"),[windowWidth / 2 - 75, windowHeight / 2 + 284, 151, 51])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 75 + 5, windowHeight / 2 + 284 + 5, 151 - 10, 51 - 10])
                window.blit(termsofServiceButtonText2, termsofServiceButtonText2Center)

        elif (display0num == 3):
            window.fill("#000000")
            window.blit(endUserLicenseAgreementTextLine1, endUserLicenseAgreementTextLine1Center)
            window.blit(endUserLicenseAgreementTextLine2, endUserLicenseAgreementTextLine2Center)
            window.blit(endUserLicenseAgreementTextLine3, endUserLicenseAgreementTextLine3Center)
            window.blit(endUserLicenseAgreementTextLine4, endUserLicenseAgreementTextLine4Center)
            window.blit(endUserLicenseAgreementTextLine5, endUserLicenseAgreementTextLine5Center)
            window.blit(endUserLicenseAgreementTextLine6, endUserLicenseAgreementTextLine6Center)
            window.blit(endUserLicenseAgreementTextLine7, endUserLicenseAgreementTextLine7Center)

            if dislpay0Num3 == 1:
                pygame.draw.rect(window,("#FFFFFF"),[windowWidth / 2 - 75, windowHeight / 2 + 284, 151, 51])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 75 + 5, windowHeight / 2 + 284 + 5, 151 - 10, 51 - 10])
                window.blit(endUserLicenseAgreementButtonText1, endUserLicenseAgreementButtonText1Center)

            elif dislpay0Num3 == 2:
                pygame.draw.rect(window,("#808080"),[windowWidth / 2 - 75, windowHeight / 2 + 284, 151, 51])
                pygame.draw.rect(window,("#000000"),[windowWidth / 2 - 75 + 5, windowHeight / 2 + 284 + 5, 151 - 10, 51 - 10])
                window.blit(endUserLicenseAgreementButtonText2, endUserLicenseAgreementButtonText2Center)

        elif (display0num == 4):
            display0num = 0
            display = 1

    elif (display == 1 and mainMenuNum == 1):
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
        if (mainMenu3Skip == True):
            display = 2

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
        userTimerDisplay = int (userTimerDisplay / 30)

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
                #30fps x 4 seconds = 120  
                userTimer = 120
                questionNum[0] = random.randint(0,9)
                questionNum[1] = random.randint(0,9)
                questionNum[2] = questionNum[0] + questionNum[1]
                question = False
            elif (question == True and userDigits == 2):
                #30fps x 7 seconds = 210
                userTimer = 210
                questionNum[0] = random.randint(10,99)
                questionNum[1] = random.randint(10,99)
                questionNum[2] = questionNum[0] + questionNum[1]
                question = False
            elif (question == True and userDigits == 3):
                #30fps x 16 seconds = 480
                userTimer = 480
                questionNum[0] = random.randint(100,999)
                questionNum[1] = random.randint(100,999)
                questionNum[2] = questionNum[0] + questionNum[1]
                questionMask1 = len(str(questionNum[0])) * "*"
                questionMask2 = len(str(questionNum[1])) * "*"
                question = False
            elif (question == True and userDigits == 4):
                #30fps x 33 seconds = 990
                userTimer = 990
                questionNum[0] = random.randint(1000,9999)
                questionNum[1] = random.randint(1000,9999)
                questionNum[2] = questionNum[0] + questionNum[1]
                questionMask1 = len(str(questionNum[0])) * "*"
                questionMask2 = len(str(questionNum[1])) * "*"
                question = False
            
            #userTimer
            if userTimer <= 0:
                window.blit(image8,image8Center)

                if (userDigits == 1 or userDigits == 2):
                    text22 = font4.render(str(questionNum[0]) + " " + userOperation + " " + str(questionNum[1]) + " = " + str(userInput), True, ("#808080"))
                    text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                    window.blit(text22,text22Center)
                    pygame.display.update()
                    pygame.time.wait(250)

                elif (userDigits == 3 or userDigits == 4):
                    text22 = font4.render(questionMask1 + " " + userOperation + " " + questionMask2 + " = " + str(userInput), True, ("#808080"))
                    text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                    window.blit(text22,text22Center)
                    pygame.display.update()
                    pygame.time.wait(250)
                
                userHearts = userHearts - 0.5
                userInput = ""
                userAnswer = ""
                userStreak = 0
                question = True

            if ((userInput != "") and (userDigits == 3 or userDigits == 4)):
                text22 = font4.render(questionMask1 + " " + userOperation + " " + questionMask2 + " = " + userInput, True, ("#FFFFFF"))
                text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                window.blit(text22,text22Center)

            elif ((userInput != "") and (userDigits == 1 or userDigits == 2)):
                text22 = font4.render(str(questionNum[0]) + " " + userOperation + " " + str(questionNum[1]) + " = " + userInput, True, ("#FFFFFF"))
                text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                window.blit(text22,text22Center)

            else:
                text22 = font4.render(str(questionNum[0]) + " " + userOperation + " " + str(questionNum[1]) + " = ", True, ("#FFFFFF"))
                text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                window.blit(text22,text22Center)

            if userAnswer != "":
                userAnswer = int(userAnswer)
                if (userAnswer == questionNum[2]):
                    userStreak = userStreak + 1
                    userScore = userScore + 1

                    #userHearts
                    if (userHearts == 0.5 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0
                    
                    elif (userHearts == 1 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0

                    elif (userHearts == 1.5 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0

                    elif (userHearts == 2 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0

                    elif (userHearts == 2.5 and userStreak == 10):
                        userHearts = userHearts + 0.5
                        userStreak = 0

                    elif (userHearts <= 3 and userStreak == 10):
                        userHearts = userHearts
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

                        if (userDigits == 1 or userDigits == 2):
                            text22 = font4.render(str(questionNum[0]) + " " + userOperation + " " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#00FF00"))
                            text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                            window.blit(text22,text22Center)
                            pygame.display.update()
                            pygame.time.wait(250)

                        elif (userDigits == 3 or userDigits == 4):
                            text22 = font4.render(questionMask1 + " " + userOperation + " " + questionMask2 + " = " + str(userAnswer), True, ("#00FF00"))
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
                        if (userDigits == 1 or userDigits == 2):
                            text22 = font4.render(str(questionNum[0]) + " " + userOperation + " " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#FF0000"))
                            text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                            window.blit(text22,text22Center)
                            pygame.display.update()
                            pygame.time.wait(250)

                        elif (userDigits == 3 or userDigits == 4):
                            text22 = font4.render(questionMask1 + " " + userOperation + " " + questionMask2 + " = " + str(userAnswer), True, ("#FF0000"))
                            text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                            window.blit(text22,text22Center)
                            pygame.display.update()
                            pygame.time.wait(250)

                        if (userDigits == 1):
                            #30fps x 4 seconds = 120
                            userTimer = 120
                        elif (userDigits == 2):
                            #30fps x 7 seconds = 210
                            userTimer = 210
                        elif (userDigits == 3):
                            #30fps x 16 seconds = 480 
                            userTimer = 480
                        elif (userDigits == 4):
                            #30fps x 33 seconds = 990
                            userTimer = 990

                        question = False
                        userAnswer = ""

        if (userOperation == "-"):
            if (question == True and userDigits == 1):
                #30fps x 4 seconds = 120
                userTimer = 120
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
                #30fps x 7 seconds = 210
                userTimer = 210
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
                #30fps x 24 seconds = 720 
                userTimer = 720
                questionNum = ["?", "?", "?"]
                questionNum2[0] = random.randint(100,999)
                questionNum2[1] = random.randint(100,999)

                if (questionNum2[0] >= (questionNum2[1])):
                    questionNum2[2] = questionNum2[0] - questionNum2[1]
                    questionNum[0] = questionNum2[0]
                    questionNum[1] = questionNum2[1]
                    questionNum[2] = questionNum2[2]
                    questionMask1 = len(str(questionNum[0])) * "*"
                    questionMask2 = len(str(questionNum[1])) * "*"
                    question = False

                else:
                    questionNum2[2] = questionNum2[1] - questionNum2[0]
                    questionNum[0] = questionNum2[1]
                    questionNum[1] = questionNum2[0]
                    questionNum[2] = questionNum2[2]
                    questionMask1 = len(str(questionNum[0])) * "*"
                    questionMask2 = len(str(questionNum[1])) * "*"
                    question = False


            elif (question == True and userDigits == 4):
                #30fps x 46 seconds = 1380 
                userTimer = 1380
                questionNum = ["?", "?", "?"]
                questionNum2[0] = random.randint(1000,9999)
                questionNum2[1] = random.randint(1000,9999)

                if (questionNum2[0] >= (questionNum2[1])):
                    questionNum2[2] = questionNum2[0] - questionNum2[1]
                    questionNum[0] = questionNum2[0]
                    questionNum[1] = questionNum2[1]
                    questionNum[2] = questionNum2[2]
                    questionMask1 = len(str(questionNum[0])) * "*"
                    questionMask2 = len(str(questionNum[1])) * "*"
                    question = False

                else:
                    questionNum2[2] = questionNum2[1] - questionNum2[0]
                    questionNum[0] = questionNum2[1]
                    questionNum[1] = questionNum2[0]
                    questionNum[2] = questionNum2[2]
                    questionMask1 = len(str(questionNum[0])) * "*"
                    questionMask2 = len(str(questionNum[1])) * "*"
                    question = False     
            
            #userTimer
            if userTimer <= 0:
                window.blit(image8,image8Center)
                if (userDigits == 1 or userDigits == 2):
                    text22 = font4.render(str(questionNum[0]) + " " + userOperation + " " + str(questionNum[1]) + " = " + str(userInput), True, ("#808080"))
                    text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                    window.blit(text22,text22Center)
                    pygame.display.update()
                    pygame.time.wait(250)

                elif (userDigits == 3 or userDigits == 4):
                    text22 = font4.render(questionMask1 + " " + userOperation + " " + questionMask2 + " = " + str(userInput), True, ("#808080"))
                    text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                    window.blit(text22,text22Center)
                    pygame.display.update()
                    pygame.time.wait(250)

                userHearts = userHearts - 0.5
                userInput = ""
                userAnswer = ""
                userStreak = 0
                question = True
            
            if ((userInput != "") and (userDigits == 3 or userDigits == 4)):
                text22 = font4.render(questionMask1 + " " + userOperation + " " + questionMask2 + " = " + userInput, True, ("#FFFFFF"))
                text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                window.blit(text22,text22Center)

            elif ((userInput != "") and (userDigits == 1 or userDigits == 2)):
                text22 = font4.render(str(questionNum[0]) + " " + userOperation + " " + str(questionNum[1]) + " = " + userInput, True, ("#FFFFFF"))
                text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                window.blit(text22,text22Center)

            else:
                text22 = font4.render(str(questionNum[0]) + " " + userOperation + " " + str(questionNum[1]) + " = ", True, ("#FFFFFF"))
                text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                window.blit(text22,text22Center)

            if userAnswer != "":
                userAnswer = int(userAnswer)
                if (userAnswer == questionNum[2]):
                    userStreak = userStreak + 1
                    userScore = userScore + 1

                    #userHearts
                    if (userHearts == 0.5 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0
                    
                    elif (userHearts == 1 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0

                    elif (userHearts == 1.5 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0

                    elif (userHearts == 2 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0

                    elif (userHearts == 2.5 and userStreak == 10):
                        userHearts = userHearts + 0.5
                        userStreak = 0

                    elif (userHearts <= 3 and userStreak == 10):
                        userHearts = userHearts
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

                        if (userDigits == 1 or userDigits == 2):
                            text22 = font4.render(str(questionNum[0]) + " " + userOperation + " " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#00FF00"))
                            text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                            window.blit(text22,text22Center)
                            pygame.display.update()
                            pygame.time.wait(250)

                        elif (userDigits == 3 or userDigits == 4):
                            text22 = font4.render(questionMask1 + " " + userOperation + " " + questionMask2 + " = " + str(userAnswer), True, ("#00FF00"))
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

                        if (userDigits == 1 or userDigits == 2):
                            text22 = font4.render(str(questionNum[0]) + " " + userOperation + " " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#FF0000"))
                            text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                            window.blit(text22,text22Center)
                            pygame.display.update()
                            pygame.time.wait(250)

                        elif (userDigits == 3 or userDigits == 4):
                            text22 = font4.render(questionMask1 + " " + userOperation + " " + questionMask2 + " = " + str(userAnswer), True, ("#FF0000"))
                            text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                            window.blit(text22,text22Center)
                            pygame.display.update()
                            pygame.time.wait(250)

                        if (userDigits == 1):
                            #30fps x 4 seconds = 120
                            userTimer = 120
                        elif (userDigits == 2):
                            #30fps x 7 seconds = 210 
                            userTimer = 210
                        elif (userDigits == 3):
                            #30fps x 24 seconds = 720 
                            userTimer = 720
                        elif (userDigits == 4):
                            #30fps x 46 seconds = 1380 
                            userTimer = 1380

                        question = False
                        userAnswer = ""

        if (userOperation == "×"):
            if (question == True and userDigits == 1):
                #30fps x 4 seconds = 120
                userTimer = 120
                questionNum[0] = random.randint(0,9)
                questionNum[1] = random.randint(0,9)
                questionNum[2] = questionNum[0] * questionNum[1]
                question = False
            elif (question == True and userDigits == 2):
                #30fps x 12 seconds = 360
                userTimer = 360
                questionNum[0] = random.randint(0,9)
                questionNum[1] = random.randint(10,99)
                questionNum[2] = questionNum[0] * questionNum[1]
                question = False
            elif (question == True and userDigits == 3):
                #30fps x 61 seconds = 1830
                userTimer = 1830
                questionNum[0] = random.randint(0,9)
                questionNum[1] = random.randint(100,999)
                questionNum[2] = questionNum[0] * questionNum[1]
                questionMask1 = len(str(questionNum[0])) * "*"
                questionMask2 = len(str(questionNum[1])) * "*"
                question = False
            elif (question == True and userDigits == 4):
                #30fps x 100 seconds = 3000
                userTimer = 3000
                questionNum[0] = random.randint(0,9)
                questionNum[1] = random.randint(1000,9999)
                questionNum[2] = questionNum[0] * questionNum[1]
                questionMask1 = len(str(questionNum[0])) * "*"
                questionMask2 = len(str(questionNum[1])) * "*"
                question = False
            
            #userTimer
            if userTimer <= 0:
                window.blit(image8,image8Center)
                if (userDigits == 1 or userDigits == 2):
                    text22 = font4.render(str(questionNum[0]) + " " + userOperation + " " + str(questionNum[1]) + " = " + str(userInput), True, ("#808080"))
                    text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                    window.blit(text22,text22Center)
                    pygame.display.update()
                    pygame.time.wait(250)

                elif (userDigits == 3 or userDigits == 4):
                    text22 = font4.render(questionMask1 + " " + userOperation + " " + questionMask2 + " = " + str(userInput), True, ("#808080"))
                    text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                    window.blit(text22,text22Center)
                    pygame.display.update()
                    pygame.time.wait(250)

                userHearts = userHearts - 0.5
                userInput = ""
                userAnswer = ""
                userStreak = 0
                question = True
            
            if ((userInput != "") and (userDigits == 3 or userDigits == 4)):
                text22 = font4.render(questionMask1 + " " + userOperation + " " + questionMask2 + " = " + userInput, True, ("#FFFFFF"))
                text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                window.blit(text22,text22Center)

            elif ((userInput != "") and (userDigits == 1 or userDigits == 2)):
                text22 = font4.render(str(questionNum[0]) + " " + userOperation + " " + str(questionNum[1]) + " = " + userInput, True, ("#FFFFFF"))
                text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                window.blit(text22,text22Center)

            else:
                text22 = font4.render(str(questionNum[0]) + " " + userOperation + " " + str(questionNum[1]) + " = ", True, ("#FFFFFF"))
                text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                window.blit(text22,text22Center)

            if userAnswer != "":
                userAnswer = int(userAnswer)
                if (userAnswer == questionNum[2]):
                    userStreak = userStreak + 1
                    userScore = userScore + 1

                    #userHearts
                    if (userHearts == 0.5 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0
                    
                    elif (userHearts == 1 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0

                    elif (userHearts == 1.5 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0

                    elif (userHearts == 2 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0

                    elif (userHearts == 2.5 and userStreak == 10):
                        userHearts = userHearts + 0.5
                        userStreak = 0

                    elif (userHearts <= 3 and userStreak == 10):
                        userHearts = userHearts
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

                        if (userDigits == 1 or userDigits == 2):
                            text22 = font4.render(str(questionNum[0]) + " " + userOperation + " " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#00FF00"))
                            text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                            window.blit(text22,text22Center)
                            pygame.display.update()
                            pygame.time.wait(250)

                        elif (userDigits == 3 or userDigits == 4):
                            text22 = font4.render(questionMask1 + " " + userOperation + " " + questionMask2 + " = " + str(userAnswer), True, ("#00FF00"))
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

                        if (userDigits == 1 or userDigits == 2):
                            text22 = font4.render(str(questionNum[0]) + " " + userOperation + " " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#FF0000"))
                            text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                            window.blit(text22,text22Center)
                            pygame.display.update()
                            pygame.time.wait(250)

                        elif (userDigits == 3 or userDigits == 4):
                            text22 = font4.render(questionMask1 + " " + userOperation + " " + questionMask2 + " = " + str(userAnswer), True, ("#FF0000"))
                            text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                            window.blit(text22,text22Center)
                            pygame.display.update()
                            pygame.time.wait(250)

                        if (userDigits == 1):
                            #30fps x 4 seconds = 120
                            userTimer = 120
                        elif (userDigits == 2):
                            #30fps x 12 seconds = 360
                            userTimer = 360
                        elif (userDigits == 3):
                            #30fps x 61 seconds = 1830
                            userTimer = 1830
                        elif (userDigits == 4):
                            #30fps x 100 seconds = 3000
                            userTimer = 3000

                        question = False
                        userAnswer = ""

        if (userOperation == "÷"):
            if (question == True and userDigits == 1):
                #30fps x 4 seconds = 120 
                userTimer = 120
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
                #30fps x 12 seconds = 360
                userTimer = 360
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
                #30fps x 31 seconds = 930
                userTimer = 930
                questionNum = ["?", "?", "?"]
                questionNum2[0] = random.randint(100,999)
                questionNum2[1] = random.randint(1,9)
                questionNum2[2] = questionNum2[0] / questionNum2[1]

                if (questionNum2[2] == int(questionNum2[2])):
                    questionNum2[2] = int(questionNum2[2])
                    questionNum[0] = questionNum2[0]
                    questionNum[1] = questionNum2[1]
                    questionNum[2] = questionNum2[2]
                    questionMask1 = len(str(questionNum[0])) * "*"
                    questionMask2 = len(str(questionNum[1])) * "*"
                    question = False

            elif (question == True and userDigits == 4):
                #30fps x 91 seconds = 2730
                userTimer = 2730
                questionNum = ["?", "?", "?"]
                questionNum2[0] = random.randint(1000,9999)
                questionNum2[1] = random.randint(1,9)
                questionNum2[2] = questionNum2[0] / questionNum2[1]

                if (questionNum2[2] == int(questionNum2[2])):
                    questionNum2[2] = int(questionNum2[2])
                    questionNum[0] = questionNum2[0]
                    questionNum[1] = questionNum2[1]
                    questionNum[2] = questionNum2[2]
                    questionMask1 = len(str(questionNum[0])) * "*"
                    questionMask2 = len(str(questionNum[1])) * "*"
                    question = False
            
            #userTimer
            if userTimer <= 0:
                window.blit(image8,image8Center)
                if (userDigits == 1 or userDigits == 2):
                    text22 = font4.render(str(questionNum[0]) + " " + userOperation + " " + str(questionNum[1]) + " = " + str(userInput), True, ("#808080"))
                    text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                    window.blit(text22,text22Center)
                    pygame.display.update()
                    pygame.time.wait(250)

                elif (userDigits == 3 or userDigits == 4):
                    text22 = font4.render(questionMask1 + " " + userOperation + " " + questionMask2 + " = " + str(userInput), True, ("#808080"))
                    text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                    window.blit(text22,text22Center)
                    pygame.display.update()
                    pygame.time.wait(250)

                userHearts = userHearts - 0.5
                userInput = ""
                userAnswer = ""
                userStreak = 0
                question = True
            
            if ((userInput != "") and (userDigits == 3 or userDigits == 4)):
                text22 = font4.render(questionMask1 + " " + userOperation + " " + questionMask2 + " = " + userInput, True, ("#FFFFFF"))
                text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                window.blit(text22,text22Center)

            elif ((userInput != "") and (userDigits == 1 or userDigits == 2)):
                text22 = font4.render(str(questionNum[0]) + " " + userOperation + " " + str(questionNum[1]) + " = " + userInput, True, ("#FFFFFF"))
                text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                window.blit(text22,text22Center)

            else:
                text22 = font4.render(str(questionNum[0]) + " " + userOperation + " " + str(questionNum[1]) + " = ", True, ("#FFFFFF"))
                text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                window.blit(text22,text22Center)

            if userAnswer != "":
                userAnswer = int(userAnswer)
                if (userAnswer == questionNum[2]):
                    userStreak = userStreak + 1
                    userScore = userScore + 1

                    #userHearts
                    if (userHearts == 0.5 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0
                    
                    elif (userHearts == 1 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0

                    elif (userHearts == 1.5 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0

                    elif (userHearts == 2 and userStreak == 10):
                        userHearts = userHearts + 1
                        userStreak = 0

                    elif (userHearts == 2.5 and userStreak == 10):
                        userHearts = userHearts + 0.5
                        userStreak = 0

                    elif (userHearts <= 3 and userStreak == 10):
                        userHearts = userHearts
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

                        if (userDigits == 1 or userDigits == 2):
                            text22 = font4.render(str(questionNum[0]) + " " + userOperation + " " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#00FF00"))
                            text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                            window.blit(text22,text22Center)
                            pygame.display.update()
                            pygame.time.wait(250)

                        elif (userDigits == 3 or userDigits == 4):
                            text22 = font4.render(questionMask1 + " " + userOperation + " " + questionMask2 + " = " + str(userAnswer), True, ("#00FF00"))
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
                        
                        if (userDigits == 1 or userDigits == 2):
                            text22 = font4.render(str(questionNum[0]) + " " + userOperation + " " + str(questionNum[1]) + " = " + str(userAnswer), True, ("#FF0000"))
                            text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                            window.blit(text22,text22Center)
                            pygame.display.update()
                            pygame.time.wait(250)

                        elif (userDigits == 3 or userDigits == 4):
                            text22 = font4.render(questionMask1 + " " + userOperation + " " + questionMask2 + " = " + str(userAnswer), True, ("#FF0000"))
                            text22Center = text22.get_rect(center = (windowWidth / 2, windowHeight / 2))
                            window.blit(text22,text22Center)
                            pygame.display.update()
                            pygame.time.wait(250)

                        if (userDigits == 1):
                            #30fps x 4 seconds = 120
                            userTimer = 120
                        elif (userDigits == 2):
                            #30fps x 12 seconds = 360
                            userTimer = 360
                        elif (userDigits == 3):
                            #30fps x 31 seconds = 930
                            userTimer = 930
                        elif (userDigits == 4):
                            #30fps x 91 seconds = 2730
                            userTimer = 2730

                        question = False
                        userAnswer = ""
        
    elif (display == 3):
        window.fill(("#000000"))
        text32 = font10.render("View Leaderboard", True, ("#FFFFFF"))
        text32Center = text32.get_rect(center = (windowWidth / 2 + 250, windowHeight / 2 + 225))
        text38 = font10.render("View Leaderboard", True, ("#808080"))
        text38Center = text38.get_rect(center = (windowWidth / 2 + 250, windowHeight / 2 + 225))

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

        with open("leaderBoards.json", "r") as leaderBoardsReview:
            leaderBoardsReviewData = json.load(leaderBoardsReview)
            #Reivews leaderboard data and checks if a user has a highscore
            if ((RandomLevelNum1 == False) and (userOperation == "+") and (review == True)):
                if ((RandomLevelNum2 == False) and (review == True) and (userDigits == 1)):
                    review1 = leaderBoardsReviewData["Users"][0]["+"][0]["1"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

                elif ((RandomLevelNum2 == False) and (review == True) and (userDigits == 2)):
                    review1 = leaderBoardsReviewData["Users"][0]["+"][1]["2"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

                elif ((RandomLevelNum2 == False) and (review == True) and (userDigits == 3)):
                    review1 = leaderBoardsReviewData["Users"][0]["+"][2]["3"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

                elif ((RandomLevelNum2 == False) and (review == True) and (userDigits == 4)):
                    review1 = leaderBoardsReviewData["Users"][0]["+"][3]["4"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

                elif ((RandomLevelNum2 == True) and (review == True) and (userDigits == 1 or userDigits == 2 or userDigits == 3 or userDigits == 4)):
                    review1 = leaderBoardsReviewData["Users"][0]["+"][4]["?"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

            elif ((RandomLevelNum1 == False) and (userOperation == "-") and (review == True)):
                if ((RandomLevelNum2 == False) and (review == True) and (userDigits == 1)):
                    review1 = leaderBoardsReviewData["Users"][0]["-"][0]["1"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

                elif ((RandomLevelNum2 == False) and (review == True) and (userDigits == 2)):
                    review1 = leaderBoardsReviewData["Users"][0]["-"][1]["2"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

                elif ((RandomLevelNum2 == False) and (review == True) and (userDigits == 3)):
                    review1 = leaderBoardsReviewData["Users"][0]["-"][2]["3"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

                elif ((RandomLevelNum2 == False) and (review == True) and (userDigits == 4)):
                    review1 = leaderBoardsReviewData["Users"][0]["-"][3]["4"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

                elif ((RandomLevelNum2 == True) and (review == True) and (userDigits == 1 or userDigits == 2 or userDigits == 3 or userDigits == 4)):
                    review1 = leaderBoardsReviewData["Users"][0]["-"][4]["?"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

            elif ((RandomLevelNum1 == False) and (userOperation == "×") and (review == True)):
                if ((RandomLevelNum2 == False) and (review == True) and (userDigits == 1)):
                    review1 = leaderBoardsReviewData["Users"][0]["x"][0]["1"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

                elif ((RandomLevelNum2 == False) and (review == True) and (userDigits == 2)):
                    review1 = leaderBoardsReviewData["Users"][0]["x"][1]["2"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

                elif ((RandomLevelNum2 == False) and (review == True) and (userDigits == 3)):
                    review1 = leaderBoardsReviewData["Users"][0]["x"][2]["3"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

                elif ((RandomLevelNum2 == False) and (review == True) and (userDigits == 4)):
                    review1 = leaderBoardsReviewData["Users"][0]["x"][3]["4"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

                elif ((RandomLevelNum2 == True) and (review == True) and (userDigits == 1 or userDigits == 2 or userDigits == 3 or userDigits == 4)):
                    review1 = leaderBoardsReviewData["Users"][0]["x"][4]["?"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

            elif ((RandomLevelNum1 == False) and (userOperation == "÷") and (review == True)):
                if ((RandomLevelNum2 == False) and (review == True) and (userDigits == 1)):
                    review1 = leaderBoardsReviewData["Users"][0]["%"][0]["1"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

                elif ((RandomLevelNum2 == False) and (review == True) and (userDigits == 2)):
                    review1 = leaderBoardsReviewData["Users"][0]["%"][1]["2"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

                elif ((RandomLevelNum2 == False) and (review == True) and (userDigits == 3)):
                    review1 = leaderBoardsReviewData["Users"][0]["%"][2]["3"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

                elif ((RandomLevelNum2 == False) and (review == True) and (userDigits == 4)):
                    review1 = leaderBoardsReviewData["Users"][0]["%"][3]["4"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

                elif ((RandomLevelNum2 == True) and (review == True) and (userDigits == 1 or userDigits == 2 or userDigits == 3 or userDigits == 4)):
                    review1 = leaderBoardsReviewData["Users"][0]["%"][4]["?"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

            elif ((RandomLevelNum1 == True) and (userDigits == 1 or userDigits == 2 or userDigits == 3 or userDigits == 4) and (review == True)):
                if ((RandomLevelNum2 == False) and (review == True) and (userDigits == 1)):
                    review1 = leaderBoardsReviewData["Users"][0]["?"][0]["1"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

                elif ((RandomLevelNum2 == False) and (review == True) and (userDigits == 2)):
                    review1 = leaderBoardsReviewData["Users"][0]["?"][1]["2"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

                elif ((RandomLevelNum2 == False) and (review == True) and (userDigits == 3)):
                    review1 = leaderBoardsReviewData["Users"][0]["?"][2]["3"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

                elif ((RandomLevelNum2 == False) and (review == True) and (userDigits == 4)):
                    review1 = leaderBoardsReviewData["Users"][0]["?"][3]["4"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

                elif ((RandomLevelNum2 == True) and (review == True) and (userDigits == 1 or userDigits == 2 or userDigits == 3 or userDigits == 4)):
                    review1 = leaderBoardsReviewData["Users"][0]["?"][4]["?"]
                    review2 = sorted(review1, key=lambda x: x["Score"], reverse = True)
                    review3 = review2[4]["Score"]
                    if (userScore > review3):
                        LeaderboardUpdate = True
                        review = False
                    else:
                        LeaderboardUpdate = False
                        review = False

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
        with open("leaderBoards.json", "r") as leaderBoardsFile:
            leaderBoardsData = json.load(leaderBoardsFile)

        additionLeaderBoardsData = leaderBoardsData["Users"][0]["+"]
        additionLeaderBoardsMode1 = additionLeaderBoardsData[0]["1"]
        additionLeaderBoardsMode2 = additionLeaderBoardsData[1]["2"]
        additionLeaderBoardsMode3 = additionLeaderBoardsData[2]["3"]
        additionLeaderBoardsMode4 = additionLeaderBoardsData[3]["4"]
        additionLeaderBoardsMode5 = additionLeaderBoardsData[4]["?"]
        subtractionLeaderBoardsData = leaderBoardsData["Users"][0]["-"]
        subtractionLeaderBoardsMode1 = subtractionLeaderBoardsData[0]["1"]
        subtractionLeaderBoardsMode2 = subtractionLeaderBoardsData[1]["2"]
        subtractionLeaderBoardsMode3 = subtractionLeaderBoardsData[2]["3"]
        subtractionLeaderBoardsMode4 = subtractionLeaderBoardsData[3]["4"]
        subtractionLeaderBoardsMode5 = subtractionLeaderBoardsData[4]["?"]
        multiplicationLeaderBoardsData = leaderBoardsData["Users"][0]["x"]
        multiplicationLeaderBoardsMode1 = multiplicationLeaderBoardsData[0]["1"]
        multiplicationLeaderBoardsMode2 = multiplicationLeaderBoardsData[1]["2"]
        multiplicationLeaderBoardsMode3 = multiplicationLeaderBoardsData[2]["3"]
        multiplicationLeaderBoardsMode4 = multiplicationLeaderBoardsData[3]["4"]
        multiplicationLeaderBoardsMode5 = multiplicationLeaderBoardsData[4]["?"]
        divisionLeaderBoardsData = leaderBoardsData["Users"][0]["%"]
        divisionLeaderBoardsMode1 = divisionLeaderBoardsData[0]["1"]
        divisionLeaderBoardsMode2 = divisionLeaderBoardsData[1]["2"]
        divisionLeaderBoardsMode3 = divisionLeaderBoardsData[2]["3"]
        divisionLeaderBoardsMode4 = divisionLeaderBoardsData[3]["4"]
        divisionLeaderBoardsMode5 = divisionLeaderBoardsData[4]["?"]
        randomLeaderBoardsData = leaderBoardsData["Users"][0]["?"]
        randomLeaderBoardsMode1 = randomLeaderBoardsData[0]["1"]
        randomLeaderBoardsMode2 = randomLeaderBoardsData[1]["2"]
        randomLeaderBoardsMode3 = randomLeaderBoardsData[2]["3"]
        randomLeaderBoardsMode4 = randomLeaderBoardsData[3]["4"]
        randomLeaderBoardsMode5 = randomLeaderBoardsData[4]["?"]

        additionLeaderBoardMode1 = sorted(additionLeaderBoardsMode1, key=lambda x: x["Score"], reverse = True)
        additionLeaderBoardMode2 = sorted(additionLeaderBoardsMode2, key=lambda x: x["Score"], reverse = True)
        additionLeaderBoardMode3 = sorted(additionLeaderBoardsMode3, key=lambda x: x["Score"], reverse = True)
        additionLeaderBoardMode4 = sorted(additionLeaderBoardsMode4, key=lambda x: x["Score"], reverse = True)
        additionLeaderBoardMode5 = sorted(additionLeaderBoardsMode5, key=lambda x: x["Score"], reverse = True)

        subtractionLeaderBoardMode1 = sorted(subtractionLeaderBoardsMode1, key=lambda x: x["Score"], reverse = True)
        subtractionLeaderBoardMode2 = sorted(subtractionLeaderBoardsMode2, key=lambda x: x["Score"], reverse = True)
        subtractionLeaderBoardMode3 = sorted(subtractionLeaderBoardsMode3, key=lambda x: x["Score"], reverse = True)
        subtractionLeaderBoardMode4 = sorted(subtractionLeaderBoardsMode4, key=lambda x: x["Score"], reverse = True)
        subtractionLeaderBoardMode5 = sorted(subtractionLeaderBoardsMode5, key=lambda x: x["Score"], reverse = True)

        multiplicationLeaderBoardMode1 = sorted(multiplicationLeaderBoardsMode1, key=lambda x: x["Score"], reverse = True)
        multiplicationLeaderBoardMode2 = sorted(multiplicationLeaderBoardsMode2, key=lambda x: x["Score"], reverse = True)
        multiplicationLeaderBoardMode3 = sorted(multiplicationLeaderBoardsMode3, key=lambda x: x["Score"], reverse = True)
        multiplicationLeaderBoardMode4 = sorted(multiplicationLeaderBoardsMode4, key=lambda x: x["Score"], reverse = True)
        multiplicationLeaderBoardMode5 = sorted(multiplicationLeaderBoardsMode5, key=lambda x: x["Score"], reverse = True)

        divisionLeaderBoardMode1 = sorted(divisionLeaderBoardsMode1, key=lambda x: x["Score"], reverse = True)
        divisionLeaderBoardMode2 = sorted(divisionLeaderBoardsMode2, key=lambda x: x["Score"], reverse = True)
        divisionLeaderBoardMode3 = sorted(divisionLeaderBoardsMode3, key=lambda x: x["Score"], reverse = True)
        divisionLeaderBoardMode4 = sorted(divisionLeaderBoardsMode4, key=lambda x: x["Score"], reverse = True)
        divisionLeaderBoardMode5 = sorted(divisionLeaderBoardsMode5, key=lambda x: x["Score"], reverse = True)

        randomLeaderBoardMode1 = sorted(randomLeaderBoardsMode1, key=lambda x: x["Score"], reverse = True)
        randomLeaderBoardMode2 = sorted(randomLeaderBoardsMode2, key=lambda x: x["Score"], reverse = True)
        randomLeaderBoardMode3 = sorted(randomLeaderBoardsMode3, key=lambda x: x["Score"], reverse = True)
        randomLeaderBoardMode4 = sorted(randomLeaderBoardsMode4, key=lambda x: x["Score"], reverse = True)
        randomLeaderBoardMode5 = sorted(randomLeaderBoardsMode5, key=lambda x: x["Score"], reverse = True)

        window.fill("#000000")
        window.blit(text41,text41Center)
        window.blit(text42,text42Center)
        window.blit(text43,text43Center)
        window.blit(text44,text44Center)
        window.blit(text45,text45Center)
        window.blit(text46,text46Center)

        if (dislpay4Num1 == 1):
            window.fill("#000000")
            window.blit(image9,image9Center)
            window.blit(image9,image9Center)
            window.blit(image9,image9Center)
            window.blit(image9,image9Center)
            window.blit(text41,text41Center)
            window.blit(text42,text42Center)
            window.blit(text43,text43Center)
            window.blit(text44,text44Center)
            window.blit(text45,text45Center)
            window.blit(text46,text46Center)

        elif (dislpay4Num1 == 2):
            window.blit(image9,image9Center)
            window.blit(image9,image9Center)
            window.blit(image9,image9Center)
            window.blit(image10,image10Center)
            window.blit(text41,text41Center)

        elif (dislpay4Num1 == 3):
            window.blit(image9,image9Center)
            window.blit(image9,image9Center)
            window.blit(image9,image9Center)
            window.blit(image11,image11Center)
            window.blit(text42,text42Center)

        elif (dislpay4Num1 == 4):
            window.blit(image9,image9Center)
            window.blit(image9,image9Center)
            window.blit(image9,image9Center)
            window.blit(image12,image12Center)
            window.blit(text43,text43Center)

        elif (dislpay4Num1 == 5):
            window.blit(image9,image9Center)
            window.blit(image9,image9Center)
            window.blit(image9,image9Center)
            window.blit(image13,image13Center)
            window.blit(text44,text44Center)

        elif (dislpay4Num1 == 6):
            window.blit(image9,image9Center)
            window.blit(image9,image9Center)
            window.blit(image9,image9Center)
            window.blit(image14,image14Center)
            window.blit(text45,text45Center)

        elif (dislpay4Num1 == 7):
            window.blit(image9,image9Center)
            window.blit(image9,image9Center)
            window.blit(image9,image9Center)
            window.blit(image15,image15Center)
            window.blit(text46,text46Center)

        if (RandomLevelNum1 == True and randomLeaderboardCheck == False):
            dislpay4Num2 = "?"
            randomLeaderboardCheck = True

        if (dislpay4Num2 == "+"):
            window.blit(image16,image16Center)
            window.blit(text47,text47Center)

            #1
            text63 = font12.render("1. " + str(additionLeaderBoardMode1[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text63,text63Center)
            text68 = font12.render("2. " + str(additionLeaderBoardMode1[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text68,text68Center)
            text73 = font12.render("3. " + str(additionLeaderBoardMode1[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text73,text73Center)
            text78 = font12.render("4. " + str(additionLeaderBoardMode1[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text78,text78Center)
            text83 = font12.render("5. " + str(additionLeaderBoardMode1[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text83,text83Center)

            #2
            text64 = font12.render("1. " + str(additionLeaderBoardMode2[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text64,text64Center)
            text69 = font12.render("2. " + str(additionLeaderBoardMode2[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text69,text69Center)
            text74 = font12.render("3. " + str(additionLeaderBoardMode2[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text74,text74Center)
            text79 = font12.render("4. " + str(additionLeaderBoardMode2[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text79,text79Center)
            text84 = font12.render("5. " + str(additionLeaderBoardMode2[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text84,text84Center)

            #3
            text65 = font12.render("1. " + str(additionLeaderBoardMode3[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text65,text65Center)
            text70 = font12.render("2. " + str(additionLeaderBoardMode3[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text70,text70Center)
            text75 = font12.render("3. " + str(additionLeaderBoardMode3[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text75,text75Center)
            text80 = font12.render("4. " + str(additionLeaderBoardMode3[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text80,text80Center)
            text85 = font12.render("5. " + str(additionLeaderBoardMode3[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text85,text85Center)

            #4
            text66 = font12.render("1. " + str(additionLeaderBoardMode4[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text66,text66Center)
            text71 = font12.render("2. " + str(additionLeaderBoardMode4[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text71,text71Center)
            text76 = font12.render("3. " + str(additionLeaderBoardMode4[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text76,text76Center)
            text81 = font12.render("4. " + str(additionLeaderBoardMode4[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text81,text81Center)
            text86 = font12.render("5. " + str(additionLeaderBoardMode4[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text86,text86Center)

            #5
            text67 = font12.render("1. " + str(additionLeaderBoardMode5[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text67,text67Center)
            text72 = font12.render("2. " + str(additionLeaderBoardMode5[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text72,text72Center)
            text77 = font12.render("3. " + str(additionLeaderBoardMode5[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text77,text77Center)
            text82 = font12.render("4. " + str(additionLeaderBoardMode5[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text82,text82Center)
            text87 = font12.render("5. " + str(additionLeaderBoardMode5[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text87,text87Center)

            #1
            text88 = font13.render("• " + str(additionLeaderBoardMode1[0]["Score"]), True, ("#00FF00"))
            window.blit(text88,text88Center)
            text93 = font13.render("• " + str(additionLeaderBoardMode1[1]["Score"]), True, ("#00FF00"))
            window.blit(text93,text93Center)
            text98 = font13.render("• " + str(additionLeaderBoardMode1[2]["Score"]), True, ("#00FF00"))
            window.blit(text98,text98Center)
            text103 = font13.render("• " + str(additionLeaderBoardMode1[3]["Score"]), True, ("#00FF00"))
            window.blit(text103,text103Center)
            text108 = font13.render("• " + str(additionLeaderBoardMode1[4]["Score"]), True, ("#00FF00"))
            window.blit(text108,text108Center)

            #2
            text89 = font13.render("• " + str(additionLeaderBoardMode2[0]["Score"]), True, ("#00FF00"))
            window.blit(text89,text89Center)
            text94 = font13.render("• " + str(additionLeaderBoardMode2[1]["Score"]), True, ("#00FF00"))
            window.blit(text94,text94Center)
            text99 = font13.render("• " + str(additionLeaderBoardMode2[2]["Score"]), True, ("#00FF00"))
            window.blit(text99,text99Center)
            text104 = font13.render("• " + str(additionLeaderBoardMode2[3]["Score"]), True, ("#00FF00"))
            window.blit(text104,text104Center)
            text109 = font13.render("• " + str(additionLeaderBoardMode2[4]["Score"]), True, ("#00FF00"))
            window.blit(text109,text109Center)

            #3
            text90 = font13.render("• " + str(additionLeaderBoardMode3[0]["Score"]), True, ("#00FF00"))
            window.blit(text90,text90Center)
            text95 = font13.render("• " + str(additionLeaderBoardMode3[1]["Score"]), True, ("#00FF00"))
            window.blit(text95,text95Center)
            text100 = font13.render("• " + str(additionLeaderBoardMode3[2]["Score"]), True, ("#00FF00"))
            window.blit(text100,text100Center)
            text105 = font13.render("• " + str(additionLeaderBoardMode3[3]["Score"]), True, ("#00FF00"))
            window.blit(text105,text105Center)
            text110 = font13.render("• " + str(additionLeaderBoardMode3[4]["Score"]), True, ("#00FF00"))
            window.blit(text110,text110Center)

            #4
            text91 = font13.render("• " + str(additionLeaderBoardMode4[0]["Score"]), True, ("#00FF00"))
            window.blit(text91,text91Center)
            text96 = font13.render("• " + str(additionLeaderBoardMode4[1]["Score"]), True, ("#00FF00"))
            window.blit(text96,text96Center)
            text101 = font13.render("• " + str(additionLeaderBoardMode4[2]["Score"]), True, ("#00FF00"))
            window.blit(text101,text101Center)
            text106 = font13.render("• " + str(additionLeaderBoardMode4[3]["Score"]), True, ("#00FF00"))
            window.blit(text106,text106Center)
            text111 = font13.render("• " + str(additionLeaderBoardMode4[4]["Score"]), True, ("#00FF00"))
            window.blit(text111,text111Center)

            #5
            text92 = font13.render("• " + str(additionLeaderBoardMode5[0]["Score"]), True, ("#00FF00"))
            window.blit(text92,text92Center)
            text97 = font13.render("• " + str(additionLeaderBoardMode5[1]["Score"]), True, ("#00FF00"))
            window.blit(text97,text97Center)
            text102 = font13.render("• " + str(additionLeaderBoardMode5[2]["Score"]), True, ("#00FF00"))
            window.blit(text102,text102Center)
            text107 = font13.render("• " + str(additionLeaderBoardMode5[3]["Score"]), True, ("#00FF00"))
            window.blit(text107,text107Center)
            text112 = font13.render("• " + str(additionLeaderBoardMode5[4]["Score"]), True, ("#00FF00"))
            window.blit(text112,text112Center)
            
        elif (dislpay4Num2 == "-"):
            window.blit(image17,image17Center)
            window.blit(text48,text48Center)

            #1
            text63 = font12.render("1. " + str(subtractionLeaderBoardMode1[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text63,text63Center)
            text68 = font12.render("2. " + str(subtractionLeaderBoardMode1[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text68,text68Center)
            text73 = font12.render("3. " + str(subtractionLeaderBoardMode1[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text73,text73Center)
            text78 = font12.render("4. " + str(subtractionLeaderBoardMode1[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text78,text78Center)
            text83 = font12.render("5. " + str(subtractionLeaderBoardMode1[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text83,text83Center)

            #2
            text64 = font12.render("1. " + str(subtractionLeaderBoardMode2[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text64,text64Center)
            text69 = font12.render("2. " + str(subtractionLeaderBoardMode2[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text69,text69Center)
            text74 = font12.render("3. " + str(subtractionLeaderBoardMode2[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text74,text74Center)
            text79 = font12.render("4. " + str(subtractionLeaderBoardMode2[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text79,text79Center)
            text84 = font12.render("5. " + str(subtractionLeaderBoardMode2[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text84,text84Center)

            #3
            text65 = font12.render("1. " + str(subtractionLeaderBoardMode3[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text65,text65Center)
            text70 = font12.render("2. " + str(subtractionLeaderBoardMode3[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text70,text70Center)
            text75 = font12.render("3. " + str(subtractionLeaderBoardMode3[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text75,text75Center)
            text80 = font12.render("4. " + str(subtractionLeaderBoardMode3[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text80,text80Center)
            text85 = font12.render("5. " + str(subtractionLeaderBoardMode3[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text85,text85Center)

            #4
            text66 = font12.render("1. " + str(subtractionLeaderBoardMode4[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text66,text66Center)
            text71 = font12.render("2. " + str(subtractionLeaderBoardMode4[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text71,text71Center)
            text76 = font12.render("3. " + str(subtractionLeaderBoardMode4[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text76,text76Center)
            text81 = font12.render("4. " + str(subtractionLeaderBoardMode4[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text81,text81Center)
            text86 = font12.render("5. " + str(subtractionLeaderBoardMode4[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text86,text86Center)

            #5
            text67 = font12.render("1. " + str(subtractionLeaderBoardMode5[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text67,text67Center)
            text72 = font12.render("2. " + str(subtractionLeaderBoardMode5[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text72,text72Center)
            text77 = font12.render("3. " + str(subtractionLeaderBoardMode5[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text77,text77Center)
            text82 = font12.render("4. " + str(subtractionLeaderBoardMode5[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text82,text82Center)
            text87 = font12.render("5. " + str(subtractionLeaderBoardMode5[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text87,text87Center)

            #1
            text88 = font13.render("• " + str(subtractionLeaderBoardMode1[0]["Score"]), True, ("#00FF00"))
            window.blit(text88,text88Center)
            text93 = font13.render("• " + str(subtractionLeaderBoardMode1[1]["Score"]), True, ("#00FF00"))
            window.blit(text93,text93Center)
            text98 = font13.render("• " + str(subtractionLeaderBoardMode1[2]["Score"]), True, ("#00FF00"))
            window.blit(text98,text98Center)
            text103 = font13.render("• " + str(subtractionLeaderBoardMode1[3]["Score"]), True, ("#00FF00"))
            window.blit(text103,text103Center)
            text108 = font13.render("• " + str(subtractionLeaderBoardMode1[4]["Score"]), True, ("#00FF00"))
            window.blit(text108,text108Center)

            #2
            text89 = font13.render("• " + str(subtractionLeaderBoardMode2[0]["Score"]), True, ("#00FF00"))
            window.blit(text89,text89Center)
            text94 = font13.render("• " + str(subtractionLeaderBoardMode2[1]["Score"]), True, ("#00FF00"))
            window.blit(text94,text94Center)
            text99 = font13.render("• " + str(subtractionLeaderBoardMode2[2]["Score"]), True, ("#00FF00"))
            window.blit(text99,text99Center)
            text104 = font13.render("• " + str(subtractionLeaderBoardMode2[3]["Score"]), True, ("#00FF00"))
            window.blit(text104,text104Center)
            text109 = font13.render("• " + str(subtractionLeaderBoardMode2[4]["Score"]), True, ("#00FF00"))
            window.blit(text109,text109Center)

            #3
            text90 = font13.render("• " + str(subtractionLeaderBoardMode3[0]["Score"]), True, ("#00FF00"))
            window.blit(text90,text90Center)
            text95 = font13.render("• " + str(subtractionLeaderBoardMode3[1]["Score"]), True, ("#00FF00"))
            window.blit(text95,text95Center)
            text100 = font13.render("• " + str(subtractionLeaderBoardMode3[2]["Score"]), True, ("#00FF00"))
            window.blit(text100,text100Center)
            text105 = font13.render("• " + str(subtractionLeaderBoardMode3[3]["Score"]), True, ("#00FF00"))
            window.blit(text105,text105Center)
            text110 = font13.render("• " + str(subtractionLeaderBoardMode3[4]["Score"]), True, ("#00FF00"))
            window.blit(text110,text110Center)

            #4
            text91 = font13.render("• " + str(subtractionLeaderBoardMode4[0]["Score"]), True, ("#00FF00"))
            window.blit(text91,text91Center)
            text96 = font13.render("• " + str(subtractionLeaderBoardMode4[1]["Score"]), True, ("#00FF00"))
            window.blit(text96,text96Center)
            text101 = font13.render("• " + str(subtractionLeaderBoardMode4[2]["Score"]), True, ("#00FF00"))
            window.blit(text101,text101Center)
            text106 = font13.render("• " + str(subtractionLeaderBoardMode4[3]["Score"]), True, ("#00FF00"))
            window.blit(text106,text106Center)
            text111 = font13.render("• " + str(subtractionLeaderBoardMode4[4]["Score"]), True, ("#00FF00"))
            window.blit(text111,text111Center)

            #5
            text92 = font13.render("• " + str(subtractionLeaderBoardMode5[0]["Score"]), True, ("#00FF00"))
            window.blit(text92,text92Center)
            text97 = font13.render("• " + str(subtractionLeaderBoardMode5[1]["Score"]), True, ("#00FF00"))
            window.blit(text97,text97Center)
            text102 = font13.render("• " + str(subtractionLeaderBoardMode5[2]["Score"]), True, ("#00FF00"))
            window.blit(text102,text102Center)
            text107 = font13.render("• " + str(subtractionLeaderBoardMode5[3]["Score"]), True, ("#00FF00"))
            window.blit(text107,text107Center)
            text112 = font13.render("• " + str(subtractionLeaderBoardMode5[4]["Score"]), True, ("#00FF00"))
            window.blit(text112,text112Center)

        elif (dislpay4Num2 == "×"):
            window.blit(image18,image18Center)
            window.blit(text49,text49Center)

            #1
            text63 = font12.render("1. " + str(multiplicationLeaderBoardMode1[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text63,text63Center)
            text68 = font12.render("2. " + str(multiplicationLeaderBoardMode1[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text68,text68Center)
            text73 = font12.render("3. " + str(multiplicationLeaderBoardMode1[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text73,text73Center)
            text78 = font12.render("4. " + str(multiplicationLeaderBoardMode1[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text78,text78Center)
            text83 = font12.render("5. " + str(multiplicationLeaderBoardMode1[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text83,text83Center)

            #2
            text64 = font12.render("1. " + str(multiplicationLeaderBoardMode2[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text64,text64Center)
            text69 = font12.render("2. " + str(multiplicationLeaderBoardMode2[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text69,text69Center)
            text74 = font12.render("3. " + str(multiplicationLeaderBoardMode2[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text74,text74Center)
            text79 = font12.render("4. " + str(multiplicationLeaderBoardMode2[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text79,text79Center)
            text84 = font12.render("5. " + str(multiplicationLeaderBoardMode2[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text84,text84Center)

            #3
            text65 = font12.render("1. " + str(multiplicationLeaderBoardMode3[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text65,text65Center)
            text70 = font12.render("2. " + str(multiplicationLeaderBoardMode3[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text70,text70Center)
            text75 = font12.render("3. " + str(multiplicationLeaderBoardMode3[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text75,text75Center)
            text80 = font12.render("4. " + str(multiplicationLeaderBoardMode3[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text80,text80Center)
            text85 = font12.render("5. " + str(multiplicationLeaderBoardMode3[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text85,text85Center)

            #4
            text66 = font12.render("1. " + str(multiplicationLeaderBoardMode4[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text66,text66Center)
            text71 = font12.render("2. " + str(multiplicationLeaderBoardMode4[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text71,text71Center)
            text76 = font12.render("3. " + str(multiplicationLeaderBoardMode4[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text76,text76Center)
            text81 = font12.render("4. " + str(multiplicationLeaderBoardMode4[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text81,text81Center)
            text86 = font12.render("5. " + str(multiplicationLeaderBoardMode4[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text86,text86Center)

            #5
            text67 = font12.render("1. " + str(multiplicationLeaderBoardMode5[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text67,text67Center)
            text72 = font12.render("2. " + str(multiplicationLeaderBoardMode5[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text72,text72Center)
            text77 = font12.render("3. " + str(multiplicationLeaderBoardMode5[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text77,text77Center)
            text82 = font12.render("4. " + str(multiplicationLeaderBoardMode5[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text82,text82Center)
            text87 = font12.render("5. " + str(multiplicationLeaderBoardMode5[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text87,text87Center)

            #1
            text88 = font13.render("• " + str(multiplicationLeaderBoardMode1[0]["Score"]), True, ("#00FF00"))
            window.blit(text88,text88Center)
            text93 = font13.render("• " + str(multiplicationLeaderBoardMode1[1]["Score"]), True, ("#00FF00"))
            window.blit(text93,text93Center)
            text98 = font13.render("• " + str(multiplicationLeaderBoardMode1[2]["Score"]), True, ("#00FF00"))
            window.blit(text98,text98Center)
            text103 = font13.render("• " + str(multiplicationLeaderBoardMode1[3]["Score"]), True, ("#00FF00"))
            window.blit(text103,text103Center)
            text108 = font13.render("• " + str(multiplicationLeaderBoardMode1[4]["Score"]), True, ("#00FF00"))
            window.blit(text108,text108Center)

            #2
            text89 = font13.render("• " + str(multiplicationLeaderBoardMode2[0]["Score"]), True, ("#00FF00"))
            window.blit(text89,text89Center)
            text94 = font13.render("• " + str(multiplicationLeaderBoardMode2[1]["Score"]), True, ("#00FF00"))
            window.blit(text94,text94Center)
            text99 = font13.render("• " + str(multiplicationLeaderBoardMode2[2]["Score"]), True, ("#00FF00"))
            window.blit(text99,text99Center)
            text104 = font13.render("• " + str(multiplicationLeaderBoardMode2[3]["Score"]), True, ("#00FF00"))
            window.blit(text104,text104Center)
            text109 = font13.render("• " + str(multiplicationLeaderBoardMode2[4]["Score"]), True, ("#00FF00"))
            window.blit(text109,text109Center)

            #3
            text90 = font13.render("• " + str(multiplicationLeaderBoardMode3[0]["Score"]), True, ("#00FF00"))
            window.blit(text90,text90Center)
            text95 = font13.render("• " + str(multiplicationLeaderBoardMode3[1]["Score"]), True, ("#00FF00"))
            window.blit(text95,text95Center)
            text100 = font13.render("• " + str(multiplicationLeaderBoardMode3[2]["Score"]), True, ("#00FF00"))
            window.blit(text100,text100Center)
            text105 = font13.render("• " + str(multiplicationLeaderBoardMode3[3]["Score"]), True, ("#00FF00"))
            window.blit(text105,text105Center)
            text110 = font13.render("• " + str(multiplicationLeaderBoardMode3[4]["Score"]), True, ("#00FF00"))
            window.blit(text110,text110Center)

            #4
            text91 = font13.render("• " + str(multiplicationLeaderBoardMode4[0]["Score"]), True, ("#00FF00"))
            window.blit(text91,text91Center)
            text96 = font13.render("• " + str(multiplicationLeaderBoardMode4[1]["Score"]), True, ("#00FF00"))
            window.blit(text96,text96Center)
            text101 = font13.render("• " + str(multiplicationLeaderBoardMode4[2]["Score"]), True, ("#00FF00"))
            window.blit(text101,text101Center)
            text106 = font13.render("• " + str(multiplicationLeaderBoardMode4[3]["Score"]), True, ("#00FF00"))
            window.blit(text106,text106Center)
            text111 = font13.render("• " + str(multiplicationLeaderBoardMode4[4]["Score"]), True, ("#00FF00"))
            window.blit(text111,text111Center)

            #5
            text92 = font13.render("• " + str(multiplicationLeaderBoardMode5[0]["Score"]), True, ("#00FF00"))
            window.blit(text92,text92Center)
            text97 = font13.render("• " + str(multiplicationLeaderBoardMode5[1]["Score"]), True, ("#00FF00"))
            window.blit(text97,text97Center)
            text102 = font13.render("• " + str(multiplicationLeaderBoardMode5[2]["Score"]), True, ("#00FF00"))
            window.blit(text102,text102Center)
            text107 = font13.render("• " + str(multiplicationLeaderBoardMode5[3]["Score"]), True, ("#00FF00"))
            window.blit(text107,text107Center)
            text112 = font13.render("• " + str(multiplicationLeaderBoardMode5[4]["Score"]), True, ("#00FF00"))
            window.blit(text112,text112Center)

        elif (dislpay4Num2 == "÷"):
            window.blit(image19,image19Center)
            window.blit(text50,text50Center)

            #1
            text63 = font12.render("1. " + str(divisionLeaderBoardMode1[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text63,text63Center)
            text68 = font12.render("2. " + str(divisionLeaderBoardMode1[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text68,text68Center)
            text73 = font12.render("3. " + str(divisionLeaderBoardMode1[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text73,text73Center)
            text78 = font12.render("4. " + str(divisionLeaderBoardMode1[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text78,text78Center)
            text83 = font12.render("5. " + str(divisionLeaderBoardMode1[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text83,text83Center)

            #2
            text64 = font12.render("1. " + str(divisionLeaderBoardMode2[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text64,text64Center)
            text69 = font12.render("2. " + str(divisionLeaderBoardMode2[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text69,text69Center)
            text74 = font12.render("3. " + str(divisionLeaderBoardMode2[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text74,text74Center)
            text79 = font12.render("4. " + str(divisionLeaderBoardMode2[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text79,text79Center)
            text84 = font12.render("5. " + str(divisionLeaderBoardMode2[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text84,text84Center)

            #3
            text65 = font12.render("1. " + str(divisionLeaderBoardMode3[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text65,text65Center)
            text70 = font12.render("2. " + str(divisionLeaderBoardMode3[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text70,text70Center)
            text75 = font12.render("3. " + str(divisionLeaderBoardMode3[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text75,text75Center)
            text80 = font12.render("4. " + str(divisionLeaderBoardMode3[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text80,text80Center)
            text85 = font12.render("5. " + str(divisionLeaderBoardMode3[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text85,text85Center)

            #4
            text66 = font12.render("1. " + str(divisionLeaderBoardMode4[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text66,text66Center)
            text71 = font12.render("2. " + str(divisionLeaderBoardMode4[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text71,text71Center)
            text76 = font12.render("3. " + str(divisionLeaderBoardMode4[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text76,text76Center)
            text81 = font12.render("4. " + str(divisionLeaderBoardMode4[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text81,text81Center)
            text86 = font12.render("5. " + str(divisionLeaderBoardMode4[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text86,text86Center)

            #5
            text67 = font12.render("1. " + str(divisionLeaderBoardMode5[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text67,text67Center)
            text72 = font12.render("2. " + str(divisionLeaderBoardMode5[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text72,text72Center)
            text77 = font12.render("3. " + str(divisionLeaderBoardMode5[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text77,text77Center)
            text82 = font12.render("4. " + str(divisionLeaderBoardMode5[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text82,text82Center)
            text87 = font12.render("5. " + str(divisionLeaderBoardMode5[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text87,text87Center)

            #1
            text88 = font13.render("• " + str(divisionLeaderBoardMode1[0]["Score"]), True, ("#00FF00"))
            window.blit(text88,text88Center)
            text93 = font13.render("• " + str(divisionLeaderBoardMode1[1]["Score"]), True, ("#00FF00"))
            window.blit(text93,text93Center)
            text98 = font13.render("• " + str(divisionLeaderBoardMode1[2]["Score"]), True, ("#00FF00"))
            window.blit(text98,text98Center)
            text103 = font13.render("• " + str(divisionLeaderBoardMode1[3]["Score"]), True, ("#00FF00"))
            window.blit(text103,text103Center)
            text108 = font13.render("• " + str(divisionLeaderBoardMode1[4]["Score"]), True, ("#00FF00"))
            window.blit(text108,text108Center)

            #2
            text89 = font13.render("• " + str(divisionLeaderBoardMode2[0]["Score"]), True, ("#00FF00"))
            window.blit(text89,text89Center)
            text94 = font13.render("• " + str(divisionLeaderBoardMode2[1]["Score"]), True, ("#00FF00"))
            window.blit(text94,text94Center)
            text99 = font13.render("• " + str(divisionLeaderBoardMode2[2]["Score"]), True, ("#00FF00"))
            window.blit(text99,text99Center)
            text104 = font13.render("• " + str(divisionLeaderBoardMode2[3]["Score"]), True, ("#00FF00"))
            window.blit(text104,text104Center)
            text109 = font13.render("• " + str(divisionLeaderBoardMode2[4]["Score"]), True, ("#00FF00"))
            window.blit(text109,text109Center)

            #3
            text90 = font13.render("• " + str(divisionLeaderBoardMode3[0]["Score"]), True, ("#00FF00"))
            window.blit(text90,text90Center)
            text95 = font13.render("• " + str(divisionLeaderBoardMode3[1]["Score"]), True, ("#00FF00"))
            window.blit(text95,text95Center)
            text100 = font13.render("• " + str(divisionLeaderBoardMode3[2]["Score"]), True, ("#00FF00"))
            window.blit(text100,text100Center)
            text105 = font13.render("• " + str(divisionLeaderBoardMode3[3]["Score"]), True, ("#00FF00"))
            window.blit(text105,text105Center)
            text110 = font13.render("• " + str(divisionLeaderBoardMode3[4]["Score"]), True, ("#00FF00"))
            window.blit(text110,text110Center)

            #4
            text91 = font13.render("• " + str(divisionLeaderBoardMode4[0]["Score"]), True, ("#00FF00"))
            window.blit(text91,text91Center)
            text96 = font13.render("• " + str(divisionLeaderBoardMode4[1]["Score"]), True, ("#00FF00"))
            window.blit(text96,text96Center)
            text101 = font13.render("• " + str(divisionLeaderBoardMode4[2]["Score"]), True, ("#00FF00"))
            window.blit(text101,text101Center)
            text106 = font13.render("• " + str(divisionLeaderBoardMode4[3]["Score"]), True, ("#00FF00"))
            window.blit(text106,text106Center)
            text111 = font13.render("• " + str(divisionLeaderBoardMode4[4]["Score"]), True, ("#00FF00"))
            window.blit(text111,text111Center)

            #5
            text92 = font13.render("• " + str(divisionLeaderBoardMode5[0]["Score"]), True, ("#00FF00"))
            window.blit(text92,text92Center)
            text97 = font13.render("• " + str(divisionLeaderBoardMode5[1]["Score"]), True, ("#00FF00"))
            window.blit(text97,text97Center)
            text102 = font13.render("• " + str(divisionLeaderBoardMode5[2]["Score"]), True, ("#00FF00"))
            window.blit(text102,text102Center)
            text107 = font13.render("• " + str(divisionLeaderBoardMode5[3]["Score"]), True, ("#00FF00"))
            window.blit(text107,text107Center)
            text112 = font13.render("• " + str(divisionLeaderBoardMode5[4]["Score"]), True, ("#00FF00"))
            window.blit(text112,text112Center)

        elif (dislpay4Num2 == "?"):
            window.blit(image20,image20Center)
            window.blit(text51,text51Center)

            #1
            text63 = font12.render("1. " + str(randomLeaderBoardMode1[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text63,text63Center)
            text68 = font12.render("2. " + str(randomLeaderBoardMode1[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text68,text68Center)
            text73 = font12.render("3. " + str(randomLeaderBoardMode1[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text73,text73Center)
            text78 = font12.render("4. " + str(randomLeaderBoardMode1[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text78,text78Center)
            text83 = font12.render("5. " + str(randomLeaderBoardMode1[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text83,text83Center)

            #2
            text64 = font12.render("1. " + str(randomLeaderBoardMode2[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text64,text64Center)
            text69 = font12.render("2. " + str(randomLeaderBoardMode2[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text69,text69Center)
            text74 = font12.render("3. " + str(randomLeaderBoardMode2[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text74,text74Center)
            text79 = font12.render("4. " + str(randomLeaderBoardMode2[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text79,text79Center)
            text84 = font12.render("5. " + str(randomLeaderBoardMode2[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text84,text84Center)

            #3
            text65 = font12.render("1. " + str(randomLeaderBoardMode3[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text65,text65Center)
            text70 = font12.render("2. " + str(randomLeaderBoardMode3[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text70,text70Center)
            text75 = font12.render("3. " + str(randomLeaderBoardMode3[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text75,text75Center)
            text80 = font12.render("4. " + str(randomLeaderBoardMode3[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text80,text80Center)
            text85 = font12.render("5. " + str(randomLeaderBoardMode3[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text85,text85Center)

            #4
            text66 = font12.render("1. " + str(randomLeaderBoardMode4[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text66,text66Center)
            text71 = font12.render("2. " + str(randomLeaderBoardMode4[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text71,text71Center)
            text76 = font12.render("3. " + str(randomLeaderBoardMode4[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text76,text76Center)
            text81 = font12.render("4. " + str(randomLeaderBoardMode4[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text81,text81Center)
            text86 = font12.render("5. " + str(randomLeaderBoardMode4[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text86,text86Center)

            #5
            text67 = font12.render("1. " + str(randomLeaderBoardMode5[0]["Username"]), True, ("#FFFFFF"))
            window.blit(text67,text67Center)
            text72 = font12.render("2. " + str(randomLeaderBoardMode5[1]["Username"]), True, ("#FFFFFF"))
            window.blit(text72,text72Center)
            text77 = font12.render("3. " + str(randomLeaderBoardMode5[2]["Username"]), True, ("#FFFFFF"))
            window.blit(text77,text77Center)
            text82 = font12.render("4. " + str(randomLeaderBoardMode5[3]["Username"]), True, ("#FFFFFF"))
            window.blit(text82,text82Center)
            text87 = font12.render("5. " + str(randomLeaderBoardMode5[4]["Username"]), True, ("#FFFFFF"))
            window.blit(text87,text87Center)

            #1
            text88 = font13.render("• " + str(randomLeaderBoardMode1[0]["Score"]), True, ("#00FF00"))
            window.blit(text88,text88Center)
            text93 = font13.render("• " + str(randomLeaderBoardMode1[1]["Score"]), True, ("#00FF00"))
            window.blit(text93,text93Center)
            text98 = font13.render("• " + str(randomLeaderBoardMode1[2]["Score"]), True, ("#00FF00"))
            window.blit(text98,text98Center)
            text103 = font13.render("• " + str(randomLeaderBoardMode1[3]["Score"]), True, ("#00FF00"))
            window.blit(text103,text103Center)
            text108 = font13.render("• " + str(randomLeaderBoardMode1[4]["Score"]), True, ("#00FF00"))
            window.blit(text108,text108Center)

            #2
            text89 = font13.render("• " + str(randomLeaderBoardMode2[0]["Score"]), True, ("#00FF00"))
            window.blit(text89,text89Center)
            text94 = font13.render("• " + str(randomLeaderBoardMode2[1]["Score"]), True, ("#00FF00"))
            window.blit(text94,text94Center)
            text99 = font13.render("• " + str(randomLeaderBoardMode2[2]["Score"]), True, ("#00FF00"))
            window.blit(text99,text99Center)
            text104 = font13.render("• " + str(randomLeaderBoardMode2[3]["Score"]), True, ("#00FF00"))
            window.blit(text104,text104Center)
            text109 = font13.render("• " + str(randomLeaderBoardMode2[4]["Score"]), True, ("#00FF00"))
            window.blit(text109,text109Center)

            #3
            text90 = font13.render("• " + str(randomLeaderBoardMode3[0]["Score"]), True, ("#00FF00"))
            window.blit(text90,text90Center)
            text95 = font13.render("• " + str(randomLeaderBoardMode3[1]["Score"]), True, ("#00FF00"))
            window.blit(text95,text95Center)
            text100 = font13.render("• " + str(randomLeaderBoardMode3[2]["Score"]), True, ("#00FF00"))
            window.blit(text100,text100Center)
            text105 = font13.render("• " + str(randomLeaderBoardMode3[3]["Score"]), True, ("#00FF00"))
            window.blit(text105,text105Center)
            text110 = font13.render("• " + str(randomLeaderBoardMode3[4]["Score"]), True, ("#00FF00"))
            window.blit(text110,text110Center)

            #4
            text91 = font13.render("• " + str(randomLeaderBoardMode4[0]["Score"]), True, ("#00FF00"))
            window.blit(text91,text91Center)
            text96 = font13.render("• " + str(randomLeaderBoardMode4[1]["Score"]), True, ("#00FF00"))
            window.blit(text96,text96Center)
            text101 = font13.render("• " + str(randomLeaderBoardMode4[2]["Score"]), True, ("#00FF00"))
            window.blit(text101,text101Center)
            text106 = font13.render("• " + str(randomLeaderBoardMode4[3]["Score"]), True, ("#00FF00"))
            window.blit(text106,text106Center)
            text111 = font13.render("• " + str(randomLeaderBoardMode4[4]["Score"]), True, ("#00FF00"))
            window.blit(text111,text111Center)

            #5
            text92 = font13.render("• " + str(randomLeaderBoardMode5[0]["Score"]), True, ("#00FF00"))
            window.blit(text92,text92Center)
            text97 = font13.render("• " + str(randomLeaderBoardMode5[1]["Score"]), True, ("#00FF00"))
            window.blit(text97,text97Center)
            text102 = font13.render("• " + str(randomLeaderBoardMode5[2]["Score"]), True, ("#00FF00"))
            window.blit(text102,text102Center)
            text107 = font13.render("• " + str(randomLeaderBoardMode5[3]["Score"]), True, ("#00FF00"))
            window.blit(text107,text107Center)
            text112 = font13.render("• " + str(randomLeaderBoardMode5[4]["Score"]), True, ("#00FF00"))
            window.blit(text112,text112Center)

        window.blit(text40,text40Center)
        window.blit(text53,text53Center)
        window.blit(text54,text54Center)
        window.blit(text55,text55Center)
        window.blit(text56,text56Center)
        window.blit(text57,text57Center)
        window.blit(text58,text58Center)
        window.blit(text59,text59Center)
        window.blit(text60,text60Center)
        window.blit(text61,text61Center)

    elif (display == 5):
        if (display5Num1 == 1):
            window.fill("#000000")
            window.blit(text136,text136Center)
            userInput2 = userInput2.upper()
            text137 = font7.render(userInput2, True, ("#FFFFFF"))
            text137Center = text137.get_rect(center = (windowWidth / 2, windowHeight / 2 + 50))
            window.blit(text137,text137Center)
            pygame.display.update()
            pygame.time.wait(250)

        elif (display5Num1 == 2):
            window.fill("#000000")
            window.blit(text113,text113Center)
            window.blit(text114,text114Center)
            pygame.display.update()
            pygame.time.wait(250)
            display5Num1 = 3

        elif (display5Num1 == 3):
            window.fill("#000000")
            window.blit(text113,text113Center)
            window.blit(text115,text115Center)
            pygame.display.update()
            pygame.time.wait(250)
            display5Num1 = 4

        elif (display5Num1 == 4):
            window.fill("#000000")
            window.blit(text113,text113Center)
            window.blit(text116,text116Center)
            pygame.display.update()
            pygame.time.wait(250)
            display5Num1 = 5

        elif (display5Num1 == 5):
            window.fill("#000000")
            window.blit(text113,text113Center)
            window.blit(text117,text117Center)
            pygame.display.update()
            pygame.time.wait(250)
            display5Num1 = 6

        elif (display5Num1 == 6):
            window.fill("#000000")
            window.blit(text113,text113Center)
            window.blit(text118,text118Center)
            pygame.display.update()
            pygame.time.wait(250)
            display5Num1 = 7

        elif (display5Num1 == 7):
            window.fill("#000000")
            window.blit(text113,text113Center)
            window.blit(text119,text119Center)
            pygame.display.update()
            pygame.time.wait(250)
            display5Num1 = 8

        elif (display5Num1 == 8):
            window.fill("#000000")
            window.blit(text113,text113Center)
            window.blit(text120,text120Center)
            pygame.display.update()
            pygame.time.wait(250)
            display5Num1 = 9

        elif (display5Num1 == 9):
            window.fill("#000000")
            window.blit(text113,text113Center)
            window.blit(text121,text121Center)
            pygame.display.update()
            pygame.time.wait(250)
            display5Num1 = 10

        elif (display5Num1 == 10):
            window.fill("#000000")
            window.blit(text113,text113Center)
            window.blit(text122,text122Center)
            pygame.display.update()
            pygame.time.wait(250)
            display5Num1 = 11

        elif (display5Num1 == 11):
            window.fill("#000000")
            window.blit(text113,text113Center)
            window.blit(text123,text123Center)
            pygame.display.update()
            pygame.time.wait(250)
            display5Num1 = 12

        elif (display5Num1 == 12):
            window.fill("#000000")
            window.blit(text113,text113Center)
            window.blit(text124,text124Center)
            pygame.display.update()
            pygame.time.wait(250)
            display5Num1 = 13

        elif (display5Num1 == 13):
            window.fill("#000000")
            window.blit(text113,text113Center)
            window.blit(text125,text125Center)
            pygame.display.update()
            pygame.time.wait(250)
            display5Num1 = 14

        elif (display5Num1 == 14):
            window.fill("#000000")
            window.blit(text113,text113Center)
            window.blit(text126,text126Center)
            pygame.display.update()
            pygame.time.wait(250)
            display5Num1 = 15

        elif (display5Num1 == 15):
            window.fill("#000000")
            window.blit(text113,text113Center)
            window.blit(text127,text127Center)
            pygame.display.update()
            pygame.time.wait(250)
            display5Num1 = 16

        elif (display5Num1 == 16):
            window.fill("#000000")
            window.blit(text113,text113Center)
            window.blit(text128,text128Center)
            pygame.display.update()
            pygame.time.wait(250)
            display5Num1 = 17

        elif (display5Num1 == 17):
            window.fill("#000000")
            window.blit(text113,text113Center)
            window.blit(text129,text129Center)
            pygame.display.update()
            pygame.time.wait(250)
            display5Num1 = 18
        
        elif (display5Num1 == 18):
            window.fill("#000000")
            window.blit(text113,text113Center)
            window.blit(text130,text130Center)
            pygame.display.update()
            pygame.time.wait(250)
            display5Num1 = 19

        elif (display5Num1 == 19):
            window.fill("#000000")
            window.blit(text113,text113Center)
            window.blit(text131,text131Center)
            pygame.display.update()
            pygame.time.wait(250)
            display5Num1 = 20

        elif (display5Num1 == 20):
            window.fill("#000000")
            window.blit(text113,text113Center)
            window.blit(text132,text132Center)
            pygame.display.update()
            pygame.time.wait(250)
            display5Num1 = 21

        elif (display5Num1 == 21):
            window.fill("#000000")
            window.blit(text113,text113Center)
            window.blit(text133,text133Center)
            pygame.display.update()

            if ((RandomLevelNum1 == False) and (userOperation == "+")):
                if ((RandomLevelNum2 == False) and (userDigits == 1)):
                    if (review3 == leaderBoardsReviewData["Users"][0]["+"][0]["1"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][0]["1"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][0]["1"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["+"][0]["1"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][0]["1"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][0]["1"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["+"][0]["1"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][0]["1"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][0]["1"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["+"][0]["1"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][0]["1"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][0]["1"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["+"][0]["1"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][0]["1"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][0]["1"][0]["Username"] = username

                elif ((RandomLevelNum2 == False) and (userDigits == 2)):
                    if (review3 == leaderBoardsReviewData["Users"][0]["+"][1]["2"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][1]["2"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][1]["2"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["+"][1]["2"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][1]["2"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][1]["2"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["+"][1]["2"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][1]["2"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][1]["2"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["+"][1]["2"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][1]["2"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][1]["2"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["+"][1]["2"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][1]["2"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][1]["2"][0]["Username"] = username

                elif ((RandomLevelNum2 == False) and (userDigits == 3)):
                    if (review3 == leaderBoardsReviewData["Users"][0]["+"][2]["3"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][2]["3"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][2]["3"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["+"][2]["3"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][2]["3"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][2]["3"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["+"][2]["3"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][2]["3"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][2]["3"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["+"][2]["3"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][2]["3"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][2]["3"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["+"][2]["3"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][2]["3"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][2]["3"][0]["Username"] = username

                elif ((RandomLevelNum2 == False) and (userDigits == 4)):
                    if (review3 == leaderBoardsReviewData["Users"][0]["+"][3]["4"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][3]["4"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][3]["4"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["+"][3]["4"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][3]["4"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][3]["4"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["+"][3]["4"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][3]["4"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][3]["4"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["+"][3]["4"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][3]["4"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][3]["4"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["+"][3]["4"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][3]["4"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][3]["4"][0]["Username"] = username

                elif (RandomLevelNum2 == True) and (userDigits == 1 or userDigits == 2 or userDigits == 3 or userDigits == 4):
                    if (review3 == leaderBoardsReviewData["Users"][0]["+"][4]["?"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][4]["?"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][4]["?"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["+"][4]["?"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][4]["?"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][4]["?"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["+"][4]["?"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][4]["?"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][4]["?"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["+"][4]["?"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][4]["?"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][4]["?"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["+"][4]["?"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["+"][4]["?"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["+"][4]["?"][0]["Username"] = username

            elif ((RandomLevelNum1 == False) and (userOperation == "-")):
                if ((RandomLevelNum2 == False) and (userDigits == 1)):
                    if (review3 == leaderBoardsReviewData["Users"][0]["-"][0]["1"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][0]["1"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][0]["1"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["-"][0]["1"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][0]["1"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][0]["1"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["-"][0]["1"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][0]["1"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][0]["1"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["-"][0]["1"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][0]["1"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][0]["1"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["-"][0]["1"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][0]["1"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][0]["1"][0]["Username"] = username

                elif ((RandomLevelNum2 == False) and (userDigits == 2)):
                    if (review3 == leaderBoardsReviewData["Users"][0]["-"][1]["2"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][1]["2"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][1]["2"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["-"][1]["2"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][1]["2"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][1]["2"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["-"][1]["2"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][1]["2"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][1]["2"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["-"][1]["2"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][1]["2"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][1]["2"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["-"][1]["2"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][1]["2"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][1]["2"][0]["Username"] = username

                elif ((RandomLevelNum2 == False) and (userDigits == 3)):
                    if (review3 == leaderBoardsReviewData["Users"][0]["-"][2]["3"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][2]["3"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][2]["3"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["-"][2]["3"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][2]["3"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][2]["3"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["-"][2]["3"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][2]["3"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][2]["3"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["-"][2]["3"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][2]["3"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][2]["3"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["-"][2]["3"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][2]["3"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][2]["3"][0]["Username"] = username

                elif ((RandomLevelNum2 == False) and (userDigits == 4)):
                    if (review3 == leaderBoardsReviewData["Users"][0]["-"][3]["4"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][3]["4"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][3]["4"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["-"][3]["4"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][3]["4"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][3]["4"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["-"][3]["4"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][3]["4"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][3]["4"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["-"][3]["4"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][3]["4"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][3]["4"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["-"][3]["4"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][3]["4"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][3]["4"][0]["Username"] = username

                elif (RandomLevelNum2 == True) and (userDigits == 1 or userDigits == 2 or userDigits == 3 or userDigits == 4):
                    if (review3 == leaderBoardsReviewData["Users"][0]["-"][4]["?"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][4]["?"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][4]["?"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["-"][4]["?"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][4]["?"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][4]["?"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["-"][4]["?"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][4]["?"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][4]["?"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["-"][4]["?"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][4]["?"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][4]["?"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["-"][4]["?"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["-"][4]["?"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["-"][4]["?"][0]["Username"] = username

            elif ((RandomLevelNum1 == False) and (userOperation == "×")):
                if ((RandomLevelNum2 == False) and (userDigits == 1)):
                    if (review3 == leaderBoardsReviewData["Users"][0]["x"][0]["1"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][0]["1"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][0]["1"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["x"][0]["1"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][0]["1"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][0]["1"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["x"][0]["1"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][0]["1"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][0]["1"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["x"][0]["1"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][0]["1"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][0]["1"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["x"][0]["1"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][0]["1"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][0]["1"][0]["Username"] = username

                elif ((RandomLevelNum2 == False) and (userDigits == 2)):
                    if (review3 == leaderBoardsReviewData["Users"][0]["x"][1]["2"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][1]["2"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][1]["2"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["x"][1]["2"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][1]["2"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][1]["2"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["x"][1]["2"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][1]["2"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][1]["2"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["x"][1]["2"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][1]["2"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][1]["2"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["x"][1]["2"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][1]["2"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][1]["2"][0]["Username"] = username

                elif ((RandomLevelNum2 == False) and (userDigits == 3)):
                    if (review3 == leaderBoardsReviewData["Users"][0]["x"][2]["3"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][2]["3"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][2]["3"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["x"][2]["3"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][2]["3"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][2]["3"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["x"][2]["3"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][2]["3"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][2]["3"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["x"][2]["3"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][2]["3"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][2]["3"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["x"][2]["3"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][2]["3"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][2]["3"][0]["Username"] = username

                elif ((RandomLevelNum2 == False) and (userDigits == 4)):
                    if (review3 == leaderBoardsReviewData["Users"][0]["x"][3]["4"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][3]["4"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][3]["4"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["x"][3]["4"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][3]["4"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][3]["4"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["x"][3]["4"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][3]["4"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][3]["4"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["x"][3]["4"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][3]["4"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][3]["4"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["x"][3]["4"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][3]["4"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][3]["4"][0]["Username"] = username

                elif (RandomLevelNum2 == True) and (userDigits == 1 or userDigits == 2 or userDigits == 3 or userDigits == 4):
                    if (review3 == leaderBoardsReviewData["Users"][0]["x"][4]["?"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][4]["?"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][4]["?"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["x"][4]["?"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][4]["?"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][4]["?"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["x"][4]["?"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][4]["?"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][4]["?"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["x"][4]["?"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][4]["?"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][4]["?"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["x"][4]["?"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["x"][4]["?"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["x"][4]["?"][0]["Username"] = username

            elif ((RandomLevelNum1 == False) and (userOperation == "÷")):
                if ((RandomLevelNum2 == False) and (userDigits == 1)):
                    if (review3 == leaderBoardsReviewData["Users"][0]["%"][0]["1"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][0]["1"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][0]["1"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["%"][0]["1"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][0]["1"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][0]["1"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["%"][0]["1"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][0]["1"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][0]["1"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["%"][0]["1"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][0]["1"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][0]["1"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["%"][0]["1"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][0]["1"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][0]["1"][0]["Username"] = username

                elif ((RandomLevelNum2 == False) and (userDigits == 2)):
                    if (review3 == leaderBoardsReviewData["Users"][0]["%"][1]["2"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][1]["2"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][1]["2"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["%"][1]["2"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][1]["2"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][1]["2"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["%"][1]["2"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][1]["2"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][1]["2"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["%"][1]["2"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][1]["2"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][1]["2"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["%"][1]["2"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][1]["2"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][1]["2"][0]["Username"] = username

                elif ((RandomLevelNum2 == False) and (userDigits == 3)):
                    if (review3 == leaderBoardsReviewData["Users"][0]["%"][2]["3"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][2]["3"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][2]["3"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["%"][2]["3"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][2]["3"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][2]["3"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["%"][2]["3"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][2]["3"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][2]["3"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["%"][2]["3"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][2]["3"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][2]["3"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["%"][2]["3"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][2]["3"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][2]["3"][0]["Username"] = username

                elif ((RandomLevelNum2 == False) and (userDigits == 4)):
                    if (review3 == leaderBoardsReviewData["Users"][0]["%"][3]["4"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][3]["4"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][3]["4"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["%"][3]["4"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][3]["4"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][3]["4"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["%"][3]["4"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][3]["4"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][3]["4"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["%"][3]["4"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][3]["4"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][3]["4"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["%"][3]["4"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][3]["4"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][3]["4"][0]["Username"] = username

                elif (RandomLevelNum2 == True) and (userDigits == 1 or userDigits == 2 or userDigits == 3 or userDigits == 4):
                    if (review3 == leaderBoardsReviewData["Users"][0]["%"][4]["?"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][4]["?"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][4]["?"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["%"][4]["?"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][4]["?"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][4]["?"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["%"][4]["?"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][4]["?"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][4]["?"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["%"][4]["?"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][4]["?"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][4]["?"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["%"][4]["?"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["%"][4]["?"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["%"][4]["?"][0]["Username"] = username
            
            elif ((RandomLevelNum1 == True) and (userDigits == 1 or userDigits == 2 or userDigits == 3 or userDigits == 4)):
                if ((RandomLevelNum2 == False) and (userDigits == 1)):
                    if (review3 == leaderBoardsReviewData["Users"][0]["?"][0]["1"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][0]["1"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][0]["1"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["?"][0]["1"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][0]["1"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][0]["1"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["?"][0]["1"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][0]["1"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][0]["1"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["?"][0]["1"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][0]["1"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][0]["1"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["?"][0]["1"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][0]["1"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][0]["1"][0]["Username"] = username

                elif ((RandomLevelNum2 == False) and (userDigits == 2)):
                    if (review3 == leaderBoardsReviewData["Users"][0]["?"][1]["2"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][1]["2"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][1]["2"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["?"][1]["2"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][1]["2"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][1]["2"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["?"][1]["2"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][1]["2"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][1]["2"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["?"][1]["2"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][1]["2"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][1]["2"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["?"][1]["2"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][1]["2"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][1]["2"][0]["Username"] = username

                elif ((RandomLevelNum2 == False) and (userDigits == 3)):
                    if (review3 == leaderBoardsReviewData["Users"][0]["?"][2]["3"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][2]["3"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][2]["3"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["?"][2]["3"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][2]["3"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][2]["3"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["?"][2]["3"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][2]["3"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][2]["3"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["?"][2]["3"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][2]["3"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][2]["3"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["?"][2]["3"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][2]["3"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][2]["3"][0]["Username"] = username

                elif ((RandomLevelNum2 == False) and (userDigits == 4)):
                    if (review3 == leaderBoardsReviewData["Users"][0]["?"][3]["4"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][3]["4"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][3]["4"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["?"][3]["4"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][3]["4"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][3]["4"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["?"][3]["4"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][3]["4"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][3]["4"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["?"][3]["4"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][3]["4"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][3]["4"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["?"][3]["4"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][3]["4"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][3]["4"][0]["Username"] = username

                elif (RandomLevelNum2 == True) and (userDigits == 1 or userDigits == 2 or userDigits == 3 or userDigits == 4):
                    if (review3 == leaderBoardsReviewData["Users"][0]["?"][4]["?"][4]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][4]["?"][4]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][4]["?"][4]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["?"][4]["?"][3]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][4]["?"][3]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][4]["?"][3]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["?"][4]["?"][2]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][4]["?"][2]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][4]["?"][2]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["?"][4]["?"][1]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][4]["?"][1]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][4]["?"][1]["Username"] = username

                    elif (review3 == leaderBoardsReviewData["Users"][0]["?"][4]["?"][0]["Score"]):
                        leaderBoardsReviewData["Users"][0]["?"][4]["?"][0]["Score"] = userScore
                        leaderBoardsReviewData["Users"][0]["?"][4]["?"][0]["Username"] = username
                        
            with open("leaderBoards.json", "w") as leaderBoardsModify:
                json.dump(leaderBoardsReviewData, leaderBoardsModify, indent = 4)

            pygame.time.wait(750)
            display5Num1 = 22

        elif (display5Num1 == 22):
            window.fill("#000000")
            window.blit(text134,text134Center)
            window.blit(text135,text135Center)
            pygame.display.update()
 
    #30 FPS
    windowClock.tick(30)
    pygame.display.update()
    