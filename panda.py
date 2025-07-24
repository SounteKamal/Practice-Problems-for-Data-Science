import pandas as pd

# data = [10,20,30,40,50]
# series = pd.Series(data)
# print(series)

# marks = pd.Series([85, 90, 75], index = ["Math", "Science","English" ])
# print(marks)
# print(marks["Math"])

# print(marks + 5)
# print((marks > 80))

# fruits = pd.Series([50,25,60], index=["Apple", "Banana", "Mango"])
# print(fruits["Mango"])
# print(fruits + 10)

# data = {
#     "Name": ["Kamal", "Karan", "Vikas"],
#     "Age": [25, 30, 35],
#     "City": ["Aulakh", "Amritsar", "Batala"]
# }

# df = pd.DataFrame(data)
# print(df)
# print(df["Name"])
# print(df.loc[0])  # Accessing the first row 
# print(df.iloc[1])  # Accessing the second row by index
# print(df.iloc[0:2,:2])  # Accessing the first two rows
# df["Country"] = ["India", "India", "India"]  # Adding a new column
# print(df)

# print(df.shape)
# print(df.describe())  # Summary statistics of the DataFrame
# print(df.info())# Information about the DataFrame

# data = {
#     "Student": ["Kamal", "Karan", "Vikas"],
#     "Marks": [25, 30, 35],
#     "Subject": ["Science","Science","Science"],}
# df = pd.DataFrame(data)
# print(df)

# df["Grade"] = ["C", "B", "A"]  # Adding a new column
# print(df)

# print(df["Marks"])

# print(df.iloc[1])

# Topic 3 : Dataframe Selection and Indexing and Filtering

# data = {
#     "Name": ["Kamal", "Karan", "Vikas"],
#     "Age": [25, 30, 35],
#     "City": ["Aulakh", "Amritsar", "Batala"],
#     "Marks": [85, 90, 75]
# }

# df = pd.DataFrame(data)
# print(df)
# print(df["Name"])  # Accessing the "Name" column
# print(df.loc[0])  # Accessing the first row
# print(df.iloc[1])  # Accessing the second row by index
# print(df.iloc[0:2, :2])  # Accessing the first two rows
# print(df[df["Age"] > 28])  # Filtering rows where Age is greater than 28
# print(df[df["Marks"] > 80])  # Filtering rows where Marks are greater than 80


# Topic 4 : Dataframe Conditional Selection and Filtering

# data  = {
#     "Name": ["Kamal", "Karan", "Vikas"],
#     "Age": [25, 30, 35],
#     "City": ["Aulakh", "Amritsar", "Batala"],
#     "Marks": [85, 90, 75]
# }

# df = pd.DataFrame(data)
# print(df[(df["Marks"] > 80) & (df["Age"] < 35)])  # Filtering rows where Marks are greater than 80 and Age is less than 35])
      

# print(df[df['Marks'].between(70,80)])



# Topic 5: DataFrame Sorting and Statistical Summaries in Pandas

# data  = {
#     "Name": ["Kamal", "Karan", "Vikas"],
#     "Age": [25, 30, 35],
#     "City": ["Aulakh", "Amritsar", "Batala"],
#     "Marks": [85, 90, 75]
# }

# df = pd.DataFrame(data)
# print(df.sort_values(by= "Marks"))
# # print(df.sort_index())
# print(df.sort_values(by="Marks", ascending=False))


# data  = {
#     "Name": ["Kamal", "Karan", "Vikas"],
#     "Age": [25, 30, 35],
#     "City": ["Aulakh", "Amritsar", "Batala"],
#     "Marks": [85, 90, 75]
# }

# df = pd.DataFrame(data)
# print(df.describe())
# print(df["Marks"].min())
# print(df["Marks"].median())
# print(df["Marks"].mean())
# print(df["Marks"].max())
# print(df["Marks"].std())
# print(df["Marks"].var())


# data = {
#     "Name": ["Kamal", "Preet", "Kamal", "Vikas", "Preet"],
#     "Stream": ["Sci", "Arts", "Sci", "Commerce", "Arts"],
#     "Marks": [85, 80, 75, 80, 95]
# }
# df = pd.DataFrame(data)

