from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import os
import sys
sys.path.insert(0, '/home/ankit/Documents')
import face_recognizer

msg = MIMEMultipart()

image_path = '/home/ankit/Documents/WizAuth/failimg.jpg'
 
password = "ap@12345"
fromadd = "ankanarn@gmail.com"
toadd = "ankanarn@gmail.com"
msg['Subject'] = "Security Alert, Wrong Password detected!"

server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

server.login(fromadd, password)

try:

	with open(image_path, 'rb') as f:
		file_data = f.read()

	person, probability = face_recognizer.detect(image_path)

	if not person == 0:
		msg.attach(MIMEImage(file_data, "jpeg"))
		
		msg['Body']="Identified as not Ankit with "+str(probability)+"% probability"

		server.sendmail(fromadd, toadd, msg.as_string())
	 
		print("successfully sent email to: {}".format(toadd))

		os.remove(image_path)
	else:
		print("Identified as Ankit with "+str(probability)+"% probability")

except Exception as e:
	pass
	print(str(e),"Error occurred")
 
server.quit()

