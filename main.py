import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email_id = 'jaydenmay040@gmail.com'
receiver_email_id = 'brentleejohnson73@gmail.com, jasoncee017@gmail.com, naeemahdavis@gmail.com'
password = input("Enter your password")
subject = "Greetings"
msg = MIMEMultipart()
msg['From'] = sender_email_id
msg['To'] = receiver_email_id
msg['Subject'] = subject
body = "Hi guys:) Do yuo fnid tihs smilpe to raed?\n\n"
body = body + "Bceuase of the phaonmneal pweor of the hmuan mnid, msot plepoe do."
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login(sender_email_id, password)
# message to be sent

# sending the mail
s.sendmail(sender_email_id, receiver_email_id, text)
# terminating the session
s.quit()
