# Student Information System

A small Python project built for the **Git & GitHub practical assignment**.

The program asks a student for their basic details and then uses **string
concatenation** to build two brand new pieces of information from what was
typed in, before printing everything out as a neatly formatted profile card.

---

## Features

- **Collects six details** from the user: full name, student ID, programme,
  level, age and favourite programming language.
- **Generates a student username.** The first three letters of the student's
  name are joined onto their student ID:

  ```python
  name_prefix = full_name[0:NAME_LETTERS_USED].lower()
  generated_username = name_prefix + student_id
  ```

  So `Taylor Norbert` with ID `22447815` becomes **`tay22447815`**.

- **Generates a student email.** The generated username is joined onto a
  fixed domain held in a constant:

  ```python
  EMAIL_DOMAIN = "@st.ug.edu.gh"
  generated_email = generated_username + EMAIL_DOMAIN
  ```

  Which gives **`tay22447815@st.ug.edu.gh`**.

- **Builds its own borders.** The `====` and `----` lines are never typed out
  by hand. They are built by joining a single character together into a
  string variable, so changing `LINE_WIDTH` resizes the whole card:

  ```python
  border = BORDER_CHARACTER * LINE_WIDTH
  divider = DIVIDER_CHARACTER * LINE_WIDTH
  ```

- **Lines up the output with concatenation.** Headings are centred and labels
  are aligned by concatenating the right number of spaces in front of the
  text, rather than counting spaces manually.

---

## How to run

```bash
python3 student_information.py
```

Then answer each prompt.

### Example output

```text
==============================================
          STUDENT INFORMATION SYSTEM
==============================================

Full Name                 : Taylor Norbert
Student ID                : 22447815
Programme                 : Information Technology
Level                     : 100
Age                       : 19
Favourite Language        : Python
----------------------------------------------
Generated Username        : tay22447815
Generated Email           : tay22447815@st.ug.edu.gh

==============================================
             UNIVERSITY OF GHANA
==============================================
```

---

## Project structure

```text
student-information-system/
├── student_information.py    # the program
├── README.md                 # this file
└── .gitignore                # keeps __pycache__ and system files out of Git
```

---

## Author

**Gideon Annor Arthur**

GitHub: [@solution3354](https://github.com/solution3354)
