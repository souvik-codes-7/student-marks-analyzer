import csv
import matplotlib.pyplot as plt

subjects = ["Python", "SQL", "Maths"]
students = []

with open("students.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)

names = [student["Name"] for student in students]

# Chart 1: Average marks by subject
averages = []
for subject in subjects:
    values = [float(student[subject]) for student in students]
    averages.append(sum(values) / len(values))

plt.figure(figsize=(8, 5))
plt.bar(subjects, averages)
plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("average_marks_by_subject.png")
plt.show()

# Chart 2: Percentage of each student
percentages = []
for student in students:
    marks = [float(student[subject]) for subject in subjects]
    percentages.append(sum(marks) / len(marks))

plt.figure(figsize=(8, 5))
plt.bar(names, percentages)
plt.title("Student Percentage")
plt.xlabel("Student")
plt.ylabel("Percentage")
plt.ylim(0, 100)
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("student_percentages.png")
plt.show()

print("Charts created successfully.")
