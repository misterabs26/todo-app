import streamlit as st
from modules import functions as fn

todos = fn.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input("", placeholder="Add your new to-do")