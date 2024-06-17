import streamlit as sl
import pandas

sl.set_page_config(layout="wide")
#'''sl = module, columns = method, col1,2 = object instences'''

col1, col2 = sl.columns(2)
#'''image = method that produce image'''
with col1:
    sl.image("images/photos.png")

with col2:
    sl.title("Abhishek Thorat")
    content = '''
    Hi I'm Abhishek! I'm python programmer, teacher and business consultant. I work as a senior business consultant in 2021. I work with various businessmen. 
    '''
    sl.info(content)  #sl.write(content)
contact2 = '''
Below you can find some of the apps of I have built in python.
'''
sl.info(contact2)

empty_head, col_header, empty_head2 = sl.columns([1.2, 0.5, 1.2])
with col_header:
    col_header = sl.header("APP'S")
    # good_header = sl.info(col_header)

col3, empty_col, col4 = sl.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        sl.header(row["title"])
        sl.subheader(row["description"])
        sl.image("images/" + row["image"])
        sl.write(f"[source code]({row['url']})")

    with col4:
        for index, row in df[10:].iterrows():
            sl.subheader(row["title"])
            sl.subheader(row["description"])
            sl.image("images/" + row["image"])
            sl.write(f"[source code]({row['url']})")