import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

if "owner" not in st.session_state:
    st.session_state.owner = Owner("Alice")

owner = st.session_state.owner

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

if st.button("Reset app data"):
    st.session_state.owner = Owner("Alice")
    st.rerun()

owner = st.session_state.owner

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks
- Represent the pet and the owner
- Build a plan/schedule for a day
- Explain the plan
"""
    )

st.divider()

st.subheader("Quick Demo Inputs")
owner_name = st.text_input("Owner name", value=owner.name)
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

if owner_name:
    owner.name = owner_name

if st.button("Add pet"):
    pet = Pet(pet_name, 0, species)
    owner.add_pet(pet)
    st.success(f"Pet '{pet_name}' has been added.")

selected_pet_name = None
if owner.pets:
    selected_pet_name = st.selectbox(
        "Choose a pet for the task",
        [pet.name for pet in owner.pets]
    )

st.markdown("### Tasks")
st.caption("Add a few tasks for your pet to see them show up in the schedule below.")

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    task_time = st.text_input("Task time (HH:MM)", value="09:00")
with col3:
    frequency = st.selectbox("Frequency", ["daily", "weekly", "bi-weekly"], index=0)

if st.button("Add task"):
    if owner.pets and selected_pet_name:
        selected_pet = next(
            (pet for pet in owner.pets if pet.name == selected_pet_name),
            None
        )

        if selected_pet:
            new_task = Task(task_title, task_time, frequency)
            selected_pet.add_task(new_task)
            st.success(f"Task '{task_title}' has been added for {selected_pet.name}")
    else:
        st.error("You must first add a pet before adding tasks.")

all_task_data = []
for pet in owner.pets:
    for task in pet.tasks:
        all_task_data.append(
            {
                "pet": pet.name,
                "title": task.description,
                "time": task.time,
                "frequency": task.frequency,
                "completed": task.completed,
            }
        )

if all_task_data:
    st.write("Current tasks:")
    st.table(all_task_data)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("Generate a schedule using your implemented scheduling logic.")

if st.button("Generate schedule"):
    scheduler = Scheduler(owner)
    tasks = scheduler.sort_tasks(owner.get_tasks())

    if tasks:
        st.subheader("Today's Schedule")
        for task in tasks:
            st.write(f"{task.time} - {task.description} ({task.frequency})")
    else:
        st.warning("No tasks available to schedule.")