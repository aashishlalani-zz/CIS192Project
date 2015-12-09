import smtplib


username = "onetimepadcis192@gmail.com"
toaddrs  = "anvita.achar@gmail.com"


def send_email():
    msg = "dagkadjhkljh"
    # Credentials (if needed)
    password = "0n3t1m3p4d"
    
    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(username, toaddrs, msg)
    server.quit()