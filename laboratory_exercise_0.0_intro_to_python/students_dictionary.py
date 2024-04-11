"""
Idea is to create two dictionaries:
    1. students [-> where a key is the students index -> where a value is their Name Surname]
    2. subjects [-> where a key is the students index -> where a value is a dictionary of Subjects with grades]

When reading a line the adequate indexes for the words are:
    0-Name, 1-Surname, 2-Index, 3-Subject, 4-1kol, 5-2kol, 6-lab
"""


def make_grade(colloquium_1, colloquium_2, exercises):
    grade = int(colloquium_1) + int(colloquium_2) + int(exercises)
    final = int(grade / 10) if grade % 10 == 0 else 1 + int(grade / 10)
    final = 5 if final < 6 else final
    return str(final)


# Make dictionaries
students = dict()
subjects_by_index = dict()
while True:
    line = input()
    if line == "end":
        break

    words = line.split(",")
    if words[2] not in subjects_by_index.keys():
        # Subjects dictionary
        student_subject = dict()
        student_subject[words[3]] = make_grade(words[4], words[5], words[6])
        subjects_by_index[words[2]] = student_subject
        # Students dictionary
        students[words[2]] = words[0] + " " + words[1]
    else:
        if words[3] not in subjects_by_index[words[2]].keys():
            # Modify dictionary of subjects for student already in dictionary
            subjects_by_index[words[2]][words[3]] = make_grade(words[4], words[5], words[6])

# Print dictionaries
for index in students.items():
    print(f"Student: {index[1]}")
    for subject in subjects_by_index[index[0]].items():
        print(f"----{subject[0]}: {subject[1]}")
    print()
