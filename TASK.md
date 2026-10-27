# Team Task: Clinic Appointments (graded)

Same business for every team. You repeat the chain from the lab: requirements, use cases, candidate classes, class diagram, sequence diagram, code. Use the same prompts P1 to P7 from the lab (change only the business words). Any AI tool is fine.

## Teams
- Teams of 2 or more. One public GitHub repository per team.
- The board has the 7 requirements R1 to R7 and your number N (the maximum upcoming appointments in R4). Do not change the requirements.
- Start with P1 (classify the requirements), then P2 to P7. Actors are Patient and Doctor.
- Do not reuse FoodNow or Cinema.

## What you submit (core)
A GitHub repo made from the template link on the board, with every file filled in:

| File | Content |
|---|---|
| README.md | Team table (ID, name, branch, PR link), N, and the line `Conflict Drill: UNCLAIMED` replaced by names (see GitHub steps) |
| 1_requirements.md | The 7 requirements, split functional / non-functional (P1) |
| 2_use_cases.md | Use cases with one alternative flow (P2) plus the Mermaid use case diagram (P3) |
| 3_candidate_classes.md | Table: class, evidence, Explicit / Inferred / Rejected (P4) |
| 4_class_diagram.md | Mermaid class diagram (P5) |
| 5_sequence_diagram.md | Mermaid sequence diagram with alt / else (P6) |
| main.py | One Python file made from your two diagrams (P7). Must run with `python main.py` |
| 6_ai_journal.md | What you checked each time, and every time the AI was wrong: what it said, why, how you noticed. Paste the output of main.py at the end |

Bonus: `test_main.py` with unit tests. A website with GitHub Pages (Settings, Pages, Source: GitHub Actions).

Mermaid in `.md` files: put the code in a block that starts with ```mermaid. GitHub draws it automatically.

## Running your code
No laptop? Use an online Python runner (for example online-python.com) or GitHub Codespaces.

## GitHub steps
1. **Leader:** open the template link from the board, click "Use this template", "Create a new repository", Public. Settings, Collaborators: add every teammate.
2. **Everyone:** open README.md, pencil icon, replace `UNCLAIMED` with your name. Commit changes, "Create a new branch", "Propose changes", "Create pull request".
3. **Review:** open a teammate's pull request, "Files changed", write one real comment (not just "ok").
4. **Conflict (on purpose):** the leader merges the first pull request. The next says "This branch has conflicts". Click "Resolve conflicts", keep ALL names on the line, "Mark as resolved", "Commit merge". Repeat until every pull request is merged.
5. Then each member adds their own files on their own branch with their own pull request.
6. **Check:** under the Actions tab (and the badge in README) the "check" must turn green. Red means a file is still TODO, a diagram does not render, main.py crashes, or conflict markers are left in a file. Click the red run to read the reason.

## Submit
Email: repo link, names and IDs of all members. Subject: `[Design Task] Team XX - Clinic`.

## Grading (100)
- 30: diagrams are correct and consistent with each other
- 20: requirements and use cases are clear and match the board
- 15: code runs, matches the diagrams, and uses your N
- 25: AI journal (what you checked, real mistakes if there were any) and teamwork evidence (commits, pull requests, a review comment by each member)
- 10: the automatic check is green

Rules: the AI drafts, you review. Do not invent AI mistakes: a journal is graded on what you actually checked. Work that nobody in the team can explain loses marks.

## Additional Doctor Appointment Booking System Instructions

Team size must be **2–4 students**. A fifth member is allowed only if necessary.

The **Dockerfile is required only for teams of 5 students**. Teams with 2–4 members can ignore the Docker task.

In this task, your team will design and implement a simple **Doctor Appointment Booking System**, following the same steps demonstrated in the lab.

### 1. Requirements

Create a file named `requirements.txt` containing the following requirements:

| ID | Requirement |
|---|---|
| R1 | A patient can view the days and times when a doctor is available. |
| R2 | A patient can book an appointment during an available time slot. |
| R3 | A doctor can accept or decline an appointment request. |
| R4 | A patient can have at most **N** upcoming appointments at any given time. |
| R5 | Patient medical data shall be accessible only to authorized staff. |
| R6 | Available appointment times shall be displayed within 2 seconds. |
| R7 | The application shall be usable on mobile phone screens. |

**Note:** `N` represents the maximum number of upcoming appointments allowed per patient. Your team must choose and document its value.

### 2. Team Responsibilities

Each student must build upon the previous student's work.

**Student 1 – Use Case Design**

- Read and create `requirements.txt` with the requirements above.
- Write the use cases in `use_cases.md`.
- Create a Use Case Diagram using Mermaid in `use_case_diagram.md`.
- Commit and push both files to the GitHub repository.

**Student 2 – Class Diagram**

- Read the requirements and Student 1's use cases.
- Design a Class Diagram using Mermaid.
- Save it in `class_diagram.md`.
- Commit and push the file to the repository.

**Student 3 – Sequence Diagram**

- Read the previous deliverables, especially the Class Diagram.
- Create a Sequence Diagram using Mermaid that illustrates the appointment booking process.
- Save it in `sequence_diagram.md`.
- Commit and push the file to the repository.

**Student 4 – Implementation**

- Read the requirements, use cases, Class Diagram, and Sequence Diagram.
- Implement a simple working application using Python or another suitable programming language.
- Keep the implementation as simple as possible, following the lab example.
- Add instructions for running the application in `README.md`.
- Commit and push the source code to the repository.

**Student 5 – Docker (If Applicable)**

- Read the implementation and its execution instructions.
- Create a `Dockerfile` for the application.
- Ensure the application can be built and run inside a Docker container.
- Add Docker build and run commands to `README.md`.
- Commit and push the files to the repository.

### 3. Important Instructions

1. **All diagrams must be written using Mermaid code**, as demonstrated in the lab, and stored in Markdown (`.md`) files.
2. Each student must use the previous student's deliverables as input.
3. Each student must work on their own Git branch and submit their changes through a Pull Request.
4. The team must review and merge the Pull Requests in the correct order.
5. The implementation must be consistent with the requirements and diagrams.
6. If your team has only four members, the Docker task is not required.
7. Keep the application simple. The objective is to practice the complete software engineering workflow, not to build a production-ready system.
