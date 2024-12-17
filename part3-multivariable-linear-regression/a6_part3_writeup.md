# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?

The r squared value is 0.86. This means that the model is quite correlated with the data.

2. Is your model accurate? Why or why not?

The model seems pretty accurate. All of the predicted values are within about 2 thousand dollars of the true value, and given that used cars have tons of variables to them, that seems pretty good.

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?

It predicts that it will be 9402.91 for the 10 year old car, and 2335 for the 20 year old car.

4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?

Though none of my predicted values are negative, I'd assume that this happens because the trend line is negative. As the cars increase in age and miles, its value continues to decrease, until it "becomes negative". That shouldn't be happening, but rather the limit as both age and miles goes towards infinity, the value = 0. 