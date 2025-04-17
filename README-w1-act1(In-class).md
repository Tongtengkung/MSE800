# MSE800
Activities 1 (in-class)
    I seperate for 5 sections by "enter"
        1.  import numpy as np    
            temperatures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])  help syntex

        2.  avg_temp = np.mean(temperatures)                            calculate average value from array and store in "avg_temp"
            print(f"Average temperature: {avg_temp:.2f}°C")             print value from "avg_temp" and using only 2 digits
            print("\n")                                                 press enter

        3.  lowest_temp = np.min(temperatures)                          store lowest value form array by using "np.min"
            highest_temp = np.max(temperatures)                         store Highest value form array by using "np.max"
            print(f"Lowest temperature: {lowest_temp}°C")               print value from "lowest_temp" with sentence
            print(f"Highest temperature: {highest_temp}°C")             print value from "highest_temp"with sentence
            print("\n")                                                 press enter

        4.  fahrenheit = temperatures*9/5+32                            create "fahrenheit" valuable from formula
            print("Fahrenheit temperature:")                            Loop printing value from "fahrenheit"
                for day_n,f_temp in enumerate(fahrenheit,start=1):          condition: create "day_n" for counting days (start from 1)
                print(f"Day{day_n} {f_temp:.2f}°C")                         and "f_temp" to print 2 digits of value following by index
            print("\n")                                                 press enter

        5.  temp_over_20_degree = np.where(temperatures > 20)[0]        search in array for finding value lower than 20 by using 
                                                                        "np.where" and using [0] because have only first element to use
            print("Temperature over 20°C:")                             Loop printing value from "temp_over_20_degree"
                for day_n2 in temp_over_20_degree:                          condition: create "day_n2" in "temp_over_20_degree"
                d_temp = temperatures[day_n2]                               and "d_temp" is a value from "temperatures" following by 
                                                                            "day_n2"
                print(f"Day{day_n2 + 1}: {d_temp:.2f}°C")               print 2 digits of over 20 degrees's day until finish



