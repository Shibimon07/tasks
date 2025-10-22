import pandas as pd

df = pd.read_csv("data.csv")
print (df)

#cleanig data for date for extra string val
df['Date'] = df['Date'].astype(str).str.replace("'", "", regex=False)



null= df.isnull().sum()
print (f"null values are \n {null} ")

rows_empty_val = df[df.isnull().any(axis=1)]
print(f" empty values of the rows \n {rows_empty_val}")

empty_count = (df == '').sum()
print(empty_count)

duplicate = df [df.duplicated()]
print (f" duplicated value {duplicate}")

# track and logging

empty_val_col=df.isnull().sum().sum()
print (empty_val_col)

logging =pd.DataFrame(
    {
        "total_null_val": [(empty_val_col)],
        "rows_null  " : [len (rows_empty_val)],
        "rows_with_dupli " : [len (duplicate)]
    }
)

logging.to_csv("data_logged.csv", mode="a", index=False, header=False )

# cloumn insert ,update , delete 

# remove
df = df.drop("Duration", axis=1)
print(df) 


#insert
df["Workout"] = "cardio"
print (df)

#update

df['Pulse'] = df['Pulse'].replace(100, 7)
print(df)

#row  insert ,update , delete

#insert

new_row = {"Duration": 60, "Date": "2021/01/01", "Pulse": 100, "Maxpulse": 120, "Calories": 300}

df = pd.concat([df, pd.DataFrame([new_row])])

#print(df)

#update 

df.loc[df['Date'] == '2020/12/02', 'Maxpulse'] = 99999

print(df)


# Remove 

df = df[df['Date'] != '2020/12/03']
print(df)