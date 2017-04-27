#!/usr/bin/python3



class Student(object):
    """A Python class to store student information"""

    def __init__(self, name, age, address):
        self.name = name
        self.address = address
        self.age = age

    def return_name(self):
        """return student name"""
        return self.name

    def return_age(self):
        """return student age"""
        return self.age

    def return_address(self):
        """return student address"""
        return self.address

    def update_address(self, address):
        """update student address"""
        self.address = address
        return self.address

if __name__ == "__main__":
    student1 = Student("John Doe", "29", "123 Main Street, Newark, CA")
    print(student1.return_address())
    print(student1.update_address("234 Main Street, Newark, CA"))
    print(Student.return_address(student1))
