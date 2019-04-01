import cv2
import numpy as np
 
cap = cv2.VideoCapture('sample-3.mp4')
template = cv2.imread("./template_4.png", cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1] 
swing_count = 0
swing_flag  = True
 
while True:
    (grabbed, frame) = cap.read()
    frame = cv2.resize(frame,(848,480))
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.7)
    #print(res)
    print("Length of locations : ",len(loc[0]),len(loc[1]))
    if(len(loc[0]) == 0 and len(loc[1]) == 0):
        swing_flag = True
    print("Locations when res > 0.7:", loc)

    for pt in zip(*loc[::-1]):
        if(swing_flag):
            swing_count += 1
            swing_flag = False
        cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 3)
        cv2.putText(frame, "Status: Filling", (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), lineType=cv2.LINE_AA)

    #frame = cv2.resize(frame,(640,480))
    #cv2.putText(frame, "Status: ---", (20,40), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 0, 0), lineType=cv2.LINE_AA)
    cv2.putText(frame, "Swing Count = "+str(swing_count), (600,20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), lineType=cv2.LINE_AA)
    cv2.imshow("Frame", frame)
 
    if not grabbed or cv2.waitKey(1) == ord("q"):
            print("User : Quit")
            break
 
cap.release()
cv2.destroyAllWindows()