# # Count how many times each Stream appears
# print(df["Stream"].value_counts())

# # Count how many times each Name appears
# print(df["Name"].value_counts())

# # Count how many times each Marks appears
# print(df["Marks"].value_counts())


# Practice Problems for Sorting and Statistical Summaries

# # Q1
# data = {
#     "Name": ["Kamal", "Preet", "Kamal", "Vikas"],
#     "Score": [85, 80, 75, 90],
#     "Age": [25, 30, 35, 28]
# }

# df = pd.DataFrame(data)

# print(df.sort_values(by="Score"))  # Sorting by Score in descending order
# print(df.sort_values(by="Age", ascending=False))  # Sorting by Age in descending order



# # Q2
# data = [12,45,67,23,89,90]
# df = pd.Series(data)
# print(df.mean())
# print(df.max())  # Summary statistics of the Series
# print(df.min())  # Summary statistics of the Series
# print(df.std())  # Summary statistics of the Series

# Q3
# data = {
#     "Product": ["A", "B", "C", "D", "E"],
#     "Category" : ["Phone", "Laptop", "Phone", "Laptop", "Tablet"],
#     "Price": [12000,55000,15000,60000,30000]
# }

# df = pd.DataFrame(data)
# print(df["Category"].value_counts())  # Count how many times each Category appears
# print(df["Price"].mean())

# Q4

# data = {
#     "Name": ["Kamal", "Sounte", "Chirag", "Vikas", "Karan","Deepjyot","Sahil"],
#     "Marks": [85, 80, 75, 80, 95, 50, 99]
# }
# df = pd.DataFrame(data)
# print(df.describe())

# data = [45, 75, 88, 62, 90, 100, 49]
# df = pd.Series(data)
# map = df.mean()
# print(map)
# print(df[df > map])  # Filtering Series to show values greater than the mean


# Q6
# data = {
#     "City": ["Delhi", "Delhi", "Mumbai", "Mumbai", "Kolkata", "Kolkata"],
#     "Temperature": [34, 36, 32, 33, 30, 31]
# }

# df = pd.DataFrame(data)
# print(df.groupby("City")["Temperature"].mean())  # Grouping by City and calculating the mean temperature

# Q7
# data = {
#     "Name": ["Kamal", "Preet", "Vikas", "Sounte", "Deep"],
#     "Department": ["IT", "HR", "IT", "HR", "Finance"],
#     "Salary": [50000, 60000, 55000, 58000, 70000]
# }
# df = pd.DataFrame(data)
# print(df.groupby("Department")["Salary"].mean())



# Q8
# data = {
#     "Student": ["A", "B", "C", "D", "E"],
#     "Class": [10, 10, 12, 12, 10],
#     "Maths": [80, 85, 90, 70, 60],
#     "Science": [75, 80, 95, 65, 55]
# }

# df = pd.DataFrame(data)

# print(df.groupby("Class")[["Maths","Science"]].mean())



# Q9
# data = {
#     "Department": ["IT", "HR", "IT", "HR", "Finance", "IT"],
#     "Salary": [50000, 60000, 52000, 58000, 70000, 53000]
# }
# df = pd.DataFrame(data)
# print(df.groupby("Department")["Salary"].sum())  # Grouping by Department and calculating the total salary
# print(df.groupby("Department")["Salary"].mean()) 

# Practice Problems
# Q1

# data = {
#     "Name": ["Aman", "Simran", "Raj", "Jaspreet", "Tina"],
#     "Age": [22, 20, 25, 23, 21],
#     "Marks": [88, 76, 90, 65, 70],
#     "City": ["Amritsar", "Ludhiana", "Jalandhar", "Amritsar", "Bathinda"]
# }

# df = pd.DataFrame(data)

# print(df.head())


# Q1
# data = [45, 75, 88, 62, 90, 100, 49]
# df = pd.Series(data)
# mean_val = df.mean()
# print(mean_val)
# print(df[df > mean_val])

