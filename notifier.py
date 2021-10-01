#!/usr/bin/env python3

import re
import smtplib
import ssl
import requests
import sys

# For testing with local server:
#port = 25
#smtp_server = "localhost"

port = 587
smtp_server = "smtp.gmail.com"
email = sys.argv[1]
password = sys.argv[2]
context = ssl.create_default_context()


message = f"""\
	Subject: BotAlert!
	To: {email}
	From: {email}

	Message from bot: Site is available!
"""

def mail_me():
	try:
		#send your message with credentials specified above
		server = smtplib.SMTP(smtp_server, port)
		server.starttls(context=context)
		server.login(email, password)
		server.sendmail(email, email, message)

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

site1 = re.findall(pattern, resp)
site2 = re.findall(pattern_two, resp)
if "Helsingborg" in site1 or pattern_two in site2:
	mail_me()
else:
	exit()
