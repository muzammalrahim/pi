import sys
import smtplib
from email.mime.text import MIMEText

sender = 'henk@waaromzomoeilijk.nl'
receivers = 'info@waaromzomoeilijk.nl'
receivers = 'timmeh@libero.it'
receivers = 'h.timmermans@kurkshop.nl'
smtp_server = 'mail.waaromzomoeilijk.nl'
mailuser = 'henk@waaromzomoeilijk.nl'
password = "Dssp4F7s&x9Gqfgd"

message = "From: From WaaromZoMoeilijk <noreply@waaromzomoeilijk.nl>\n"
message += "To: To HenkT <" + receivers + ">\n"
message += "Subject: Dit is de subject\n\n"

server = smtplib.SMTP_SSL(smtp_server, 465)

server.ehlo()
server.login(mailuser, password)
server.sendmail(sender, receivers, message)
server.quit()
