import numpy as np    
temperatures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

avg_temp = np.mean(temperatures)                              #AVG temp.
print(f"Average temperature: {avg_temp:.2f}°C")
print("\n")

lowest_temp = np.min(temperatures)                            #Lowest temp.
highest_temp = np.max(temperatures)                           #Highest temp.
print(f"Lowest temperature: {lowest_temp}°C")
print(f"Highest temperature: {highest_temp}°C")
print("\n")

fahrenheit = temperatures*9/5+32                              #Convert temp.
print("Fahrenheit temperature:")
for day_n,f_temp in enumerate(fahrenheit,start=1):
    print(f"Day{day_n} {f_temp:.2f}°C")
print("\n")

temp_over_20_degree = np.where(temperatures > 20)[1]          #Find the temp over 20 degrees
print("Temperature over 20°C:")
for day_n2 in temp_over_20_degree:
    d_temp = temperatures[day_n2]                             #Use the index to get the temperature value
    print(f"Day{day_n2 + 1}: {d_temp:.2f}°C")