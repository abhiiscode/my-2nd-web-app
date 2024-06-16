import streamlit as st
st.set_page_config(layout="wide")
#'''st = module, columns = method, col1,2 = object instences'''

col1, col2 = st.columns(2)
#'''image = method that produce image'''
with col1:
    st.image("images/photos.png")

with col2:
    st.title("Abhishek Thorat")
    content = '''
    Hi I'm Abhishek! I'm python programmer, teacher and business consultant. I work as a senior business consultant in 2021. I work with various businessmen. 
    '''
    st.info(content)  #st.write(content)
