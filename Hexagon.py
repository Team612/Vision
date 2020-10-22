import numpy as np, cv2, pyautogui, unique_vars

print(unique_vars.screensize)
print("Press escape key to close window")

while True: #Creates a screenshot to save as array lines 7-8, 9 BGR to RGB, 10-13 show images until escape key is pressed
    img = pyautogui.screenshot(region = unique_vars.desired_pixels) 
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(frame, 10, 300)
    cv2.imshow("name", edged)
    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    im2 = cv2.drawContours(edged, contours, -1, 20)
    
    if cv2.waitKey(unique_vars.time) & 255 == 27:
        break
cv2.destroyAllWindows() #removes windows when loop breaks, i.e. when esc pressed