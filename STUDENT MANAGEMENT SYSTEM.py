import json

#---------STUDENT CLASS------------

class Student:          
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade



    # ----------Convert object to dictionary for saving in JSON-----------

    def to_dict(self):
        return {
            "name": self.name,
            "id": self.student_id,
            "grade": self.grade
        }




# ---------------- MANAGER CLASS ----------------
class StudentManager:
    def __init__(self):
        self.students = []  
        self.file_name = "students.json"
        self.load_data() 



 # -------- LOAD DATA FROM FILE --------
    def load_data(self):
        try:
            with open(self.file_name, "r") as file:
                data = json.load(file)
                for item in data:
                    student = Student(item["name"], item["id"], item["grade"])
                    self.students.append(student)
        except FileNotFoundError:
            # If file not found, start with empty list
            self.students = []



  # -------- SAVE DATA TO FILE --------
    def save_data(self):
        data = [student.to_dict() for student in self.students]
        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)



  # -------- ADD STUDENT --------
    def add_student(self):
        name = input("Enter Name: ")
        student_id = input("Enter ID: ")
        grade = input("Enter Grade: ")


 # Check if ID is unique
        for student in self.students:
            if student.student_id == student_id:
                print("ID already exists!")
                return

        new_student = Student(name, student_id, grade)
        self.students.append(new_student)
        self.save_data()
        print("Student added successfully!")


   # -------- VIEW STUDENTS --------
    def view_students(self):
        if not self.students:
            print("No records found.")
            return

        print("\n--- Student List ---")
        for student in self.students:
            print(f"ID: {student.student_id} | Name: {student.name} | Grade: {student.grade}")


  # -------- UPDATE STUDENT --------
    def update_student(self):
        student_id = input("Enter ID to update: ")

        for student in self.students:
            if student.student_id == student_id:
                student.name = input("Enter new name: ")
                student.grade = input("Enter new grade: ")
                self.save_data()
                print("Student updated successfully!")
                return

        print("Student not found!")


    # -------- DELETE STUDENT --------
    def delete_student(self):
        student_id = input("Enter ID to delete: ")

        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                self.save_data()
                print("Student deleted successfully!")
                return

        print("Student not found!")



# ---------------- MAIN PROGRAM ----------------
def main():
    manager = StudentManager()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.update_student()
        elif choice == "4":
            manager.delete_student()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")


# Run program
main()