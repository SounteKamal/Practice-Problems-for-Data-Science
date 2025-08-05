import matplotlib.pyplot as plt

x = [1,2,3,4,5,3,4,2,1,6,9,7,0,8]
y = [10,20,15,25,30,10,40,50,60,40,80,70,90,60]

# Line chart/Line plot
# plt.plot(x,y,color="red")
# plt.title("Simple Line Plot")
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.grid(True)
# plt.show()

# # Bar Chart
# plt.bar(x,y,color="red")
# plt.title("Simple Line Plot")
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.grid(True)
# plt.show()

# # Scatter
# plt.scatter(x,y,color="blue",marker="*")
# plt.title("Simple Line Plot")
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.grid(True)
# plt.show()

# Histogram
# plt.hist(x,bins = 10,color="yellow",edgecolor = "black")
# plt.title("Simple Line Plot")
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.grid(True)
# plt.show()

# import matplotlib.pyplot as plt

# Data
# activities = ['Study', 'Sleep', 'Exercise', 'Entertainment', 'Others']
# hours = [8, 7, 2, 4, 3]

# # Plot
# plt.pie(hours, labels=activities, autopct='%1f%%', startangle=90,shadow=True)
# plt.title("Daily Time Distribution")
# plt.axis('equal')  # Make circle perfect
# plt.show()

# import matplotlib.pyplot as plt

# # Sample data
# x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
# y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]

# # Plot
# plt.scatter(x, y, color='blue')
# plt.title("Scatter Plot Example")
# plt.xlabel("X Values")
# plt.ylabel("Y Values")
# plt.grid(True)
# plt.show()


# import numpy as np

# x = np.random.randint(1, 100, 50)
# y = np.random.randint(1, 100, 50)

# plt.scatter(x, y, color='green')
# plt.title("Random Scatter Plot")
# plt.xlabel("Random X")
# plt.ylabel("Random Y")
# plt.show()

# Box plot
# import matplotlib.pyplot as plt

# # Sample marks of students
# data = [75, 88, 91, 65, 77, 86, 95, 55, 78, 89, 99, 100, 72]

# plt.boxplot(data)
# plt.title("Box Plot of Student Marks")
# plt.ylabel("Marks")
# plt.grid(True)
# plt.show()


# math_scores = [72, 78, 80, 65, 90, 100, 88, 92]
# science_scores = [70, 75, 85, 80, 60, 95, 98, 89]

# data = [math_scores, science_scores]

# plt.boxplot(data, labels=['Math', 'Science'])
# plt.title("Subject-wise Score Distribution")
# plt.ylabel("Scores")
# plt.grid(True)
# plt.show()

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 25, 30, 40]   # Line chart layi
y2 = [5, 10, 15, 20, 25]    # Bar chart layi
plt.subplot(1, 2, 1)   # 1 row, 2 columns, chart 1
plt.plot(x, y1, color='green')
plt.title("Line Chart")

plt.subplot(1, 2, 2)   # 1 row, 2 columns, chart 2
plt.bar(x, y2, color='orange')
plt.title("Bar Chart")

# plt.tight_layout()    # Layout nu clean banayi da
plt.show()
