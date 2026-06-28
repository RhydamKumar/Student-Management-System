from student import Student

def menu():
    while True:
        print("\n ========================= Student Management System =========================")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by ID/Name")
        print("4. Update Student Information")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your Option (1-6): ")
        if choice == '1':
            Student.add_student()
        elif choice == '2':
            Student.show_all_students()
        elif choice == '3':
            Student.search_student()
        elif choice == '4':
            Student.update_student()
        elif choice == '5':
            Student.delete_student()
        elif choice == '6':
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please Enter between 1-6")

if __name__ == "__main__":
    menu()
