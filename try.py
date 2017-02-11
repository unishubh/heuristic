import cv2
import time
import numpy as np
from opencv_functions import create_blank


def main():
	width, height = 1000, 500

	white = (255, 255, 255)
	

	while 1:
		image = create_blank(width, height, rgb_color=white)
		x=np.random.randint(1,1000)
		y=np.random.randint(1,500)	    
		cv2.circle(image,(x,y),13,(255,0,0),-1)
		cv2.imwrite('white.jpg', image)
		image = cv2.imread("white.jpg")
		cv2.imshow('image', image)
		cv2.waitKey(1)
		


# cv2.destroyAllWindows()

if __name__ == "__main__":  
    main()