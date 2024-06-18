import smtplib, ssl

def send_email_fung(info_messgae):  #second
    host = "smtp.gmail.com"
    port = 465

    username = "pythonwithabhi@gmail.com"
    password = "aoyn uzec jjjyidld"  #add passwoed when ur code is completed

    receiver = "abktpass@gmail.com"
    my_contaxt = ssl.create_default_context()

    # message = '''\
    # Subject: MSG sended form pycham IDE!
    # how are you?
    # bye!
    # '''

    with smtplib.SMTP_SSL(host, port, context=my_contaxt) as server:
        server.login(username, password)
        server.sendmail(username, receiver, info_messgae) #3rd



