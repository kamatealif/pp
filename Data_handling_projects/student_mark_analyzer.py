def get_student_info():
    student = {}
    while True: 
        name = input("Enter the name : ")

        if name == 'done':
            break
        if name in student:
            print("Name already exists")
            continue
    
        try:
            marks = float(input(f"Enter the marks {name} : "))
            student[name]  = marks
        except ValueError:
            print("Invalid input. Please enter a number.")

    return student;

def display_report(student):
    if not student:
        print("No student information available.")
        return 
    
    marks = list(student.values())
    min_marks = min(marks)
    max_marks = max(marks)
    total_marks = sum(marks)
    average_marks = sum(marks) / len(marks)
    topper = [name for name, score in student.items() if score == max_marks]
    loser = [name for name, score in student.items() if score == min_marks]

    print("-" * 40)
    print("Report:")
    print(f"Total number of students: {len(student)}")
    print(f"Minimum marks: {min_marks}")
    print(f"Maximum marks: {max_marks}")
    print(f"Average marks: {average_marks:.2F}")
    print(f"Topper: {" ".join(topper)}")
    print(f"Loser: {" ".join(loser)}")


student = get_student_info()
display_report(student)
