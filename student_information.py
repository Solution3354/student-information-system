# ==========================================================
# STUDENT INFORMATION SYSTEM
# A small Python program that collects a student's details,
# generates extra information from them using string
# concatenation, and prints a formatted profile.
# ==========================================================

# --- Settings used to build the display ---
LINE_WIDTH = 46          # how wide the profile card is
LABEL_WIDTH = 26         # how much room each label is given
BORDER_CHARACTER = "="
DIVIDER_CHARACTER = "-"

# The domain every generated student email is joined onto.
EMAIL_DOMAIN = "@st.ug.edu.gh"

# How many letters of the name are used to start the username.
NAME_LETTERS_USED = 3

# The border and divider are BUILT by joining a single character
# together, instead of typing "==========" out by hand each time.
border = BORDER_CHARACTER * LINE_WIDTH
divider = DIVIDER_CHARACTER * LINE_WIDTH


def centre(text):
    """Put spaces in front of the text so it sits in the middle of the card."""
    spaces_needed = (LINE_WIDTH - len(text)) // 2
    return " " * spaces_needed + text


def build_row(label, value):
    """Build one line of the profile: label + padding + ' : ' + value."""
    padding = " " * (LABEL_WIDTH - len(label))
    return label + padding + ": " + value


# --- Welcome the user ---
print(border)
print(centre("STUDENT INFORMATION SYSTEM"))
print(border)
print()

# --- Collect the information from the user ---
full_name = input("Full Name                      : ")
student_id = input("Student ID                     : ")
programme = input("Programme                      : ")
level = input("Level                          : ")
age = input("Age                            : ")
favourite_language = input("Favourite Programming Language : ")

# --- Generate new information using string concatenation ---
# The username is the first few letters of the name joined onto the
# student ID, for example "tay" + "22447815" gives "tay22447815".
name_prefix = full_name[0:NAME_LETTERS_USED].lower()
generated_username = name_prefix + student_id

# The email is that same username joined onto the fixed domain.
generated_email = generated_username + EMAIL_DOMAIN

# --- Display everything in a formatted profile ---
print()
print(border)
print(centre("STUDENT INFORMATION SYSTEM"))
print(border)
print()
print(build_row("Full Name", full_name))
print(build_row("Student ID", student_id))
print(build_row("Programme", programme))
print(build_row("Level", level))
print(build_row("Age", age))
print(build_row("Favourite Language", favourite_language))
print(divider)
print(build_row("Generated Username", generated_username))
print(build_row("Generated Email", generated_email))
print()
print(border)
print(centre("UNIVERSITY OF GHANA"))
print(border)
