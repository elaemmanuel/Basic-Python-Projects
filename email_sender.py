from email.message import EmailMessage
import ssl
import smtplib

email_sender = "Sender's Email address"
email_password = "Sender's Password"

email_receiver = "Recepients Email address"

subject = "Email Subject"
body = "Email Body"

#create a message object
try:
    mail = EmailMessage()
    mail['from'] = email_sender
    mail['To'] = email_receiver
    mail['subject'] = subject
    mail.set_content(body)

    context = ssl.create_default_context()

    #Connect to SMTP sever and send mail
    with smtplib.SMTP_SSL('smtp.gmal.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, mail.as_string())
        print("\nEmail Sent Successfully\n")
except Exception as error:
    print("Error Sending Mail:", str(error))


