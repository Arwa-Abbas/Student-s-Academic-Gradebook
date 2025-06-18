import sys             #exit function
import json
 
studentids=[]
students={}
id_count=0

#create account functinon
def createaccount():
    global id_count
    name=input("\nEnter your Name: ")
    studentid=input("Enter your Teacher ID: ")
    if studentid in studentids:
        print("Teacher ID already exists! Try logging in.")
    else:
        studentids.append(studentid)
        id_count += 1
        print("\nAccount created successfully for", name)
        print("\n----Login Now------\n")
        login()

#login function
def login():
    studentid = input("Enter your Teacher ID: ")
    if studentid in studentids:
        print("Login successful!")
        return True
    else:
        print("Teacher ID not found. Please create an account first.")
        return False

#addrecord function
def addrecord():
    studentid = input("\nEnter Student ID: ")
    if studentid in students:
        print("Student record already exists.")
        return
    
    name = input("Enter Student Name: ")
    students[studentid] = {
        "name": name,
        "marks": [],
        "average": 0.0,
        "grade": ""
    }
    print(f"Record added for {name}")

#student marks function
def studentmarks():
    studentid=input("\nEnter Student ID: ")
    if studentid not in students:
        print("\nRecord not found")
        return
    
    marks=[]
    for i in range(3):
        mark = float(input(f"Enter marks for Subject {i+1}: "))
        marks.append(mark)
    students[studentid]["marks"] = marks
    print("\nMarks have been added for 3 Subjects")

#grade calculation function
def gradecal():
    for studentid, data in students.items():
        marks = data["marks"]
        if not marks:
            continue
        avg = sum(marks)/len(marks)
        data["average"] =avg

        if avg >= 90:
            data["grade"] = "A+"
        elif avg >= 80:
            data["grade"] = "A"
        elif avg >= 70:
            data["grade"] = "B"
        elif avg >= 60:
            data["grade"] = "C"
        else:
            data["grade"] = "F"
    
    print("\nGrades calculated for all students.")

#display all students record function
def displayrecords():
    if not students:
        print("No student records available.")
        return
    
    for studentid, data in students.items():
        print(f"\nID: {studentid}")
        print(f"Name: {data['name']}")
        print(f"Marks: {data['marks']}")
        print(f"Average: {data['average']}")
        print(f"Grade: {data['grade']}")

#search a student record function
def searchrecord():
    studentid=input("Enter Student ID: ")
    if studentid not in students:
        print("\nSuch student id doesnt exit.")
        return
    else:
        data = students[studentid]
        print(f"\nName: {data['name']}")
        print(f"Marks: {data['marks']}")
        print(f"Average: {data['average']}")
        print(f"Grade: {data['grade']}")
    
    
#delete a student record function
def deleterecord():
    studentid = input("\nEnter Student ID to delete: ")
    if studentid in students:
        del students[studentid]
        print("Record deleted.")
    else:
        print("Student not found.")

#ranking function
def ranking():
    ranked = sorted(students.items(), key=lambda x: x[1]["average"], reverse=True)
    print("\nStudent Rankings:")
    for i, (studentid, data) in enumerate(ranked, 1):
        print(f"{i}. {data['name']} - {data['average']} ({data['grade']})")

#saving, loading data in file
def savedata():
    filename = "students_data.json"
    with open(filename, "w") as f:
        json.dump(students, f)
    print("Data saved successfully.")

    print("Loading data from file:")
    with open(filename, "r") as f:
        loaded_data = json.load(f)
    for sid, data in loaded_data.items():
        print(f"\n{sid}: {data}")

#main
while True:
    print("\n--------Welcome to Student's Academic Gradebook--------\n")
    print("1-Login")
    print("2-Create Account")
    print("3-Exit")

    choice = int(input("\nEnter option: "))
    match choice:
        case 1:
            if login():
                while True:
                    print("\n1-Add Student Record")
                    print("2-Enter Student Marks")
                    print("3-Grade Calculation")
                    print("4-Display All Students Record")
                    print("5-Search a Student Record")
                    print("6-Delete a Student Record")
                    print("7-Show Students Ranking")
                    print("8-Save and Load Data")
                    print("9-Logout")

                    choice2 = int(input("\nEnter option: "))
                    match choice2:
                        case 1:
                            addrecord()
                        case 2:
                            studentmarks()
                        case 3:
                            gradecal()
                        case 4:
                            displayrecords()
                        case 5:
                            searchrecord()
                        case 6:
                            deleterecord()
                        case 7:
                            ranking()
                        case 8:
                            savedata()
                        case 9:
                            print("\nLogging out...")
                            break
                        case _:
                            print("\nInvalid option")
        case 2:
            createaccount()
        case 3:
            print("\nYou have exited the student's academic gradebook!")
            sys.exit()
        case _:
            print("Invalid choice")
