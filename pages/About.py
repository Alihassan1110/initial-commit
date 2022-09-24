import streamlit as st
import pandas as pd

st.title("About")

st.info("This is a test")

st.success("This is a test")

name = st.text_input("What is your name?")

age = st.number_input("What is your age?")

height = st.slider("What is your height?", 0, 200)

dic = {"Name": name, "Age": age, "Height": height}
df = pd.DataFrame(dic, index=[0])

st.write(df)

def get_data():
    return pd.DataFrame({'name' : name, 'age' : age, 'height' : height })
