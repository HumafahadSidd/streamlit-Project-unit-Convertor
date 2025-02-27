import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize session state for tasks if it doesn't exist
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

def add_task(task, due_date):
    """Add a new task to the list"""
    if task:  # Check if task is not empty
        new_task = {
            'task': task,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'due_date': due_date.strftime("%Y-%m-%d") if due_date else None
        }
        st.session_state.tasks.append(new_task)
        return True
    return False

def delete_task(index):
    """Delete a task from the list"""
    del st.session_state.tasks[index]

def toggle_task(index):
    """Toggle task completion status"""
    st.session_state.tasks[index]['completed'] = not st.session_state.tasks[index]['completed']

# App title and description
st.title("📝 ToDo App")
st.write("Keep track of your tasks with this simple ToDo app!")

# Input section
with st.form("task_form", clear_on_submit=True):
    col1, col2 = st.columns([3, 1])
    
    with col1:
        task_input = st.text_input("Add a new task:", key="task_input")
    
    with col2:
        due_date = st.date_input("Due date:", key="due_date")
    
    submit_button = st.form_submit_button("Add Task")
    
    if submit_button:
        if add_task(task_input, due_date):
            st.success("Task added successfully!")
        else:
            st.error("Please enter a task!")

# Display tasks
if st.session_state.tasks:
    st.write("### Your Tasks")
    
    # Filter options
    filter_status = st.selectbox(
        "Filter tasks:",
        ["All", "Active", "Completed"]
    )
    
    # Filter tasks based on selection
    filtered_tasks = st.session_state.tasks
    if filter_status == "Active":
        filtered_tasks = [task for task in st.session_state.tasks if not task['completed']]
    elif filter_status == "Completed":
        filtered_tasks = [task for task in st.session_state.tasks if task['completed']]

    # Display tasks in a more organized way
    for idx, task in enumerate(filtered_tasks):
        col1, col2, col3, col4 = st.columns([0.1, 2, 0.5, 0.5])
        
        with col1:
            st.checkbox(
                "",
                value=task['completed'],
                key=f"checkbox_{idx}",
                on_change=toggle_task,
                args=(st.session_state.tasks.index(task),)
            )
        
        with col2:
            if task['completed']:
                st.markdown(f"~~{task['task']}~~")
            else:
                st.write(task['task'])
        
        with col3:
            if task['due_date']:
                st.write(f"Due: {task['due_date']}")
        
        with col4:
            if st.button("🗑️", key=f"delete_{idx}"):
                delete_task(st.session_state.tasks.index(task))
                st.rerun()

    # Task statistics
    st.write("---")
    total_tasks = len(st.session_state.tasks)
    completed_tasks = len([task for task in st.session_state.tasks if task['completed']])
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Tasks", total_tasks)
    with col2:
        st.metric("Completed", completed_tasks)
    with col3:
        st.metric("Remaining", total_tasks - completed_tasks)

else:
    st.info("No tasks yet! Add a task to get started.")

# Add some styling
st.markdown("""
    <style>
    .stButton button {
        width: 100%;
    }
    .stTextInput input {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True) 