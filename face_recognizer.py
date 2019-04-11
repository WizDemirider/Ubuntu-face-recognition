# -*- coding: utf-8 -*-

import cv2
import os
import numpy
import pickle

def train():
	path = '/home/ankit/Documents/database'
	train_images = []
	labels = []
	classes_names = []
	for (subdirs,dirs,files) in os.walk(path):
		for i,subdir in enumerate(dirs):
		    classes_names.append(subdir)
		    for file_name in os.listdir(path+'/'+subdir):
		        if file_name!='.DS_Store':
		        	try:
		        		img = cv2.imread(path+'/'+subdir+'/'+file_name,0)
		        		img = cv2.resize(img,(100,100))
		        		train_images.append(img)
		        		labels.append(i)
		        	except Exception as e:
		        		pass
		            
	(train_images,labels) = [numpy.array(lis) for lis in [train_images,labels]]

	p = numpy.random.permutation(len(train_images))
	train_images = train_images[p]
	labels = labels[p]
	model = cv2.face.FisherFaceRecognizer_create()
	model.train(train_images, labels)

	model.save('/home/ankit/Documents/mymodel.xml')

def detect(image_path):

	face_cascade = cv2.CascadeClassifier("/home/ankit/Documents/face_detection_models/haarcascade_frontalface_default.xml")

	model = cv2.face.FisherFaceRecognizer_create()
	model.read('/home/ankit/Documents/mymodel.xml')
	image = cv2.imread(image_path)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray,1.1,5)
	if list(faces):
		face = max(faces, key = lambda x:x[2]*x[3])
		roi = gray[face[1]:face[1]+face[3],face[0]:face[0]+face[2]]
		roi = cv2.resize(roi,(100,100))
		person,probability = model.predict(roi)
		return person,probability
	return 1,100
	
#if __name__ == "__main__":
	#print(detect('/home/ankit/Downloads/'+input("name:")+'.jpg'))
