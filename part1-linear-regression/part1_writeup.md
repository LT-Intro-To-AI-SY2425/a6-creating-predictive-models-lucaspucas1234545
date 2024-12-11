# Part 1 - Linear Regression Writeup

After completing `a6_part1.py` answer the following questions

## Questions to answer

1. What is the r squared value?  What does this say about this linear regression model?

The r squared value represents how correlated the data is, squared. The closer this value is to 1, the more correlated the data is, and the closer it is to 0, the less correlated it is. It basically says whether the linear regression of the data is possible.

2. According to your model, what is the predicted systolic blood pressure for a person who is 42 years old?

It predicted a value of 136.52.

3. How accurate do you think this model's predictions are?  Do you think this model is accurate enough to reliably predict someone's blood pressure based on their age?  Why or why not?  And if not, what could improve the model?

Its not amazingly accurate, but it does make an educated guess about where your blood pressure might be. I don't think its good enough to predict it exactally based on their age. What if they're really healthy for their age, or vice versa? The model doesn't take into consideration enough factors that influence blood pressure. I think there needs to be more variables and more data points.