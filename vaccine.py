#!/usr/bin/env python3

import re
import smtplib
import ssl
import requests

#port = 25
#smtp_server = "localhost"
port = 587
smtp_server = "smtp.gmail.com"
sender = "jscds07@gmail.com"
receivers = ["jscds07@gmail.com", "stangertz_6@hotmail.com"]
recv2 = "stangertz_6@hotmail.com"
password = "Uzs7CRZ7"
context = ssl.create_default_context()


message = """\
	Subject: Vaccin-check
	To: jscds07@gmail.com,stangertz_6@hotmail.com
	From: jscds07@gmail.com

	Boka vaccin nu!
"""

def mail_me():
	try:
		#send your message with credentials specified above
		server = smtplib.SMTP(smtp_server, port)
		server.starttls(context=context)
		server.login(sender, password)
		server.sendmail(sender, receivers, message)

		# tell the script to report if your message was sent or which errors need to be fixed
		print('Sent')
	except smtplib.SMTPServerDisconnected:
		print('Failed to connect to the server. Wrong user/password?')
	except smtplib.SMTPException as e:
		print('SMTP error occurred: ' + str(e))

def mail_billie():
	try:
		#send your message with credentials specified above
		server = smtplib.SMTP(smtp_server, port)
		server.starttls(context=context)
		server.login(sender, password)
		server.sendmail(sender, recv2, message)

		# tell the script to report if your message was sent or which errors need to be fixed
		print('Sent')
	except smtplib.SMTPServerDisconnected:
		print('Failed to connect to the server. Wrong user/password?')
	except smtplib.SMTPException as e:
		print('SMTP error occurred: ' + str(e))

r = requests.get("https://www.skane.se/Halsa-och-vard/hitta-vard/covid-19-coronavirus/fragor-och-svar-om-covid-19-vaccination/lediga-tider-for-vaccination-mot-covid-19/")

resp = r.text
pattern = "<a href=\"https\:\/\/.*Boka\stid\shos\sSvea.*</a>"
pattern_two = "SE162321000255-O18986"

svea = re.findall(pattern, resp)
#print(result)
berga = re.findall(pattern_two, resp)
if "Helsingborg" in svea:
	mail_me()
	mail_billie()
elif pattern_two in berga:
	mail_me()
	mail_billie()
else:
	exit()