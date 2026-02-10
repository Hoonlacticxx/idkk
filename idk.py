import streamlit as st
import random

st.title("fnklkfnsakl")

def number_input(
    label: str,
    min_value: int | None = None,
    max_value: int | None = None,
    value: FloatOrNone@number_input | Literal['min'] = "min",
    step: float | None = None,
    format: str | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
windows = ["1", "2", "3"]
p1, p2, p3 = st.tabs(windows)

num = random.randint(1, 100)

with p1:
    while True:

        att = st.number_input("Elige un numero: ")
        att = int(att)
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