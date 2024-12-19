# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?

The score of the model decreases significnatly. It used to be 0.91, but now its only 0.65. Its probably because standard scaler is something typically used to preprocess data, so without that preprocessing the model isn't as accurate. 

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.

With the standardScaler, the model is quite accurate. It only got a few wrong, with a score of 0.91, so I'd say its good enough to trust it. 

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?

It did relatively well. When the third value is aproximately 0.98, then it is most likely to get the prediction wrong. 

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.

The model guesses that based on the imputs, she would not purchase an suv.