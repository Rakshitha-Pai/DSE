import pandas as pd
df=pd.read_excel(r"D:\data.xlsm")
print("First Few Rows")
print(df.head())
print("\nSummary Statistics")
print(df.describe())
filtered_data=df[df['Age']>30]
print("\n Filtered data (Age>30):")
print(filtered_data)
sorted_data =df.sort_values(by='salary',ascending=False)
print("\n Sorted data(by salary):")
print(sorted_data)
df['Bonus']=df['Salary']*0.1
print("\n Data with new column (Bonus):")
print(df)
df.to_excel('output.xlsx',index=false)
print("\n Data written to output.xlsx")





#output
First Few Rows
               1                        2         3     4   \
0             NaN                      NaN       NaN   NaN   
1            Name              Designation     Month  Year   
2      Raj Sharma  Chief Technical Officer  December  2016   
3   Sharad Gandhi               Accountant  December  2016   
4  Danish D'Souza     Senior Web Developer  December  2016   

                    5              6            7            8      9   \
0                  NaN            NaN          NaN          NaN    NaN   
1  Total Days of Month  Allowed Leave  Leave taken  Worked Days    CTC   
2                   30              2            0           30  60000   
3                   30              0            0           30  30000   
4                   30              0            0           30  20000   

                      10  ...              27     28           29      30  \
0                    NaN  ...             NaN    NaN          NaN     NaN   
1  CTC for December 2016  ...  Salary Advance  TOTAL  NET PAYABLE  Gender   
2                  60000  ...             NaN   8800        63050    Male   
3                  30000  ...             NaN   2300        28750    Male   
4                  20000  ...             NaN   1440        17310    Male   

       31                            32             33  \
0     NaN                           NaN            NaN   
1  Prefix  Name of Authorised Signatory  PF Applicable   
2      Mr             Managing Director            Yes   
3      Mr             Managing Director            Yes   
4      Mr             Managing Director            Yes   

                       34                   35                  36  
0                     NaN                  NaN                 NaN  
1  Medical Bill Submitted  Medical Bill Amount   Your Company Name  
2                     Yes                 1250        Company Name  
3                     Yes                 1250   ABC & Company Ltd  
4                     Yes                 2000  Sabu & Company Ltd  

[5 rows x 36 columns]

Summary Statistics
               1              2         3     4   5   6   7   8     9      10  \
count          22             22        22    22  22  22  22  47    22     22   
unique         22              9         2     2   2   3   5   4    14     15   
top     Sayad K M  Web Developer  December  2016  30   2   2   0  8000  14000   
freq            1              9        21    21  21  19   8  25     4      4   

        ...              27  28    29    30  31                 32   33   34  \
count   ...               1  47    22    22  22                 22   22   22   
unique  ...               1  16    21     3   3                  2    2    2   
top     ...  Salary Advance   0  6620  Male  Mr  Managing Director  Yes  Yes   
freq    ...               1  25     2    17  17                 21   21   21   

          35                 36  
count     22                 47  
unique    12                  4  
top     1250  ABC & Company Ltd  
freq       4                 44  

[4 rows x 36 columns]
