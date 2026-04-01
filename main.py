from pawpal_system import Owner, Pet, Task, Scheduler

# Create an owner and two pets
owner = Owner("Alice")
dog = Pet("Boxer", 15, "Bulldog")
cat = Pet("Kitty", 8, "Siamese")

# Pets are added to owner's list of pets
owner.add_pet(dog)
owner.add_pet(cat)

# Create tasks
task_1 = Task("Feed breakfast", "08:00", "daily")
task_2 = Task("Walk around the block", "12:00", "daily")
task_3 = Task("Groom hair", "10:00", "bi-weekly")

# Assign tasks to pets
dog.add_task(task_1)
dog.add_task(task_2)
cat.add_task(task_3)

# Create scheduler
scheduler = Scheduler(owner)

# Show today's schedule
scheduler.show_schedule()