from dataclasses import dataclass, field
from typing import List
from datetime import datetime


@dataclass
class Task:
    description: str
    time: str          # "HH:MM" format, e.g. "08:00"
    frequency: str     # e.g. "daily", "weekly"
    completed: bool = False

    def set_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True

    def __str__(self) -> str:
        """Return a human-readable summary of the task."""
        status = "Done" if self.completed else "Pending"
        return f"[{status}] {self.description} at {self.time} ({self.frequency})"

@dataclass
class Pet:
    name: str
    age: int
    breed: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet's task list."""
        self.tasks.append(task)

    def remove_task(self, task: Task) -> None:
        """Remove an existing task from this pet's task list."""
        self.tasks.remove(task)

    def show_tasks(self) -> List[Task]:
        """Return all tasks assigned to this pet."""
        return self.tasks

    def __str__(self) -> str:
        """Return a human-readable summary of the pet."""
        return f"{self.name} ({self.breed}, age {self.age})"

class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner's pet list."""
        self.pets.append(pet)

    def get_pets(self) -> List[Pet]:
        """Return all pets belonging to this owner."""
        return self.pets

    def get_tasks(self) -> List[Task]:
        """Aggregates all tasks across every pet this owner has."""
        return [task for pet in self.pets for task in pet.tasks]

    def __str__(self) -> str:
        """Return a human-readable summary of the owner."""
        return f"Owner: {self.name} ({len(self.pets)} pet(s))"

class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def show_todays_tasks(self) -> List[Task]:
        """Returns all incomplete tasks for today across every pet."""
        return [task for task in self.owner.get_tasks() if not task.completed]

    def sort_tasks(self, tasks: List[Task]) -> List[Task]:
        """Sorts tasks chronologically by their scheduled time."""
        return sorted(tasks, key=lambda t: datetime.strptime(t.time, "%H:%M"))

    def show_schedule(self) -> None:
        """Prints a formatted, time-sorted schedule of today's pending tasks."""
        tasks = self.sort_tasks(self.show_todays_tasks())
        if not tasks:
            print(f"No pending tasks for {self.owner.name}'s pets today.")
            return

        print(f"--- Today's Schedule for {self.owner.name} ---")
        for pet in self.owner.get_pets():
            pending = [t for t in pet.tasks if not t.completed]
            if pending:
                print(f"\n  {pet.name}:")
                for task in self.sort_tasks(pending):
                    print(f"    {task}")
