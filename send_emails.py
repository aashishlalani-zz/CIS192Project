import smtplib

fromaddr = 'lol@gmail.com'
toaddrs  = 'lol@gmail.com'
fromline = 'From: '+ fromaddr
toline = 'To: '+ toaddrs 
msg = "\r\n".join([
  "From: user_me@gmail.com",
  "To: user_you@gmail.com",
  "Subject: Just a message",
  "",
  "Why, oh why"
  ])


# Credentials (if needed)
username = 'anvita.achar'
password = 'ADD YOUR PASSWORD'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()