# Passive-Aggressive GPA Calculator
# Calculates GPA, analyzes semesters, and judges your life choices—gently.

def get_valid_grade(prompt):
    """Get a valid grade between 0.0 and 4.0 from the user, because apparently that’s hard."""
    while True:
        try:
            grade = float(input(prompt))
            if 0.0 <= grade <= 4.0:
                return grade
            else:
                print("Oh wow, impressive. I said between 0.0 and 4.0. Let's try that again.")
        except ValueError:
            print("That’s not even a number. We’re off to a strong start.")

def calculate_gpa(grade_list):
    """Return the GPA from a list of grades."""
    return sum(grade_list) / len(grade_list)

# Step 1: Create and validate grades list
print("Welcome to the GPA Calculator—because you can’t do basic math yourself.")
num_grades = 0
while num_grades < 5:
    try:
        num_grades = int(input("How many grades do you want to enter? (at least 5, hopefully you can count): "))
        if num_grades < 5:
            print("You need at least 5 grades. I know, numbers are hard.")
    except ValueError:
        print("Nice try, but words aren’t numbers. Try again.")

grades = []
for i in range(num_grades):
    grades.append(get_valid_grade(f"Enter grade #{i+1}: "))

# Step 3: Calculate current GPA
current_gpa = calculate_gpa(grades)

# Step 4: Display GPA
print(f"\nCrunching the numbers you could’ve easily done yourself...")
print(f"Based on {len(grades)} classes, your GPA is: {current_gpa:.2f}. Not bad, I guess.")

# Step 5: Semester GPA analysis (slicing)
print("\nLet’s see if you actually improved or just coasted through.")
half = len(grades) // 2
choice = input("Do you want to look at the 'first' or 'second' half of your classes? ").strip().lower()

if choice == "first":
    semester_grades = grades[:half]
    semester_name = "first"
elif choice == "second":
    semester_grades = grades[half:]
    semester_name = "second"
else:
    print("Couldn’t follow simple directions? Fine. We’ll just do the first half.")
    semester_grades = grades[:half]
    semester_name = "first"

semester_gpa = calculate_gpa(semester_grades)
print(f"\nYour {semester_name} semester GPA is: {semester_gpa:.2f}.")

# Compare performance
if semester_gpa > current_gpa:
    print("Wow, improvement! Didn’t think you had it in you.")
elif semester_gpa < current_gpa:
    print("Yikes. Seems like motivation took a vacation that semester.")
else:
    print("Perfectly consistent. Mediocrity really suits you.")

# Step 6: Goal GPA analysis
goal_gpa = None
while goal_gpa is None:
    try:
        goal_gpa = float(input("\nWhat’s your goal GPA (0.0 - 4.0)? Aim high, or at least higher than before: "))
        if not (0.0 <= goal_gpa <= 4.0):
            print("Between 0.0 and 4.0, remember? This isn’t complicated.")
            goal_gpa = None
    except ValueError:
        print("That’s not a number. Math still not your strong suit, huh?")

if current_gpa >= goal_gpa:
    print(f"Well look at you. Your current GPA of {current_gpa:.2f} already beats your goal of {goal_gpa:.2f}. Good for you, I guess.")
else:
    achievable = []
    for i in range(len(grades)):
        temp_grades = grades.copy()
        temp_grades[i] = 4.0
        new_gpa = calculate_gpa(temp_grades)
        if new_gpa >= goal_gpa:
            achievable.append(i + 1)
    if achievable:
        print(f"\nApparently your goal GPA of {goal_gpa:.2f} isn’t a total fantasy.")
        print("If you could manage to get one of these grades up to a 4.0, you might actually hit it:")
        for idx in achievable:
            print(f" - Grade #{idx} (currently {grades[idx-1]:.2f})")
    else:
        print(f"\nOof. Even if you magically turned one grade into a 4.0, you’d still miss your goal GPA of {goal_gpa:.2f}.")
        print("Might want to start doing your homework… just a thought.")
