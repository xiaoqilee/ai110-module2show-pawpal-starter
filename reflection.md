# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

My initial UML design includes four classes: Owner, Pet, Task, and Scheduler.

Owner: The Owner class stores the owner's name and is responsible for managing a list of pets. 

Pet: The Pet class stores a pet's name, age, breed, and associated tasks.  

Task: The Task class represents a specific pet care activity and includes details such as a description, frequency, and completion status.  

Scheduler: The Scheduler class is responsible for organizing and displaying tasks.

**b. Design changes**

Based on the AI provided feedback, the Task class was altered to include a time field. THis is helpful so that the Scheduler can sort and display tasks more effectively. 

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

My scheduler considers constraints such as time, task frequency, and completion status. The tasks are organized based on their scheduled time and recurring tasks depend on their frequency. I decided that time was the most important constraint because the goal of the app is to create a clear daily schedule. Frequency and completion status are also important for keeping tasks up to date.

**b. Tradeoffs**

One tradeoff in my scheduler is that conflict detection only checks for exact matches in due date and time. This makes the logic simple and easy to understand, but it does not detect overlapping tasks with different start times. This tradeoff is reasonable for this scenario because the project focuses on basic scheduling features rather than handling complex time ranges. Using exact matches helps to make things easier to debug while being sufficient to demo the app's core functionalities. I also chose to keep my original conflict detection code instead of using defaultdict because the original version is a little longer but easier for me to read.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI tools like VS Code Copilot to help with tasks like design brainstorming, generating test cases, and debugging code. The most helpful prompts were ones that were more detailed in describing what I wanted the function to do, such as how to handle recurring tasks with timedelta.

**b. Judgment and verification**

One instance where I did not accept an AI suggestion as-is was when Copilot suggested using defaultdict for conflict detection. Although it made the code shorter, I chose not to use it because my original version more readable. I verified AI suggestions by using test cases and making sure the logic matched my design.

---

## 4. Testing and Verification

**a. What you tested**

I tested behaviors such as task completion, adding tasks to pets, sorting tasks by time, recurring task generation, and conflict detection. These tests were important because they make up the core functionality of the scheduler. If these components are functional, a user would be able to reliably create, manage, and view their pet care tasks.

**b. Confidence**

I am fairly confident that my scheduler works correctly because all 20/20 tests passed successfully. The tests cover both standard use cases and edge cases. If I had more time, I would test more scenarios such as overlapping task durations and larger numbers of concurrent tasks.

---

## 5. Reflection

**a. What went well**

The part of this project I am most satisfied with is the implementation of the scheduling logic, especially recurring tasks and conflict detection. These features made the system feel more realistic and useful.

**b. What you would improve**

I would improve the scheduling logic to handle more advanced scenarios, such as overlapping task durations instead of only exact time matches. I would also adjust the UI to make it more interactive and user-friendly.

**c. Key takeaway**

One important thing I learned is that designing a system requires both planning and iteration. It was useful to first create an outline and break the project into smaller features like sorting, filtering, and conflict detection, then build them step-by-step.