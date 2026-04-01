from datetime import date, timedelta
from pawpal_system import Task, Pet, Owner, Scheduler


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


# ---------------------------------------------------------------------------
# Sorting
# ---------------------------------------------------------------------------

def test_sort_by_time_returns_chronological_order():
    owner = Owner("Alice")
    scheduler = Scheduler(owner)

    tasks = [
        Task(description="Evening walk", time="18:00", frequency="daily"),
        Task(description="Lunch snack",  time="12:00", frequency="daily"),
        Task(description="Morning feed", time="07:30", frequency="daily"),
    ]

    sorted_tasks = scheduler.sort_by_time(tasks)

    assert [t.time for t in sorted_tasks] == ["07:30", "12:00", "18:00"]


def test_sort_by_time_boundary_times():
    # Midnight and end-of-day are the extremes; midnight should sort first
    owner = Owner("Alice")
    scheduler = Scheduler(owner)

    tasks = [
        Task(description="Last task",  time="23:59", frequency="once"),
        Task(description="Midday",     time="12:00", frequency="once"),
        Task(description="First task", time="00:00", frequency="once"),
    ]

    sorted_tasks = scheduler.sort_by_time(tasks)

    assert sorted_tasks[0].time == "00:00"
    assert sorted_tasks[-1].time == "23:59"


def test_sort_by_time_single_item_unchanged():
    owner = Owner("Alice")
    scheduler = Scheduler(owner)

    tasks = [Task(description="Solo task", time="09:00", frequency="once")]
    assert scheduler.sort_by_time(tasks) == tasks


def test_sort_by_time_empty_list_returns_empty():
    owner = Owner("Alice")
    scheduler = Scheduler(owner)

    assert scheduler.sort_by_time([]) == []


def test_sort_by_time_already_sorted_is_stable():
    owner = Owner("Alice")
    scheduler = Scheduler(owner)

    tasks = [
        Task(description="A", time="06:00", frequency="daily"),
        Task(description="B", time="10:00", frequency="daily"),
        Task(description="C", time="22:00", frequency="daily"),
    ]
    assert scheduler.sort_by_time(tasks) == tasks


def test_sort_by_time_does_not_mutate_original_list():
    owner = Owner("Alice")
    scheduler = Scheduler(owner)

    tasks = [
        Task(description="Late",  time="20:00", frequency="daily"),
        Task(description="Early", time="06:00", frequency="daily"),
    ]
    original_order = [t.time for t in tasks]

    scheduler.sort_by_time(tasks)

    assert [t.time for t in tasks] == original_order  # original list unchanged


# ---------------------------------------------------------------------------
# Recurrence
# ---------------------------------------------------------------------------

def _make_scheduler_with_pet():
    """Helper: returns (scheduler, pet) with owner already wired up."""
    owner = Owner("Bob")
    pet = Pet(name="Rex", age=4, breed="Boxer")
    owner.add_pet(pet)
    return Scheduler(owner), pet


def test_complete_daily_task_creates_next_day_task():
    scheduler, pet = _make_scheduler_with_pet()
    today = date(2026, 3, 31)
    task = Task(description="Morning walk", time="08:00", frequency="daily", due_date=today)
    pet.add_task(task)

    next_task = scheduler.complete_task(pet, task)

    assert next_task is not None
    assert next_task.due_date == today + timedelta(days=1)
    assert next_task.description == "Morning walk"
    assert next_task.time == "08:00"
    assert next_task.frequency == "daily"
    assert next_task.completed is False


def test_complete_weekly_task_creates_next_week_task():
    scheduler, pet = _make_scheduler_with_pet()
    today = date(2026, 3, 31)
    task = Task(description="Bath time", time="10:00", frequency="weekly", due_date=today)
    pet.add_task(task)

    next_task = scheduler.complete_task(pet, task)

    assert next_task is not None
    assert next_task.due_date == today + timedelta(weeks=1)


def test_complete_daily_task_adds_new_task_to_pet():
    scheduler, pet = _make_scheduler_with_pet()
    task = Task(description="Feed dinner", time="18:00", frequency="daily")
    pet.add_task(task)

    scheduler.complete_task(pet, task)

    assert len(pet.tasks) == 2  # original + new occurrence


