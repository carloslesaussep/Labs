import pandas as pd


### Data understanding:

#1
df = pd.read_csv("C:/Users/carlo/Downloads/nba.csv")
#2
df_five = df[:6][:]
#3
print(df.shape)
#4
print(df.columns)

### Data understanding:
#5, 6, and 7 - 458 total entries but onle 446 registered in salaries andconsidered as non null
print("Info in salary variable:")
print(df["Salary"].info())
print("Missing Salaries: ")
print(df["Salary"].isnull().sum())

print("Salary data will be cleansed...")
df_cl_sal = df.dropna(subset = ["Salary"])
print("Info in salary variable after cleanse:")
print(df_cl_sal["Salary"].info())
print("Missing Salaries after cleanse: ")
print(df_cl_sal["Salary"].isnull().sum())

#8
print("Info in College variable:")
print(df_cl_sal["College"].info())
print("Missing Colleges: ")
print(df_cl_sal["College"].isnull().sum())
print("College data will be updated to 'Unknown' if null: ")
df_cl_sal["College"] = df_cl_sal["College"].fillna("Unknown")
df_cl_sal_col = df_cl_sal
print("Info in College variable after cleanse:")
print(df_cl_sal_col["College"].info())
print("Missing Colleges after cleanse: ")
print(df_cl_sal_col["College"].isnull().sum())

#filtering data:
#9
print("Celtics players: ")
print(df_cl_sal_col[df_cl_sal_col["Team"] == "Celtics"])

#10
print("Players over 30: ")
print(df_cl_sal_col[df_cl_sal_col["Age"] > 30])

#11
print("Registered Point Guards: ")
print(df_cl_sal_col[df_cl_sal_col["Position"] == "PG"])

#12
print("Players with a salary over 50M: ")
print(df_cl_sal_col[df_cl_sal_col["Salary"] > 5000000])

#Sorting
#13
top_1_salary = df_cl_sal_col.sort_values(by = "Salary", ascending = False)
print("top 1st highest paid player: ")
print(top_1_salary.head(1))      

#14
top_1_age = df_cl_sal_col.sort_values(by = "Age", ascending = False)
print("Oldest player: ")
print(top_1_age.head(1))      

#Group By
#15
gp_salary_per_team = df_cl_sal_col.groupby("Team")["Salary"].mean().reset_index(name='Mean Salary')
print(gp_salary_team.sort_values(by = "Mean Salary", ascending = False))

#16
gp_players_per_team = df_cl_sal_col.groupby("Team")["Name"].count().reset_index(name='Players per Team')
print(gp_players_per_team.sort_values(by = "Players per Team", ascending = False))

#17
gp_maxsalary_per_team = df_cl_sal_col.groupby("Team")["Salary"].max().reset_index(name='Max Salary')
print(gp_maxsalary_per_team)

#Aggregations
#18
print(round(df_cl_sal_col["Age"].mean(), ))

#19
print(round(df_cl_sal_col["Salary"].max(), ))
#20
print(round(df_cl_sal_col["Weight"].min(), ))

#Column Operations:
#21
df_cl_sal_col["AgeInFive"] = df_cl_sal_col["Age"]+5
print(df_cl_sal_col)
#22
df_cl_sal_col["SalaryInMilions"] = round(df_cl_sal_col["Salary"]/1000000, 3)
print(df_cl_sal_col)

#Bonus
#23
max_sal = df_cl_sal_col.groupby("Team")["Salary"].sum().reset_index(name='Total Salary Count')
max_sal = max_sal.sort_values(by = 'Total Salary Count', ascending = False)
print(max_sal.iloc[0])
#24