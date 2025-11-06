stud = int(input("Enter number of students: "))
subj = int(input("Enter number of subjects: "))
class_score = 0
for i in range (1,stud + 1):
    total = 0
    print(f"Student {i}")
    for j in range (1, subj + 1):
        score = int(input(f"Enter score {j}: "))
        total += score
    stud_avg = total/subj
    print(f"Average for Student {i} = ", stud_avg)
    class_score += stud_avg
class_avg = class_score/stud
print(f"Class Average = ", class_avg)