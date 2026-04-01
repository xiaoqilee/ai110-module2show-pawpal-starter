from pawpal_system import Task, Pet

def test_task_completion():
    task = Task(description="Morning walk", time="08:00", frequency="daily")
    assert task.completed is False

    task.set_complete()

    assert task.completed is True

def test_add_task_increases_pet_task_count():
    pet = Pet(name="Buddy", age=3, breed="Labrador")
    assert len(pet.tasks) == 0

    task = Task(description="Feed breakfast", time="07:30", frequency="daily")
    pet.add_task(task)

    assert len(pet.tasks) == 1
