if __name__ == "__main__":
    students = {}

    while True:
        student = input().strip().split(',')

        if student[0] == "end":
            break

        first_name, last_name, index, subject, theory, practical, laboratory = student
        full_name = f"{first_name} {last_name}"
        theory, practical, laboratory = int(theory), int(practical), int(laboratory)
        total = theory + practical + laboratory
        grade = None

        if total <= 50:
            grade = 5
        elif total <= 60:
            grade = 6
        elif total <= 70:
            grade = 7
        elif total <= 80:
            grade = 8
        elif total <= 90:
            grade = 9
        else:
            grade = 10

        if full_name not in students:
            students[full_name] = {}

        students[full_name][subject] = grade

        for student, subjects in students.items():
            print(f"Student: {student}")
            for subject, grade in subjects.items():
                print(f"----{subject}: {grade}")
