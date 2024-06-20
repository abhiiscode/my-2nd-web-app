import smtplib, ssl
from dotenv import load_dotenv
# from os import getenv
import os
import smtplib

load_dotenv()

password = os.getenv("PASSWORD_for_app2")
api_url = os.getenv("API_URL")
def send_email_fung(info_messgae):  #3rd

    load_dotenv()
    host = "smtp.gmail.com"
    port = 465

    username = "pythonwithabhi@gmail.com"


    #add passwoed when ur code is completed

    receiver = "abktpass@gmail.com"
    my_contaxt = ssl.create_default_context()

    # message = '''\
    # Subject: MSG sended form pycham IDE!
    # how are you?
    # bye!
    # '''

    with smtplib.SMTP_SSL(host, port, context=my_contaxt) as server:
        server.login(username, password)
        server.sendmail(username, receiver, info_messgae) #4th

# from dotenv import load_dotenv
# from os import getenv
# # import smtplib
# import ssl
#
# # Load environment variables from .env file
# load_dotenv()
#
# # Import environment variables directly
# API_URL = getenv("API_URL")
# PASSWORD_FOR_APP2 = getenv("PASSWORD_FOR_APP2")
#
# def send_email_fung(info_message):
#     host = "smtp.gmail.com"
#     port = 465
#     username = "pythonwithabhi@gmail.com"
#     receiver = "abktpass@gmail.com"
#
#     context = ssl.create_default_context()
#
#     # Construct your email message
#     email_message = f"Subject: Your Subject\n\n{info_message}\n\nAPI URL: {API_URL}"
#
#     with smtplib.SMTP_SSL(host, port, context=context) as server:
#         server.login(username, PASSWORD_FOR_APP2)
#         server.sendmail(username, receiver, email_message)
#
# # Example usage of send_email_fung function
# send_email_fung("Hello! This is a test email message.")



