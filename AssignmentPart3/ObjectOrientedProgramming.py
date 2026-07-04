"""
Object-Oriented Programming (OOP) Concepts Assignment
Language: Python 3
"""

from abc import ABC, abstractmethod
import math

# ==========================================
# 1. CLASS CREATION & ENCAPSULATION
# ==========================================

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        # Encapsulation: '__age' is a private attribute, inaccessible directly outside the class
        self.__age = age  
        self.grade = grade

    # Encapsulation: Getter method to safely retrieve the private age
    def get_age(self):
        return self.__age

    # Encapsulation: Setter method to safely modify the private age with validation
    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age > 0:
            self.__age = new_age
        else:
            print("Error: Age must be a positive integer.")

    # Class Creation: Method to display student information
    def display_info(self):
        return f"Student Name: {self.name}, Age: {self.__age}, Grade: {self.grade}"


# ==========================================
# 2. INHERITANCE
# ==========================================

# HighSchoolStudent inherits all properties and methods from the Student class
class HighSchoolStudent(Student):
    def __init__(self, name, age, grade, grade_level):
        # Call the parent class (Student) constructor to initialize shared attributes
        super().__init__(name, age, grade)
        # Unique attribute specific to HighSchoolStudent
        self.grade_level = grade_level

    # Inheritance & Polymorphism: Overriding the parent's display_info method
    def display_info(self):
        # We must use get_age() because __age is private to the parent class
        return f"HighSchool Student Name: {self.name}, Age: {self.get_age()}, Grade: {self.grade}, Level: {self.grade_level}"


# ==========================================
# 3. POLYMORPHISM
# ==========================================

def print_student_info(student_object):
    """
    Polymorphism: This function accepts an object of either Student or HighSchoolStudent
    class and dynamically calls the correct display_info() method at runtime.
    """
    print(student_object.display_info())


# ==========================================
# 4. ABSTRACTION
# ==========================================

# Abstract class acting as a blueprint; cannot be instantiated directly
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        """Abstract method that must be overridden by all subclasses"""
        pass

# Circle subclass implementing the abstract Shape class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Providing specific implementation for the abstract method
    def calculate_area(self):
        return math.pi * (self.radius ** 2)

# Rectangle subclass implementing the abstract Shape class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Providing specific implementation for the abstract method
    def calculate_area(self):
        return self.width * self.height


# ==========================================
# 5. TESTING AND VERIFICATION
# ==========================================
if __name__ == "__main__":
    print("--- Testing Class Creation & Encapsulation ---")
    student1 = Student("Alice Smith", 15, "A")
    print(student1.display_info())
    
    # Testing Encapsulation: Modifying private attribute via setter
    print("\nUpdating Alice's age using set_age()...")
    student1.set_age(16) 
    print(f"Verified age via getter (get_age()): {student1.get_age()}")

    print("\n--- Testing Inheritance & Polymorphism Function ---")
    # Instantiating the subclass
    hs_student1 = HighSchoolStudent("Bob Jones", 17, "B+", "Senior")
    
    # Demonstrating Polymorphism via the external function
    print_student_info(student1)    # Calls Student.display_info()
    print_student_info(hs_student1) # Calls HighSchoolStudent.display_info()

    print("\n--- Testing Abstraction ---")
    circle_instance = Circle(5)
    rectangle_instance = Rectangle(4, 6)
    
    print(f"Circle Area (Radius 5): {circle_instance.calculate_area():.2f}")
    print(f"Rectangle Area (Width 4, Height 6): {rectangle_instance.calculate_area():.2f}")