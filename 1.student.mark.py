def input_student_info():
    students = []
    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student Name: ")
        student_dob = input("Enter date of birth (DD-MM-YYYY): ")
        students.append({'ID': student_id, 'Name': student_name, 'DOB': student_dob})
    return students

def input_course_info():
    courses = []
    while True:
        try:
            num_courses = int(input("Enter the number of courses: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses.append({'ID': course_id, 'Name': course_name})
    return courses

def input_student_marks(courses, students):
    marks = []
    while True:
        course_id = input("Enter course ID for marks: ")

        if any(course['ID'] == course_id for course in courses):
            break
        else:
            print("Invalid course ID. Please try again.")

    for student in students:
        student_name = student['Name']
        while True:
            try:
                mark = float(input(f"Enter marks for {student_name} in {course_id}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for marks.")

        marks.append({'StudentID': student['ID'], 'CourseID': course_id, 'Mark': mark})
    return marks

def display_student_info(students):
    print("\n== Student Information ==")
    for student in students:
        print(f"ID: {student['ID']}")
        print(f"Name: {student['Name']}")
        print(f"Date of Birth: {student['DOB']}")

def display_course_details(courses):
    print("\n== Course Details ==")
    for course in courses:
        print(f"ID: {course['ID']}")
        print(f"Name: {course['Name']}")

def display_student_performance(marks, courses, students):
    print("\n== Student Performance ==")
    for course in courses:
        course_id = course['ID']
        print(f"\nCourse ID: {course_id}")
        print(f"Course Name: {course['Name']}")
        print("\nStudent Marks:")
        for student in students:
            student_id = student['ID']
            student_name = student['Name']
            mark_entry = next((mark['Mark'] for mark in marks if mark['StudentID'] == student_id and mark['CourseID'] == course_id), None)
            if mark_entry is not None:
                print(f"\nStudent ID: {student_id}")
                print(f"Name: {student_name}")
                print(f"Score: {mark_entry}")
            else:
                print(f"\nStudent ID: {student_id}")
                print(f"Name: {student_name}")
                print("Score: Not available")

students_data = []
courses_data = []
marks_data = []

while True:
    print("\nChoose your option:")
    print("1. Input Student Information")
    print("2. Input Course Information")
    print("3. Input Marks for selected course")
    print("4. Display Student Information")
    print("5. Display Course Information")
    print("6. Display Student Marks")
    print("0. Exit")

    user_choice = input("Enter your choice (0-6): ")

    if user_choice == "1":
        students_data = input_student_info()
    elif user_choice == "2":
        courses_data = input_course_info()
    elif user_choice == "3":
        if students_data and courses_data:
            marks_data.extend(input_student_marks(courses_data, students_data))
        else:
            print("Please enter student and course information first.")
    elif user_choice == "4":
        if students_data:
            display_student_info(students_data)
        else:
            print("Please enter student information first.")
    elif user_choice == "5":
        if courses_data:
            display_course_details(courses_data)
        else:
            print("Please enter course information first.")
    elif user_choice == "6":
        if students_data and courses_data and marks_data:
            display_student_performance(marks_data, courses_data, students_data)
        else:
            print("Please enter student and course information and marks first.")
    elif user_choice == "0":
        break
    else:
        print("Enter a number between 0 and 6.")