# Q2
# data = {
#     "Name": ["Aman", "Babli", "Chetan", "Dolly"],
#     "Age": [22, 24, 23, 25],
#     "Marks": [85, 91, 76, 88]
# }

# df = pd.DataFrame(data)
# print(df[df["Marks"] > 80])

# df["Passed"] = ["Yes","Yes","No","Yes"]
# print(df)


# Q3
# data = {
#     "Product": ["Pen", "Notebook", "Pen", "Notebook", "Pen"],
#     "Price": [10, 40, 15, 35, 12],
#     "Units": [3, 2, 2, 1, 5]
# }
# df = pd.DataFrame(data)
# df["Total"] = df["Price"] * df["Units"]

# print(df.groupby("Product")[["Total" , "Price", "Units"]].sum())
# print(df["Total"])


# # Q4
# data = {
#     "City": ["Delhi", "Mumbai", "Chennai", "Delhi", "Mumbai", "Chennai"],
#     "Year": [2020, 2020, 2020, 2021, 2021, 2021],
#     "Sales": [250, 300, 200, 280, 320, 210]
# }
# df = pd.DataFrame(data)
# print(df.groupby("City")["Sales"].mean())
# print(df.groupby("Year")["Sales"].sum())
# print(df.groupby(["City" , "Year"])["Sales"].max().unstack())


# # Q5

# data = {
#     "Company": ["Tata", "Tata", "Infosys", "Infosys", "TCS", "TCS", "Tata", "TCS"],
#     "Year": [2021, 2022, 2021, 2022, 2021, 2022, 2023, 2023],
#     "Revenue": [100, 150, 120, 180, 130, 170, 160, 190],
#     "Profit": [20, 35, 25, 40, 30, 45, 38, 50]
# }

# df = pd.DataFrame(data)
# print(df.groupby("Company")[["Revenue" , "Profit"]].sum())
# print(df[(df["Company"] == "TCS") & (df["Revenue"] > 150)] )
# print(df.groupby("Year")["Profit"].mean())

# df["Profit Margin(%)"] = ((df.Profit/df.Revenue) * 100) 
# print(df)

# print(df.sort_values(by="Profit Margin(%)",ascending = False))

# # Q6

# data = {
#     "Name": ["Aman", "Babli", "Chetan", "Dolly", "Esha"],
#     "Marks": [88, 75, 92, 85, 92],
#     "Age": [21, 22, 20, 23, 21]
# }

# df = pd.DataFrame(data)
# print(df)

# sorted_df = (df.sort_values(by=["Marks","Age"],ascending = (False,True)))

# print(sorted_df)


# Q7

# data = {
#     "Name": ["Aman", "Babli", "Chetan", "Dolly", "Esha"],
#     "Marks": [88, 75, 92, 85, 92],
#     "Age": [21, 22, 20, 23, 21]
# }

# df = pd.DataFrame(data)

# # Q1: Show only those students who scored more than 85
# # Q2: Show students who are 21 years old AND have marks >= 85
# # Q3: Add a column "Result" -> "Pass" if marks >= 80 else "Fail"
# # Q4: Show only the students who Failed


# print(df[df["Marks"] > 85])

# print(df[(df["Age"] == 21) & (df["Marks"] >=85)])

# df["Result"] = df["Marks"].apply(lambda x :"Pass"  if x>=80 else "Fail")
# print(df)


# print(df[df["Result"] == "Fail"])

# Filtered_df= df[(df["Result"] == "Pass")]
# Sorted_df = Filtered_df.sort_values(by ="Marks",ascending = False)
# print(Sorted_df.head(2))

# Q8


# data = {
#     "Name": ["Aman", "Babli", "Chetan", "Dolly", "Esha", "Farah", "Gagan"],
#     "Subject": ["Math", "English", "Math", "Science", "English", "Math", "Science"],
#     "Marks": [88, 75, 92, 85, 91, 66, 78]
# }

# df = pd.DataFrame(data)

# # 🔶 Task 1: Filter students who have either "Math" or "Science" as subject using isin()

