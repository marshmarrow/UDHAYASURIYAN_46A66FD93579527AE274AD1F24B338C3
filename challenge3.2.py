class Student:
    def __init__(self,name,roll_number,cgpa):
        self.name =name
        self.roll_number = roll_number
        self.cgpa = cgpa


def sort_students(student_list):
    sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
    return sorted_students

students = [
    Student("king","A123",7.3),
    Student("saundhar", "A348", 7.4),
    Student("lukha", "A183", 7.9),
    Student("queen", "A143", 8.9),
]

sorted_students = sort_students;

for student in sorted_students(students):
    print("name : {}, Roll number : {}, CGPA : {}".format(student.name,
                                                          student.roll_number,
                                                          student.cgpa))