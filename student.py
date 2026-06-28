class Student:     
    all_students = []    #Object based Variable for storing data (name ,marks,rollno. etc)
    file_name = "students.txt"

    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
    
    def update_marks(self,new_marks):
        self.marks = new_marks
        print(f"Marks for {self.name} updated to {self.marks}.")

    @classmethod
    def find_student_by_roll(cls, roll):
        for student in cls.all_students:
            if student.roll_number == roll:
                return student
        return None

    def show_details(self):
        print(f"\n Student Details:")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")

    
    @classmethod
    def load_data(cls):
        cls.all_students = []
        try:
            with open(cls.file_name, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        name, roll, marks = parts
                        cls.all_students.append(cls(name, roll, int(marks)))
        except FileNotFoundError:
            pass

    @classmethod
    def save_data(cls):
        with open(cls.file_name, "w") as f:
            for student in cls.all_students:
                f.write(f"{student.name},{student.roll_number},{student.marks}\n")

    
    @classmethod
    def add_student(cls):
        cls.load_data()
        name = input("Enter Student name: ")
        roll = input("Enter Student roll number: ")
        marks = int(input("Enter student marks: "))
        student = cls(name,roll,marks)
        cls.all_students.append(student)
        cls.save_data()
        print (f"Student {name} added successfully")

    # ---------------- Show All ----------------
    @classmethod 
    def show_all_students(cls):
        cls.load_data()
        if not cls.all_students:
            print("No students found.")
            return
        for student in cls.all_students:
            student.show_details()

    
    @classmethod
    def search_student(cls):
        cls.load_data()
        keyword = input("Enter Student Roll Number or Name to search: ")
        found = False
        for student in cls.all_students:
            if student.roll_number == keyword or student.name.lower() == keyword.lower():
                student.show_details()
                found = True
        if not found:
            print("Student not Found.")

   
    @classmethod
    def update_student(cls):
        cls.load_data()
        roll = input("Enter student roll number to update: ")
        student = cls.find_student_by_roll(roll)
        if student:
            new_name = input("Enter new name (leave blank to keep current): ")
            if new_name.strip() != "":
                student.name = new_name
            new_marks = input("Enter new marks (leave blank to keep current): ")
            if new_marks.strip() != "":
                student.marks = int(new_marks)
            cls.save_data()
            print(f"Student {student.roll_number} updated Successfully!")
        else:
            print("Student not Found.")

    
    @classmethod
    def delete_student(cls):
        cls.load_data()
        roll = input("Enter student roll number to delete: ")
        student = cls.find_student_by_roll(roll)
        if student:
            cls.all_students.remove(student)
            cls.save_data()
            print(f"Student {roll} deleted successfully!")
        else:
            print("Student not Found.")
