import streamlit as st
import pandas as pd
print("helo")
st.set_page_config(layout="wide")
col1,col2=st.columns(2)
with col1:
    with st.container(height=400):
        st.image("images/photo.png",width=600)
with col2:
    st.title("Shaik Sohany")
    content="""
    Hi am sohany shaik learning python to become python developer
    by changing my domain from NON-IT to IT software development.
    """
    st.info(content)    
content2 = """
Below you can find some of the apps,i have built in python.
feel free to contact me!
"""
st.write(content2)
col3,col4=st.columns(2)

df=pd.read_csv("data.csv",sep=";")
with col3:
    
    for index,row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[source code]({row["url"]})")

with col4:
    for index,row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write("[source code](https://pythonhow.com)") 
        