# # 🔶 Task 2: From above result, show only those with Marks > 80

# # 🔶 Task 3: Add a new column "Grade" using lambda:
# #            >=90 -> "A"
# #           80-89 -> "B"
# #           else  -> "C"

# # 🔶 Task 4: Show top 2 "Math" students based on Marks (descending)

# filtered_result = (df[df["Subject"].isin(["Math","Science"])])

# print(filtered_result[filtered_result["Marks"] > 80])

# df["Grade"] = df["Marks"].apply(lambda x : "A" if x>=90 else("B"if ((80<= x<=89)) else "C") )
# print(df)

# filtered_result1 = (df[df["Subject"].isin(["Math"])])
# sorted_data = filtered_result1.sort_values(by = "Marks",ascending = False)
# print(sorted_data.head(2))


# Q9


# data = {
#     "Student": ["Aman", "Babli", "Aman", "Dolly", "Esha", "Chetan"],
#     "Subject": ["Math", "Math", "Science", "Math", "Science", "Science"],
#     "Marks": [85, 78, 90, 88, 95, 70]
# }

# df = pd.DataFrame(data)
# print(df)


# print(df.pivot_table(index = "Subject" , values = "Marks" , aggfunc = "mean"))

# print(df.pivot_table(index="Subject",values = "Student",aggfunc = "count"))


# Q10

# import pandas as pd

# data = {
#     "Student": ["Aman", "Babli", "Chetan", "Dolly", "Esha", "Aman", "Babli", "Chetan", "Dolly", "Esha"],
#     "Subject": ["Math", "Math", "Math", "Math", "Math", "Science", "Science", "Science", "Science", "Science"],
#     "Marks": [88, 75, 92, 85, 92, 91, 78, 85, 89, 95]
# }

# df = pd.DataFrame(data)

# print(df.pivot_table(index="Subject",values = "Marks",aggfunc="mean"))

# print(df.pivot_table(index="Student",values = "Marks",aggfunc="sum"))

# print(df.pivot_table(index="Student",values ="Subject",aggfunc="count"))

# print(df.pivot_table(index="Student",columns="Subject",values = "Marks",aggfunc ="mean"))

# df["Grade"] = df["Marks"].apply(lambda x : "A" if x>=90 else("B" if (80<=x<=89) else "C"))
# print(df.pivot_table(index="Subject",columns = "Grade",values = "Student" , aggfunc = "count"))


# print(df.pivot_table(index="Subject",values="Marks",aggfunc="max"))

# print(df.pivot_table(index="Grade",columns = "Subject",values="Student",aggfunc="count"))

# print(df.pivot_table(index="Grade", columns="Subject", values="Student", aggfunc="count", margins=True))


# Topic: Missing Values


# import pandas as pd
# import numpy as np

# data = {
#     "Name": ["Aman", "Babli", "Chetan", np.nan],
#     "Age": [21, 22, np.nan, 24],
#     "Marks": [88, np.nan, 92, 85]
# }

# df = pd.DataFrame(data)

# print(df.isnull())
# print(df.isnull().sum())

# df["Name"].fillna("NoName",inplace = True)
# df["Age"].fillna(df["Age"].mean(),inplace=True)
# df["Marks"].fillna(df["Marks"].median(),inplace=True)

# print(df)
# print(df.isnull().sum())

# Topic: Duplicated and drop_Duplicates

# import pandas as pd

# data = {
#     "Name": ["Aman", "Babli", "Chetan", "Aman", "Babli", "Deepak"],
#     "Marks": [90, 85, 92, 90, 85, 88]
# }

# df = pd.DataFrame(data)

# print(df.duplicated())

# print(df.duplicated().sum())

# df1 = pd.DataFrame(df.drop_duplicates())
# print(df1)

# print(df.drop_duplicates(subset="Name",keep="first"))

# print(df.drop_duplicates(subset="Name",keep="last"))

# print(df1["Name"].count())

# Topic: Sorting and Ranking in Pandas

# data = {
#     "Name": ["Aman", "Babli", "Chetan", "Divya", "Esha"],
#     "Marks": [88, 92, 75, 95, 85]
# }
# df = pd.DataFrame(data)

