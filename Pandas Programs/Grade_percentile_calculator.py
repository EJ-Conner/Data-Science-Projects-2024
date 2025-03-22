import pandas as pd
import numpy as np

grades_dict = {'Wally':[87, 96, 70], 'Eva':[100, 87, 90], 'Sam':[94, 77, 90], 'Katie':[100, 81, 82], 
               'Bob':[83, 65, 85]}

grades = pd.DataFrame(grades_dict)
grades.index = ['Test1', 'Test2', 'Test3']

percent_list = [20, 40, 60, 80]

def percentile_calc(grades: pd.DataFrame, percent_li: list[int]):
    
    percentiles = {}

    # percentile algorithm
    # index k is found by   
    # k = (N - 1) * (p / 100)
    # where k is the index, N is the number of elements and p is percentile
    # if k is not integer it can be expressed by: k - i + f
    # where i is the integer part (floor value) and f is the fractional part
    # percentile = value_1 + f * (value_2 - value_1)

    for x in grades.columns:
        student_grades = grades[x].values
        grades_sorted = np.sort(student_grades)
        N = len(grades_sorted)

        student_percentiles = {}

        for p in percent_li:
            #index k 
            k = (N - 1) * (p / 100)
            i = int(k)
            f = k - i

            if i < N - 1:
                # percentile = value_1 + f * (value_2 - value_1)
                p_value = grades_sorted[i] + f * (grades_sorted[i + 1] - grades_sorted[i])
            else:
                p_value = grades_sorted[i]
            
            student_percentiles[p] = p_value
        percentiles[x] = student_percentiles
    # convert to df
    percentiles_df = pd.DataFrame(percentiles)
    percentiles_df.index = ['20%', '40%', '60%', '80%']
    return percentiles_df

print(grades)
print(percentile_calc(grades, percent_list))

    
