import pickle
import json
import csv
from csv import DictWriter

# txt:
# with open("students.txt", "r")as file:
#     print(file.read())
#     print()
#     file.seek(0)
#     lines = file.readlines()
#
# studentsinfo = []
# with open("students.txt", "w")as file:
#     for line in lines:
#         names, grade = line.rsplit(" - ", 1)
#         grade = int(grade.strip())
#         if grade < 80:
#             grade += 5
#         studentsinfo.append(f"{names} - {grade}\n")
#     file.writelines(studentsinfo)
#
# with open("students.txt", "r")as file:
#     print(file.read())

# pickle:
# data = [
#     {"name": "John Smith", "grade": 85},
#     {"name": "Emily Johnson", "grade": 90},
#     {"name": "Michael Brown", "grade": 78},
#     {"name": "Sarah Davis", "grade": 92},
#     {"name": "David Wilson", "grade": 69},
# ]
#
# with open("students.pkl", "wb")as file:
#     pickle.dump(data, file)
#
# with open("students.pkl", "rb")as file:
#     students_data = pickle.load(file)
#
# for student in students_data:
#     print(f"{student["name"]} - {student["grade"]}")
#
# for student in students_data:
#     if student["grade"] < 80:
#         student["grade"] += 5
#
# with open("students.pkl", "wb")as file:
#     pickle.dump(students_data, file)
#
# with open("students.pkl", "rb")as file:
#     new_grades = pickle.load(file)
#
# print()
# for student in new_grades:
#     print(f"{student["name"]} - {student["grade"]}")

# json:
# data = [
#     {"name": "John Smith", "grade": 85},
#     {"name": "Emily Johnson", "grade": 90},
#     {"name": "Michael Brown", "grade": 78},
#     {"name": "Sarah Davis", "grade": 92},
#     {"name": "David Wilson", "grade": 69},
# ]
# with open("students.json", "w")as file:
#     json.dump(data, file)
#
# with open("students.json", "r")as file:
#     students_data = json.load(file)
#
# for student in students_data:
#     print(f"{student["name"]} - {student["grade"]}")
#
# for student in students_data:
#     if student["grade"] < 80:
#         student["grade"] += 5
#
# with open("students.json", "w")as file:
#     json.dump(students_data, file)
#
# with open("students.json", "r")as file:
#     new_grades = json.load(file)
#
# print()
# for student in new_grades:
#     print(f"{student["name"]} - {student["grade"]}")


# csv:
data = [
    {"name": "John Smith", "grade": 85},
    {"name": "Emily Johnson", "grade": 90},
    {"name": "Michael Brown", "grade": 78},
    {"name": "Sarah Davis", "grade": 92},
    {"name": "David Wilson", "grade": 69},
]
with open("students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "grade"])
    writer.writeheader()
    writer.writerows(data)

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    students_data = list(reader)

for student in students_data:
    print(f"{student["name"]} - {student["grade"]}")

for student in students_data:
    if int(student["grade"]) < 80:
        student["grade"] = str(int(student["grade"]) + 5)

with open("students.csv", "w", newline="") as file:
    writer = DictWriter(file, fieldnames=["name", "grade"])
    writer.writeheader()
    writer.writerows(students_data)

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    new_grades = list(reader)

print()
for student in students_data:
    print(f"{student["name"]} - {student["grade"]}")