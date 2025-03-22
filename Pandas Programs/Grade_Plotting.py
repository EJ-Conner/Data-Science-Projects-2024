import pandas as pd
import matplotlib.pyplot as plt

grades_dict = {'Wally':[87, 96, 70], 'Eva':[100, 87, 90], 'Sam':[94, 77, 90], 'Katie':[100, 81, 82], 
               'Bob':[83, 65, 85]}

grades = pd.DataFrame(grades_dict)
grades.index = ['Test1', 'Test2', 'Test3']

x = grades.index


colors = ['red', 'green', 'blue']
linestyles = ['--', '-.', '-']
legend_labels = ['Test1', 'Test2', 'Test3']
for i in range(grades.shape[0]):
               plt.plot(grades.columns, grades.iloc[i],
                        marker='*', 
                        color=colors[i],
                        linestyle=linestyles[i],
                        label=legend_labels[i])


plt.ylim(0,100)
plt.xlabel('Student Names')
plt.ylabel('Grades')
plt.title('Student Grades')
plt.legend(loc='lower left')
plt.show()