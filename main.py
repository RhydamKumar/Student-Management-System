from student import Student

def menu():
    while True:
        print("\n ========================= Student Management System =========================")
        print("1. Add Student")
        print("2. Update Marks")
        print("3. Show All Student")
        print("4. Exit")

        choice = (input("Enter your Option (1-4): "))
        if choice == '1':
            Student.add_student()
        elif choice == '2':
            Student.update_student_marks()
        elif choice == '3':
            Student.show_all_students()
        elif choice == '4':
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print ("Invalid choice. Please Enter between 1-4")

if __name__=="__main__":
     menu()
