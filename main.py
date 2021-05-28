import smtplib
# please note go to https://myaccount.google.com/lesssecureapps and
# turn it off to allow gmail to send
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
sender_email_id = 'jaydenmay040@gmail.com'
receiver_email_id = 'brentleejohnson73@gmail.com, jasoncee017@gmail.com, naeemahdavis@gmail.com'
password = input("Enter senders email password")
# start TLS for security
s.starttls()
# Authentication
s.login(sender_email_id, password)
# message to be sent
message = "Hi guys\n"
message = message + "Do yuo fnid tihs smilpe to raed?\n"
message = message + "Bceuase of the phaonmneal pweor of the hmuan mnid, msot plepoe do."
# sending the mail
s.sendmail(sender_email_id, receiver_email_id, message)
# terminating the session
s.quit()
