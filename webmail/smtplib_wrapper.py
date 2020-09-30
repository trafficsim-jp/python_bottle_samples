# -*- coding: utf-8 -*-
import argparse

import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

FROM_ADDRESS="current-checker <kaz@trafficsim.co.jp>"
SUBJECT="current-checker notice"
MAIL_MESSAGE="current notice"

SMTP_SERVER='smtp.gmail.com'
SMTP_PORT=587

def create_message(from_addr, to_addrs, subject, body):
	msg = MIMEText(body)
	msg['Subject'] = subject
	msg['From'] = from_addr
	msg['To'] = to_addrs
	msg['Date'] = formatdate()
	return msg

def sendmail(username, password, from_addr, to_addrs, msg):
	smtpobj = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	try:
		smtpobj.ehlo()
		smtpobj.starttls()
		smtpobj.ehlo()
		smtpobj.login(username, password)
		smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
	except smtplib.SMTPException as e:
		# 送信に失敗した理由が例外で飛んでくる
		print(e)
	finally:
		# SMTP QUITの結果が却って来るが無視して良い
		result = smtpobj.quit()
		print(result)

if __name__ == '__main__':

	argparser = argparse.ArgumentParser()
	argparser.add_argument("-u", "--user", type=str, required=True, help="user name")
	argparser.add_argument("-p", "--password", type=str, required=True, help="password")
	argparser.add_argument("-d", "--destinations", type=str, required=True, help="destination mail address")

	args = argparser.parse_args()
	print "sendmail program"

	to_addrs = args.destinations

	msg = create_message(FROM_ADDRESS, args.destinations, SUBJECT, MAIL_MESSAGE)
	# to_addrsに渡すときはsplitで分割して文字列の配列にする.
	sendmail(args.user, args.password, FROM_ADDRESS, args.destinations.split(','), msg)

