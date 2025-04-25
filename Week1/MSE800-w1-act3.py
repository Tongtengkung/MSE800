import numpy as np
scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])

#Calculate and print the average score for each student.
average_score = np.mean(scores, axis=1)                                         #avg along axis1 (Row)
for std_no, avg_score in enumerate(average_score,start=1):
    print(f"Average score for student{std_no}: {avg_score:.1f} points")
print("\n")            

#Calculate and print the average score for each subject.
average_score2 = np.mean(scores, axis=0)                                         #avg along axis0 (Column)
for sbj_no, avg_score2 in enumerate(average_score2,start=1):
    print(f"Average score for subject{sbj_no}: {avg_score2:.1f} points")
print("\n")

#Identify the student (row index) with the highest total score.
highest_score = np.sum(scores, axis=1)
highest_point_student = np.argmax(highest_score)                                #reture max value to "highest_point_student"
print(f"The highest score student is {highest_point_student+1} with a point: {highest_score[highest_point_student]} points")
print("\n")

#Add 5 bonus points to the third subject for all students
third_sub_score = scores[:, 2]                                                  #select subject
third_sub_score += 5                                                            #plus 5 point and update into score 2D-array
print("Update scores")                                         
print(scores)