# # 1. Sort the DataFrame by Marks in ascending order.
# # 2. Sort by Marks in descending order.

# print(df.sort_values(by="Marks"))
# print(df.sort_values(by="Marks",ascending = False))


# data = {
#     "Name": ["Aman", "Babli", "Chetan", "Divya", "Esha"],
#     "Marks": [88, 92, 88, 95, 88],
#     "Age": [20, 19, 21, 18, 22]
# }
# df = pd.DataFrame(data)
# # 1. First sort by Marks, then by Age.
# # 2. Sort Marks descending and Age ascending.

# print(df.sort_values(by = ["Marks","Age"]))
# print(df.sort_values(by = ["Marks","Age"],ascending = [False,True]))

# data = {
#     "Name": ["Aman", "Babli", "Chetan"],
#     "Marks": [88, 92, 75]
# }
# df = pd.DataFrame(data)
# # 1. Set Name as index and then sort index alphabetically.
# # 2. Try sorting index in reverse.

# print(df["Name"].sort_index())
# print(df.sort_index(ascending = False))


# data = {
#     "Student": ["A", "B", "C", "D", "E"],
#     "Score": [90, 85, 95, 80, 85]
# }
# df = pd.DataFrame(data)

# # 1. Rank in ascending order
# # 2. Rank in descending order

# print(df.rank())
# print(df.rank(ascending=False))


# data = {
#     "Player": ["Virat", "Rohit", "Rahul", "Hardik", "Rishabh"],
#     "Runs": [78, 102, 89, 78, 90]
# }
# df = pd.DataFrame(data)
# # 1. Use `method='min'` and `method='dense'`
# # 2. Rank in descending order

# print(df.rank(method="min"))
# print(df.rank(method="dense"))
# print(df.rank(ascending=False))



# data = {
#     "Student": ["Aman", "Babli", "Chetan", "Divya", "Esha"],
#     "Marks": [92, 88, 75, 95, 85]
# }
# df = pd.DataFrame(data)
# # 1. Apply percentage rank using `pct=True`

# print(df.rank(pct=True))



# data = {
#     "Employee": ["John", "Karan", "Lily", "Aditi", "Raj"],
#     "Sales": [2000, 1800, 2000, 1500, 1800]
# }
# df = pd.DataFrame(data)
# # 1. Sort by Sales descending.
# # 2. Then assign rank to each using `dense` method.

# sorted_df = df.sort_values(by="Sales",ascending=False)
# print(sorted_df.rank(method="dense"))


# Topic: Concatenation

# import pandas as pd

# df1 = pd.DataFrame({
#     'Name': ['Aman', 'Babli'],
#     'Marks': [85, 90]
# })

# df2 = pd.DataFrame({
#     'Name': ['Chetan', 'Divya'],
#     'Marks': [88, 95]
# })
# result = pd.concat([df1, df2])
# result1 = pd.concat([df1, df2],ignore_index=True)
# print(result)
# print(result1)

# df1 = pd.DataFrame({'A': [1, 2]})
# df2 = pd.DataFrame({'B': [3, 4]})

# result = pd.concat([df1, df2],axis=1)
# print(result)

# result = pd.concat([df1, df2], keys=["First", "Second"])
# print(result)

# Q1

# df1 = pd.DataFrame({
#     "Name": ["Aman", "Babli"],
#     "Marks": [85, 90]
# })

# df2 = pd.DataFrame({
#     "Name": ["Chetan", "Divya"],
#     "Marks": [88, 95]
# })

# df3 = pd.DataFrame({
#     "Age": [21, 22]
# })


# print(pd.concat([df1,df2]))

# print(pd.concat([df1,df2],ignore_index=True))


# print(pd.concat([df1,df3],axis=1))

# print(pd.concat([df1,df2,df3],axis=1))

# result = (pd.concat([df1,df2],keys=["First","Second"]))

# print(result.loc["Second"])


