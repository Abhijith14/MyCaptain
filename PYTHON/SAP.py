#School Administration Program

import csv

def write_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Class", "Division", "Register_no"])
        writer.writerow(info_list)




condition = True
Stud_no = 1
while(condition):
    student_info = input("Enter Student #{} Info: ".format(Stud_no))
    print("Entered info : " + student_info)

    #split
    student_info_list = student_info.split(' ')
    print("Entered Student Info;\nName: {}\nAge: {}\nClass: {}\nDivision: {}\nReg No: {}\n"
          .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3], student_info_list[4]))

    choice_check = input("Is the entered info correct (Y|N): ")
    if choice_check == "Y":
        write_csv(student_info_list)

        condition_check = input("Enter (Y/N) if you want to enter next student: ")
        if condition_check == "Y":
            condition = True
            Stud_no = Stud_no + 1
        elif condition_check == "N":
            condition = False
    else:
        print("Please Re-enter !!")

