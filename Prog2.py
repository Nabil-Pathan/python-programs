rno = input("Enter Roll no : ")
name = input("Enter Name : ")
marks = []
result = ""
student_class = ""

for i in range(6):
    subject_marks = int(input(f"Enter Marks of Subjet {i+1} : "))
    marks.append(subject_marks)

total = sum(marks)

failed_subjects = sum(marks < 35 for marks in marks)

if failed_subjects > 2:
    result = "FAIL"

elif failed_subjects <= 2 and failed_subjects > 0:
    result = "ATKT"  

else :
    result = "PASS"   

per = total / 6 


if per < 48:
    student_class = "PASS"

elif per >= 48 and per < 60:
    student_class = "second"  

elif per >= 60 and per < 70:
    student_class = "Third"  

elif per > 70 :
    student_class = "First" 

print("---------- Marksheet ------------")
print("Name ", name)
print("Roll No.  ", rno)
print("Total ", total)
print("Percantage ", per)
print("Result ", result)
print("Class ", student_class)





      



