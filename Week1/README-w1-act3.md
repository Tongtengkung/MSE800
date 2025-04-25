# MSE800
Activities 3
    I seperate for 5 sections by "enter"
        1.  import numpy as np                                                          import library "numpy"
            scores = np.array([                                                         create "scores" by 2D-array
                    [78, 85, 90],
                    [88, 79, 92],
                    [84, 76, 88],
                    [90, 93, 94],
                    [75, 80, 70]
            ])
        
        2.  average_score = np.mean(scores, axis=1)                                     calculate average value from array on each 
                                                                                        "row"(axis=1) and store in "average_score"
                for std_no, avg_score in enumerate(average_score,start=1):              Loop printing "average_score"                
                print(f"Average score for student{std_no}: {avg_score:.1f} points")         condition: create "std_no" for each student
                                                                                            (start from 1) and "avg_score" for printing 1 digit of point for each "student"
            print("\n")                                                                 press enter

        3.  average_score2 = np.mean(scores, axis=0)                                     calculate average value from array on each 
                                                                                        "column"(axis=0) and store in "average_score2"
                for sbj_no, avg_score2 in enumerate(average_score2,start=1):            Loop printing "average_score2"                
                print(f"Average score for student{std_no}: {avg_score2:.1f} points")        condition: create "sbj_no" for each subject
                                                                                            (start from 1) and "avg_score" for printing 1 digit of point for each "subject"
            print("\n")                                                                 press enter
        
        4.  highest_score = np.sum(scores, axis=1)                                      sum all "row" (axis=1) value from "scores" and 
                                                                                        store in "highest_score"
            highest_point_student = np.argmax(highest_score)                            reture maximum value index to 
                                                                                        "highest_point_stuent"
            print(f"The highest score student is {highest_point_student+1}              print value "highest_point_student"+1 (because
            with a point: {highest_score[highest_point_student]} points")               from index) with the sentence
            print("\n")                                                                 press enter

        5.  third_sub_score = scores[:, 2]                                              create "third_sub_score" value by select from
                                                                                        "scores" array (choose every row, second column)
            third_sub_score += 5                                                        increase value at "third_sub_score" by 5
            print("Update scores")                                                      print phase "Undate scores"
            print(scores)                                                               print new "scores" array