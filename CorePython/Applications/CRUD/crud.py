studentList = []

def create():
    print("Create Student Record...")
    studentId = int(input("Enter ID : "))
    studentName = input("Enter name : ")
    studentCourse = input("Enter course : ")
    studentNo = int(input("Enter number : "))

    studentList.append([studentId, studentName, studentCourse, studentNo])
    for s in studentList:
        print(s)

def read():
    print("Read Student Record...")

def update():
    print("Update Student Record...")

def delete():
    print("Delete Student Record...")


while True:
    print("""
    1. Create Record
    2. Read Record
    3. Update Record
    4. Delete Record
    5. Search Record
    6. Sort Record
    7. Save Record
    8. Load Record
    9. Quit
    """)

    todo = {
        "1" : create,
        "2" : read,
        "3" : update,
        "4" : delete,
        "9" : quit
    }

    userChoice = input("Enter your choice : ")

    todo.get(userChoice)()
