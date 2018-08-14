# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
fp = open("171.jpg", 'rb')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()

me ="isapy7@o2.pl"
you ="lukasz.falkowicz@develocraft.com"
msg['Subject'] = 'The contents of %s' % "171.jpg"
msg['From'] = me
msg['To'] = you


# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('poczta.o2.pl')

s.login(me ,"isapython7")
s.sendmail(me , [you], msg.as_string())
s.quit()