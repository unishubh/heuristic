#imports
import cv2
import numpy as np
import math

#opencv functions from coordinate to node_number mapping


#function for generating the white image with blue bot on it 
def create_blank(width, height, rgb_color=(0, 0, 0)):
    """Create new image(numpy array) filled with certain color in RGB"""
    # Create black blank image
    image = np.zeros((height, width, 3), np.uint8)

    # Since OpenCV uses BGR, convert the color first
    color = tuple(reversed(rgb_color))
    # Fill image with color
    image[:] = color

    return image

#x coordinate for column ni and y for row number
def get_center(block_no):
	
	if(block_no%10):
		row_no = block_no%10
	else:
		row_no = 10

	if(block_no%10):
		column_no = block_no/10 + 1
	else:
		column_no = block_no/10

	cx = (50*column_no) - 25
	cy = (50*row_no) - 25

	return cx, cy

def get_block_no(cx, cy):

	column_no = (cx)/50 + 1
	row_no = (cy)/50 + 1
	print "Vishakha"
	print row_no, column_no
	block_no = 10*(column_no) + row_no
	return block_no

def get_block_no_rand(cx, cy):
	
	column_no = int(math.floor(cx/50))+1
	
	row_no = int(math.floor(cy/50))+1
	
	block_no = 10*(column_no-1) + row_no
	print "vishakha", block_no
	return block_no
