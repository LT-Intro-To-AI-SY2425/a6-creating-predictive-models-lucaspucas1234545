import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#imports and formats the data
data = pd.read_csv("part3-multivariable-linear-regression/car_data.csv")
x = data[["miles","age"]].values
y = data["Price"].values

#split the data into training and testing data
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = .2)
#create linear regression model
model = LinearRegression().fit(xtrain, ytrain)
#Find and print the coefficients, intercept, and r squared values. 
#Each should be rounded to two decimal places. 
coef = np.round(model.coef_, 2)
intercept = round(float(model.intercept_), 2)
r_squared = round(model.score(x,y), 2)



print(f"Coefficent is {coef}")
print(f"The intercept is {intercept}")
print(f"r squared value is {r_squared}")

#Prediction
predict = model.predict(xtest)
predict = np.around(predict, 2)
print(f"prediction is {predict}")

print("predictions for writeup__________________________________")
miles_1=150000
age_1=20
predict_1=model.predict([[miles_1, age_1]])
print(f"prediction for 10 y.o. {predict_1}")

#Loop through the data and print out the predicted prices and the 
#actual prices
print("***************")
print("Testing Results")

for index in range(len(xtest)):
    actual = ytest[index]
    predicted_y = predict[index]
    x_coord = xtest[index]
    print(f"Miles: {x_coord[0]} Age: {x_coord[1]} actual: {actual} Predicted: {predicted_y}")
    
