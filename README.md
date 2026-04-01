# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## Smarter Scheduling

To improve PawPal+, I added smarter scheduling features:

1. Sorting Tasks: Tasks can  be sorted by time to create a clear daily schedule.
2. Filtering Tasks: Tasks can be filtered by pet name or completion status, which makes it easier to view specific tasks.
3. Recurring Tasks: Tasks with a frequency like "daily" or "weekly" automatically generate a new task when completed.
4. Conflict Detection: The system detects scheduling conflicts when multiple tasks have the same due date and time.

## Testing PawPal+

Run the test suite using:
python -m pytest

These tests cover the core functionality of the PawPal+ system such as  task creation and completion, adding tasks to pets, and verifying that task lists update correctly. They also test the scheduling logic by making sure tasks are sorted in chronological order and do not modify the original data. Recurring task behavior is also verified and it is checked that non-recurring tasks do not create additional entries. Lastly, the tests check conflict detection by comparing outputs for tasks that occur at the same date and time and for those that do not.

Based on the test case results, my confidence Level is 4.5/5 regarding the system’s reliability because all 20/20 test cases that cover both happy cases along with edge cases passed successfully. However, there may still be more complex scenarios that have not been fully tested.