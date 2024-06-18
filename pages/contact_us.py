import streamlit as sl
from send_email import send_email_fung

sl.header("For More Information CONTACT Us!")

with sl.form(key="email_form"):
    user_email = sl.text_input("Enter your email")
    user_message = sl.text_area("Enter your message")
#1    info_message = info_message + "\n" + user_email
    #for f"" \ is very imp
    info_message = f"""\       
Subject: New Email from {user_email}
From: {user_email} 
{user_message}
"""
    '''it will send sender email address'''
    button = sl.form_submit_button("Submit")
if button:
    send_email_fung(info_message)  #fist
    sl.info("Your Email Was Send Sucessfully!")