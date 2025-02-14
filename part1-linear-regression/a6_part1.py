import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("part1-linear-regression/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values

# Use reshape to turn the x values into 2D arrays:
x = x.reshape(-1,1)

# Create the model

model = LinearRegression().fit(x, y)

# Find the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 

coef = round(float(model.coef_[0]), 2)
intercept = round(float(model.intercept_), 2)
r_squared = model.score(x, y)

# Print out the linear equation and r squared value

print(f"The linear equation: y= {coef}x + {intercept} ")
print(f"The r squared value: {r_squared}")

# Predict the the blood pressure of someone who is 42 years old.
# Print out the prediction

prediction_input = 42
prediction_val = model.predict([[prediction_input]])
print(f"Prediction when x is {prediction_input}: {prediction_val}")

# Create the model in matplotlib and include the line of best fit
# plt.figure(10,10)
plt.scatter(x,y, c="orange")
plt.scatter(prediction_input, prediction_val, c="blue")
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.title("Blood Pressure by Age")
plt.plot(x, coef*x + intercept, c="r", label="Line of Best Fit")
plt.legend()
plt.show()