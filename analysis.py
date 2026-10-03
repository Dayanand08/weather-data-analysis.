#analysis.py loads Weather Data.csv into a pandas DataFrame, displays an overview of the data, then runs several weather analyses.

#It checks unique values and record counts, finds rows for specific conditions such as clear weather or snow, counts missing values, renames columns, calculates visibility’s mean, pressure’s standard deviation, humidity’s variance, and grouped numeric averages/minimums/maximums for each weather condition. It also filters records using combinations of weather, wind speed, humidity, and visibility conditions.

#The script prints results directly to the terminal; numpy is imported but not currently used.
import pandas as pd
import numpy as np
df=pd.read_csv("Weather Data.csv")
print(df.head()) # shows first 5 rows in the dataset
print(df.shape) #shows no of rows and columns in dataset
print(df.index) # shows index of dataset
print(df.columns) # shows name of columns in dataset
print(df.dtypes) # shows data type of each column
print(df["Weather"].unique()) # shows unique values of single column. Not applied for whole dataset
print(df.nunique()) # Shows no of unique values in single column. It is applied for single column as well as whole dataframe
print(df.count()) # shows no of non-null values in each column as well as whole dataframe
print(df["Weather"].value_counts()) #Shows no of unique values in single column. It is applied for only single column 
print(df.info()) # Shows basic info about the dataframe

#Q1 To find unique values of wind speed column
print(df["Wind Speed_km/h"].unique())

#Q2 Find no of times when the weather is exactly clear
print(df["Weather"].value_counts())

print(df[df.Weather == "Clear"])

print(df.groupby("Weather").get_group("Clear"))

#Q3 Find no of times when the wind speed was exactly 4 km/h
print(df[df["Wind Speed_km/h"] == 4])

#Q4 find out all the null values in the data
print(df.isnull().sum())

#Q5 Rename the column name "Weather" of the dataframe to "Weather Condition"
df.rename(columns={'Weather': 'Weather Condition'}, inplace=True)
print(df.head(2)) 

#Q6 What is the mean of visibility
print(df.Visibility_km.mean())

#Q7 What is the standard deviation of pressure in data
print(df.Press_kPa.std())  #std - standard deviation

#Q8 What is the variance of the Relative Humidity in the data
df.rename(columns={'Rel Hum_%': 'Rel_Hum_%'}, inplace=True)
print(df["Rel_Hum_%"].var())  #var - variance

#Q9 Find all instances when snow was recorded
print(df[df["Weather Condition"] == "Snow"])  #Filtering the data for all instances when snow was recorded
print(df[df["Weather Condition"].str.contains("Snow")]) #Shows all instances when snow was recorded. str.contains()

#Q10 Find all instances when wind speed is above 24 and visibility is 25
print(df[(df["Wind Speed_km/h"]>24) & (df["Visibility_km"]==25)]) #Shows all instances when wind speed is above 24 and visibility is 25)

#Q11 What is the mean value of each column against each weather condition
print(df.groupby("Weather Condition").mean(numeric_only=True))

#Q12 What is the minimum & maximum value of each column against each weather condition
print(df.groupby("Weather Condition").min(numeric_only=True))
print(df.groupby("Weather Condition").max(numeric_only=True))

#Q13 Show all the records where weather condition is fog
print(df[df["Weather Condition"]=="Fog"])

#Q14 Find all instances when weather is clear or visibility is above 40
print(df[(df["Weather Condition"] == "Clear") | (df["Visibility_km"] > 40)])

#Q15 Find all instances when weather is clear and relative humidity is greater than 50 or visibility is above 40
print(df[((df["Weather Condition"] == "Clear") & (df["Rel Hum_%"] > 50)) | (df["Visibility_km"] > 40)])

