# 
import numpy as np
import cv2
import datetime
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#cap.set(3)
#cap.set(4)
ttext = "Date & Time:" + str(datetime.datetime.now())
dtext = "Width:" + str(cap.get(3)) + "Height:" + str(cap.get(4))
font = cv2.FONT_HERSHEY_SIMPLEX
print(cap.get(3))
print(cap.get(4))
out = cv2.VideoWriter('output.avi',fourcc,20,(500,400))
while True:
	ret,frame = cap.read()
	#print(cap.get(3))
	#print(cap.get(4)) 
	#gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.putText(frame,ttext,(0,50),font,1,(0,0,200),2)
	cv2.putText(frame,dtext,(0,390),font,1,(0,200,0),2)
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xff == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
