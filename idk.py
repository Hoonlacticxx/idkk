import streamlit as st
import random

st.title("fnklkfnsakl")

windows = ["1", "2", "3"]
p1, p2, p3 = st.tabs(windows)

num = random.randint(1, 100)

with p1:
    while True:

        att = st.number_input("Elige un numero: ")
        if att < num:
            st.write("Tu num es menor")
        elif att > num:
            st.write("Tu num es mayor")
        else:
            st.write("Has acertado")
            break

with p2:
    st.write("Texto de prueba lol")

with p3:
    st.write("Texto de prueba faj")