# jan = pd.DataFrame({"Product": ["A", "B"], "Sales": [100, 150]})
# feb = pd.DataFrame({"Product": ["A", "B"], "Sales": [110, 130]})
# mar = pd.DataFrame({"Product": ["A", "B"], "Sales": [120, 140]})

# result = pd.concat([jan,feb,mar],keys=["jan","feb","mar"])
# print(result)

# print(result.loc["feb"])



# import pandas as pd

# data = {
#     "Region": ["North", "South", "East", "West", "North", "South", "East", "West"],
#     "Salesperson": ["Aman", "Babli", "Chetan", "Divya", "Esha", "Farhan", "Gaurav", "Heena"],
#     "Sales": [2500, 3000, 1800, 2200, 2700, 3200, 1600, 2100],
#     "Units Sold": [12, 15, 10, 13, 11, 16, 9, 12]
# }

# df = pd.DataFrame(data)

# print(df.groupby(["Region"])["Sales"].sum())

# print(df.groupby(["Region"])["Units Sold"].mean())

# print(df.groupby(["Region"])["Salesperson"].count())

# print(df.groupby("Region").agg({"Sales":"sum","Units Sold":"mean"}))


# Topic: Merge


# employees = pd.DataFrame({
#     'EmpID': [101, 102, 103],
#     'Name': ['Raj', 'Simran', 'Amit']
# })

# departments = pd.DataFrame({
#     'EmpID': [101, 103, 104],
#     'Dept': ['HR', 'Finance', 'IT']
# })

# # TODO: Merge karke full outer join karo

# outer = pd.merge(employees,departments,on='EmpID',how='outer')
# print(outer)

# df1 = pd.DataFrame({
#     'EmpID': [1, 2, 3],
#     'Dept': ['HR', 'IT', 'Finance'],
#     'Salary': [50000, 60000, 70000]
# })

# df2 = pd.DataFrame({
#     'EmpID': [1, 2, 3],
#     'Dept': ['HR', 'Finance', 'Finance'],
#     'Bonus': [5000, 3000, 7000]
# })

# # 👉 TASK: Merge df1 and df2 on EmpID and Dept using inner join
# merged = pd.merge(df1,df2,on=['EmpID','Dept'],how='inner')

# merged_left = pd.merge(df1,df2,on='EmpID',how='left')

# merged_right = pd.merge(df1,df2,on='EmpID',how='right')

# print(merged)
# print(merged_left)
# print(merged_right)


# Topic: Reshaping Data with melt,stack,unstack

# df = pd.DataFrame({
#     "Name": ["Raj", "Simran"],
#     "English": [85, 87],
#     "Hindi": [78, 80],
#     "Punjabi": [92, 90]
# })

# melted = pd.melt(df,id_vars="Name",var_name = "Subject",value_name = "Marks")
# print(melted)


# data = {
#     'Store': ['Store A', 'Store B', 'Store C'],
#     'Jan': [2500, 3000, 2200],
#     'Feb': [2700, 3100, 2100],
#     'Mar': [2600, 3050, 2300]
# }

# df = pd.DataFrame(data)
# df.set_index('Store', inplace=True)
# print("Original Data:\n", df)

# stacked = df.stack()
# print(stacked)


# unstacked = stacked.unstack()
# print(unstacked)

# clean = stacked.reset_index()
# clean.columns = ['Store','Month','Sales']
# print(clean)
# print(clean.columns)

# Q1

# df = pd.DataFrame({
#     "Student": ["Aman", "Babli", "Chetan"],
#     "Math": [85, 90, 88],
#     "English": [78, 92, 81],
#     "Science": [89, 85, 91]
# })
# melted = pd.melt(df,id_vars = "Student",var_name= "Subject",value_name="Marks")
# print(melted)

# df = pd.DataFrame({
#     "Product": ["Mobile", "Laptop", "Tablet"],
#     "Jan": [10000, 20000, 15000],
#     "Feb": [11000, 19000, 16000],
#     "Mar": [12000, 21000, 17000]
# })

# melted = pd.melt(df,id_vars="Product",var_name="Month",value_name="Sales")
# print(melted)


# Topic:
