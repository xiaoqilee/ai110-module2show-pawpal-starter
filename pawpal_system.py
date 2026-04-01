from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    description: str
    frequency: str
    completed: bool = False

    def set_complete(self) -> None:
        pass


@dataclass
class Pet:
    name: str
    age: int
    breed: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass

    def remove_task(self, task: Task) -> None:
        pass

    def show_tasks(self) -> List[Task]:
        pass


class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def get_pets(self) -> List[Pet]:
        pass

    def add_pet(self, pet: Pet) -> None:
        pass

    def get_tasks(self) -> List[Task]:
        pass


class Scheduler:
    def show_todays_tasks(self, owner: Owner) -> List[Task]:
        pass

    def sort_tasks(self, tasks: List[Task]) -> List[Task]:
        pass
