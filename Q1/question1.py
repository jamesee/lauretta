
# import the necessary packages
import numpy as np
import cv2
import imutils
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--path", required=True, help="path to the input image. e.g python question1.py -i fumo")
args = vars(ap.parse_args())

# define the list of boundaries
boundaries = [
	# blue range
	([200, 0, 0], [255, 20, 20]),
	# red range
	([0, 0, 200], [20, 20, 255]),
]

def maxRowCol(list):
	row=[]
	col=[]
	for x in list:
		row.append(x[0])
		col.append(x[1])

	return max(row), max(col)

# Reference: 
# https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/
# https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/		
def myCV(file):
	myCoordinate =[]
	image = cv2.imread(os.path.join(args["path"], file))

	# loop over the boundaries
	for (lower, upper) in boundaries:
		# create NumPy arrays from the boundaries
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")

		# find the colors within the specified boundaries and apply
		# the mask
		mask = cv2.inRange(image, lower, upper)
		output = cv2.bitwise_and(image, image, mask = mask)

		# find contour
		gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
		blurred = cv2.GaussianBlur(gray, (5, 5), 0)
		thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_TRUNC)[1]
		# thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

		cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)
		myCoordinate.append(len(cnts))

	myCoordinate.append(os.path.join(args["path"], file))
	return myCoordinate

# Reference : 
# https://note.nkmk.me/en/python-opencv-hconcat-vconcat-np-tile/
def concat_tile(im_list_2d):
	return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])

def myStitchPicture(list):
	maxrow, maxcol = maxRowCol(list)
	
	# stitch the picture
	pic = []
	for y in range(maxrow):
		row_pic =[]
		for x in range(maxcol):
			image = cv2.imread(list[x + maxcol * y][2])
			row_pic.append(image)
		pic.append(row_pic)
	
	return concat_tile(pic)

def main():
	files =[]
	myArrangement =[]
	print("[INFO] Path to images : ", args["path"])
	# read files from directory
	files = os.listdir(args["path"])

	for file in files:
		# perform CV operation to detect number of red dots and blue dots
		myArrangement.append(myCV(file))

	# sort the list
	mySortedArrangement = sorted(myArrangement)	

	# show the images
	print('[INFO] showing images')
	cv2.imshow("Output Image", myStitchPicture(mySortedArrangement))
	cv2.waitKey(0)
	
if __name__ == "__main__":
    main()

