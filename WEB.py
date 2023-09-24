import streamlit as st
import function

todos=function.get_todos()
def add_todo():
    todo=st.session_state["new_todo"]
    todos.append(todo+"\n")
    function.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my to-do app")
st.write("This app will increase your productivity")



for index,todo in enumerate(todos):
    check_box=st.checkbox(todo,key=todo)
    if check_box:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
st.text_input(label="",placeholder="ADD NEW TODO",on_change=add_todo,key="new_todo")
