import keyboard
import os
import pyautogui as pg

screenWidth, screenHeight = pg.size()
print(screenWidth,screenHeight)

mouse = pg.position()
print(mouse)


# startButton = pg.locateOnScreen('.\Image\Test2.png', confidence = 0.6)
# if startButton:
#     #if not empty
#     x1,y1 = pg.center(pg.locateOnScreen(".\Image\Test2.png", confidence=0.6))
#     print(x1,y1)
#     print(startButton)
#     pg.moveTo(x1,y1,1,pg.easeInOutQuad)
#     pg.click(x1,y1)
# else:
#     #if empty
#     print("empty")
# #os.system("taskkill /im firefox.exe /f")