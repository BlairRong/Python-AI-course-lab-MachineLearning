2026.1.28 Todays Lab: Working with Image Data

 
Data Transformation
 
In this lab, you will continue working with image-based datasets, where each image is composed of pixel values. Our goal is to begin preparing this data so that it can be used effectively in a machine learning model. You will walk through several key steps in the preprocessing pipeline.
 
The first part involves transforming the data so that it falls within a more manageable range.
Right now, each pixel value ranges from 0 to 255.
 
Consider what effect this might have on your model, and think about how you could convert this to a more consistent format — something that many machine learning models handle better.
 
Once you’ve made that adjustment, try running the code and examining the output. One way to verify that your transformation worked is to inspect a single image and print out only certain values — for example, those that are greater than zero.
 
This can help you:
- Get a feel for what kind of data you're working with
- Confirm that your processing is doing what you expect
 
-----------------------------------------------------------------------------------------------
 
Reshaping the Data
 
Next, think about how the image data is currently structured.
Each image is a 2D array — in this case, 28 by 28 pixels.
 
However, many machine learning algorithms expect input in a different format.
 
Reflect on how you might reshape or reorganize the data so that each image is represented as a single vector rather than a matrix.
 
Checking the Shape
 
Once you've restructured the data, it's a good idea to print out the shape of the dataset both before and after this transformation.
 
Doing so will help you:
- Understand how the data has changed
- Confirm that your reshaping step worked as intended
 
Things to Reflect On:
 
- Why might it be helpful to scale pixel values to a different range?
- How does viewing specific pixel values help you debug your preprocessing steps?
- Why do some models require flat vectors instead of 2D matrices?
- How does reshaping the data affect the input size for your future model?
 
Final Note
 
Take your time and make sure you understand why you're performing each step — not just how to do it. These concepts are essential when working with real-world image data and will come up again in future labs and projects.





2026.1.29 Todays Lab

Prediction Generation:
How can you generate predictions from a trained neural network model using a test dataset? What function or method would you use?
Accessing Prediction Details:
How would you access the prediction details for the second image in the test dataset? Which index would you use to retrieve this information from the predictions array?
Finding the Predicted Class:
How can you determine the predicted class from the output of a neural network? What function would you use to find the index of the highest probability?
Visualizing Test Data:
Which function would you use to visualize a specific test image, and what parameters might you need to provide to display it in grayscale?
Comparing with Actual Labels:
How would you retrieve the actual label for the second image in the test dataset? Which index should you use to access this information?
Converting Predictions to Class Labels:
How can you convert a list of prediction probabilities into class labels for each test image? What Python technique or method would help you iterate over the predictions and extract the labels?
Examining Initial Predictions:
How would you access the first five predicted class labels from your converted predictions? Which part of the list would you slice to get this subset?
Good Luck! 





2026.2.2 Todays Lab

Today’s task
Your task today is to enhance our model by reducing the number of errors. Let’s create a new version, Model 2, and experiment with different parameters.
You can, for example:
Adjust the number of epochs
Try different activation functions
Modify the hidden layers
Experiment with other relevant parameters
We already have a good test score, so don’t expect dramatic improvements — the goal is to further optimize the model.