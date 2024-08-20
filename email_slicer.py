def mail_slicer():
    email_input = input("\nEnter the email address: \n")

#Splits the name from the domain using the @ sysmbol
    (username, domain) = email_input.split('@')
    
#splits the domain from the extension using the .
    (domain, extension) = domain.split('.')

    print(f"\nUsername: {username}")
    print(f"\nDomain: {domain}")
    print(f"\nExtension: {extension}")


while True:
    mail_slicer()