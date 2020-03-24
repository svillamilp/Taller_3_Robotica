import cv2
import numpy as np
import argparse



#Esto sirve para la entrada por parametro
parser = argparse.ArgumentParser()
parser.add_argument("a")
args = parser.parse_args()
a = 'ssl1'
if args.a == 'ssl1.mp4':
	a = 'ssl1.mp4'
elif args.a == 'ssl2.mp4':
	a = 'ssl2.mp4'
elif args.a == 'ssl3.mp4':
	a = 'ssl3.mp4'

#Aca se abre el video
cap = cv2.VideoCapture(a)
fourcc = cv2.VideoWriter_fourcc(*'X264')
out = cv2.VideoWriter('NEW'+a+'.mp4v',fourcc, 30, (900,600))
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

    	cv2.imshow('Frame',frame)


    #Esto es para salirse del video oprimiendo q
    	if cv2.waitKey(30) & 0xFF == ord('q'):
        	break
    else:
    	break
cap.release()
cv2.destroyAllWindows()

# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
# Define the fps to be equal to 10. Also frame size is passed.


	
