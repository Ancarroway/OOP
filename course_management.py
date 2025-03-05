
"""
Program to demonstrate the use of objects and classes in Object Oriented Programming
Program written by Ashley Carroway on February 25, 2025
"""

from tabulate import tabulate

class Course:
    def __init__(self, course_code, credits, enrollment, room_number):
        self.course_code = course_code
        self.credits = credits
        self.enrollment = enrollment
        self.room_number = room_number

    def get_info(self):
        return [self.course_code, self.credits, self.enrollment, self.room_number]

# Creating course instances
courses = [
    Course("CS101", 3, 40, "Room 101"),
    Course("MATH202", 4, 35, "Room 205"),
    Course("PHY303", 4, 30, "Room 310"),
    Course("ENG150", 6, 50, "Room 120"),
    Course("HIST404", 3, 25, "Room 405"),
    Course("IT1010", 6, 15, "Room 220"),
    Course("COM1150", 4, 32, "Room 350")
]

# Preparing data for tabulation
data = [course.get_info() for course in courses]
headers = ["Course Code", "Credits", "Enrollment", "Room Number"]

# Displaying courses in a table format
print(tabulate(data, headers=headers, tablefmt="grid"))

# Program end message
print("\nProgram execution completed. Thank you!")
