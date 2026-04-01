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

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

One tradeoff in my scheduler is that conflict detection only checks for exact matches in due date and time. This makes the logic simple and easy to understand, but it does not detect overlapping tasks with different start times. This tradeoff is reasonable for this scenario because the project focuses on basic scheduling features rather than handling complex time ranges. Using exact matches helps to make things easier to debug while being sufficient to demo the app's core functionalities. I also chose to keep my original conflict detection code instead of using defaultdict because the original version is a little longer but easier for me to read.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
