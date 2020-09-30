import argparse

import smtplib
from email.utils import formatdate

FROM_ADDRESS="current-checker <kaz@trafficsim.co.jp>"
SUBJECT="current-checker notice"
MAIL_MESSAGE="current notice"



if __name__ == '__main__':

	argparser = argparse.ArgumentParser()
	argparser.add_argument("-u", "--user", type=str, required=True, help="user name")
	argparser.add_argument("-p", "--password", type=str, required=True, help="password")
	argparser.add_argument("-d", "--destination", type=str, required=True, help="destination mail address")

	args = argparser.parse_args()
	print "sendmail program"
	print args.user
