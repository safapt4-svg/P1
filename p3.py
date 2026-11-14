# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# df = pd.read_csv(r"C:\Users\dell\Downloads\student_marks.csv")
# print("Student Dataset")
# print(df)
# print("\nSummary Statistics")
# print(df.describe())
# # NumPy Calculations
# math = np.array(df["Math"])
# science = np.array(df["Science"])
# english = np.array(df["English"])
# computer = np.array(df["Computer"])

# print("\nNumPy Calculations")
# print("Average Math Marks:", np.mean(math))
# print("Highest Science Mark:", np.max(science))
# print("Lowest English Mark:", np.min(english))
# print("Lowest Computer Mark:", np.min(computer))
# # Total and Percentage
# df["Total"] = df[["Math", "Science", "English","Computer"]].sum(axis=1)
# df["Percentage"] = df["Total"] / 400 * 100
# print("\nUpdated Dataset")
# print(df)
# # Bar Chart
# plt.figure(figsize=(6,4))
# plt.bar(df["Student"],df["Science"])
# plt.title("Science Marks")
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.show()

#   Pie Chart
# subject_totals = [
#     df["Math"].sum(),
#     df["Science"].sum(),
#     df["English"].sum(),
#     df["Computer"].sum()
# ]

# subjects = ["Math", "Science", "English","Computer"]

# plt.figure(figsize=(5,5))
# plt.pie(subject_totals,
#         labels=subjects,
#         autopct="%1.1f%%",
#         startangle=90)
# plt.title("Subject-wise Total Marks")
# plt.show()

# # Line Chart
# plt.figure(figsize=(6,4))
# plt.plot(df["Student"], df["Percentage"], marker="o")
# plt.title("Student Percentage")
# plt.xlabel("Students")
# plt.ylabel("Percentage")
# plt.grid(True)
# plt.show()

# # Histogram
# plt.figure(figsize=(6,4))
# plt.hist(df["Math"], bins=5)
# plt.title("Distribution of Math Marks")
# plt.xlabel("Marks")
# plt.ylabel("Frequency")
# plt.show()

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# df = pd.read_csv(r"C:\Users\dell\Downloads\ipl_practice_dataset_200_rows.csv")
# print("IPL Dataset")
# print(df)
# print("\nSummary Statistics")
# print(df.describe())
# print("Average Runs :", np.mean(df["Runs"]))
# print("Highest Score :", np.max(df["Runs"]))
# print("Lowest Score :", np.min(df["Runs"]))
# wins = df["Winner"].value_counts()
# print(wins)
# plt.figure(figsize=(10,5))
# plt.bar(wins.index, wins.values)
# plt.title("Matches Won by Teams")
# plt.xlabel("Teams")
# plt.ylabel("Number of Wins")
# plt.show()