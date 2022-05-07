import pandas as pd
patients = [0,1,2,3]
res = [True,True,False,False]
p_seris = pd.Series(data=res,index=patients)
print(p_seris)

patients = ["a","b","c","d"]
res = [True,True,False,False]
p_seris = pd.Series(data=res,index=patients)
print(p_seris)

patients = ["a","b","c","d"]
cols = {
    "sys_init": [120,126,130,115],
    "dia_init": [75,85,90,87],
    "sys_fin": [115,123,130,118],
    "dia_fin": [70,82,92,87]
}
df = pd.DataFrame(cols,index=patients)
print(df)

#creating DataFrame using Series for each column
patients = pd.Series(["a","b","c","d"])
cols = {
    "sys_init": pd.Series([120,126,130,115],index=patients),
    "dia_init": pd.Series([75,85,90,87],index=patients),
    "sys_fin": pd.Series([115,123,130,118],index=patients),
    "dia_fin": pd.Series([70,82,92,87],index=patients)
}
df = pd.DataFrame(cols)
#print(df.head())
#Accessing dataframe values
print(df.loc["a","dia_init"])
print(df.loc["a"].loc["dia_init"])

#accessing dataframe value using index values
print(df.iloc[0,2])
print(df.iloc[0].iloc[2])