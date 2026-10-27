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
