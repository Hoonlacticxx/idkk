import streamlit as st

st.title("fnklkfnsakl")

windows = ["1", "2", "3"]
p1, p2, p3 = st.tabs(windows)

with p1:
    st.write("Texto de prueba")

with p2:
    st.write("Texto de prueba lol")

with p3:
    st.write("Texto de prueba faj")