import RPi.GPIO as GPIO
import time
import random
import numpy as np
import os
import cv2
from keras.preprocessing.image import ImageDataGenerator, array_to_img
from keras.models import load_model
import paho.mqtt.publish as publish

def preprocess_input_icpt(x):
    from keras.applications.inception_v3 import preprocess_input
    X = np.expand_dims(x, axis=0)
    X = preprocess_input(X)
    return X[0]

datagen = ImageDataGenerator(preprocessing_function=preprocess_input_icpt,
                                   fill_mode='nearest')

start = time.time()
model = load_model('apple_icpt.h5')
end = time.time()
quantboas = 0
quantpodres = 0
print(end - start)
try:
	os.mkdir('test')
except:
	pass
try:
	os.mkdir('test/check')
except:
	pass	
cam = cv2.VideoCapture(0)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)          
GPIO.setup(7, GPIO.IN)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.LOW)
podre = 1
while(1):
	ret, frame = cam.read()
	if GPIO.input(7) == 1:
		
		cv2.imshow('img',frame)
		cv2.imwrite('test/check/test.jpg', frame)
		check = datagen.flow_from_directory(directory='test/',
                                          target_size=[140,140],
                                          batch_size=1,
                                          shuffle = False,
                                          class_mode='categorical')

		X_val_sample, res = next(check)
		y_pred = model.predict(X_val_sample)
		print(y_pred)

		#reconhecimento
		podre = np.argmax(y_pred)
		if podre:
			quantpodres += 1	
			GPIO.output(11, GPIO.HIGH)
			time.sleep(1)
			GPIO.output(11, GPIO.LOW)
			publish.single('/dse/maca/podre', quantpodres, hostname='iot.eclipse.org')
				
		else:
			quantboas += 1
			publish.single('/dse/maca/boas', quantboas, hostname='iot.eclipse.org')

		
		while GPIO.input(7)!=0:
			pass	
				 
	time.sleep(0.1)
	
