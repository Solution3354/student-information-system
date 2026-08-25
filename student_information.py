# ==========================================================
# STUDENT INFORMATION SYSTEM
# A small Python program that collects a student's details,
# generates extra information from them using string
# concatenation, and prints a formatted profile.
# ==========================================================

# The domain every generated student email is joined onto.
EMAIL_DOMAIN = "@st.ug.edu.gh"

# How many letters of the name are used to start the username.
NAME_LETTERS_USED = 3

print("STUDENT INFORMATION SYSTEM")
print("Please enter the student's details below.")
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

print()
print("Thank you! The details below were received.")
print(full_name)
print(student_id)
print(programme)
print(level)
print(age)
print(favourite_language)
print(generated_username)
print(generated_email)
