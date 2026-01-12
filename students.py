students = []

def add_student():
    usn = input("Enter USN: ")
    name = input("Enter Name: ")
    marks = []

    for i in range(3):
        m = int(input(f"Enter marks {i+1}: "))
        marks.append(m)

    students.append([usn, name, marks])
    print(" Student added successfully\n")


def display_students():
    if not students:
        print("No records found\n")
        return

    for s in students:
        avg = sum(s[2]) / len(s[2])
        print(f"USN: {s[0]}, Name: {s[1]}, Marks: {s[2]}, Avg: {avg:.2f}")
    print()


def find_topper():
    if not students:
        print("No records found\n")
        return

    topper = students[0]
    max_avg = sum(topper[2]) / len(topper[2])

    for s in students:
        avg = sum(s[2]) / len(s[2])
        if avg > max_avg:
            topper = s
            max_avg = avg

    print(f" Topper: {topper[1]} ({topper[0]}) with Avg: {max_avg:.2f}\n")


def sort_by_average():
    sorted_students = sorted(
        students,
        key=lambda s: sum(s[2]) / len(s[2]),
        reverse=True
    )

    for s in sorted_students:
        avg = sum(s[2]) / len(s[2])
        print(f"{s[1]} - Avg: {avg:.2f}")
    print()


def search_student():
    key = input("Enter USN or Name to search: ")

    for s in students:
        if s[0] == key or s[1].lower() == key.lower():
            print(f"Found → USN: {s[0]}, Name: {s[1]}, Marks: {s[2]}\n")
            return

    print("Student not found\n")


while True:
    print("---- Student Performance Analyzer ----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Find Topper")
    print("4. Sort by Average")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        find_topper()
    elif choice == "4":
        sort_by_average()
    elif choice == "5":
        search_student()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice\n")
