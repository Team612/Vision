import pyautogui

screensize = pyautogui.size()
desired_pixels = (1510, 770, 650, 670) #top, left, width, height
#set these based off of your screen size. on my 2160x1440 computer, these pixels are for the bottom right corner.
time = 15 #amount of seconds that the picture will show itself before retaking another picture