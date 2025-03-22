import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

grade_list = []
grade = 0
while grade >= 0:
    grade = float(input("Enter a grade (- number to stop): "))
    if grade < 0:
        break
    else:
        grade_list.append(grade)

grades_Arr = np.array(grade_list)

grades = pd.Series(grades_Arr)


A = len(grades[(grades >= 90)])
B = len(grades[(grades >= 80) & (grades < 90)])
C = len(grades[(grades >= 70) & (grades < 80)])
D = len(grades[(grades >= 60) & (grades < 70)])
F = len(grades[(grades < 60)])

grades_pie = [A,B,C,D,F]

labels_pie = ['A', 'B', 'C', 'D', 'F']

plt.pie(grades_pie, labels=labels_pie, colors=('r','g','b','y','m'), startangle=90, autopct='%1.1f%%', explode=(0,0,0,0,.1), shadow=True)

plt.title('Grades') 
plt.show()