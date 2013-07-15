import cv2
import numpy as np

def blackbodysegment(img1, lowerlim, upperlim):
	element = cv2.getStructuringElement(cv2.MORPH_CROSS,(4,4))
	img_np = np.asarray(img1)
	blue, green, red = img_np.T
	res = (green>100)#|(red>50)|(blue>50)
	res = res.astype(np.uint8)*255
	res = np.transpose(res)
	offset = 50
	img_erode = cv2.erode(res,element)
	ret,thresh = cv2.threshold(img_erode,127,255,0)
	contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	#img_crop = img1
	
	for i in range(len(contours)):
			rect = cv2.minAreaRect(contours[i])
			(x, y), (w, h), theta =rect
			if (w*h > lowerlim and w*h< upperlim):		
				rect = (x+5, y+10), (w+offset, h+offset), theta
				box  = cv2.cv.BoxPoints(rect)
				box = np.int0(box)
				img_crop = img1[box[2][1]:box[0][1], box[1][0]:box[3][0]]
				break
				#cv2.drawContours(img1, [box], 0, (0,0,255), 2)
	
	return img_crop
	
	#print x+5, y+10, w+offset, h+offset, theta
	#print box
	#print img_crop.shape
	#img1 = cv2.resize(img1,(670,480))
	#cv2.imshow('filter_area', img1)
	#cv2.imshow('cropped', img_crop)
	#cv2.waitKey(50000)

if __name__=='__main__':
	pass
	#cap = cv2.VideoCapture('output.avi')
	#flag,img1 = cap.read()
	##img1 = cv2.imread('input.png')
	#img_crop = blackbodysegment(img1, 0, 2300) 
	#cv2.imshow('cropped', img_crop)
	#cv2.waitKey(50000)