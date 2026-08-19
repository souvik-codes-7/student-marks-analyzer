import csv

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def load_students(filename):
    students = []
    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            marks = [float(row[subject]) for subject in ["Python", "SQL", "Maths"]]
            total = sum(marks)
            percentage = total / len(marks)
            row["Total"] = total
            row["Percentage"] = percentage
            row["Grade"] = calculate_grade(percentage)
            students.append(row)
    return students

def show_report(students):
    print("\n===== STUDENT MARKS REPORT =====")
    for student in students:
        print(
            f'{student["Name"]}: '
            f'Total={student["Total"]:.1f}, '
            f'Percentage={student["Percentage"]:.2f}%, '
            f'Grade={student["Grade"]}'
        )

    topper = max(students, key=lambda x: x["Percentage"])
    average = sum(s["Percentage"] for s in students) / len(students)

    print("\n===== SUMMARY =====")
    print(f'Class Average: {average:.2f}%')
    print(f'Topper: {topper["Name"]} ({topper["Percentage"]:.2f}%)')

if __name__ == "__main__":
    data = load_students("students.csv")
    show_report(data)
