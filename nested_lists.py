if __name__ == '__main__':
    students = []    
    for _ in range(int(input())):
        name = input()
        grade = float(input())
        students.append([name, grade])   
    unique_grades = sorted(set([grade for name, grade in students]))  
    second_lowest_grade = unique_grades[1]    
    second_lowest_students = [name for name, grade in students if grade == second_lowest_grade]    
    second_lowest_students.sort()   
    for student in second_lowest_students:
        print(student)
