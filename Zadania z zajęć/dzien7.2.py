import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

fp = open("plik.txt", 'r')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()



# me == the sender's email address
# you == the recipient's email address

me ="isapy7@o2.pl"
you ="lukasz.falkowicz@develocraft.com"

msg['Subject'] = 'The contents of %s' % "plik.txt"
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('poczta.o2.pl')
s.login(me ,"isapython7")

s.sendmail(me, [you], msg.as_string())
s.quit()