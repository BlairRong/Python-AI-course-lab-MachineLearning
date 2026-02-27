2026.1.21 Todays Lab
 
Earlier in the project, we mentioned that there might be conflicts when comparing sizes based on different measurements (e.g., chest circumference and shoulder breadth). For instance, a person might have size S for chest but size M for shoulders. Your task is to get a clearer picture of how many individuals have matching sizes for both measurements and how many have different sizes (i.e., they fall into different sizes for shoulder breadth and chest circumference).
 
Use the size chart: Use a size chart that specifies the limits for shoulder breadth and chest circumference for each size.
 
Create a function: Write a function that iterates through each person's measurements and compares them with the size chart.
 
Count matches and conflicts: The function should count the number of individuals who have exactly one matching size and the number of individuals who have multiple possible sizes (conflicts).
 
Test your function with both female and male datasets, and use appropriate size charts for each gender.
 
Good Luck! 







2026.1.22 Todays Lab

 
Last time, we created a function get_size to get a clearer view of how many matches and ties we had. Now, I want you to do the same thing for the new size charts we created, but this time taking into consideration that we have two measurements instead of one. The goal remains the same: find out how many matches and how many ties we have.
 
Task
Analyze the data: Use the new size charts to determine the number of matches and ties based on two measurements.
Count matches and ties: Write a function that iterates through each person's measurements, compares them with the new size charts, and counts the number of matches and ties.
Bonus
Modify the function to handle ties. If there is a tie and the sizes are adjacent, choose the larger size to increase the number of matches.
 
OBS
Tomorrow we will not have a lecture. I want you to continue working on the lab and also revise everything we have covered so far. I will be in meetings all day tomorrow, so if you have any questions, please write to Haithem.
Good Luck! 



2026.1.27 Today’s Lab

We have now had the opportunity to explore and experiment with scikit-learn, a powerful machine learning library in Python. In this lab, we specifically used the KNeighborsClassifier along with train_test_split to build and evaluate a basic classification model. This hands-on experience gave us a glimpse into how machine learning workflows operate, from data preparation to training and testing.
Although we managed to get a model up and running, there is definitely room for improvement in our test results. Today’s challenge is all about digging deeper and exploring different ways to influence and potentially improve the outcome of our model’s performance.
Whether or not you actually succeed in improving the results is not the most important part. What truly matters is that you engage deeply with the process, try different ideas, and reflect on what happens and why.
Some key questions to think about:
Can we manipulate our data in a meaningful way to help the model learn better?
Are there preprocessing steps we can add, such as normalization or feature scaling?
How does changing parameters in KNeighborsClassifier affect the results?
What impact does the way we split our data have on model accuracy?
Use this time to experiment freely. Try:
Adjusting the number of neighbors (n_neighbors)
Using different values for test_size in train_test_split
Evaluating with cross_val_score instead of a single train/test split
Visualizing the data to see if there are patterns or outliers affecting performance
Make sure to take notes on what you try, what changes you observe, and what you learn along the way. This is an excellent opportunity to develop your problem-solving skills and build intuition about machine learning models.
 
Good Luck 