import smtplib


username = "onetimepadcis192@gmail.com"


def send_email(msg, toaddrs):
    # Credentials (if needed)
    password = "0n3t1m3p4d"
    
    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    SUBJECT = "A friend has sent you a new encrypted message"
    message = 'Subject: %s\n\n%s' % (SUBJECT, msg)
    server.sendmail(username, toaddrs, message)
   
    server.quit()
    