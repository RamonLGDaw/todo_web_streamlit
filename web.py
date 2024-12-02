import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state['new_todo']
    todos.append(new_todo + '\n')
    functions.write_todos(todos)
    

st.title('Todo app')
st.subheader('This is my todo app')
st.write('This app is to increase your productivity!')

for index,item in enumerate(todos):
    check_box = st.checkbox(item, key=item)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item]
        st.rerun()

st.text_input(label='Enter a todo:', placeholder='Add a new todo', on_change=add_todo, key='new_todo')


