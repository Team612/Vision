import numpy as np, cv2, pyautogui

screensize = pyautogui.size() #equals (2160, 1440)
print("Press escape key to close window")

while True: #Creates a screenshot to save as array lines 7-8, 9 BGR to RGB, 10-12 show image until escape key is pressed
    img = pyautogui.screenshot(region = (1080, 720, 1080, 720)) #top, left, width, height
    frame = np.array(img)
    frame = frame[...,::-1]
    cv2.imshow("screenshot", frame)
    if cv2.waitKey(15) & 255 == 27:
        break
cv2.destroyAllWindows()