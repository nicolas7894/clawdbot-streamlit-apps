import streamlit as st

st.title("✅ To-Do List")
st.markdown("Manage your tasks efficiently!")

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add new task
st.subheader("Add a New Task")
col1, col2 = st.columns([3, 1])
with col1:
    new_task = st.text_input("Task name", placeholder="Enter a new task...", label_visibility="collapsed")
with col2:
    add_clicked = st.button("➕ Add Task", use_container_width=True)

if add_clicked and new_task.strip():
    st.session_state.tasks.append({"text": new_task.strip(), "completed": False})
    st.rerun()
elif add_clicked:
    st.warning("Please enter a task name.")

st.divider()

# Display tasks
st.subheader("Your Tasks")

if not st.session_state.tasks:
    st.info("No tasks yet. Add one above! ☝️")
else:
    # Show task count
    completed_count = sum(1 for t in st.session_state.tasks if t["completed"])
    total_count = len(st.session_state.tasks)
    st.caption(f"{completed_count}/{total_count} tasks completed")
    
    # Progress bar
    if total_count > 0:
        progress = completed_count / total_count
        st.progress(progress)
    
    st.markdown("---")
    
    # Task list
    for idx, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([0.1, 3, 0.5])
        
        with col1:
            # Checkbox for complete/uncomplete
            completed = st.checkbox(
                "",
                value=task["completed"],
                key=f"check_{idx}"
            )
            if completed != task["completed"]:
                st.session_state.tasks[idx]["completed"] = completed
                st.rerun()
        
        with col2:
            # Task text with strikethrough if completed
            if task["completed"]:
                st.markdown(f"~~{task['text']}~~")
            else:
                st.markdown(f"**{task['text']}**")
        
        with col3:
            # Delete button
            if st.button("🗑️", key=f"delete_{idx}", help="Delete task"):
                st.session_state.tasks.pop(idx)
                st.rerun()
    
    st.markdown("---")
    
    # Clear all button
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🗑️ Clear All Tasks"):
            st.session_state.tasks = []
            st.rerun()
    with col2:
        if st.button("✅ Clear Completed"):
            st.session_state.tasks = [t for t in st.session_state.tasks if not t["completed"]]
            st.rerun()
