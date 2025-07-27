import pandas as pd

data = {
    "Name":["Kamal","Sorav","Karan","Vikas","Chirag","Sahil","Sunny","Kaash","Gagan"],
    "Age":[20,22,23,23,21,20,23,18,18],
    "Course":["Btech","Bca","Btech","Btech","Btech","Bcom","Mtech","BE","Mba"],
    "Roll_no":[2231581,2231580,2231520,2231593,2231498,2231583,2231584,2231585,2231586],
    "Cgpa":[7.5,7,7,7.5,7,7,6,5,8]

}

df = pd.DataFrame(data)
df.to_csv("Student_data.csv",index=False)
df = pd.read_csv("Student_data.csv")

def show_menu():
    print("\n===== Student Result Management =====")
    print("1. Show All Student Data")
    print("2. Show Topper")
    print("3. Course-wise Average")
    print("4. Filter Passed Students (Cgpa >= 6)")
    print("5. Add New Student")
    print("6. Save & Exit")
    print("=====================================")

def add_new_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    roll_no = int(input("Enter Roll Number: "))
    cgpa = float(input("Enter CGPA: "))
    new_row = pd.DataFrame([[name, age, course, roll_no, cgpa]], columns=df.columns)
    return new_row



while True:
    show_menu()
    choice = input("Enter Your Choice\n")
    print("Choice entered: ", choice)

    if(choice == "1"):
        print(df)
    elif(choice == "2"):
        filtered_df = df.sort_values(by="Cgpa",ascending = False)
        print(filtered_df.head(1))
        print("Topper Student")
    elif(choice == "3"):
        filtered_df = df.groupby("Course")["Cgpa"].mean()
        print(filtered_df)
        print("Course-wise Average")
    elif(choice == "4"):
        filtered_df = df[df["Cgpa"]>6]
        print(filtered_df)
        print("Passed Student")
    elif(choice == "5"):
        new_row = add_new_student()
        df = pd.concat([df,new_row],ignore_index=True)
        df.to_csv("Student_data.csv",index=False)
        print("Added New Student")
        print(new_row)
    elif(choice == "6"):
        df.to_csv("Student_data.csv",index=False)
        print("Data Saved. Exit...")
        break
    else:
        print("Invalid Choice!")

        






