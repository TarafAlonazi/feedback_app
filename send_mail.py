import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'sandbox.smtp.mailtrap.io'
    message = "<h3>New Feedback Submission</h3><ul><li>Customer:"+customer+"</li><li>Dealer: "+dealer+"</li><li>Rating: "+rating+"</li><li>Comments: "+comments+"</li></ul>"
    # sender_email = 'email1@example.com'
    # receiver_email = 'email2@example.com'
    sender = "Private Person <from@example.com>"
    receiver = "A Test User <to@example.com>"
    server = smtplib.SMTP(smtp_server, port)
    server.login("22fed8542237c3", "63331a0ab28cba")
    server.sendmail(sender, receiver, message)
    server.quit()

# def send_mail(customer, dealer, rating, comments):
#     port = 2525
#     smtp_server = 'sandbox.smtp.mailtrap.io'
#     login = '22fed8542237c3'
#     password = '63331a0ab28cba'
#     # message = comments
#     message = "<h3>New Feedback Submission</h3><ul><li>Customer:"+customer+"</li><li>Dealer: "+dealer+"</li><li>Rating: "+rating+"</li><li>Comments: "+comments+"</li></ul>"

#     sender_email = 'email1@example.com'
#     receiver_email = 'email2@example.com'
#     msg = MIMEText(message, 'html')
#     msg['Subject'] = 'Lexus Feedback'
#     msg['From'] = sender_email
#     msg['To'] = receiver_email

#     # Send email
#     with smtplib.SMTP(smtp_server, port) as server:
#         server.login(login, password)
#         server.sendmail(sender_email, receiver_email, msg.as_string())

######################################################

# def send_mail(customer, dealer, rating, comments):
#     sender = "Private Person <from@example.com>"
#     receiver = "A Test User <to@example.com>"

#     message = """\
#     Subject: Hi Mailtrap
#     To: """+receiver+"""
#     From: """+sender+"""
#     This is a test e-mail message."""

#     with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
#         server.login("22fed8542237c3", "63331a0ab28cba")
#         server.sendmail(sender, receiver, message)
#         server.quit()