def test_complete_once_task_returns_none_and_no_new_task():
    scheduler, pet = _make_scheduler_with_pet()
    task = Task(description="Vet visit", time="09:00", frequency="once")
    pet.add_task(task)

    result = scheduler.complete_task(pet, task)

    assert result is None
    assert len(pet.tasks) == 1  # no new task added


def test_complete_biweekly_task_returns_none():
    # "bi-weekly" is not in the intervals dict, so recurrence is not supported
    scheduler, pet = _make_scheduler_with_pet()
    task = Task(description="Grooming", time="11:00", frequency="bi-weekly")
    pet.add_task(task)

    result = scheduler.complete_task(pet, task)

    assert result is None


def test_completed_task_is_marked_done_regardless_of_frequency():
    scheduler, pet = _make_scheduler_with_pet()
    task = Task(description="Nail trim", time="14:00", frequency="once")
    pet.add_task(task)

    scheduler.complete_task(pet, task)

    assert task.completed is True


# ---------------------------------------------------------------------------
# Conflict Detection
# ---------------------------------------------------------------------------

def test_find_conflicts_detects_same_date_and_time():
    owner = Owner("Carol")
    pet = Pet(name="Luna", age=1, breed="Husky")
    owner.add_pet(pet)
    scheduler = Scheduler(owner)

    slot_date = date(2026, 3, 31)
    task_a = Task(description="Walk",      time="08:00", frequency="daily",  due_date=slot_date)
    task_b = Task(description="Vet visit", time="08:00", frequency="once",   due_date=slot_date)
    pet.add_task(task_a)
    pet.add_task(task_b)

    conflicts = scheduler.find_conflicts()

    assert (slot_date, "08:00") in conflicts
    assert len(conflicts[(slot_date, "08:00")]) == 2


def test_find_conflicts_across_different_pets():
    owner = Owner("Carol")
    pet1 = Pet(name="Luna",  age=1, breed="Husky")
    pet2 = Pet(name="Bruno", age=3, breed="Poodle")
    owner.add_pet(pet1)
    owner.add_pet(pet2)
    scheduler = Scheduler(owner)

    slot_date = date(2026, 3, 31)
    pet1.add_task(Task(description="Walk",  time="09:00", frequency="daily", due_date=slot_date))
    pet2.add_task(Task(description="Brush", time="09:00", frequency="daily", due_date=slot_date))

    conflicts = scheduler.find_conflicts()

    assert (slot_date, "09:00") in conflicts


def test_find_conflicts_three_tasks_same_slot():
    owner = Owner("Carol")
    pet = Pet(name="Luna", age=1, breed="Husky")
    owner.add_pet(pet)
    scheduler = Scheduler(owner)

    slot_date = date(2026, 3, 31)
    for desc in ("Walk", "Feed", "Meds"):
        pet.add_task(Task(description=desc, time="08:00", frequency="daily", due_date=slot_date))

    conflicts = scheduler.find_conflicts()

    assert len(conflicts[(slot_date, "08:00")]) == 3


def test_find_conflicts_same_time_different_date_is_not_a_conflict():
    owner = Owner("Carol")
    pet = Pet(name="Luna", age=1, breed="Husky")
    owner.add_pet(pet)
    scheduler = Scheduler(owner)

    pet.add_task(Task(description="Walk", time="08:00", frequency="daily", due_date=date(2026, 3, 31)))
    pet.add_task(Task(description="Walk", time="08:00", frequency="daily", due_date=date(2026, 4, 1)))

    conflicts = scheduler.find_conflicts()

    assert conflicts == {}


def test_find_conflicts_same_date_different_time_is_not_a_conflict():
    owner = Owner("Carol")
    pet = Pet(name="Luna", age=1, breed="Husky")
    owner.add_pet(pet)
    scheduler = Scheduler(owner)

    slot_date = date(2026, 3, 31)
    pet.add_task(Task(description="Morning walk", time="07:00", frequency="daily", due_date=slot_date))
    pet.add_task(Task(description="Evening walk", time="18:00", frequency="daily", due_date=slot_date))

    conflicts = scheduler.find_conflicts()

    assert conflicts == {}


def test_find_conflicts_empty_schedule_returns_empty_dict():
    owner = Owner("Carol")
    owner.add_pet(Pet(name="Luna", age=1, breed="Husky"))
    scheduler = Scheduler(owner)

    assert scheduler.find_conflicts() == {}
