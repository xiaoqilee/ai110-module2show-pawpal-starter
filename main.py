from pawpal_system import Owner, Pet, Task, Scheduler

# Create an owner and two pets
owner = Owner("Alice")
dog = Pet("Boxer", 15, "Bulldog")
cat = Pet("Kitty", 8, "Siamese")

# Add pets to owner
owner.add_pet(dog)
owner.add_pet(cat)

# Create tasks
task_1 = Task("Walk around the block", "12:00", "daily")
task_2 = Task("Feed breakfast", "08:00", "daily")
task_3 = Task("Groom hair", "10:00", "bi-weekly")
task_4 = Task("Give medicine", "07:30", "daily")
task_5 = Task("Veterinarian visit", "12:00", "once")

# Assign tasks to pets
dog.add_task(task_1)
dog.add_task(task_2)
cat.add_task(task_3)
cat.add_task(task_4)
cat.add_task(task_5)

# Create scheduler
scheduler = Scheduler(owner)

# Test recurring task
scheduler.complete_task(dog, task_2)

print("\nAfter completing a task:")
for task in scheduler.sort_by_time(owner.get_tasks()):
    print(task)

# Get all tasks
all_tasks = owner.get_tasks()

# Test sorting
sorted_tasks = scheduler.sort_by_time(all_tasks)
print("\nSorted Tasks:")
for task in sorted_tasks:
    print(task)

# Test filtering by completion status
completed_tasks = scheduler.filter_tasks(completed=True)
print("\nCompleted Tasks:")
for task in completed_tasks:
    print(task)

# Test filtering by pet name
kitty_tasks = scheduler.filter_tasks(pet_name="Kitty")
print("\nKitty's Tasks:")
for task in kitty_tasks:
    print(task)

# Test filtering by pet name + completion status
kitty_pending = scheduler.filter_tasks(pet_name="Kitty", completed=False)
print("\nKitty's Pending Tasks:")
for task in kitty_pending:
    print(task)

# Detect scheduling conflicts
conflicts = scheduler.find_conflicts()
print("\nConflicts:")
if conflicts:
    for (due_date, time), tasks in conflicts.items():
        print(f"  {due_date} at {time}:")
        for task in tasks:
            print(f"    - {task.description}")